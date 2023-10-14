#include <iostream>
using namespace std;

int main()
{
    int ln = 1;
    int un = 60;

    srand((unsigned int)time(NULL));

//Time Unit
    int vari1 = 6;
    int RandIndex1 = rand() % vari1;
    string timeunitarray[vari1]={"seconds","minutes","hours","days","weeks","months"};
//Verb
    int vari2 = 6;
    int RandIndex2 = rand() % vari2;
    string verbage[vari2]={"paint","film","draw","write","photo","record"};
//Item
    int vari3 = 6;
    int RandIndex3 = rand() % vari3;
    string itemarray[vari3]={"a video","a painting","an illustration","a song","a story","a picture"};
//Nouns
    int vari4 = 1505;
    int RandIndex4 = rand() % vari4;
    string nounarray[vari4]={"slip","hockey","birthday","platinum blonde","page","dragon","cave","pistol","tom bombadil","hand","birth","zipper","telephoner","begonia","ferris wheel","stomach","zephyr","heart","pear","lettuce","peace","bronco","oil-rich seed","nudism","weight","thingumajig","chalk","selection","mass","attraction","smoke","feeling","hot air balloon","suit","trees","whey","carcas","board","payment","babies","jellyfish","prison","hotel","first name","road","ray","circle of life","graveyard","breath","wood chisel","steel","radio beam","stick","investment advisor","earthquake","space","foodstuff","wilderness","observation tower","squirting cucumber","increase","hobbies","chop shop","snakes","drain","brothers","slacks","guardsman","city limit","instrument","hole","ocean state","candlestick","sidewalk","tent","solar sound barrier","liquid","bomb","crib","nut","snowshoe hare","yard","external maxillary artery","primitive baptist church","leg extensor","mortician","magic","slave","trouble","card","pocket","wave","litter pan","vanquisher of everything","daughter","screw","team","bedroom","walk","brass","laborer","miner’s lettuce","point","news","glass","nose","income","start","place of business","peg leg","knee","lieutenant governor","process","sack","crack","cream colored sofa","fool’s huckleberry","rattail cactus","bear","female monarch","soda","protest","puppy","grape","measure","things","climbing madman","kite","anger","first born","middling","knight’s service","statement","dirt","brakes","dog poop","zoo","life raft","cheese","lizards","clover","offer","writing","spiders","harbor","distribution","buster","rat kangaroo","anti-takeover building","cherry","bouncy ball","snail","watch","scentless sanatorium","disgust","hourglass","red cape","wish","stick figure","repayment","recess","key","distance","party","push","fog","stove","nation","sleet","unilateral quark decision","toys","berry","unearned increment","cookie","suggestion","care","invisibility cloak","vein","slippers","wind","crate","sweatpants","fool’s huckleberry","building","reading","need","library","lip","biology lab","ukulele","family","science","street","mind","kick","pipe","stone","hose","fall","year","leafy spurge","iron","slacker","destruction","paving sandpiper","secondhand car","giants","christian science","sock gnomes","dogs","number","yogurt","dentist’s drill","aunt","debt","bath","nibblets","rat","wood","personal credit line","tax","tomato concentrate","veggieland","cow","unicorn","belief","son","inner resource spiral","join","dinosaurs","exchange","beam","polish","counterbalance","ear","horn","boric acid","pan","modern times","antidepressant drug","wrist watch","dock","change for the good","cuban monetary unit","dust bunny","goat","division","song","computer file name","seal","notebook","humor","railway","corn","overstuffed chair","fact","toilet","motor hotel","reading party","primogenitor","sideboard","cavity search","relation","nut grass","tin","cart","carrot","hope","reward","plough","toes","red currant","bigwig","mine","boys","flame","beef","flight","example","deer","sweet tailpipe","arithmetic","pendulum clock","wine palm","trust fund","hall","uncle","jellybean","bridge","crush","suburbanite","bakery","fuel","chain","operating capital","vacation","dress","religion","curtains","stream","men","part","apostrophe","observation","wax","spark","bottom layer","grade","horses","giraffe","vessel","patch","government","gym rat","produce","mucous secretion","sand dollar","cub","coil","won-lost record","ideal inconstancy","jail","trousers","school bus","the nested plunge","pelican","oatmeal","article of furniture","machine","size","child prodigy","swimsuit","office","class","skin","burn","discussion","body","kentucky fried chicken","phonograph record","hurricane","spot","jar","winter","sky","ferret","lunchroom","mask","vase","private investor","mimicker","cellar","wild, wild sheep","stop","stage","brake","verse","planes","bucket","cape town","pile of decomposition","dinner","friends","international law enforcement agency","voting waistline","fowl","matrimonial law","perverted photography","yak","control","lan","bait","houses","carcinogen","senor","crime","idea","light bulb","toast","tea cosy","hellfire raising preacher","language","erie canal","rabbit","straw","globophobia","amphibian","pleasure","cyrus the elder","bull pine","amish sect","bracelet","thermal emission","fork","linen","record","playground","doctor","national security agency","existence","teaching","drug addict","writer","society","hairy lip fern","faucet","elegant cat’s ear","basin","baseboard","death","common iguana","humidity","silk","karate","friend","stolen property","town","fruit","brigand","duck","thread","brother","wedge bone","sofa","hyacinth","brick","range","field","foot","lunch meat","obviousness","aspen pine","school","chronic bronchitis","broken printer","hot","jungle psychology","gold","upholstery","lead","noise","pail","chief justice","love grass","tail","lathe","strep throat","winter squash plant","shoulder pads","bike","pelted orphan","violin","chicken","detail","ring","string","flag","latency","cause","pig","donkey","raspberry bush","plants","experience","chair","bag","vehicular traffic of the ear","net","group","sense","food","upper limit","week","shamanism","apple","umbrella","degree","pull","descending color","feather","bean","volcanic crater","wash","store","gothic romance","trip","root","positive feedback","general baptist","chemist","oil","onionskin","caution sign","mediation","company","scottish terrier","moral philosophy","chicken stew","cat flea","reaction","mark","juice","japanese jelly","bunny","cupcake","jump","station","jailbreak","invention","cough","beggar","landmine","the ways of the world","chairs","twist","administrative hearing","banana","thumb","plant","grandmother","carousel","representative","earth","tentacle","heat","suitcase","lock","dog","stetson hat","swat","lake","indirect expression","shivering pink toenails","scene","mad-dog skullcap","ornament","plot","level","rain","hunting ground","swim","hub","creature","snails","stamp","collar","friction","tract of arms","clam","scorpion","dust","third baseman","connection","meal","manager","multi-billionaire","woman","stranger","roof","political party","flame fish","stole","pets","bell glass","police","lemon lily","stew","coach","servant","game-board","natural history","french bread","bus","stem","backhoe","time","fairies","gate","middle","rocket sack","rate of exchange","claw","tiger","cook","throat","porter","top","shoe","farm","position","morning","painted tortoise","crow","miles standish","sweatsuit","scientific method","health","barrel","voice","view","grain","lamp","holiday","trains","rose","hydrogen","profit","downtown","rainstorm","talk","boy","chess","locker room","unit","trucks","mint","canvas","insurance","story","wealth","zinc","consumer","stitch","sailfish","button","waves","prickly-seeded spinach","laugh","kangaroo’s-foot","trick","unemployed people","crayon","hot seat","flyleaf","behavior","guide","cats","lecherous fern","order","drawer","depersonalization disorder","butter","substance","pipefitting","regional atomic mass","volleyball","birthday cake","soap","milk","trampoline","tendency","sledding people","lighthouse","optical crown glass","edge","arm candy","grandfather","false schoolyard","larch","secretary","sea anemone","hyena","north","birth","christian hero","sunglasses","pollution","electric furnace","glove","kangaroo’s-foot","mathematics department","amusement","mom","front","cast","plane","knife","shelf","antelope","rule","turn","cobweb","ink","hour","quilt","carpenter","hygienic","old church slavonic","scarecrow","fiction","soup","brush","shorts","physics lab","wiener","test","river","transport","notions counter","curtain","speaker","manure","dare","ice","fairy lantern","pilot chart","breakfast table","copper","match","bubble","bed","skull","park","kettle","fang","hat","bare bottom","class fellow","play","industry","kitty","jeans","lunch","skin","sex shadowgraph","muscle","planetary house","false partnership","olfactory bulb","grass","striped hyena","pies","frog","pillow","night","shorthair","month","upset stomach","end","lined snake","blow","flesh","hubcap","sleep","request","colored audition","climbing madman","drug","rough-skinned newt","stock car","motor-truck","doll","governor","cattle","flavor","tractor","totem","children","sheep dip","ground","mist","aggressive criminal","use","pin","rainbow flag","extremity","sheep","color","self-renewal","coal","lumber","storage battery","orbital plane","beanie","music","cover","crowd pleaser","twisting parsnip","scale","sign","reg ret","pigs","eggs","breakfast","decision","rub","sound","knowledge","system","radio beam","weather","thing","pole dancer","strawberry daiquiri","bead","twinkling uncleanness","angelfish","internal respiration","trumpet section","man","cakes","letter","burglar alarm","pest","potato","sea barnacle","light","camera","back","department of justice","print","direction","flying fish","horse","flock","market","toothbrush","pet","legs","rabbits","sea cow","girls","jerusalem cherry","mermaid egg","saddle horse","pencil","history","bun","industrial park","presbyterian church","upholsterer","bite","title","jelly","cherries","upper limit","sand","musical chairs","run","pippin","town planning","chemical science","joke","badge","bone","false schoolyard","sock","brain","african yellowwood","wheel","line","sheet","artillery range","egg","notepad","bushes","event","facility","cord","disease","pocket flask","bread","feast","hospital","obsessive-compulsive disorder","air","festival of lights","time limit","hen","locomotive","smile","candy kiss","authority","truck","parent","oranges","stockings","current","clock","jewel","shop","sail","marble","knight’s service","sweater","digestion","insect","carriage","minute","opinion","glue","thought","eternal life","spring","space emulator","fur ball","dentist’s drill","sinus","plantlet","competition","credit","committee","sink","six-gilled shark","constructor","seat","preventive strike","belly dance","crowd","opera singer","voyage","thrill","boiling water","plantation","bee","house","beetle","passenger","willow","toejam","yoke","overlord","corn cake","tissue paper","treatment","sombrero","pizza","quantum leap","cars","shade","kitten","lasagna","hair","tongue","miner’s lettuce","partner","seashore","beast","tense system","plate","organization","tooth","anaconda","clan member","good-bye","microwave radar","mountain","laundry","can","visitor","water","glitter","steam","sisters","tank","rifle","cloth","punishment","meat","pot","game","chief constable","cultivated strawberry","print","curve","general knowledge","camp","face card","baby","finger","temper","calendar","leaf","throne","shotgun","bipolar cupcake","dime","praying mantis","receipt","frump","cap","monkey","fish","map","comparison","harmony","command prompt","logroller","place","hippopotamus","mice","head","eskimo dog","burst","car","riddle","smash","rate","blade","skirt","popcorn","diplomatic negotiations","cows","stocking","paper","sewing-machine operator","fan","plot","mitten","room","ghost","copy","trail","suit of armor","ninja","boundary","scum bag","perennial ragweed","revivalist","cat","bears","eye","sweatshirt","van","believer","star","cake","haircut","purpose","club","hood","suspenders","travel guidebook","way","snake","chemical plant","nest","wire","sister","ocean","fireman","toe","generalized seizure","lawyer","elastic band","journey","leg","toothpaste","burying ground","negative moon","basket","check mark","rowboat","mother","wing","paint","bathrobe","remnants of chaos","clocks","spy","flower","owl","metal","cemetery","move","book","wrist","nervelessness","battle","six day war","skinny","basketball","patrol","thunder","mental disorder","fear","description","letters","frogs","bareboat","dog sled","hands","tray","dissension","surprise","education","toad","rake","sneaky snake","motion","meeting","spoon","hovercraft","whip","wrinkle","governing body","twig","smell","territory","island","cardiologist","lace","marching band","dad","pickle","love","pizzas","war","person","loss","telephone","bloodstained carpet","rhythm","conjugal visitation","balloon","ball","garden","taste","rod","box","oven","lift","hotdog","presidency","interest","wellbeing","church","help","tree","sea cucumber","promotion system","liquid oxygen","summer","veil","expert","balance","side","yam","baseball","play therapy","mother figure","drum","greater green mamba","soft mouth police","impulse","shirt","fistful","girl","growth","calculator","spade","loaf","toy","army","ducks","theory","farmer","licensed rat breeder","scallop","kazoo","indigestion","kola nut tree","memory","touch","judge","expansion","captain fantastic","firehouse","cable","hearing","laser beams","nerve","cracker","plastic","sun","contradictoriness","underwear","yellowstone river","error","country","self incrimination","law","ship","orange","operation","rice","moon","grape jelly","shoes","creator","beds","hydrant","money","respect","snow","time and a half","dinnertime","poison","sentry box","knot","business","the defection stock","snake fern","tomatoes","fly","texture","gun","honey","frozen food","needle","northern snakehead","pump","fire","white-headed mongo","paste","test copy","tub","european brown bat","legal document","support","nudist camp owner","show","pudding stone protector","rouge grandma","aspirin powder","sundress","ticket","pervasiveness","low","hook","list","caption","price","elbow","gorilla","police squad","sutural bone","skate","engine","poison gas","tailspin","scarf","minister","whistle","sea","whole blood","vegetable","beginner","feet","priory","toast mistress","spiral cake","sky burial","hoe","british columbia","crook","patrolman","cream","city boy","bruges","sinus delay","carnival","baloney","celery","leaf-nosed snake","dry wall","bird dog","railroad worm","tramp","teeth","cottage pie","bat","wine","day","circus","messiness","merry bells","turkey","battle of bull run","junker","women","structure","working papers","dingleberry","door","cactus","ladybug","effect","wet suit","nail","shock","gas fitter","locket","table","father","painting","oil well","train","cent","sneakers","natural childbirth","mouth","lecher","comb","cork","dicky","eye disease","beefsteak","scissors","wall","towelette","discovery","owner","salamander","hydrofoil","step","landscape painting","silver","statue","cloud","grinning guardsman","comptroller general","volcano","sneeze","coat","grip","neck","irish republican army","jam","jungle warfare","mailbox","route","leather","revenue tariff","clothesline","wool","fight","name","bulb","cup","fold","fairies","wood garlic","keepsake machete","trade","control account","salad","exorcism","book of smut","squirrel","tissue typing","bells","pie","election","blink of an eye","sponge","salt","zebra","self-taught art","internal control","sealion","brainchild","work","eggnog","picture","bell","swing","floor","ship’s company","conditional reaction","note","pain","crown","wrench","hammer","sugar","lynch law","cry","bird brain","colombian hitman","selection","geese","mulled cider","bird","town clerk","rock","powder","people","mistress","solar furnace","value","test paper","private area","home","trickle trails","square","elegant cat’s ear","character witness","constant reminder","rest","nonbeliever","condition","rainbows","wren","ice cream","pancake","clouds","word","desk","dick head","bathing suit","dolls","boot","short-haired idiot","sort","desire","yarn","refrigerator","development","spacesuit","atlantic sailfish","maid","wound","tract of arms","ascending artery","hill","codswallop","jet ski","drop","cornish hen","suckling pig","roadblock","chin","branch","design","alligator","limit","vest","power","divergent thinking","rail","roll","property","coffee pot","icicle","lips","linoleum cutter","robin","sportswoman","reason","driving","disk file","cushion","coffee table","land","lamb","self-sacrifice","drink","poop","ship’s company","force","fourth power","pen","cabbage","gentlefolk","double fault","tire iron","parcel","sphere of influence","window","normal distribution","unit of unholy depth","frame","furniture","antechamber","shape","laura","bad tempered nun","rings","boat","cannon","skull and crossbones","waste","carrot people","slope","kiss","worm","kittens","guitar","circle","library","face","latex","chickens","prose","goose","form","goldfish","republic of tunisia","banjo","stretch","sticks","polka dot","car loan","coast"};
//Noun2
    int RandIndex5 = rand() % vari4;
//Emotion
    int vari6 = 6;
    int RandIndex6 = rand() % vari6;
    string emotionarray[vari6]={"happiness","sadness","joy","fear","anger","envy"};

//Print
    cout<<"You have " << ln+rand() % static_cast<int>(un-ln+1) << " " << timeunitarray[RandIndex1] << " to " << verbage[RandIndex2] << " " << itemarray[RandIndex3] << ". Your keywords are " << nounarray[RandIndex4]  << ", " << nounarray[RandIndex5]  << ", and " << emotionarray[RandIndex6] << ". Good Luck!";
    return 0;
}
