#!/usr/bin/python

fe=1
je=2
jee=3
ain=3
dai=5
ne=2
ai=2

def damage(spell):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage 
    """
    damage=0
    begin=spell.split('fe')

    # checking if 'fe' is more the one time and if the spell is even ending somewhere by 'ai'
    if len(begin) == 2 and 'ai' in begin[1]:
        subspell=begin[1]
        damage = fe+ai
        
        # find index of every 'ai'
        spellend=[]
        for i in range(len(subspell)):
            if subspell[i:i+2] == 'ai':
                spellend.append(i)
    
        # cutting trash letters from end of the spell
        if len(spellend) > 1:
            for i in range(len(spellend)):
                if subspell[spellend[i]-1] == 'd' and len(spellend) != i+1:
                    continue
                elif subspell[spellend[i]+2] == 'n' and len(spellend) != i+1:
                    continue
                else:
                    subspell=subspell[:spellend[i]]
                    break
        else:
            subspell=subspell[:spellend[0]]

        not_used=subspell
        for i in range(len(subspell)):
            if subspell[i:i+3] == 'jee':
                damage += jee
                not_used=not_used[0:not_used.find('jee')]+not_used[not_used.find('jee')+3:]
            elif subspell[i:i+3] == 'dai':
                damage += dai
                not_used=not_used[0:not_used.find('dai')]+not_used[not_used.find('dai')+3:]
            elif subspell[i:i+3] == 'ain':
                damage += ain
                not_used=not_used[0:not_used.find('ain')]+not_used[not_used.find('ain')+3:]
            elif subspell[i:i+2] == 'je':
                damage += je
                not_used=not_used[0:not_used.find('je')]+not_used[not_used.find('je')+2:]
            elif subspell[i:i+2] == 'ne':
                damage += ne
                not_used=not_used[0:not_used.find('ne')]+not_used[not_used.find('ne')+2:]

        # remove from damage mistakenly putted letters
        damage -= len(not_used)

        if damage < 0:
            return 0
        else:
            return damage
    else:
        return 0

def main():
    result=damage('xxxxxfejedaijeeaindaiyaiaixxxxxx')
    print result

if __name__ == "__main__":
    main()
