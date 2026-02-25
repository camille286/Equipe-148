def pointfixe(fonction_pointfixe, Q0, tolr, nmax):

    iterations = [Q0]

    for n in range(1, nmax + 1):
        Q_prev = iterations[-1]
        Q_new = fonction_pointfixe(Q_prev)

        iterations.append(Q_new)

        if Q_new != 0:
            err_rel = abs(Q_new - Q_prev) / abs(Q_new)
        else:
            err_rel = abs(Q_new - Q_prev)

        if err_rel < tolr:
            return iterations

    return iterations
