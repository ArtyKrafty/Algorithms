def my_agent(obs, conf) :
    def get_results(x, y, mark, multiplier) :
        board[x][y] = mark
        results = []
        do_not_use = [False, False, False, False]
        for i in range(conf.inarow, 2, -1) :
            p = 0
            lc = 0
            ap = 0
            if i == conf.inarow and do_not_use[0] is False :
                (p, lc, ap, do_not_use[0]) = process_results(
                    p, lc, ap,
                    check_axis(mark, i, x, lambda z : z, y + inarow_m1, lambda z : z - 1)
                    )
            if do_not_use[1] is False :
                (p, lc, ap, do_not_use[1]) = process_results(
                    p, lc, ap,
                    check_axis(mark, i, x - inarow_m1, lambda z : z + 1, y + inarow_m1, lambda z : z - 1)
                    )
            if do_not_use[2] is False :
                (p, lc, ap, do_not_use[2]) = process_results(
                    p, lc, ap,
                    check_axis(mark, i, x + inarow_m1, lambda z : z - 1, y, lambda z : z)
                    )
            if do_not_use[3] is False :
                (p, lc, ap, do_not_use[3]) = process_results(
                    p, lc, ap,
                    check_axis(mark, i, x + inarow_m1, lambda z : z - 1, y + inarow_m1, lambda z : z - 1)
                    )
            results.append((p * multiplier, lc, ap))
        board[x][y] = 0
        return results

    def check_axis(mark, inarow, x, x_fun, y, y_fun) :
        (x, y, axis_max_range) = get_x_y_and_axis_max_range(x, x_fun, y, y_fun)
        zeros_allowed = conf.inarow - inarow
        lowest_cell = 0
        for i in range(axis_max_range) :
            x_temp = x
            y_temp = y
            zeros_remained = zeros_allowed
            marks = 0
            in_air = 0
            for j in range(conf.inarow) :
                if board[x_temp][y_temp] != mark and board[x_temp][y_temp] != 0 :
                    break
                elif board[x_temp][y_temp] == mark :
                    marks += 1
                else :
                    zeros_remained -= 1
                    if (y_temp + 1) < conf.rows and board[x_temp][y_temp + 1] == 0 :
                        in_air -= 1
                if marks == inarow and zeros_remained == 0 :
                    return (sp, lowest_cell, in_air, True)
                x_temp = x_fun(x_temp)
                y_temp = y_fun(y_temp)
                if y_temp < 0 or y_temp >= conf.rows or x_temp < 0 or x_temp >= conf.columns :
                    return (0, 0, 0, False)
            x = x_fun(x)
            y = y_fun(y)
        return (0, 0, 0, False)

    def get_x_y_and_axis_max_range(x, x_fun, y, y_fun) :
        axis_max_range = conf.inarow
        while y < 0 or y >= conf.rows or x < 0 or x >= conf.columns :
            x = x_fun(x)
            y = y_fun(y)
            axis_max_range -= 1
        return (x, y, axis_max_range)

    def process_results(p, lc, ap, axis_check_results) :
        (points, lowest_cell, in_air, do_not_use) = axis_check_results
        if points > 0 :
            if lc < lowest_cell :
                lc = lowest_cell
            ap += in_air
            p += points
        return (p, lc, ap, do_not_use)

    def get_best_cell(best_cell, current_cell) :
        for i in range(len(current_cell["factors"])) :
            for j in range(3) :
                if best_cell["factors"][i][j] < current_cell["factors"][i][j] :
                    return current_cell
                if best_cell["factors"][i][j] > current_cell["factors"][i][j] :
                    return best_cell
        return best_cell

    def get_factors(results) :
        factors = []
        for i in range(conf.inarow - 2) :
            if i == 1 :
                factors.append(results[0][0][i] if results[0][0][i][0] > st else (0, 0, 0))
                factors.append(results[0][1][i] if results[0][1][i][0] > st else (0, 0, 0))
                if len(results) > 1 :
                    factors.append(results[1][1][i] if -results[1][1][i][0] > st else (0, 0, 0))
                    factors.append(results[1][0][i] if -results[1][0][i][0] > st else (0, 0, 0))
                else :
                    for j in range(2) :
                        factors.append((0, 0, 0))
            else :
                for j in range(2) :
                    factors.append((0, 0, 0))
                for j in range(2) :
                    factors.append((0, 0, 0))
            if results[0][1][i][2] == 0 :
                factors.append(results[0][1][i])
            else :
                factors.append((0, 0, 0))
            factors.append(results[0][0][i])
            factors.append((1 if i == 1 and shift == 0 else 0, 0, 0))
            if len(results) > 1 :
                factors.append(results[1][1][i])
                factors.append(results[1][0][i])
            else :
                for j in range(2) :
                    factors.append((0, 0, 0))
        if len(results) > 2 :
            for i in range(conf.inarow - 2) :
                factors.append(results[2][0][i])
                factors.append(results[2][1][i])
        else :
            for i in range(conf.inarow - 2) :
                for j in range(2) :
                    factors.append((0, 0, 0))
        return factors

    my_mark = obs.mark
    opp_mark = 2 if my_mark == 1 else 1
    board = []
    for column in range(conf.columns) :
        board.append([])
        for row in range(conf.rows) :
            board[column].append(obs.board[conf.columns * row + column])
    best_cell = None
    board_center = conf.columns // 2
    inarow_m1 = conf.inarow - 1
    sp = 1
    st = 1
    x = board_center
    shift = 0
    while x >= 0 and x < conf.columns :
        y = conf.rows - 1
        while y >= 0 and board[x][y] != 0 :
            y -= 1
        if y >= 0 :
            results = []
            results.append((get_results(x, y, my_mark, 1), get_results(x, y, my_mark, 1)))
            if (y - 1) >= 0 :
                results.append((get_results(x, y - 1, my_mark, -1), get_results(x, y - 1, opp_mark, -1)))
            if (y - 2) >= 0 :
                results.append((get_results(x, y - 2, my_mark, 1), get_results(x, y - 2, opp_mark, 1)))
            factors = get_factors(results)
            if best_cell is None :
                best_cell = {
                    "column" : x,
                    "factors" : factors
                    }
            else :
                current_cell = {
                    "column" : x,
                    "factors" : factors
                    }
                best_cell = get_best_cell(best_cell, current_cell)
        if shift >= 0 : shift += 1
        shift *= -1
        x = board_center + shift
    return best_cell["column"]

    import random
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)
