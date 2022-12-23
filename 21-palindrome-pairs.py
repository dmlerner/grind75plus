# https://leetcode.com/problems/palindrome-pairs/
# 7:24
# 7:27 idea
# 7:42 maybe
# 7:46 obvious bug found, now for obobs...
# 8:03 DLE (94/136 pass)
# 8:13, ah I need a Trie. And to stop for the night.
from david import *

from collections import defaultdict, Counter

class Solution:
    def palindromePairs(self, words):
        return list(palindrome_pairs(words))

def palindrome_pairs(words):
    words_by_first_letter = defaultdict(set)
    words_by_last_letter = defaultdict(set)
    counts_by_word = {}
    index_by_word = {}
    empty_word = None
    for i, word in enumerate(words):
        if not word:
            first, last = "", ""
        else:
            first, last = word[0], word[-1]
        words_by_first_letter[first].add(word)
        words_by_last_letter[last].add(word)
        counts_by_word[word] = Counter(word)
        index_by_word[word] = i

    # print(f'{words_by_first_letter =}')
    # print(f'{words_by_last_letter =}')
    # print(f'{counts_by_word =}')
    # print(f'{index_by_word =}')

    def palindrome(first_word, second_word):
        combined_counts = counts_by_word[first_word] + counts_by_word[second_word]
        length = len(first_word) + len(second_word)
        odd = length % 2
        odd_count = False
        def get(i):
            if i >= len(first_word):
                return second_word[i-len(first_word)]
            return first_word[i]

        for letter, count in combined_counts.items():
            if count % 2:
                if not odd or odd_count:
                    return False
                odd_count = True
                middle_char = get(length//2)
                if middle_char != letter:
                    return False

        i = length//2
        di = 0
        while True:
            try:
                if not get(i-di-(not odd)) == get(i+di):
                    return False
            except IndexError:
                return True
            di += 1

    for first_letter, first_words in words_by_first_letter.items():
        for first_word in first_words:
            if not first_word:
                second_words = words
            else:
                second_words = words_by_last_letter[first_letter]
            for second_word in second_words:
                if first_word == second_word:
                    continue
                if palindrome(first_word, second_word):
                    yield [index_by_word[first_word], index_by_word[second_word]]
                    if not first_word or not second_word:
                        yield [index_by_word[second_word], index_by_word[first_word]]



words = ["abcd","dcba","lls","s","sssll", ""]
words = ["a", ""]
words = ["ceihdihhjf","cgadb","cfhbaf","fcfbejidbddced","cihhbiajagbh","cabhfhch","gfhdcdhejigcc","g","cbhbcgch","difbbdhdhaeciib","effecbhbhdf","fgcafcd","efh","ijjajdcaj","aiaihadf","ef","ccceif","jfacd","fgcgfhfadhhgbbgfej","ebibdhabj","haegbddgahihieic","hhajiidj","jajhff","fffhhddfee","ea","hd","hbhdagbgjb","afhajbccijfadicebd","bcai","ijfdhibgejfjbaacifa","fbgafffffigbe","gdghjddjbja","cefjaebbgdgdih","cehjfb","bhidfccig","hhd","ccdhbdede","jjeae","hbaaghcccfcbeedagfg","dhjbb","cfbjifggehh","hjfcdgbijjcaj","djcjh","eajdjhihjjggicceadd","jdifcieabhbd","bfhdf","egafffffhgi","jdaceccg","ichfjd","badidae","igccchcdbigbhffcb","gffcecgajiieahcdhebi","eheeeciidfg","ga","haeifij","hbgjgbaig","jiehhdhjcaiagbfhgeah","fedig","bbgigihc","eicjffbjfcgch","j","dhb","jghighcdggdhieeeb","eahiabfeic","eecdjg","fdcf","gfggh","hjaifeeejahcb","iiibfggebecc","iiaaidecgcajjjbhfi","hcjbicbdch","gaicbddaf","iijhf","giaejieefchf","dhffaheghcafch","gjabdhhefdiaehjhjj","fhffbad","jdifdhfhfdcb","gfihcjacji","jefbejjgeahbjhijgg","dacbaiaibgjbfdcigie","idjgbfgjieidg","eejhghgcjhefgihgde","ecfdgeehdi","bbddhiiahdicbhdhjcbe","adfehde","bfg","fdhdcjagbbgdiij","jfijbbaghjjfgjaahf","aefdfigadfbghhbdjb","fchhgfjdfciehjici","fiiaic","a","gafjhejdcaghibjee","bggeaheggcfhe","bcdcijdcagbhfga","ee","jijbidb","dfhjeggbajcejddig","hfcejgdfejdgdcghfadd","cffcegcedfdi","cigigbif","cfacci","eeefghfhgigajb","jhhfhii","cbfj","ffc","cbfhbchigghiaeighcff","idiibcefghgeii","ghhgfcibj","bj","bahbcbig","difcajjfedbideggibca","hhbchfhe","eejefejfchaccgfcec","dceaag","hfebcbf","ffebfajachfid","fidjceeijiibe","gdcf","hja","hbacbbffbiafbaddgffi","ifeicggcgfddihjgcghj","gjchif","dbjgccigejjbafdedefg","gicjjeacejeaebdj","aghcfeibidebhbebbaa","id","fhcdbb","bhahe","ch","hjhii","cccgehajgcaijfggahca","adiegcibbhjad","djcbbibidhcghj","djhdbgechjcgif","eah","hgcf","hdb","bdhcdgbccaiebe","daiffbeg","hbfifcabjjcbbbgfcc","geghddihhjdjijhdc","dcba","ddcaggiefii","hhfgbf","fjhdedgeiajah","cfceffhjbjdee","iddhdaae","ageecde","fdf","dahc","chafidaaeh","ic","fdfifibjja","dhbhjjbef","jihgdjgegaj","dceeabhdicjjcbdfae","ec","dacfacbifdaidb","hdga","ji","didjjghgfecidfjjhdeb","cg","fa","bafdjeifbb","igeebdabeijbhdbj","bfchdfecbch","adegbgi","gicjia","ggbaegcabaigiaed","dh","d","bigadficje","hca","hhjecafijiebffgdji","aeeeefficab","addgehffb","fci","bghgfgcage","cafidhegehcjdbagic","egehiibbicd","dhjajggj","efbbbhifafgddidhc","bhhaffghebjcdfaagc","fdfahadidhbeachegg","cbihi","gfdhh","gddcidjafg","bhchddaggifchceedf","hcceecbeiaebbaiefi","effebhafgjcadbhheah","agadihecd","ebcadbjjfdddebfbgg","jjbcaceabicjcb","ebdaghghic","bhajb","jfifhgbhj","abdcfbjcdcbfig","agcga","jedcfihdbbfgefhjbeeg","ghechefddiac","agjhfeifhggecfeeje","fifjdhddchgee","ejidcdjjbebj","ccehcbaai","bifadabfeef","bcjbhgeeiihgggj","idhjhgdfjhjihhjj","agdbehhjdfdjab","bhgaddi","difjcbfdhi","affchbcjgb","cidijjic","ifbgjjbga","gacgaigejjfejcbc","babegbfabe","dgihbbhbfjigccidjaig","hhfegcbfdaa","iccda","gbfjgfjahicegfhgffj","fchdg","cfhdciiiddchhchb","diafafchccjhhchcfbc","befcaifhcebjdeghc","ihdbccgjjhe","iiigdec","eafaidf","chfee","bjjjabbibggad","jfjeb","dfbfiheceieja","hjfcfbhdhdgeeaee","fafbb","acijhacdhccbadfehbfb","bedfehgeidadgechddgd","dfbcbeifabfefigfi","iafbdc","acibc","bgehddbcecb","aaigbdaaefhcfhbfdfhh","ffaibdaghe","gchhbcficdeifidebcg","ccidaeeggh","aidcacdacaahhhbhfci","dd","fafehbgicjehbaj","eggdieibgaidhjjhfdj","jieeagfgbecfg","igjdihhcehiacheegaa","gejijggfjih","cjfbejbhfba","ifdb","ehhhgh","eaaabfge","agd","edffcjfjgbbjbcac","bafbhhecghf","da","begadd","fheggfhfcjhb","dhbb","efahf","eddcdagiejjibejc","cbjibibdhieii","edajcghgebcgfga","hghaeggea","bjecdbifg","afgajchhdfcbjcdajb","hdhadcdcabdbdb","dahgjdaeaddhhcafai","bebdg","eichhfagcahbiadh","gfahfcaiehiijigc","gibhcg","hef","jaiibaif","agecc","fajhbgfgh","fddacfcf","cgifaigbdadcefabfdia","gjdghcibhiaac","ae","hagiee","ajadhgccgb","iciaffifdicbd","hbgici","aejcbhdhaicdafebdad","gefjbcjdhg","eh","ibeaa","ffihdjachggficfehbb","jaahf","dgiaaacjcdhbeja","hgcajbi","jgjccbeigc","hjehjihi","bcjigii","aih","ggdjhfhaiccfieb","acgifejfjgb","ghfefbaijfdifjhjh","dbeeaeb","cidabj","ichjahdghf","hcejiaccggebj","djaaaecifecjegj","icgcbacebjcaaed","fga","djdahgghbafecjhgggha","hbhecfb","bfjaacif","eeidheg","b","ifjicahcgaba","cgagijiabddfjfgbj","fjgjeabgchheeedebbfd","edabdbdg","e","hhabcjfdajcj","cdihgdjeadcfcgfg","fidgjhccihdaiahfjad","babbfjdeg","igcbaid","affgaid","jfe","iideaa","fhhee","eecbefbajihegecjecai","bebgfechifdceihfj","gdcidfgh","daibbdeafd","aciaeehcag","iffedcbhahbejchc","gejbbijhfia","ejhdfajbechehjddd","afdcabfbbchbicfaeea","bdgbjaabafh","iahfjeg","haciacehiefhba","acdegchdb","ehbddfjdfjhahbggeje","bcaejdi","abhce","gdiicf","ebfgfhbegcbeecdh","efibajhieedic","bggfagageeijbcbhg","hgdgabbijadgecchee","ehgfihcijfefeacca","ffbfhgaebbbihbibgcf","cebj","dachdifb","cedbfgfid","fedbhhhdbhciifjghdc","afjghdbbefciba","febfefhiiaiegggic","egjchhehfaeacejg","jjagghagcfaiacadei","fcjigfbf","ehffdibghhcg","ibaeadhha","bachbfjjefbgab","bgaghbcdgdafaeaf","gggcegbhdibchggjhej","hfh","ihg","gac","bgbibicf","jhbceajacegabgc","gdijbejgfghfhjai","afijddcdjdehgji","hig","hiceebeccefieggi","ibejeejeijiidjbc","jebdbbhfifc","cahbajaaahf","ifdfeeeabec","cagfcjachhfffh","gfce","ejejfdgfc","dajjgjdafddf","ifcgechcc","ciiffheiffefbaadf","eijaiijccgfeb","bjbgaeijfdfcjhad","hjafeeeajc","gi","ihihj","i","hhjebbiicgfjbbciecf","eahhbie","gej","fb","ejfaagdefgh","gcaddjejd","aiedige","fdjhffdhbfdf","idcdfebiffi","bffbbbch","bajbcdcea","hajfgehfe","hgcidecedbddgae","hchijjhdbcbjdbfja","gjaejbdfgdcjdab","achhcaaei","ghbbe","hfidfjefbiaif","hhfbhgeedhgc","accajgcggdfa","ecbdcj","fgbf","gafdhbcfhehefffhj","hhg","gjcfchfeafcbgb","fbbdijjcc","fgacffcidh","fdgj","fbgadfheabdf","acfeebediijjdghgj","eijjgibdecfj","dbbj","daicjhchcchfcdh","jfjgdjfgcgi","baba","fedhibaifad","igehejicdgii","bdjhgch","eibhibajfccfiffh","faj","jdbhdihgiggfjfd","iieaajejdi","ehdgfc","gjcdgjjahhbeaafbcgg","hbecgccff","fbjeghfhgh","ddjbd","jjcffdij","jchhbf","ebafiggdhdibbdi","ib","jacigfjhbffjbd","afjigefihcabej","iaiccbhdgcahijhada","cihifhacdgjfacfej","iffigaaabfg","ccibccf","aajhjdfjhjdihdhbg","h","agcfieja","fjdgjiiabjdjdcfcdfb","jdjf","bdabcegcbdbbafce","jedifaejjggffef","cccah","heha","egfehaeie","ichffja","iachcedbg","ffiiibbec","adigide","jhcbchieabgajfcdh","cf","acdhgjiidjaiafchcfgi","hfci","dfaggfjehc","hgadjcfhhjjeiacd","gebjfajgaha","iajeiafc","dhe","aebeefdhfhhj","idja","eajh","hbadebdj","fcdceidehgjedhfh","jgghhaafi","ihigjc","jfegcjihfbjbgi","daebbihjiccd","bjd","acgchegfhedccaifc","bgcafedigicbffbjea","ggeajcadafdhgfecg","ccbcgecgcghcff","bdjeigghah","caehjfbebad","ibjjhahgf","ajbdhaabiebbjd","eccgifcccdacjcbce","jdbbhhb","fjaecagdgghi","eidciccjifighhffjecd","adcfbdecaehbhf","deaiig","eiajggaabjhgdgbdj","ddecjdc","ccibdeijbebfbe","igdhgdbhjhajaibiee","cfecfchgdch","ahaabdgibchcijceicd","ecjgfciahee","gciijjb","iajg","fgefbdb","jbdebf","cbb","ajaidd","bfghefdiecdea","gbddjj","chdb","fdfi","acdif","jdbhjhe","dbhcajicgdeicbggcgb","dcbfbafgbh","jbcdhgdbdjfd","eehehecgdgfejgjhifb","iaahaij","ffhjaibjihdgefg","eecedhdjehf","figgfhiia","ah","ebigjefcfegadghj","ededgbedaegeiffifjd","hdcciijhiid","fdehgbcaaddedbcebbgi","caciajjbege","aeecaeibaghhjggbadjg","achjai","geghfgicfhihhciggaj","feghgghcggc","cffjhbgfjb","adjbieig","aejjjg","bgghfgheechcgjiidf","ihbffed","ehfcdgffbicghhh","cfhefdidbjihhfcijhei","igficbj","abfeeghjc","hjid","bficcdeghcaed","hia","jgaabaajiggcgccjgj","ajiccddejgahdiddbii","djbeceahejhffcg","deejjfbgdadbajjdg","djijcjgdch","aihje","ajbdheebaadhjjidhjb","fcbgdjdgjfbd","dg","iag","cdceahbcijaeicfcjagg","bafdbdefhhbdg","fhdiijigcghihhjiah","fefhaedaajg","gibdbbfhfcjajif","jhigdid","bjhbg","jejg","fcbbbhdchc","cccdfhbijjdfcacfdegg","fjbdhccdcfiij","gfffibjjbjdbf","giccdjchhebfhjiddba","jhg","eidd","hicgfhfb","fabafcbfaaefgabef","gajegda","egjgffedcijd","fadafc","hjefbhjidichdejbibad","fjaiifgbjj","iaheejde","becfbgibhfadbig","c","habiibajcfaiihgg","bchfghdab","caj","ebgjgicijijigcgjjb","faggcaceaebghfc","aeeefajcijjffdej","ehcdjaiii","gdcejeed","bifjggajiehgggd","egacdbhgehjj","cddjiddj","idgagcejdijejhdhg","jhfahhcagdjechh","bbbeidjehhajj","dhijaegfiha","hedgeifaaefeehbigff","jgaifh","ibiacgeahieicdchfhd","hfedajjg","iccgggbecbj","effgbhgibaefga","jfadghhgfhgdjddecfd","dcdhg","abejdahiadbcihcf","dagjeg","hagedebfebjbejac","hadbjeeaghbjgbhhajh","jcagbjdbfe","caf","jbdcc","cbbffgb","acdijjcceffgcib","ddaabbdjigibeicfgefc","agjdhdedfechajjjf","idgeaiachii","aghfhgajgebgdcifgbjd","fha","gaadcgjaci","bh","ifgedi","gjaiebjiafbggbajf","adddachee","iaijfbfhfbjejbf","ifajegfbii","jhiabchddifjjg","afafdfjifgc","cebchcaaeaecbh","idigjejighhb","jfedejbjdbae","ccbjbdh","ibgebaeaigejcbgdjii","bi","ijgbfcecfgdbbaeeihj","aaiccbicde","cjieffjaifbe","hahabfddbe","caff","eheichbjgejhgcgeecca","dafi","fjbiejeaabcddaa","bcceciadcejghdjffcc","dghgfeeccidcbie","gijhcg","heaabebabebgdgdgb","abfdfdcgffihjfdef","abibbhceghjjejcaae","icdfdf","ihgfgceafggge","hadcecibdieag","agjabf","abaihg","jbcbb","icdfdigfj","cefa","eaiaagghbdhbjc","gcgcijdbaiibfhgheig","bhijfjejficea","cgbdhhbdhhicbb","bdjaad","dchajdgbdd","jddcbieficfe","ihahhffiafjecab","ifiefejhdgae","dfdjdebbdfhj","iijgijbfigdghb","abbi","hfahaeaefededhdg","jbgifbfefaidcjeeic","fagfdgjgebaedhd","bhdf","jbcgfh","jdhhdfeabiafjc","fchgejeibb","jcjccah","bigb","digijeacaafjbjaidi","hfabeicbffbhbiahcbed","chddfde","efegbhficfcfh","ihdgg","hcgdejbfbjjcb","ahcag","hjhffjihjg","bcbaidfgafecc","afafehajchfbhi","idbejgihdeia","daajgjahbfeij","jjdjicidiiiaefbibafc","iifhgdhcchaae","gahd","dgab","ccbcaebcigegighceica","ehgbjdgd","ajc","fgihdbhfebehgicdbhhc","eicfeajifbhif","igdacjf","giiaaijjjbccfbjfeigj","bedffcbjajieig","hfdichgjgcabfge","djghhef","jgaicjdajjdjahjiab","gacfgiadjeecgbgghhc","idhbdjbffefgbagjhf","gajadecgadje","gfbegidc","ihigjcdiff","jhgigjahjaifbce","cjghafff","jihcf","hheeeeddbajafff","dgcdcfcha","egbdcbg","iccj","adbfaiddch","iahacdbjgdgggigiejh","bjiedeadbjfcjfbce","bifbiiehfjifbjigi","iadcijefg","gecjhcbcjff","efggchbcidaeheged","eeacfdca","hegebejeigfjaf","iadeif","bhieceaghjihfigii","bihdefdcfbjjfbgfece","gbg","dggbeabgfddfjdhabb","acdbje","caecf","cijaejfhh","beeadha","hgfajfciafbej","fheigichbajbfj","becehfgddhbceiicg","dhecjha","cajaib","ecidghihidffhaaacf","fieahbfgbbijadjghjf","icjgdcfj","ajabeacfiahbhbbgicfj","hj","abghhcafebjcjigggidj","gadbifacejjaag","ifdf","icffjchfbgijebij","igaabaaefdhb","bhbiachcb","heddffihdedeffc","gffjg","fhae","adjhbfeeafgbfccbgj","defi","idecjibbdfiafhf","hagcicfac","idhdd","haaiadcgdaajieihjg","dhjhcjcijj","aefgecehagfeehhhhe","decficaijjaej","ecebficebafgid","dfhiaafd","edadgaibfdfj","bifighfgd","ajiijdbidjjgjca","effdgje","iajcjaeegafefgfb","jgiaddd","aibh","chjejdci","biggbjhageichidibhi","cb","fddfgciebfha","hgccbdabffhgg","jcgibeigcf","gffehegbjfcigbf","jfaaebifddgibcd","ihcagbggabbf","bifgdhcg","gijfeaiiaicjfhjgjg","hbgfhgg","dedfcjbejghfdgabbihg","dgficcaeieghaffef","fefddddfddhgifhfbgjf","dheicfcdifbjabgeg","cic","jhajfb","bbhfhgaibde","cedaeiggjgdcfa","jjjbgafgi","dfgccei","ffdgg","jfhhhjfhhdgheahhfgg","abjcgc","jihjg","dehjjfiijhc","ehjhbfgijf","fejgjgchdhidic","fgdeab","aje","bgiaijiidjfahifj","aaacjachejjabadbfd"]
dt, pairs = benchmark(lambda: Solution().palindromePairs(words))
pairs.sort()
print(dt)
expected = [[0,1],[1,0],[3,2],[2,4],[3,5]]
expected = [[0,1],[1,0]]
expected.sort()
print(pairs)
print(expected)
assert pairs == expected
