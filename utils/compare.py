import cv2
import numpy as np
import utils.slack as slack

def compare_images(img1, img2, path):
    previous = cv2.imread(img1)
    current = cv2.imread(img2)

    # find difference between two images and save to new file only the difference
    diff = cv2.absdiff(previous, current)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    th = 1
    imask = mask > th
    canvas = np.zeros_like(current, np.uint8)
    canvas[imask] = current[imask]

    if canvas.any():
        h1, w1 = previous.shape[:2]
        h2, w2 = current.shape[:2]
        vis = np.zeros((max(h1, h2), w1 * 3 + 20, 3), np.uint8)
        vis[:h1, :w1, :3] = previous
        vis[:h2, w1 + 20:w1 + w2 + 20, :3] = canvas
        vis[:h2, w1 * 2 + 20:w1 * 2 + w2 + 20, :3] = current

        cv2.imwrite(path, vis)

        difference_percentage = str(cv2.countNonZero(mask) * 100 / mask.size)[:4] + '%'
        difference_message = 'Difference found in ' + path + ' (' + difference_percentage + ')'
        print(difference_message)
        slack.send_slack_message(difference_message, path)
    else:
        print('No diff found!')
