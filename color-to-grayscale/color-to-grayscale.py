def color_to_grayscale(image):
    grayscale = []

    for i in range(len(image)):
        row = []
        for j in range(len(image[i])):
            R = image[i][j][0]
            G = image[i][j][1]
            B = image[i][j][2]

            Y = 0.299 * R + 0.587 * G + 0.114 * B
            row.append(Y)

        grayscale.append(row)

    return grayscale
