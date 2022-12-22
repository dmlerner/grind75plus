# https://leetcode.com/problems/word-search-ii/
from david import *

from itertools import product
from collections import Counter

WORD_KEY = "$"


def build_trie(words):
    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # retrieve the next node; If not found, create a empty node.
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[WORD_KEY] = word
    return trie

used = set()
def find_words(grid, word_list):
    def in_bounds(rc):
        r, c = rc
        return 0 <= r < R and 0 <= c < C
        # return r in row_indices and c in column_indices

    # @show
    def get(rc):
        r, c = rc
        return grid[r][c]

    def grid_set(rc, letter):
        r, c = rc
        grid[r][c] = letter

    def get_neighbors(rc):
        r, c = rc
        offsets = (-1, 0), (1, 0), (0, -1), (0, 1)
        for (dr, dc) in offsets:
            neighbor = r + dr, c + dc
            if in_bounds(neighbor):
                yield neighbor

    # @show
    # @listify
    def _find_words2(rc, trie):
        '''
        consider adding rc to a word.
        '''
        # assert rc not in used

        letter = get(rc)
        # assert letter is not None # trivially true via used
        if letter not in trie:
            return

        # grid_set(rc, None)
        next_trie = trie[letter]

        if WORD_KEY in next_trie:
            yield next_trie.pop(WORD_KEY)
        if not next_trie:
            trie.pop(letter)
            return

        used.add(rc)

        for neighbor in get_neighbors(rc):
            if neighbor in used:
                continue
            yield from _find_words2(neighbor, next_trie)

        used.remove(rc)







    # @show
    # @listify
    def _find_words(rc, parent_trie):
        print(f'{rc=}')
        if not parent_trie:
            return
        # breakpoint()
        letter = get(rc)
        print(f'{letter =}')
        r,c = rc
        grid[r][c] = None
        next_letter_trie = parent_trie.get(letter)
        # try:
        #     assert next_letter_trie
        # except:
        #     breakpoint()
        if next_letter_trie and WORD_KEY in next_letter_trie:
            yield next_letter_trie.pop(WORD_KEY)
        if not next_letter_trie:
            return
        # now nlt can be empty because we popped
        # Optimization: put back once basic works again
        # if not next_letter_trie and parent_trie:
        #     parent_trie.pop(get(rc))
        #     grid[r][c] = letter
        #     return


        for neighbor in get_neighbors(rc):
            print(f'{neighbor =}')
            # could exit loop if nlt becomes empty; optimization
            neighbor_letter = get(neighbor)
            print(f'{neighbor_letter =}')
            # assert neighbor_letter
            if neighbor_letter is None: # could move to get_neighbors; reasonable to have.
                continue

            # neighbor_letter = get(neighbor)
            if neighbor_letter in next_letter_trie:
                assert neighbor_letter is not None
                # nr, nc = neighbor
                # grid[nr][nc] = None
                # used.add(neighbor)
                yield from _find_words(neighbor, next_letter_trie)
                # grid[nr][nc] = neighbor_letter
                # used.remove(neighbor)

        grid[r][c] = letter


    R, C = len(grid), len(grid[0])
    row_indices = range(R)
    column_indices = range(C)
    grid_counts = sum(map(Counter, grid), Counter())

    word_list = list(filter(lambda word: Counter(word) <= grid_counts, word_list))

    trie = build_trie(word_list)
    for rc in product(row_indices, column_indices):
        yield from _find_words2(rc, trie)

def official(board, words):
    WORD_KEY = '$'

    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # retrieve the next node; If not found, create a empty node.
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[WORD_KEY] = word

    rowNum = len(board)
    colNum = len(board[0])

    matchedWords = []

    def backtracking(row, col, parent):

        letter = board[row][col]
        currNode = parent[letter]

        # check if we find a match of word
        word_match = currNode.pop(WORD_KEY, False)
        if word_match:
            # also we removed the matched word to avoid duplicates,
            #   as well as avoiding using set() for results.
            matchedWords.append(word_match)

        # Before the EXPLORATION, mark the cell as visited
        board[row][col] = '#'

        # Explore the neighbors in 4 directions, i.e. up, right, down, left
        for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newRow, newCol = row + rowOffset, col + colOffset
            if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                continue
            if not board[newRow][newCol] in currNode:
                continue
            backtracking(newRow, newCol, currNode)

        # End of EXPLORATION, we restore the cell
        board[row][col] = letter

        # Optimization: incrementally remove the matched leaf node in Trie.
        if not currNode:
            parent.pop(letter)

    for row in range(rowNum):
        for col in range(colNum):
            # starting from each of the cells
            if board[row][col] in trie:
                backtracking(row, col, trie)

    return matchedWords

def verify(actual, expected):
    actual = set(actual)
    expected = set(expected)
    try:
        assert actual == expected
    except:
        print(f'{expected=}')
        print(f'{actual  =}')

board = [["a"]]
words = ["a"]
verify(find_words(board, words), ('a'))
# breakpoint()
board = [["a", "a"]]
words = ["aaa"]
verify(find_words(board, words), ())
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
verify(find_words(board, words), ("oath", "eat"))

import time
board = [["m","b","c","d","e","f","g","h","i","j","k","l"],["n","a","a","a","a","a","a","a","a","a","a","a"],["o","a","a","a","a","a","a","a","a","a","a","a"],["p","a","a","a","a","a","a","a","a","a","a","a"],["q","a","a","a","a","a","a","a","a","a","a","a"],["r","a","a","a","a","a","a","a","a","a","a","a"],["s","a","a","a","a","a","a","a","a","a","a","a"],["t","a","a","a","a","a","a","a","a","a","a","a"],["u","a","a","a","a","a","a","a","a","a","a","a"],["v","a","a","a","a","a","a","a","a","a","a","a"],["w","a","a","a","a","a","a","a","a","a","a","a"],["x","y","z","a","a","a","a","a","a","a","a","a"]]
words = ["aaaaaaaaaa","aaaaaaaaab","aaaaaaaaac","aaaaaaaaad","aaaaaaaaae","aaaaaaaaaf","aaaaaaaaag","aaaaaaaaah","aaaaaaaaai","aaaaaaaaaj","aaaaaaaaak","aaaaaaaaal","aaaaaaaaam","aaaaaaaaan","aaaaaaaaao","aaaaaaaaap","aaaaaaaaaq","aaaaaaaaar","aaaaaaaaas","aaaaaaaaat","aaaaaaaaau","aaaaaaaaav","aaaaaaaaaw","aaaaaaaaax","aaaaaaaaay","aaaaaaaaaz","aaaaaaaaba","aaaaaaaabb","aaaaaaaabc","aaaaaaaabd","aaaaaaaabe","aaaaaaaabf","aaaaaaaabg","aaaaaaaabh","aaaaaaaabi","aaaaaaaabj","aaaaaaaabk","aaaaaaaabl","aaaaaaaabm","aaaaaaaabn","aaaaaaaabo","aaaaaaaabp","aaaaaaaabq","aaaaaaaabr","aaaaaaaabs","aaaaaaaabt","aaaaaaaabu","aaaaaaaabv","aaaaaaaabw","aaaaaaaabx","aaaaaaaaby","aaaaaaaabz","aaaaaaaaca","aaaaaaaacb","aaaaaaaacc","aaaaaaaacd","aaaaaaaace","aaaaaaaacf","aaaaaaaacg","aaaaaaaach","aaaaaaaaci","aaaaaaaacj","aaaaaaaack","aaaaaaaacl","aaaaaaaacm","aaaaaaaacn","aaaaaaaaco","aaaaaaaacp","aaaaaaaacq","aaaaaaaacr","aaaaaaaacs","aaaaaaaact","aaaaaaaacu","aaaaaaaacv","aaaaaaaacw","aaaaaaaacx","aaaaaaaacy","aaaaaaaacz","aaaaaaaada","aaaaaaaadb","aaaaaaaadc","aaaaaaaadd","aaaaaaaade","aaaaaaaadf","aaaaaaaadg","aaaaaaaadh","aaaaaaaadi","aaaaaaaadj","aaaaaaaadk","aaaaaaaadl","aaaaaaaadm","aaaaaaaadn","aaaaaaaado","aaaaaaaadp","aaaaaaaadq","aaaaaaaadr","aaaaaaaads","aaaaaaaadt","aaaaaaaadu","aaaaaaaadv","aaaaaaaadw","aaaaaaaadx","aaaaaaaady","aaaaaaaadz","aaaaaaaaea","aaaaaaaaeb","aaaaaaaaec","aaaaaaaaed","aaaaaaaaee","aaaaaaaaef","aaaaaaaaeg","aaaaaaaaeh","aaaaaaaaei","aaaaaaaaej","aaaaaaaaek","aaaaaaaael","aaaaaaaaem","aaaaaaaaen","aaaaaaaaeo","aaaaaaaaep","aaaaaaaaeq","aaaaaaaaer","aaaaaaaaes","aaaaaaaaet","aaaaaaaaeu","aaaaaaaaev","aaaaaaaaew","aaaaaaaaex","aaaaaaaaey","aaaaaaaaez","aaaaaaaafa","aaaaaaaafb","aaaaaaaafc","aaaaaaaafd","aaaaaaaafe","aaaaaaaaff","aaaaaaaafg","aaaaaaaafh","aaaaaaaafi","aaaaaaaafj","aaaaaaaafk","aaaaaaaafl","aaaaaaaafm","aaaaaaaafn","aaaaaaaafo","aaaaaaaafp","aaaaaaaafq","aaaaaaaafr","aaaaaaaafs","aaaaaaaaft","aaaaaaaafu","aaaaaaaafv","aaaaaaaafw","aaaaaaaafx","aaaaaaaafy","aaaaaaaafz","aaaaaaaaga","aaaaaaaagb","aaaaaaaagc","aaaaaaaagd","aaaaaaaage","aaaaaaaagf","aaaaaaaagg","aaaaaaaagh","aaaaaaaagi","aaaaaaaagj","aaaaaaaagk","aaaaaaaagl","aaaaaaaagm","aaaaaaaagn","aaaaaaaago","aaaaaaaagp","aaaaaaaagq","aaaaaaaagr","aaaaaaaags","aaaaaaaagt","aaaaaaaagu","aaaaaaaagv","aaaaaaaagw","aaaaaaaagx","aaaaaaaagy","aaaaaaaagz","aaaaaaaaha","aaaaaaaahb","aaaaaaaahc","aaaaaaaahd","aaaaaaaahe","aaaaaaaahf","aaaaaaaahg","aaaaaaaahh","aaaaaaaahi","aaaaaaaahj","aaaaaaaahk","aaaaaaaahl","aaaaaaaahm","aaaaaaaahn","aaaaaaaaho","aaaaaaaahp","aaaaaaaahq","aaaaaaaahr","aaaaaaaahs","aaaaaaaaht","aaaaaaaahu","aaaaaaaahv","aaaaaaaahw","aaaaaaaahx","aaaaaaaahy","aaaaaaaahz","aaaaaaaaia","aaaaaaaaib","aaaaaaaaic","aaaaaaaaid","aaaaaaaaie","aaaaaaaaif","aaaaaaaaig","aaaaaaaaih","aaaaaaaaii","aaaaaaaaij","aaaaaaaaik","aaaaaaaail","aaaaaaaaim","aaaaaaaain","aaaaaaaaio","aaaaaaaaip","aaaaaaaaiq","aaaaaaaair","aaaaaaaais","aaaaaaaait","aaaaaaaaiu","aaaaaaaaiv","aaaaaaaaiw","aaaaaaaaix","aaaaaaaaiy","aaaaaaaaiz","aaaaaaaaja","aaaaaaaajb","aaaaaaaajc","aaaaaaaajd","aaaaaaaaje","aaaaaaaajf","aaaaaaaajg","aaaaaaaajh","aaaaaaaaji","aaaaaaaajj","aaaaaaaajk","aaaaaaaajl","aaaaaaaajm","aaaaaaaajn","aaaaaaaajo","aaaaaaaajp","aaaaaaaajq","aaaaaaaajr","aaaaaaaajs","aaaaaaaajt","aaaaaaaaju","aaaaaaaajv","aaaaaaaajw","aaaaaaaajx","aaaaaaaajy","aaaaaaaajz","aaaaaaaaka","aaaaaaaakb","aaaaaaaakc","aaaaaaaakd","aaaaaaaake","aaaaaaaakf","aaaaaaaakg","aaaaaaaakh","aaaaaaaaki","aaaaaaaakj","aaaaaaaakk","aaaaaaaakl","aaaaaaaakm","aaaaaaaakn","aaaaaaaako","aaaaaaaakp","aaaaaaaakq","aaaaaaaakr","aaaaaaaaks","aaaaaaaakt","aaaaaaaaku","aaaaaaaakv","aaaaaaaakw","aaaaaaaakx","aaaaaaaaky","aaaaaaaakz","aaaaaaaala","aaaaaaaalb","aaaaaaaalc","aaaaaaaald","aaaaaaaale","aaaaaaaalf","aaaaaaaalg","aaaaaaaalh","aaaaaaaali","aaaaaaaalj","aaaaaaaalk","aaaaaaaall","aaaaaaaalm","aaaaaaaaln","aaaaaaaalo","aaaaaaaalp","aaaaaaaalq","aaaaaaaalr","aaaaaaaals","aaaaaaaalt","aaaaaaaalu","aaaaaaaalv","aaaaaaaalw","aaaaaaaalx","aaaaaaaaly","aaaaaaaalz","aaaaaaaama","aaaaaaaamb","aaaaaaaamc","aaaaaaaamd","aaaaaaaame","aaaaaaaamf","aaaaaaaamg","aaaaaaaamh","aaaaaaaami","aaaaaaaamj","aaaaaaaamk","aaaaaaaaml","aaaaaaaamm","aaaaaaaamn","aaaaaaaamo","aaaaaaaamp","aaaaaaaamq","aaaaaaaamr","aaaaaaaams","aaaaaaaamt","aaaaaaaamu","aaaaaaaamv","aaaaaaaamw","aaaaaaaamx","aaaaaaaamy","aaaaaaaamz","aaaaaaaana","aaaaaaaanb","aaaaaaaanc","aaaaaaaand","aaaaaaaane","aaaaaaaanf","aaaaaaaang","aaaaaaaanh","aaaaaaaani","aaaaaaaanj","aaaaaaaank","aaaaaaaanl","aaaaaaaanm","aaaaaaaann","aaaaaaaano","aaaaaaaanp","aaaaaaaanq","aaaaaaaanr","aaaaaaaans","aaaaaaaant","aaaaaaaanu","aaaaaaaanv","aaaaaaaanw","aaaaaaaanx","aaaaaaaany","aaaaaaaanz","aaaaaaaaoa","aaaaaaaaob","aaaaaaaaoc","aaaaaaaaod","aaaaaaaaoe","aaaaaaaaof","aaaaaaaaog","aaaaaaaaoh","aaaaaaaaoi","aaaaaaaaoj","aaaaaaaaok","aaaaaaaaol","aaaaaaaaom","aaaaaaaaon","aaaaaaaaoo","aaaaaaaaop","aaaaaaaaoq","aaaaaaaaor","aaaaaaaaos","aaaaaaaaot","aaaaaaaaou","aaaaaaaaov","aaaaaaaaow","aaaaaaaaox","aaaaaaaaoy","aaaaaaaaoz","aaaaaaaapa","aaaaaaaapb","aaaaaaaapc","aaaaaaaapd","aaaaaaaape","aaaaaaaapf","aaaaaaaapg","aaaaaaaaph","aaaaaaaapi","aaaaaaaapj","aaaaaaaapk","aaaaaaaapl","aaaaaaaapm","aaaaaaaapn","aaaaaaaapo","aaaaaaaapp","aaaaaaaapq","aaaaaaaapr","aaaaaaaaps","aaaaaaaapt","aaaaaaaapu","aaaaaaaapv","aaaaaaaapw","aaaaaaaapx","aaaaaaaapy","aaaaaaaapz","aaaaaaaaqa","aaaaaaaaqb","aaaaaaaaqc","aaaaaaaaqd","aaaaaaaaqe","aaaaaaaaqf","aaaaaaaaqg","aaaaaaaaqh","aaaaaaaaqi","aaaaaaaaqj","aaaaaaaaqk","aaaaaaaaql","aaaaaaaaqm","aaaaaaaaqn","aaaaaaaaqo","aaaaaaaaqp","aaaaaaaaqq","aaaaaaaaqr","aaaaaaaaqs","aaaaaaaaqt","aaaaaaaaqu","aaaaaaaaqv","aaaaaaaaqw","aaaaaaaaqx","aaaaaaaaqy","aaaaaaaaqz","aaaaaaaara","aaaaaaaarb","aaaaaaaarc","aaaaaaaard","aaaaaaaare","aaaaaaaarf","aaaaaaaarg","aaaaaaaarh","aaaaaaaari","aaaaaaaarj","aaaaaaaark","aaaaaaaarl","aaaaaaaarm","aaaaaaaarn","aaaaaaaaro","aaaaaaaarp","aaaaaaaarq","aaaaaaaarr","aaaaaaaars","aaaaaaaart","aaaaaaaaru","aaaaaaaarv","aaaaaaaarw","aaaaaaaarx","aaaaaaaary","aaaaaaaarz","aaaaaaaasa","aaaaaaaasb","aaaaaaaasc","aaaaaaaasd","aaaaaaaase","aaaaaaaasf","aaaaaaaasg","aaaaaaaash","aaaaaaaasi","aaaaaaaasj","aaaaaaaask","aaaaaaaasl","aaaaaaaasm","aaaaaaaasn","aaaaaaaaso","aaaaaaaasp","aaaaaaaasq","aaaaaaaasr","aaaaaaaass","aaaaaaaast","aaaaaaaasu","aaaaaaaasv","aaaaaaaasw","aaaaaaaasx","aaaaaaaasy","aaaaaaaasz","aaaaaaaata","aaaaaaaatb","aaaaaaaatc","aaaaaaaatd","aaaaaaaate","aaaaaaaatf","aaaaaaaatg","aaaaaaaath","aaaaaaaati","aaaaaaaatj","aaaaaaaatk","aaaaaaaatl","aaaaaaaatm","aaaaaaaatn","aaaaaaaato","aaaaaaaatp","aaaaaaaatq","aaaaaaaatr","aaaaaaaats","aaaaaaaatt","aaaaaaaatu","aaaaaaaatv","aaaaaaaatw","aaaaaaaatx","aaaaaaaaty","aaaaaaaatz","aaaaaaaaua","aaaaaaaaub","aaaaaaaauc","aaaaaaaaud","aaaaaaaaue","aaaaaaaauf","aaaaaaaaug","aaaaaaaauh","aaaaaaaaui","aaaaaaaauj","aaaaaaaauk","aaaaaaaaul","aaaaaaaaum","aaaaaaaaun","aaaaaaaauo","aaaaaaaaup","aaaaaaaauq","aaaaaaaaur","aaaaaaaaus","aaaaaaaaut","aaaaaaaauu","aaaaaaaauv","aaaaaaaauw","aaaaaaaaux","aaaaaaaauy","aaaaaaaauz","aaaaaaaava","aaaaaaaavb","aaaaaaaavc","aaaaaaaavd","aaaaaaaave","aaaaaaaavf","aaaaaaaavg","aaaaaaaavh","aaaaaaaavi","aaaaaaaavj","aaaaaaaavk","aaaaaaaavl","aaaaaaaavm","aaaaaaaavn","aaaaaaaavo","aaaaaaaavp","aaaaaaaavq","aaaaaaaavr","aaaaaaaavs","aaaaaaaavt","aaaaaaaavu","aaaaaaaavv","aaaaaaaavw","aaaaaaaavx","aaaaaaaavy","aaaaaaaavz","aaaaaaaawa","aaaaaaaawb","aaaaaaaawc","aaaaaaaawd","aaaaaaaawe","aaaaaaaawf","aaaaaaaawg","aaaaaaaawh","aaaaaaaawi","aaaaaaaawj","aaaaaaaawk","aaaaaaaawl","aaaaaaaawm","aaaaaaaawn","aaaaaaaawo","aaaaaaaawp","aaaaaaaawq","aaaaaaaawr","aaaaaaaaws","aaaaaaaawt","aaaaaaaawu","aaaaaaaawv","aaaaaaaaww","aaaaaaaawx","aaaaaaaawy","aaaaaaaawz","aaaaaaaaxa","aaaaaaaaxb","aaaaaaaaxc","aaaaaaaaxd","aaaaaaaaxe","aaaaaaaaxf","aaaaaaaaxg","aaaaaaaaxh","aaaaaaaaxi","aaaaaaaaxj","aaaaaaaaxk","aaaaaaaaxl","aaaaaaaaxm","aaaaaaaaxn","aaaaaaaaxo","aaaaaaaaxp","aaaaaaaaxq","aaaaaaaaxr","aaaaaaaaxs","aaaaaaaaxt","aaaaaaaaxu","aaaaaaaaxv","aaaaaaaaxw","aaaaaaaaxx","aaaaaaaaxy","aaaaaaaaxz","aaaaaaaaya","aaaaaaaayb","aaaaaaaayc","aaaaaaaayd","aaaaaaaaye","aaaaaaaayf","aaaaaaaayg","aaaaaaaayh","aaaaaaaayi","aaaaaaaayj","aaaaaaaayk","aaaaaaaayl","aaaaaaaaym","aaaaaaaayn","aaaaaaaayo","aaaaaaaayp","aaaaaaaayq","aaaaaaaayr","aaaaaaaays","aaaaaaaayt","aaaaaaaayu","aaaaaaaayv","aaaaaaaayw","aaaaaaaayx","aaaaaaaayy","aaaaaaaayz","aaaaaaaaza","aaaaaaaazb","aaaaaaaazc","aaaaaaaazd","aaaaaaaaze","aaaaaaaazf","aaaaaaaazg","aaaaaaaazh","aaaaaaaazi","aaaaaaaazj","aaaaaaaazk","aaaaaaaazl","aaaaaaaazm","aaaaaaaazn","aaaaaaaazo","aaaaaaaazp","aaaaaaaazq","aaaaaaaazr","aaaaaaaazs","aaaaaaaazt","aaaaaaaazu","aaaaaaaazv","aaaaaaaazw","aaaaaaaazx","aaaaaaaazy","aaaaaaaazz"]

start = time.time()
assert set(find_words(board, words))
stop = time.time()
print(stop - start)

start = time.time()
assert set(official(board, words))
stop = time.time()
print(stop - start)

