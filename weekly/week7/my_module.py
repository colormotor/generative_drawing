def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b

def say_hello(name):
    print(f"Hello, {name}")

def find_contours(img, thresh=127, blur=5, invert=True, eps=1.0):
    ''' Utility function to get contours compatible with py5canvas.
    Assumes a grayscale image as a result
    The eps parameter controls the amount of simplification (if > 0)
    '''
    import cv2
    gray_img = np.array(img.convert('L'))
    gray_img = cv2.blur(gray_img, (blur, blur))

    # Threshold and find contours
    _, thresh_img = cv2.threshold(gray_img, thresh, 256, int(invert))
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    S = []
    for ctr in contours:
        if eps > 0:
            ctr = cv2.approxPolyDP(ctr, eps, True)
        if len(ctr) > 3:
            S.append(np.vstack([ctr[:,0,0], ctr[:,0,1]]).T)
    return S