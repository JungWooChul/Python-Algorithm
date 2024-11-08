def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx, pnp = 0, 0 # check: 사용할 수 있는 스킬의 종류(인덱스), pnp: pass or fail 
        for branch in skill_tree: 
            if skill[idx] == branch: # 선행 스킬 순서대로 스킬트리 확인
                idx += 1
                if idx == len(skill): # 선행 스킬 모두 확인
                    break
            else:
                if branch in skill: # 선행 스킬의 순서대로 나오지 않은 경우
                    pnp += 1
                    break
                else:
                    continue
        if not pnp:
            answer += 1
    
    return answer