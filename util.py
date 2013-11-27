def collision (rayon1, rayon2, pos1, pos2):
    if (rayon1 + rayon2) * (rayon1 + rayon2) < (pos1[0] - pos2[0]) * (pos1[0] - pos2[0]) + (pos1[1] - pos2[1]) * (pos1[1] - pos2[1]):
        return False
    return True

