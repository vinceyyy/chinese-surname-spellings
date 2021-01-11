# chinese-surname-spellings

A table contains common chinese surnames and all the possible spellings, to make life easier.

Souce:

1. Surnames from Wiki https://zh.wikipedia.org/wiki/中国姓氏排名 2013 年 4 月 first 300 surnames. Convert to pinyin using [pypinyin](https://github.com/mozillazg/python-pinyin).
   Finding old Wade-Giles spelling for chinese surnames is harder than I thought. I cannot find a tool, a chart, or even the name of the system that converts 李 to Lee. Eventually I found the list at https://www.cnblogs.com/geovindu/archive/2009/12/12/1622658.html and it looks good enough.
2. Wiki https://zh.wikipedia.org/zh-hans/漢姓羅馬字標注

# Output

| chinese | pinyin    | taiwan                      | hk         | macau            | singapore           | wade_giles                 |
| ------- | --------- | --------------------------- | ---------- | ---------------- | ------------------- | -------------------------- |
| 赵      | ZHAO      | CHAO                        | CHIU       | CHIO             | TEO/TIO             | CHIU                       |
| 钱      | QIAN      | CHIEN                       | CHIN       | CHIN             | ZEE/CHEE            | CHIN                       |
| 孙      | SUN       | SUN                         | SUEN       | SUN              | SOON/SNG            | SUEN/SHUEN                 |
| 李      | LI        | LEE/LI                      | LEE/LI     | LEI              | LEE                 | LI/LEE                     |
| 周      | ZHOU      | CHOU                        | CHOW/CHAU  | CHAO             | CHEW                | CHAU/CHOW                  |
| 吴      | WU        | WU                          | NG         | NG               | GOH/NGO             | NG                         |
| 郑      | ZHENG     | CHENG                       | CHENG      | CHEANG           | TAY                 | CHENG/CHANG                |
| 王      | WANG      | WANG                        | WONG       | VONG/WONG        | ONG/HENG/WONG/WANG  | WANG/WONG                  |
| 冯      | FENG      | FENG                        | FUNG       | FONG             | PANG                | FUNG                       |
| 陈      | CHEN      | CHEN                        | CHAN       | CHAN             | TAN/CHAN/TING       | CHAN/TAN/CHEN              |
| 褚      | CHU       | CHU                         | CHU        | CHU              | THI/SOO             |                            |
| 卫      | WEI       | WEI                         | WAI        | WAI              | WEE                 | WAI                        |
| 蒋      | JIANG     | CHIANG                      | CHEUNG     | CHEONG           | CHIO                | CHEUNG                     |
| 沈      | SHEN      | SHEN                        | SHUM/SUM   | SAM              | SIM                 | SHUM/SUM                   |
| 韩      | HAN       | HAN                         | HON        | HON              | HANG                | HON                        |
| 杨      | YANG      | YANG                        | YEUNG      | IEONG            | YEO/YEOH/YONG       | YEUNG/YANG/YOUNG           |
| 朱      | ZHU       | CHU                         | CHU        | CHU              | CHOO                | CHU                        |
| 秦      | QIN       | CHIN                        | CHUN       | CHUN             | CHIN/CHING          | CHUN                       |
| 尤      | YOU       | YU                          | YAU        | IAO              | YEW                 | YAU                        |
| 许      | XU        | HSU                         | HUI        | HOI/HUI          | HEE/KOH/KHOH        | HSUI/HUI/HSU               |
| 何      | HE        | HO                          | HO         | HO               | HOR/HOH             | HO                         |
| 吕      | LU/LYU/LV | LU                          | LUI        | LOI              | LI                  | LUI                        |
| 施      | SHI       | SHIH                        | SZE        | SI               | SI/SEE              | SEE/SZE/SHIH/SI            |
| 张      | ZHANG     | CHANG                       | CHEUNG     | CHEONG           | TEO/TEOH/CHEONG     | CHEONG/ZHANG/CHIANG/CHEUNG |
| 孔      | KONG      | KUNG                        | HUNG       | HONG             | KHONG               | HUNG                       |
| 曹      | CAO       | TSAO                        | CHO/TSO    | CHOU             | CHOW/CHAU           | CHO/TSO                    |
| 严      | YAN       | YEN                         | YIM        | IM               | GIAM/NGIAM          | YIM                        |
| 华      | HUA       | HUA                         | WA/WAH     | VA               | HOA/HUA             | WAH                        |
| 金      | JIN       | CHIN                        | KAM        | KAM              | KIM                 | KAM                        |
| 魏      | WEI       | WEI                         | NGAI       | NGAI             | GUI/NGUI            | NGAI                       |
| 陶      | TAO       | TAO                         | TO/TAO     | TOU              | TAU/TOW             |                            |
| 姜      | JIANG     | CHIANG                      | KEUNG      | KEONG            | KIANG               | KEUNG                      |
| 戚      | QI        | CHI                         | CHIK       | CHEK             | CHEK                | CHI/CHICK/CHIK             |
| 谢      | XIE       | HSIEH                       | TSE        | CHE              | CHEAH/TAY/CHIA      | TSE                        |
| 邹      | ZOU       | TSOU                        | CHAU/CHOW  | CHAO/CHAU        | CHEW/CHOU/CHU       | CHAU/CHOW                  |
| 喻      | YU        | YU                          | YU         | U                | ZU/JOO/JU           |                            |
| 柏      | BAI       | PO                          | PAK        | PAK              | PEK/PEH             | PAK                        |
| 水      | SHUI      | SHUI                        | SUI        | SOI              | CHWEE/CHUI          |                            |
| 窦      | DOU       | TOU                         | TAU        | TAO              | TOU/TOH             | TAU                        |
| 章      | ZHANG     | CHANG                       | CHEUNG     | CHEONG           | CHIO/CHIOH/CHEOH    | CHEONG                     |
| 云      | YUN       | YUN                         | WAN        | WAN/VAN          | HOON/HUNG           |                            |
| 苏      | SU        | SU                          | SO         | SOU              | SOH                 | SO                         |
| 潘      | PAN       | PAN                         | POON/PUN   | PUN              | PHUA                | POON/PUN                   |
| 葛      | GE        | KO                          | KOT        | KOT              | KAT/KUAH            | KOT                        |
| 奚      | XI        | HSI                         | HAI        | HAI              | HEE                 |                            |
| 范      | FAN       | FAN                         | FAN        | FAN              | HUANG               | FAN                        |
| 彭      | PENG      | PENG                        | PANG       | PANG             | PEH                 | PANG                       |
| 郎      | LANG      | LANG                        | LONG       | LONG             | LONG/LANG           |                            |
| 鲁      | LU        | LU                          | LO         | LOU              | LOO                 | LO                         |
| 韦      | WEI       | WEI                         | WAI        | WAI              | WEE                 | WAI                        |
| 昌      | CHANG     | CHANG                       | CHEUNG     | CHEONG           | CHIANG              |                            |
| 马      | MA        | MA                          | MA         | MA               | BEH                 | MAR/MA                     |
| 苗      | MIAO      | MIAO                        | MIU        | MIO              | MIAU                | MIU                        |
| 凤      | FENG      | FENG                        | FUNG       | FONG             | HONG                |                            |
| 花      | HUA       | HUA                         | FA         | FA               | HUAY                | FA                         |
| 方      | FANG      | FANG                        | FONG       | FONG             | PNG/PUNG            | FONG/FANG                  |
| 俞      | YU        | YU                          | YU         | U                | JOO/JU              | YU/YUE                     |
| 任      | REN       | JEN                         | YAM        | IAM              | ZIM/JIM             | YAM                        |
| 袁      | YUAN      | YUAN                        | YUEN       | UN/IUN           | WANG                | YUEN                       |
| 柳      | LIU       | LIU                         | LAU        | LAO              | LEW                 | LAU                        |
| 酆      | FENG      | FENG                        | FUNG       | FONG             | HONG                |                            |
| 鲍      | BAO       | PAO                         | PAU        | PAO              | POW/PAU             |                            |
| 史      | SHI       | SHIH                        | SZE        | SI               | SZE/SU/SER          | SI                         |
| 唐      | TANG      | TANG                        | TONG       | TONG             | TNG/TANG            | TONG                       |
| 费      | FEI       | FEI                         | PEI        | PEI              | HWEE/HUI            |                            |
| 廉      | LIAN      | LIEN                        | LIM        | LIM              | LIAM                |                            |
| 岑      | CEN       | TSEN                        | SUM/SHUM   | SAM              | NGIM                | SHUM                       |
| 薛      | XUE       | HSUEH                       | SIT        | SIT              | SIH                 | SIT                        |
| 雷      | LEI       | LEI                         | LUI        | LOI              | LUI                 | LUI                        |
| 贺      | HE        | HO                          | HO         | HO               | HOR                 | HO                         |
| 倪      | NI        | NI                          | NGAI       | NGAI             | GEH/GOI             | NGAI                       |
| 汤      | TANG      | TANG                        | TONG       | TONG             | TNG                 | TONG                       |
| 滕      | TENG      | TENG                        | TANG       | TANG             | TENG/THENG          |                            |
| 殷      | YIN       | YIN                         | YAN        | IAN              | YAM/HNG/HEUNG       | YEN/YAN                    |
| 罗      | LUO       | LO                          | LAW/LO     | LO               | LO/LOR/LAW          | LAW                        |
| 毕      | BI        | PI                          | PUT        | PAT              | BIK                 | PAT                        |
| 郝      | HAO       | HAO                         | KOK        | KOK              | HOW/HAK             |                            |
| 邬      | WU        | WU                          | WU         | VU / WU          | WOO                 |                            |
| 安      | AN        | AN                          | ON         | ON               | ANN/ANG             | ON                         |
| 常      | CHANG     | CHANG                       | SHEUNG     | SHEONG           | SEONG/SIONG/SIOH    |                            |
| 乐      | YUE       | YUEH                        | LOK/OK     | LOK/OK/NGOK      | LAK                 | LOK                        |
| 于      | YU        | YU                          | YU         | U                | YEE                 |                            |
| 时      | SHI       | SHIH                        | SEE/SZE    | SI               | SEE/SI              | SI                         |
| 傅      | FU        | FU                          | FU/FOO     | FU               | POO/POH             | FU                         |
| 皮      | PVANI     | PI                          | PEI        | PEI              | PUAY                |                            |
| 卞      | BIAN      | PIEN                        | PIN        | PIN              | PIANG               | PIN                        |
| 齐      | QI        | CHI                         | CHAI       | CHAI             | CHEE                | CHAI                       |
| 康      | KANG      | KANG                        | HONG       | HONG             | KANG/KHANG          | HONG                       |
| 伍      | WU        | WU                          | NG         | NG               | NG/NGOH             | NG                         |
| 余      | YU        | YU                          | YU/YUE     | U                | EU/YEE/I            | YU                         |
| 元      | YUAN      | YUAN                        | YUEN       | UN / IUN         | NGUANG              |                            |
| 卜      | BU        | PU                          | PUK        | POK              | POK                 |                            |
| 顾      | GU        | KU                          | KOO        | KU               | KOH                 |                            |
| 孟      | MENG      | MENG                        | MANG       | MANG             | MENG                | MANG                       |
| 平      | PING      | PING                        | PING       | PENG             | PENG/PHENG          |                            |
| 黄      | HUANG     | HUANG                       | WONG       | VONG/WONG        | NG                  | HWANG/WONG/HUANG/VONG      |
| 和      | HE        | HO                          | WO         | VO               | HUA/HOA             | WO                         |
| 穆      | MU        | MU                          | MUK        | MOK              | MOK                 |                            |
| 萧      | XIAO      | HSIAO                       | SIU/SHIU   | SIO              | SEOW/SIAO           | SIU/SHIU                   |
| 尹      | YIN       | YIN                         | WAN        | WAN              | UN/EUNG             | WAN                        |
| 姚      | YAO       | YAO                         | YIU        | IU/IO            | YEO                 | YIU                        |
| 邵      | SHAO      | SHAO                        | SIU/SHIU   | SIO              | SHAW/SEOW/SIOH      | SIU                        |
| 湛      | ZHAN      | CHAN                        | CHAM       | CHAM             | KAM/KHAM            |                            |
| 汪      | WANG      | WANG                        | WONG       | VONG/WONG        | WANG                | WONG                       |
| 祁      | QI        | CHI                         | KEI        | KEI              | KEE                 |                            |
| 毛      | MAO       | MAO                         | MO         | MOU              | MOH/MOR             | MO                         |
| 禹      | YU        | YU                          | YU         | U                | WOO                 |                            |
| 狄      | DI        | TI                          | TIK/DICK   | TEK              | TEK                 |                            |
| 米      | MI        | MI                          | MAI        | MAI              | BEE                 |                            |
| 贝      | BEI       | PEI                         | PUI        | PUI              | PUAY                |                            |
| 明      | MING      | MING                        | MING       | MENG             | MENG                | MING                       |
| 臧      | ZANG      | TSANG                       | CHONG      | TSANG/CHANG/CHAN | TSANG/CHANG/CHAN    |                            |
| 计      | JI        | CHI                         | KAI        | KAI              | KOI                 |                            |
| 伏      | FU        | FU                          | FUK        | FOK              | HOK                 |                            |
| 成      | CHENG     | CHENG                       | SHING/SING | SENG             | SENG                | SING/SHING                 |
| 戴      | DAI       | TAI                         | TAI        | TAI              | TE/TO/TOR           | TAI/TYE                    |
| 谈      | TAN       | TAN                         | TAM        | TAM              | TAM                 | TAM                        |
| 宋      | SONG      | SUNG / SOONG                | SUNG       | SONG             | SONG                | SUNG                       |
| 茅      | MAO       | MAO                         | MAU        | MAO              | MAU/MOW             |                            |
| 庞      | PANG      | PANG                        | PONG       | PONG             | PANG                | PONG                       |
| 熊      | XIONG     | HSIUNG                      | HUNG       | HONG             | HIM                 | HUNG                       |
| 纪      | JI        | CHI                         | KEI        | KEI              | KEE                 | KEI                        |
| 舒      | SHU       | SHU                         | SHU        | SHU              | SOO/SU              | SHU/SHUE                   |
| 屈      | QU        | CHU                         | WAT        | VAT / WAT        | KUT/KUK             | WAT/WUT                    |
| 项      | XIANG     | HSIANG                      | HONG       | HONG             | HANG                |                            |
| 祝      | ZHU       | CHU                         | CHUK       | CHOK             | CHOK                |                            |
| 董      | DONG      | TUNG                        | TUNG       | TONG             | TANG/TONG           | TUNG                       |
| 梁      | LIANG     | LIANG                       | LEUNG      | LEONG            | NEO/NIO/NIU         | LEONG/LEUNG/LIANG          |
| 杜      | DU        | TU                          | TO/TAO/TOE | TOU              | TOH/TOO             | TAO/TO                     |
| 阮      | RUAN      | JUAN                        | YUEN       | UN               | NGWAN/NGUANG        | YUEN                       |
| 蓝      | LAN       | LAN                         | LAM/NAM    | LAM              | NAH                 | LAM/LARM                   |
| 闵      | MIN       | MIN                         | MAN        | MAN              | MIANG               |                            |
| 席      | XI        | HSI                         | TSIK       | CHEK             | CHEOH/CHIOH         |                            |
| 季      | JI        | CHI                         | KWAI       | KUAI             | KWEE/KUI            |                            |
| 麻      | MA        | MA                          | MA         | MA               | MUA                 |                            |
| 强      | QIANG     | CHIANG                      | KEUNG      | KEONG            | KIANG/KHIANG        | KEUNG                      |
| 贾      | JIA       | CHIA                        | KA         | KA               | KA/KIA              | KAR                        |
| 路      | LU        | LU                          | LO         | LOU              | LOH                 |                            |
| 娄      | LOU       | LOU                         | LAU        | LAO              | LOO                 |                            |
| 危      | WEI       | WEI                         | NGAI       | NGAI             | NGUI/NGWEE          |                            |
| 江      | JIANG     | CHIANG                      | KONG       | KONG             | KANG                | KONG                       |
| 童      | TONG      | TUNG                        | TUNG       | TONG             | TONG/THONG          | TUNG                       |
| 颜      | YAN       | YEN                         | NGAN       | NGAN             | GAN/NGAN/NGANG      | NGAN                       |
| 郭      | GUO       | KUO                         | KWOK       | KUOK/KUOC        | KUEH/KUEK/KOAY/QUEK | KWOK                       |
| 梅      | MEI       | MEI                         | MUI        | MUI              | BOEY/BUAY           | MUI                        |
| 盛      | SHENG     | SHENG                       | SHING      | SENG             | SENG                | SHING                      |
| 林      | LIN       | LIN                         | LAM        | LAM              | LIM/LAM             | LAM/LIM/LUM                |
| 刁      | DIAO      | TIAO                        | TIU        | TIU              | TEOW/TIAU/TIAO      |                            |
| 锺      | ZHONG     | CHUNG                       | CHUNG      | CHONG            | CHENG               |                            |
| 徐      | XU        | HSU                         | CHUI/TSUI  | CHOI             | SU/CHEE/CHER/CHEU   | TSUI/CHUI                  |
| 邱      | QIU       | CHIU                        | YAU        | IAO/IAU          | KHOO                | YAU/YAO                    |
| 骆      | LUO       | LO                          | LOK        | LOK              | LOK                 | LOK                        |
| 高      | GAO       | KAO                         | KO         | KOU              | KOH/KOR             | KO                         |
| 夏      | XIA       | HSIA                        | HA         | HA               | HAY                 | HA                         |
| 蔡      | CAI       | TSAI                        | CHOI/TSOI  | CHOI             | CHUA                | CHOI/CHOY/TSOI             |
| 田      | TIAN      | TIEN                        | TIN        | TIN              | CHAN                | TIN                        |
| 樊      | FAN       | FAN                         | FAN        | FAN              | HAN/HUANG           |                            |
| 胡      | HU        | HU                          | WOO/WU     | VU/WU            | OH                  | WOO/WO/WU                  |
| 凌      | LING      | LING                        | LING       | LENG             | LENG                | LING                       |
| 霍      | HUO       | HUO                         | FOK        | FOK              | KAK/KHAK            | FORK/FOK/FOG               |
| 虞      | YU        | YU                          | YU         | U                | NGOH/NGOR           | YU                         |
| 万      | WAN       | WAN                         | MAN        | MAN              | MAN/BUANG           | MAN                        |
| 支      | ZHI       | CHIH                        | CHI/TZE    | CHI              | CHEE                |                            |
| 柯      | KE        | KO                          | OR         | O                | KOA/KWA/KUA         | OR                         |
| 昝      | ZAN       | TSAN                        |            |                  |                     |                            |
| 管      | GUAN      | KUAN                        | KWUN       | KUN              | KUANG/KWAN          |                            |
| 卢      | LU        | LU                          | LO/LU/LOO  | LOU              | LOH                 | LO/LOO/LOW                 |
| 莫      | MO        | MO                          | MOK        | MOK              | MOK                 | MOK                        |
| 经      | JING      | CHING                       | KING       | KENG             | KENG                |                            |
| 房      | FANG      | FANG                        | FONG       | FONG             | PANG                |                            |
| 裘      | QIU       | CHIU                        | KAU        | KAO              | KEW                 |                            |
| 缪      | MIAO      | MIAO                        | MIU/ MAU   | MIO              | MOK                 |                            |
| 干      | GAN       | KAN                         | KON        | KON              |                     |                            |
| 解      | XIE       | HSIEH                       | KAI        | KAI              | HAI/HYE             |                            |
| 应      | YING      | YING                        | YING       | IENG             | ENG                 | YING                       |
| 宗      | ZONG      | TSUNG                       | CHUNG      | CHONG            | CHONG               | CHUNG                      |
| 丁      | DING      | TING                        | TING       | TENG             | TENG                | TING                       |
| 宣      | XUAN      | HSUAN                       | SUEN       | SUN              | SUANG               |                            |
| 贲      | BEN       | PEN                         |            |                  |                     |                            |
| 邓      | DENG      | TENG                        | TANG       | TANG             | TENG                | TANG                       |
| 郁      | YU        | YU                          | YUK        | IOK              | HIOK                |                            |
| 单      | SHAN      | SHAN                        | SIN        | SIN              | SIANG               | SIN                        |
| 杭      | HANG      | HANG                        | HONG       | HONG             | HANG                |                            |
| 洪      | HONG      | HUNG                        | HUNG       | HONG             | ANG                 | HUNG                       |
| 包      | BAO       | PAO                         | PAU        | PAO/BAO          | POW/PAO             | PAU                        |
| 诸      | ZHU       | CHU                         | CHU        | CHU              | CHOO                |                            |
| 左      | ZUO       | TSO                         | CHOR/JOR   | CHO              | CHO/CHOR            |                            |
| 石      | SHI       | SHIH                        | SHEK       | SEK              | CHEOH/CHIOH         | SHEK/SECK/SEK              |
| 崔      | CUI       | TSUI                        | CHUI/TSUI  | CHOI             | CHWEE/CHUI          | TSUI/CHUI                  |
| 吉      | JI        | CHI                         | KUT        | KAT/KIT          | KIK                 |                            |
| 钮      | NIU       | NIU                         | NAU        | NAO              | NEW/NIU             |                            |
| 龚      | GONG      | KUNG                        | KUNG       | KONG             | KIONG/KONG          | KUNG                       |
| 程      | CHENG     | CHENG                       | CHING      | CHENG            | THIA                | CHING                      |
| 嵇      | JI        | CHI                         |            |                  | KEE                 |                            |
| 邢      | XING      | HSING                       | YING       | IENG             | HIAH/HIA            | YING                       |
| 滑      | HUA       | HUA                         |            |                  |                     |                            |
| 裴      | PEI       | PEI                         | PUI        | PUI              | PUAY                | PUI                        |
| 陆      | LU        | LU                          | LUK        | LOK              | LOK/LEK             | LUK/LOOK                   |
| 荣      | RONG      | JUNG                        | WING       | VENG/VING        | YONG                | WING                       |
| 翁      | WENG      | WENG                        | YUNG       | IONG             | ANG/ENG             | YUNG                       |
| 荀      | XUN       | HSUN                        |            | SON              | SOON/SUNG           |                            |
| 羊      | YANG      | YANG                        | YEUNG      | IEONG            | YEOH                |                            |
| 於      | YU        | YU                          | YU         | U                | YEE                 |                            |
| 惠      | HUI       | HUI                         | WAI        | VAI              | HWEE                | WAI                        |
| 甄      | ZHEN      | CHEN                        | YAN        | IAN              | YING                | YAN                        |
| 麹      | QU        | CHU                         | KUK        | KOK              | KHEK/KEK            |                            |
| 家      | JIA       | CHIA                        | KA/KAH     | KA               |                     |                            |
| 封      | FENG      | FENG                        | FUNG       | FONG             | HONG                |                            |
| 芮      | RUI       | JUI                         |            | IOI              | JUAY                |                            |
| 羿      | YI        | I/YI                        | YIK        | IEK              | NGEE                |                            |
| 储      | CHU       | CHU                         | CHU        | CHU              |                     |                            |
| 靳      | JIN       | CHIN                        | KAN        |                  | KING/KEUNG          |                            |
| 汲      | JI        | CHI                         |            |                  |                     |                            |
| 邴      | BING      | PING                        |            |                  | PENG                |                            |
| 糜      | MI        | MI                          | MEI        | MEI              |                     |                            |
| 松      | SONG      | SUNG                        | CHUNG      | CHONG            | SONG                |                            |
| 井      | JING      | CHING                       |            | CHENG            |                     |                            |
| 段      | DUAN      | TUAN                        | TUEN       | TUN              | TEUNG               | TUEN                       |
| 富      | FU        | FU                          | FOO        | FU               | POO                 |                            |
| 巫      | WU        | WU                          | MO         | MOU              | BOO                 | MO                         |
| 乌      | WU        | WU                          | WOO        | WU               | WOO/OH              |                            |
| 焦      | JIAO      | CHIAO                       | CHIU       | CHIO             | CHEOW/CHIAU         |                            |
| 巴      | BA        | PA                          | PA         | PA               | PA                  |                            |
| 弓      | GONG      | KUNG                        | KUNG       | KONG             | KENG                |                            |
| 牧      | MU        | MU                          | MUK        | MOK              | MOK                 |                            |
| 隗      | KUI       | KUI                         |            |                  | NGWEE/NGUI          |                            |
| 山      | SHAN      | SHAN                        | SAN        | SAN              |                     |                            |
| 谷      | GU        | KU                          | KUK        | KOK              | KOK                 | KUK                        |
| 车      | CHE       | CHE                         |            | CHE              | CHIA                |                            |
| 侯      | HOU       | HOU                         | HAU        | HAO              | HOH/HOU             | HOU/HAU                    |
| 宓      | MI        | MI                          |            |                  | MIK                 |                            |
| 蓬      | PENG      | PENG                        | PANG       | PANG             | PONG/PHONG          |                            |
| 全      | QUAN      | CHUAN                       | CHUEN      | CHUN             | CHUANG              | CHUEN                      |
| 郗      | XI        | HSI                         |            |                  | HEE                 |                            |
| 班      | BAN       | PAN                         | PAN        | PAN              | PANG                |                            |
| 仰      | YANG      | YANG                        | YEUNG      | IEONG            | NGIANG              |                            |
| 秋      | QIU       | CHIU                        | CHAU       | CHAO             | CHEW                |                            |
| 仲      | ZHONG     | CHUNG                       | CHUNG      | CHONG            | TONG                | CHUNG                      |
| 伊      | YI        | I/YI                        | YEE        | I                | YEE                 | YEE                        |
| 宫      | GONG      | KUNG                        | KUNG       | KONG             | KENG                |                            |
| 甯      | NING      | NING                        | NING       | NENG             | LENG                |                            |
| 仇      | QIU       | CHIU                        | SAU        | SAO              | CHEW                |                            |
| 栾      | LUAN      | LUAN                        | LUEN       |                  | LUANG               |                            |
| 暴      | BAO       | PAO                         | PO         | POU              | POW/PAU             |                            |
| 甘      | GAN       | KAN                         | KAM        | KAM              | KAM                 | KAM                        |
| 钭      | DOU       | TOU                         |            |                  | TOH/TOU             |                            |
| 厉      | LI        | LI                          | LAI        | LAI              | LEE                 |                            |
| 戎      | RONG      | JUNG                        | YUNG       | IONG             | JONG                |                            |
| 祖      | ZU        | TSU                         | CHO        | CHOU             | CHOH/CHOU           |                            |
| 武      | WU        | WU                          | MO         | MOU              | BOO                 | MO                         |
| 符      | FU        | FU                          | FOO        | FU               | HOO                 | FU/FOO                     |
| 刘      | LIU       | LIU                         | LAU        | LAO              | LOW/LAU             | LAU                        |
| 景      | JING      | CHING                       | KING       | KENG             | KENG                | KING                       |
| 詹      | ZHAN      | CHAN                        | JIM/TSIM   | CHIM             | CHIAM               | TSIM/JIM                   |
| 束      | SHU       | SHU                         |            | CHOK             | SOK                 |                            |
| 龙      | LONG      | LUNG                        | LUNG/LOONG | LONG             | LENG                | LUNG/LOONG                 |
| 叶      | YE        | YEH                         | IP/YIP     | IP               | YAP                 | YIP/IP                     |
| 幸      | XING      | HSING                       | HANG       | HANG             | HENG                |                            |
| 司      | SI        | SSU                         | SZE        | SI               | SEE                 | SZE                        |
| 韶      | SHAO      | SHAO                        | SIU        | SIO              | SEOW                |                            |
| 郜      | GAO       | KAO                         |            |                  | KOW/KAU             |                            |
| 黎      | LI        | LI                          | LAI        | LAI              | LOI/LEE/LI          | LAI                        |
| 蓟      | JI        | CHI                         |            | KAI              | KEE                 |                            |
| 薄      | BO        | PO                          |            | POK              | POH                 |                            |
| 印      | YIN       | YIN                         | YAN        | IAN              | YING                |                            |
| 宿      | SU        | SU                          | SUK        | SOK              |                     |                            |
| 白      | BAI       | PAI                         | PAK        | PAK              | PEH                 | PAK                        |
| 怀      | HUAI      | HUAI                        | WAI        | WAI              | HUAI                |                            |
| 蒲      | PU        | PU                          | PO         | POU              | PHOO                |                            |
| 邰      | TAI       | TAI                         | TAI        |                  | THAI/TAI            |                            |
| 从      | CONG      | TSUNG                       | CHUNG      | CHONG            | CHONG               |                            |
| 鄂      | E         | O                           |            | NGOK             | NGAK                |                            |
| 索      | SUO       | SO                          |            | SOK              | SOK/SOH             |                            |
| 咸      | XIAN      | HSIEN                       | HAM        | HAM              | HAM                 |                            |
| 籍      | JI        | CHI                         |            | CHEK             |                     |                            |
| 赖      | LAI       | LAI                         | LAI        | LAI              | LAI/NAI             | LAI                        |
| 卓      | ZHUO      | CHO                         | CHEUK      | CHEOK            | TOH                 | CHEUK                      |
| 蔺      | LIN       | LIN                         | LUN        | LON              | LIANG               |                            |
| 屠      | TU        | TU                          | TO         | TOU              | TOO/TU              |                            |
| 蒙      | MENG      | MENG                        | MUNG       | MONG             | MONG                |                            |
| 池      | CHI       | CHIH                        | CHI/TSZ    | CHI              | TEE                 | CHI                        |
| 乔      | QIAO      | CHIAO                       | KIU        | KIO              | KEOW                | KIU                        |
| 阴      | YIN       | YIN                         | YAM        | IAM              | YIM                 |                            |
| 鬱      | YU        | YU                          | WAT        | VAT              | HIOK                |                            |
| 胥      | XU        | HSU                         | SUI        | SOI              | SOO                 |                            |
| 能      | NAI       | NAI                         | NANG       | NANG             | LENG                |                            |
| 苍      | CANG      | TSANG                       | CHONG      | CHONG            | CHANG               |                            |
| 双      | SHUANG    | SHUANG                      | SHEUNG     | SEONG            | SANG                |                            |
| 闻      | WEN       | WEN                         | MAN        | MAN              | BOON                |                            |
| 莘      | SHEN      | SHEN                        |            |                  | SING                |                            |
| 党      | DANG      | TANG                        | TONG       | TONG             | TANG                |                            |
| 翟      | ZHAI      | CHAI                        | CHAK       | CHAK             | TEK                 | CHAK                       |
| 谭      | TAN       | TAN                         | TAM        | TAM              | THAM                | TAM                        |
| 贡      | GONG      | KUNG                        | KUNG       | KONG             | KONG                |                            |
| 劳      | LAO       | LAO                         | LO         | LOU              | LOW                 | LO                         |
| 逄      | PANG      | PANG                        | FUNG       | FONG             | PHANG               |                            |
| 姬      | JI        | CHI                         | KEI        | KEI              | KEE                 |                            |
| 申      | SHEN      | SHEN                        | SAN/SUN    | SON              | SING                | SUN                        |
| 扶      | FU        | FU                          | FOO        | FU               | HOO                 |                            |
| 堵      | DU        | TU                          | TO         | TOU              |                     |                            |
| 冉      | RAN       | JAN                         |            |                  | ZIAM/JIAM           |                            |
| 宰      | ZAI       | TSAI                        | CHOI       | CHOI             | CHAI                |                            |
| 郦      | LI        | LI                          |            |                  | LEE                 |                            |
| 雍      | YONG      | YUNG                        | YUNG       | IONG             | YONG                |                            |
| 郤      | XI        | HSI                         |            | LIO              | KHIAH/KIAH          |                            |
| 璩      | QU        | CHU                         |            |                  |                     |                            |
| 桑      | SANG      | SANG                        | SONG       | SONG             | SNG/SEUNG           |                            |
| 桂      | GUI       | KUI                         | KWAI       | KUAI             | KWEE/KUI            | KAI                        |
| 濮      | PU        | PU                          |            |                  |                     |                            |
| 牛      | NIU       | NIU                         | NGAU       | NGAO             | GOO                 | NGAU                       |
| 寿      | SHOU      | SHOU                        | SAU        | SAO              | SEW                 |                            |
| 通      | TONG      | TUNG                        | TUNG       | TONG             | TONG/THONG          |                            |
| 边      | BIAN      | PIEN                        | PIN        | PIN              | PIANG               |                            |
| 扈      | HU        | HU                          | WOO        | VU               | HOO                 |                            |
| 燕      | YAN       | YEN                         | YIN        | IN               | YIN                 | YIN                        |
| 冀      | JI        | CHI                         | KEI        | KEI              | KEE                 |                            |
| 郏      | JIA       | CHIA                        |            |                  |                     |                            |
| 浦      | PU        | PU                          | PO         | POU              | POH/POU             |                            |
| 尚      | SHANG     | SHANG                       | SHEUNG     | SEONG            | SIANG               | SHEUNG                     |
| 农      | NONG      | NUNG                        | NUNG       | NONG             | LONG                |                            |
| 温      | WEN       | WEN                         | WAN        | VAN              | WOON/OON            | WAN                        |
| 别      | BIE       | PIEH                        | PIT        | PIT              | PIAK                |                            |
| 庄      | ZHUANG    | CHUANG                      | CHONG      | CHONG            | CHNG                | CHONG                      |
| 晏      | YAN       | YEN                         |            | NGAN             | ANG                 | NGAN                       |
| 柴      | CHAI      | CHAI                        | CHAI       | CHAI             | CHA                 |                            |
| 瞿      | QU        | CHU                         | KUI        | KOI              | KEU                 |                            |
| 阎      | YAN       | YEN                         | YIM        | IM               | GIAM/NGIAM          |                            |
| 充      | CHONG     | CHUNG                       | CHUNG      | CHONG            | CHONG               |                            |
| 慕      | MU        | MU                          | MO         | MOU              | MOR                 |                            |
| 连      | LIAN      | LIEN                        | LIN        | LIN              | LIAN/LIANG          | LIN                        |
| 茹      | RU        | JU                          | YU         | U                | JOO                 |                            |
| 习      | XI        | HSI                         | CHAP       | CHAP             | SIP/SIK             |                            |
| 宦      | HUAN      | HUAN                        | WAN        | VAN              | HUANG               |                            |
| 艾      | AI        | AI                          | NGAI       | NGAI             | HIAN/NGAI           | NGAI                       |
| 鱼      | YU        | YU                          | YU         | U                |                     |                            |
| 容      | RONG      | JUNG                        | YUNG       | IONG             | YONG                |                            |
| 向      | XIANG     | HSIANG                      | HEUNG      | HEONG            | HIANG               | HEUNG                      |
| 古      | GU        | KU                          | KOO        | KU               | KOH                 | KU/KHOO/KOO/KUO            |
| 易      | YI        | I/YI                        | YIK        | IEK              | EK                  | YICK/YIK                   |
| 慎      | SHEN      | SHEN                        |            | SAN              |                     |                            |
| 戈      | GE        | KO                          |            | KO               | KHO/KOR             |                            |
| 廖      | LIAO      | LIAO                        | LIU        | LIO/LIU          | LEOW                | LIAO/LIU/LIEW              |
| 庾      | YU        | YU                          | YU         | U                | JOO/JU              |                            |
| 终      | ZHONG     | CHUNG                       | CHUNG      | CHONG            | CHONG               |                            |
| 暨      | JI        | CHI                         |            | KEI              | KEE                 |                            |
| 居      | JU        | CHU                         | KUI        | KOI              | KEU/KER             |                            |
| 衡      | HENG      | HENG                        |            | HANG             | HUANG               |                            |
| 步      | BU        | PU                          | PO         | POU              | POH                 |                            |
| 都      | DU        | TU                          | TO         | TOU              | TOH/TOU             |                            |
| 耿      | GENG      | KENG                        |            | KANG             | KUANG               |                            |
| 满      | MAN       | MAN                         | MUN        | MUN              | MUAN                | MOON                       |
| 弘      | HONG      | HUNG                        | WUNG       | VANG             | HONG                |                            |
| 匡      | KUANG     | KUANG                       | HONG       | HONG             | KUANG               | HONG                       |
| 国      | GUO       | KUO                         | KWOK       | KUOK             | KOK                 |                            |
| 文      | WEN       | WEN                         | MAN        | MAN              | BOON/BUNG           | MAN                        |
| 寇      | KOU       | KOU                         | KAU        | KAO              | KOH/KOU             |                            |
| 广      | GUANG     | KUANG                       | KWONG      | KUONG            | KUANG               |                            |
| 禄      | LU        | LU                          | LUK        | LOK              | LOK                 |                            |
| 阙      | QUE       | CHUEH                       | KUIT       | KUET             | KUEK/KUEH           |                            |
| 东      | DONG      | TUNG                        | TUNG       | DONG             | TONG/TANG           |                            |
| 欧      | OU        | OU                          | AU         | AO               | OW/AU/AO            | AU                         |
| 殳      | SHU       | SHU                         |            |                  |                     |                            |
| 沃      | WO        | WO                          |            | IOK              |                     |                            |
| 利      | LI        | LI                          | LEE/LI     | LEI/LEE          | LEE                 |                            |
| 蔚      | WEI       | WEI                         | WAI        | WAI              | WAY/WE              |                            |
| 越      | YUE       | YUEH                        |            | UT               | WAK                 |                            |
| 夔      | KUI       | KUEI                        |            |                  | KWEE/KUI            |                            |
| 隆      | LONG      | LUNG                        | LUNG       | LONG             | LONG                |                            |
| 师      | SHI       | SHIH                        | SZE        | SI               | SZE/SER             | SI                         |
| 巩      | GONG      | KUNG                        | KUNG       | KONH             | KIONG               |                            |
| 厍      | SHE       | SHE                         |            |                  |                     |                            |
| 聂      | NIE       | NIEH                        | NIP/LIP    |                  | NIAP                | LIP                        |
| 晁      | ZHAO      | CHAO                        |            |                  |                     |                            |
| 勾      | GOU       | KOU                         |            | NGAO             |                     |                            |
| 敖      | AO        | AO                          | NGO        |                  |                     | O/NGO                      |
| 融      | RONG      | JUNG                        | YUNG       | IONG             | YONG                |                            |
| 冷      | LENG      | LENG                        |            | LANG             |                     |                            |
| 訾      | ZI        | TZU                         |            |                  |                     |                            |
| 辛      | XIN       | HSIN                        | SAN/SUN    | SON              | SING                | SUN                        |
| 阚      | KAN       | KAN                         |            |                  |                     |                            |
| 那      | NA        | NA                          | NA         | NA               |                     |                            |
| 简      | JIAN      | CHIEN                       | KAN        | KAN              | KAN/KANG            | KAN                        |
| 饶      | RAO       | JAO                         | YIU        | IO               | JEOW/JIAU           | YIU                        |
| 空      | KONG      | KUNG                        | HUNG       | HONG             |                     |                            |
| 曾      | ZENG      | TSENG                       | TSANG      | CHANG            | CHAN/TJAN           | TSANG                      |
| 毋      | WU        | WU                          | MO         | MOU              |                     |                            |
| 沙      | SHA       | SHA                         | SHA        | SA               | SHA/SUA             |                            |
| 乜      | MIE       | NIEH                        |            | NE               |                     |                            |
| 养      | YANG      | YANG                        | YEUNG      | IEONG            |                     |                            |
| 鞠      | JU        | CHU                         |            | KOK              |                     |                            |
| 须      | XU        | HSU                         |            | SEOI/SOI         | SOO/SU              |                            |
| 丰      | FENG      | FENG                        | FUNG       | FONG             | HONG                |                            |
| 巢      | CHAO      | CHAO                        |            | CHAO             | CHOW/CHAU/CHAO      |                            |
| 关      | GUAN      | KUAN                        | KWAN       | KUAN             | KWAN/KUANG          | KWAN                       |
| 蒯      | KUAI      | KUAI                        |            |                  |                     |                            |
| 相      | XIANG     | HSIANG                      | SHEUNG     | SEONG            |                     |                            |
| 查      | CHA       | CHA                         | CHA        | CHA              | CHA                 |                            |
| 后      | HOU       | HOU                         | HAU        | HAO              |                     |                            |
| 荆      | JING      | CHING                       | KING       | KENG             | KENG                |                            |
| 红      | HONG      | HUNG                        | HUNG       | HONG             | ANG                 |                            |
| 游      | YOU       | YU                          | YAU        | IAO              | YEW/YU              | YAU                        |
| 竺      | ZHU       | CHU                         |            |                  |                     |                            |
| 权      | QUAN      | CHUAN                       | KUEN       | KUN              | KUAN/KUANG          | KUEN                       |
| 逯      | LU        | LU                          |            |                  |                     |                            |
| 盖      | GAI       | KO                          | KOI        | KOI              |                     |                            |
| 益      | YI        | I / YI                      | YIK        | IEK              |                     |                            |
| 桓      | HUAN      | HUAN                        | WUN        | VUN              |                     |                            |
| 公      | GONG      | KUNG                        | KUNG       | KONG             | KONG                |                            |
| 丘      | QIU       | CHIU                        | YAU        | IAO              | KHEW/KHOO           |                            |
| 万俟    | MOQI      | MO-CHI                      |            |                  | MOK KEE             |                            |
| 司马    | SIMA      | SSU-MA                      | SZEMA      | SI MA            | SEE BEH             |                            |
| 上官    | SHANGGUAN | SHANG-KUAN                  | SHEUNGKWUN | SEONG KUN        |                     |                            |
| 欧阳    | OUYANG    | OU-YANG                     | AUYEUNG    | AO IEONG         |                     |                            |
| 夏侯    | XIAHOU    | HSIA-HOU                    | HAHAU      | HA HAO           |                     |                            |
| 诸葛    | ZHUGE     | CHU-KO                      | CHUKOK     |                  | CHUKAT              |                            |
| 闻人    | WENREN    | WEN-JEN                     | MANYAN     | MAN IAN          |                     |                            |
| 东方    | DONGFANG  | TUNG-FANG                   | TUNGFONG   | TONG FONG        |                     |                            |
| 赫连    | HELIAN    | HO-LIEN                     |            |                  |                     |                            |
| 皇甫    | HUANGFU   | HUANG-FU                    |            |                  |                     |                            |
| 尉迟    | YUCHI     | YU-CHIH                     | WAICHI     | VAI CHI          | UTTI                |                            |
| 公羊    | GONGYANG  | KUNG-YANG                   | KUNGYEUNG  | KONG IEONG       |                     |                            |
| 澹台    | TANTAI    | TAN-TAI                     |            |                  |                     |                            |
| 公冶    | GONGYE    | KUNG-YEH                    |            |                  |                     |                            |
| 宗政    | ZONGZHENG | TSUNG-CHENG                 |            | CHONG CHENG      |                     |                            |
| 濮阳    | PUYANG    | PU-YANG                     |            |                  |                     |                            |
| 淳于    | CHUNYU    | CHUN-YU                     |            |                  |                     |                            |
| 单于    | CHANYU    | CHAN-YU                     |            | SIN U            | SIANG WOO           |                            |
| 太叔    | TAISHU    | TAI-SHU                     |            | TAI SOK          |                     |                            |
| 申屠    | SHENTU    | SHEN-TU                     |            | SAN TOU          |                     |                            |
| 公孙    | GONGSUN   | KUNG-SUN                    | KUNGSUEN   | KONG SUN         |                     |                            |
| 仲孙    | ZHONGSUN  | CHUNG-SUN                   | CHUNGSUEN  | CHONG SUN        |                     |                            |
| 轩辕    | XUANYUAN  | HSUAN-YUAN                  | HINYUEN    | HIN UN           |                     |                            |
| 令狐    | LINGHU    | LING-HU                     | LINGWOO    | LENG VU          |                     |                            |
| 锺离    | ZHONGLI   | CHUNG-LI                    |            | CHONG LEI        |                     |                            |
| 宇文    | YUWEN     | YU-WEN                      | YUMAN      | U MAN            |                     |                            |
| 长孙    | ZHANGSUN  | CHANG-SUN                   | CHEUNGSUEN | CHEONG SUN       |                     |                            |
| 慕容    | MURONG    | MU-JUNG                     | MOYUNG     | MOU IONG         |                     |                            |
| 鲜于    | XIANYU    | HSIEN-YU                    |            |                  |                     |                            |
| 闾丘    | LUQIU     | LU-CHIU                     |            |                  |                     |                            |
| 司徒    | SITU      | SSU-TU                      | SZETO      | SI TOU           |                     |                            |
| 司空    | SIKONG    | SSU-KUNG                    | SZEHUNG    | SI HONG          |                     |                            |
| 亓官    | QIGUAN    |                             |            |                  |                     |                            |
| 司寇    | SIKOU     |                             | SZEKAU     | SI KAO           |                     |                            |
| 仉      | ZHANG     |                             |            |                  |                     |                            |
| 督      | DU        | TU                          | TUK        |                  |                     |                            |
| 子车    | ZICHE     |                             |            | CHI CHE          |                     |                            |
| 颛孙    | ZHUANSUN  |                             |            |                  |                     |                            |
| 端木    | DUANMU    | TUAN-MU                     |            | TUN MOK          |                     |                            |
| 巫马    | WUMA      | WU-MA                       | MOMA       | MOU MA           |                     |                            |
| 公西    | GONGXI    | KUNG-HSI                    | KUNGSAI    | KONG SAI         |                     |                            |
| 漆雕    | QIDIAO    | CHI-TIAO                    |            | CHAT TIU         |                     |                            |
| 乐正    | YUEZHENG  | YUEH-CHENG                  |            | NGOK CHENG       |                     |                            |
| 壤驷    | XIANGSI   |                             |            |                  |                     |                            |
| 公良    | GONGLIANG | KUNG-LIANG                  | KUNGLEUNG  | KONG LEONG       |                     |                            |
| 拓拔    | TUOBA     | TO-PA                       |            | TOK PAT          |                     |                            |
| 夹谷    | JIAGU     | CHIA-KU                     |            | KAP KOK          |                     |                            |
| 宰父    | ZAIFU     |                             |            | CHOI FU          |                     |                            |
| 穀梁    | GULIANG   | KU-LIANG                    |            | KOK LEONG        |                     |                            |
| 晋      | JIN       | CHIN                        | CHUN       | CHON             |                     |                            |
| 楚      | CHU       | CHU                         | CHOR       | CHO              |                     | CHOR                       |
| 闫      | YAN       | YEN                         | YIM        | IM               |                     |                            |
| 法      | FA        | FA                          | FA         | FAT              |                     |                            |
| 汝      | RU        | JU                          | YU         | U                |                     |                            |
| 鄢      | YAN       | YEN                         | YIN        | IN               |                     |                            |
| 涂      | TU        | TU                          | TO         | TOU              |                     |                            |
| 钦      | QIN       | CHIN                        |            | IAM              |                     |                            |
| 段干    | DUANGAN   | TUAN-KAN                    |            | TUN KON          |                     |                            |
| 百里    | BAILI     | PAI-LI                      |            | PAK LEI          |                     |                            |
| 东郭    | DONGGUO   | TUNG-KUO                    |            | TONG KUOK        |                     |                            |
| 南门    | NANMEN    | NAN-MEN                     | NAMMUN     | NAM MUN          |                     |                            |
| 呼延    | HUYAN     | HU-YEN                      |            | FU IN            |                     |                            |
| 归      | GUI       | KUEI                        | KWAI       | KUAI             |                     |                            |
| 海      | HAI       | HAI                         | HOI        | HOI              |                     | HOI                        |
| 羊舌    | YANGSHE   |                             |            | IEONG SIT        |                     |                            |
| 微生    | WEISHENG  |                             |            | MEI SANG         |                     |                            |
| 岳      | YUE       | YUEH                        | NGOK       | NGOK             |                     |                            |
| 帅      | SHUAI     |                             |            | SOI              |                     |                            |
| 缑      | GOU       | KOU                         |            |                  |                     |                            |
| 亢      | KANG      | KANG                        | HONG       |                  |                     |                            |
| 况      | KUANG     | KWANG/KUANG                 | KWONG      | FONG             |                     |                            |
| 后      | HOU       | HOU                         | HAU        | HAO              |                     |                            |
| 有      | YOU       | YU                          | YAU        | IAO              |                     |                            |
| 琴      | QIN       | CHIN                        |            | KAM              | KIM                 |                            |
| 梁丘    | LIANGQIU  | LIANG-CHIU                  |            | LEONG IAO        |                     |                            |
| 左丘    | ZUOQIU    |                             |            | CHO IAO          |                     |                            |
| 东门    | DONGMEN   | TUNG-MEN                    | TUNGMUN    | TONG MUN         |                     |                            |
| 西门    | XIMEN     | HSI-MEN                     | SAIMUN     | SAI MUN          |                     |                            |
| 商      | SHANG     | SHANG                       | SHEUNG     | SEONG            | SIANG               |                            |
| 牟      | MOU       | MOU                         |            | MAO              |                     |                            |
| 佘      | SHE       |                             | SHEH       | SE               | SIA/SIAH/SEAH       |                            |
| 佴      | ER        |                             |            |                  |                     |                            |
| 伯      | BO        | PO                          | BAK        | PAK              | PEK/PEH             |                            |
| 赏      | SHANG     | SHANG                       | SHEUNG     | SEONG            |                     |                            |
| 南宫    | NANGONG   | NAN-KUNG                    | NAMKUNG    | NAM KONG         |                     |                            |
| 墨      | MO        | MO                          | MAK        | MAK              | BAK                 |                            |
| 哈      | HA        | HA                          | HA         | HA               |                     |                            |
| 谯      | QIAO      | CHIAO                       |            |                  |                     |                            |
| 笪      | DA        | TA                          |            |                  |                     |                            |
| 年      | NIAN      | NIEN                        | NIN        | NIN              | NEE                 |                            |
| 爱      | AI        | AI                          | OI         | OI               |                     |                            |
| 阳      | YANG      | YANG                        | YEUNG      | IEONG            |                     | YEUNG                      |
| 佟      | TONG      | TUNG                        | TUNG       | TONG             | TONG/THONG          |                            |
| 第五    | DIWU      | TI-WU                       | TAING      | TAI NG           |                     |                            |
| 言      | YAN       | YEN                         | YIN        | IN               |                     |                            |
| 福      | FU        | FU                          | FUK        | FOK              | HOK                 |                            |
| 麦      | MAI       | MAI                         | MAK        | MAK              | BEH                 | MAK                        |
| 源      | YUAN      | YUAN                        | YUEN       | UN               |                     |                            |
| 难      | NAN       | NAN                         | NAN        | NAN              |                     |                            |
| 星      | XING      | XING/HSING/HSING/SYING/SING | SING       | SENG             |                     |                            |
|         |

Other userful link:

1. https://www.boca.gov.tw/cp-2-4226-c0eff-1.html
