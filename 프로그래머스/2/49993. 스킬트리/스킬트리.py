def solution(skill, skill_trees):
    graph = {skill[i]:skill[i+1:] for i in range(len(skill))}
    answer = 0
    for skill_tree in skill_trees:
        idx, pnp = 0, 0 # check: 사용할 수 있는 스킬의 종류(인덱스), pnp: pass or fail 
        for branch in skill_tree:
            if skill[idx] == branch:
                idx += 1
                if idx == len(skill):
                    break
            else:
                if branch in skill:
                    pnp += 1
                    break
                else:
                    continue
        if not pnp:
            answer += 1
    
    return answer