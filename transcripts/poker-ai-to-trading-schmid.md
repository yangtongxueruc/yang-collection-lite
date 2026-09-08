
## 开场与演讲者背景

**SECTION_NOTE**
- 主持人介绍 Martin Schmid：布拉格查理大学数学物理学院（Matfyz）校友，曾任 DeepMind，现为 EquiLibre Technologies 代表
- 讲座目标：讲清「应用强化学习」的故事与历史，给听众关于 RL 的直觉，以及它为何藏在今天 AI/大语言模型的「魔法」里
**END_SECTION_NOTE**

**[00:00 – 00:15]**
**捷克语：** Vítám na další přednášce ze série matematické problémy. Na matematiku je to předposlední v tomhletom semestru. Naším speakerem dneska je Martin Schmit Equiliber Technologies. Eh, je to bývalý matfizák, je to tak?
**中文：** 欢迎来到「数学问题」系列的另一场讲座。这学期数学方向的讲座就剩倒数第二场了。今天我们的演讲者是 Martin Schmid（EquiLibre Technologies）。呃，他以前是数学物理系（Matfyz）的学生，对吧？

**[00:15 – 00:30]**
**捷克语：** Nebo možná jednou matfizák. Vždycky matfizák říká náš pan děkan. Takže je to matfizák. >> Já myslím, že ještě pořád matfizák. Ještě nějaký uvazek mám tady. >> Výborně. Takže je to matfizák. eh prošel mnoha mnoha zajímavými firmami, jako je
**中文：** 或者说曾经是数学物理系的学生。我们的院长总说「数学物理系出身」。所以他就是数学物理系的。>> 我觉得我现在还是数学物理系的人，在这里还挂着点职位。>> 太好了。那他就是数学物理系出身。他曾在很多很多有趣的公司待过，比如……

**[00:30 – 00:44]**
**捷克语：** třeba Google Deep Mind si to říkám správně, až nakonec založil tuhletu firmu, kterou tady zastupuje dneska, která se věnuje využití AI ve specifických aplikacích. To asi nebudu
**中文：** 比如 Google DeepMind——我说对了吧——最后他创立了今天代表来的这家公司，专注于把 AI 用在特定的应用里。这个我大概就不替他介绍了……

**[00:44 – 00:53]**
**捷克语：** mluvit za vás a nechám to na vás. Děkuju, že jste teda přišel, že jste si na nás udělal čas. Jsme moc rádi a těšíme se na přednášku.
**中文：** 替你介绍了，剩下的交给你自己。谢谢你今天能来，抽空跟我们见面。我们非常高兴，也很期待这场讲座。

**[00:53 – 01:00]**
**捷克语：** >> Super. Tak jo, díky. Eh, jednu má svý zálou neslyšel a je to pěkný.
**中文：** >> 太好了。好的，谢谢。呃，有一段我自己的讲座他没听到，还挺有意思的。

**[01:00 – 01:15]**
**捷克语：** A tím pádem si zrovna udělám reklamu na svůj předmět. Kdyby se vám jako líbilo něco, co tady je a chtěli byste o tom vědět víc, tak já mám jednou za semester na malej straně předmět, kterej jako hodně souvisí s tím, o čem si tady trošku budeme povídat.
**中文：** 借此机会我也给自己的课做个宣传。如果你们喜欢今天讲的东西、想了解更多，我每学期会在小课堂上开一门课，内容和我们今天要聊的很相关。

**[01:15 – 01:23]**
**捷克语：** A dneska dneska vám chci říct nějakj příběh. Obecně si myslím, že je fajn fajn říct nějakej příběh, protože to si lidi víc
**中文：** 今天我想跟大家讲一个故事。总的来说我觉得讲个故事挺好的，因为故事大家更容易记住。

**[01:23 – 01:39]**
**捷克语：** zapamatujou. A ten příběh, kterej jsem si vybral dneska pro vás, je nějaká příběh a historie aplikovanýho refman learningu. A já doufám, že si dneska i z toho trošku něco odnesete. Já doufám, že si odnesete několik věcí. jedna věc,
**中文：** 我今天选来给大家讲的故事，是关于「应用强化学习」的一段历史和来龙去脉。我希望今天你们能从中有所收获。我希望你们带走几样东西。第一件……

**[01:39 – 01:52]**
**捷克语：** aspoň nějak jako jemnej insight, intuici na to, o čem vůbec ten reinforcement learning je, jak se liší od deep learningu, proč ten reinforcement learning je dneska všude okolo nás. Eh, hopefully dostanete i trošku lepší
**中文：** 至少对「强化学习到底是什么、它和深度学习有什么区别、为什么今天强化学习无处不在」有一点感觉和直觉。呃，希望你们也能对……有更好的直觉。

**[01:52 – 02:07]**
**捷克语：** intuici, když používáte dneska AI AI modely, jazykový modely, tak kde tam to kde ten reinforcement learning tam dělá tu magii. A eh snad do budoucna e si
**中文：** 当你们今天使用 AI 模型、语言模型时，强化学习到底在哪里施展了魔法。呃，希望将来你们……

**[02:07 – 02:23]**
**捷克语：** časem jako vzpomenete na to a třeba i tydlety metody buď využijete sami ve svejch aplikacích a nebo třeba váš research časem bude blíž a víc tíhnout víc tíhnout k tomudle tomuhle typu AI. A
**中文：** 会想起今天讲的，也许你们会在自己的应用里用上这些方法，或者你们的研究将来会更靠近、更倾向于这类 AI。

**[02:23 – 02:37]**
**捷克语：** abych tak nějak jako věděl, jak ten jak je ten příběh a na který věci co nejvíc se zaměřit, tak já se možná zeptám jenom jako takový rychlý hlasování na pár e základních věcí. Eh a první věc, co se
**中文：** 为了知道这个故事该怎么讲、重点放在哪些地方，我想先做个快速的小调查，问几个基础问题。呃，第一个问题是……

**[02:37 – 02:47]**
**捷克语：** zeptám, kdo z vás používá denně nebo často nějaký EA modelyp Gemini clot? Super. >> Nebojte se shodnout.
**中文：** 你们当中有谁每天或经常使用某种 AI 模型，比如 Gemini、ChatGPT？太好了。>> 别不好意思举手。

**[02:47 – 02:57]**
**捷克语：** >> Paráda. Já [smích] jsem taky přítel >> pecka. A teďka kdo z vás ví, že za těmahle modelama je něco jako deep learning?
**中文：** >> 好极了。我[笑]也是用户>> 棒。那现在，你们当中谁知道这些模型的背后是「深度学习」？

**[02:57 – 03:07]**
**捷克语：** Super. A kdo z vás ví, že za těmahle modelama je něco jako renforce melanic? Super. Tak teďka to procento droplo výrazně, ale pořád tam nějaký lidi jsou.
**中文：** 很好。那谁知道这些模型的背后还有「强化学习」？很好。现在这个比例明显下降了很多，但还是有那么些人知道。

**[03:07 – 03:18]**
**捷克语：** A dobře. A teďka k tomu jako spojený poslední dva dotazy. Kdo z vás by řekl, kdo tak nějak jako tuší, jak funguje Deep Planet samotnej? Hej.
**中文：** 好。现在把最后两个问题连起来看。你们当中谁觉得自己大概知道 DeepMind 本身是怎么运作的？嗯。

**[03:18 – 03:31]**
**捷克语：** Jasně. A ten samej dotaz pro reinforce managing. Super. Tak jo. Tak tolencto si myslím, že je skoro eh optimální distribuce hlasů, protože tím pádem si myslím, že
**中文：** 明白。同样的问题问强化学习。很好。好的。我觉得这几乎是个「最优的举手分布」，因为这样一来我认为……

**[03:31 – 03:44]**
**捷克语：** tenhlecten příběh by se vám jak mohl líbit, tak zároveň si z něho možná i něco odnesete. Tak se tak se do toho spolu pustíme a [kašel] já rovnou skočím na druhej slaj. A v
**中文：** 这个故事你们既可能觉得有意思，也可能从中有所收获。那我们就一起开始吧，[咳嗽]我直接跳到第二张幻灯片。

**[03:44 – 03:59]**
**捷克语：** tomhlectom slaju se snažím ukázat, že reinforce Learning jako takovj už začíná bejt dostatečně mainstream na to, aby tak nějak všichni o něm aspoň slyšeli
**中文：** 这张幻灯片我想说明：强化学习本身已经开始足够「主流」了，以至于大家至少都听说过它……

**[03:59 – 04:14]**
**捷克语：** nebo tušeli, že tady kolem nás je. Stejně jak jsem se teďka ptal, tak hromada jako eh jako dost lidí zvedlo eh ruku. A co je zajímavý, když se podíváme kolem sebe, taky jako mainstreamový publikace jako Forbes píšou o tom, že
**中文：** 或者意识到它就在我们身边。就像我刚才问的，一大堆人举了手。有意思的是，看看周围，像《福布斯》这样的主流媒体也在写……


## 强化学习为何成为主流

**SECTION_NOTE**
- 类比深度学习十余年前的路径：从纯学术话题走向工业界主流
- 图灵奖线索：2018 年颁给深度学习（Bengio、Hinton、LeCun），约两年前（2024）颁给强化学习（Sutton & Barto）
- Forbes 等主流媒体已开始把「强化学习」称作 AI 革命、通往 AGI 的推动力
**END_SECTION_NOTE**

**[04:14 – 04:29]**
**捷克语：** Renaring je za eh za AI revolucí, třeba, že nás to dostane e až k AGI. Takže point tohodle slaju jenom říct, že se to stává čím dál tím víc mainstream. A tu analogii, kterou chci říct, je to samý
**中文：** 强化学习是 AI 革命背后的推手，比如它会把我们带向 AGI。所以这张幻灯片的观点只是：它正变得越来越主流。我想做的类比是，这和……是一回事。

**[04:29 – 04:43]**
**捷克语：** se v podstatě dělo s deep learningem jako takovým třeba 10 10 až 15 let zpátky, kde se v podstatě přehodnul z toho, že to byl čistě akademickej výzkumnej topik na univerzitách.
**中文：** 大概 10 到 15 年前深度学习所经历的过程——它从纯粹大学里的学术研究课题……

**[04:43 – 04:58]**
**捷克语：** Přehnul se k tomu, že začíná mít najednou velkej impact industryi. Začínalo to mít impakt na naše životy a deeplaned aplikace najednou začaly vznikat všude všude kolem nás. Tak to samý se teďka začíná dít maling.
**中文：** 转向开始对工业界产生巨大影响。它开始影响我们的生活，深度学习应用突然在我们身边到处涌现。现在强化学习正在经历同样的事情。

**[04:58 – 05:10]**
**捷克语：** Další analogie, kterou chci říct, že zmímco v roce 2018 díky tomu, jakj měl Deeping obrovskej impact na celej svět, tak dostali tyhlety tři pánové Joshua
**中文：** 我还想说另一个类比：2018 年，因为深度学习对整个世界产生了巨大影响，这三位先生——Joshua……

**[05:10 – 05:25]**
**捷克语：** Bener, Hinton Alekun dostali něco jako nobelovku pro computer science lidi a to je Touring Touring Award. A dva roky zpátky to samý obdrželi pánové za
**中文：** Bengio、Hinton、LeCun——拿到了计算机科学界的「诺贝尔奖」，也就是图灵奖。而两年前，同样奖项颁给了（强化学习领域）的几位先生。

**[05:25 – 05:40]**
**捷克语：** rainforce Melaning. Tak zase ta analogie toho, že Rainforce Maring je ta další revoluce, která se děje několik let po tom, co Deep Larning způsobil revoluci, tak je tady pěkně vidět eh pěkně vidět, když se podíváme jako na nějaký eventy v
**中文：** 强化学习。这就再次印证了那个类比：强化学习是继深度学习引发革命几年之后的「下一次革命」，如果我们看看时间线上的事件，就能很清楚地看到这一点。

**[05:40 – 05:51]**
**捷克语：** historii a v čase a porovnáme to spolu. Tak jo. A zase abych jakože drive home jako tu message, kterou vás chci jako nabudit na to, proč byste dneska neměli
**中文：** 在历史和时间的维度上对比一下就知道了。好的。再说一遍，为了把那个「为什么你们今天不该……」的信息讲透、让你们打起精神……

**[05:51 – 06:05]**
**捷克语：** usnout a proč tydlety věci by vás mohly zajímat do budoucna, je, že deplaning jako někoho takovej už v podstatě vyhrál, zatímco todle neplatilo 15 let zpátky nebylo ještě jasný, který metody eh machine learningu a AI v podstatě
**中文：** 睡着、为什么这些事值得你们将来关注——那就是：深度学习某种程度上已经「赢」了，而 15 年前还不清楚哪些机器学习、AI 方法……

**[06:05 – 06:19]**
**捷克语：** vyhrajou a jestli způsobej nějakou revoluci. Tak e teď už je to eh teď už je to prostě jako ta diskuze je over. Deep learning způsobil revoluci kolem nás v podstatě ve všech oborech.
**中文：** 会胜出、会不会引发一场革命。现在这场讨论已经结束了。深度学习几乎在所有领域都引发了我们身边的革命。

**[06:19 – 06:28]**
**捷克语：** Způsobilo to revoluci ve Vision, v Language, speech, robotics, prostě všude kolem nás, ať už prostě jedete autem,
**中文：** 它引发了视觉、语言、语音、机器人等各领域的革命，就在我们身边无处不在，无论你是在开车……

**[06:28 – 06:36]**
**捷克语：** otevřete si, otevřete si počítač, googlíte něco, jste na mapách, povídáte si, povídáte si s vaším chat GPT, tak
**中文：** 打开电脑、用谷歌搜索、用地图、和你的 ChatGPT 聊天……

**[06:36 – 06:44]**
**捷克语：** úplně všude už je dneska eh aplikovanej deep learning a v podstatě to úplně změnilo hrozně moc odbětí. No a ten
**中文：** 今天深度学习已经应用到几乎所有地方，它彻底改变了非常多领域。而那个……

**[06:44 – 06:53]**
**捷克语：** point, který teďka vidíme, že se děje, tak Rainfelink je v podstatě ten druhej přirozenj krůček nad tím a zase
**中文：** 我们现在看到的趋势是：强化学习本质上是往上的「第二步」，它又……

**[06:53 – 07:09]**
**捷克语：** přehoupává se to do toho, že způsobuje zase revoluci v těhletěch obdětvích a postupně to jako zlepšuje eh zlepšuje ty domény a umožňuje nám to dělat věci, který jsme předtím nikdy nedokázali dělat. A jako pěkný příklad je, kdo z
**中文：** 正在引发这些领域的又一场革命，逐步改善这些领域，让我们能做到以前做不到的事。一个很好的例子：你们当中有谁……

**[07:09 – 07:23]**
**捷克语：** vás, že jo, my jsme tady na matematické budově, tak kdo z vás si všimnul, že dneska ty největší jazykový modely dokážou už dokonce vyhrávat zlatý medaile na matematické olympiádě. Kdo z vás to nějak zaznamenal?
**中文：** 我们是在数学楼里，你们当中有谁注意到，今天最大的语言模型已经能在数学奥林匹克竞赛里拿金牌了？你们谁留意到这件事了？

**[07:23 – 07:37]**
**捷克语：** Super. Eh, tak to je jako soubojem strašidelný, že vy tady ten budete pět let studovat magistra, pak možná si uděláte doktorát a pak vás pak vás porazí porazí deep learning.
**中文：** 很好。呃，这真有点吓人——你们在这里读五年硕士，可能还要读博士，结果最后被深度学习打败了。

**[07:37 – 07:51]**
**捷克语：** Ale dneska se snad aspoň trošku víc dozvíme o tom, proč proč vás to poráží. A druhá druhé jako doména, kterou tady mám teďka je to jako velkej velkej topik, tak robotika taky začíná zažívat
**中文：** 但今天我们希望至少多了解一点，为什么它会打败你们。第二个领域，也就是现在很火的机器人，也开始经历……

**[07:51 – 08:00]**
**捷克语：** jako hodně exciting období díky tomu, že tam tyhlencty techniky začínají fungovat. Tak jo.
**中文：** 一个非常令人兴奋的时期，因为那些技术开始起作用了。好的。


## 深度学习速成：一个大函数与梯度

**SECTION_NOTE**
- 深度学习的直觉：神经网络就是一个由许多小函数依次组合而成的巨大函数
- 训练 = 计算梯度（误差对每个权重的敏感度），沿梯度方向微调权重以最小化数据集上的误差
- 本质是「监督学习」：给定输入，给定期望输出，让网络逼近映射
**END_SECTION_NOTE**

**[08:00 – 08:15]**
**捷克语：** A eh první věc, že já jsem mluvil o deep learningu enforcement learningu a dával jsem tam nějaký analogy, tak pojďme spolu pochopit, jaký je mezi těma věcma rozdíl, jak je to spolu spojený a eh
**中文：** 呃，刚才我讲了深度学习和强化学习，也做了一些类比，那我们一起来弄明白：这两者到底有什么区别、它们怎么关联，以及……

**[08:15 – 08:31]**
**捷克语：** potom se trošku zanoříme spolu pořádněc nebo jako pořádně dostáme trošku lepší intuici na to, jak ten renalenik vůbec [odkašlání] funguje. Eh co to co to zhruba dělá. Takže zase já se rychle zeptám, abych jenom jakože zopakoval ty čísla pro nás všechny. Kdo tak nějak
**中文：** 然后我们稍微深入一点，好好建立一点关于「强化学习到底[清嗓]是怎么运作的、它大致在做什么」的直觉。所以我再快速问一遍，帮大家回顾一下刚才的数字。谁大概……

**[08:31 – 08:42]**
**捷克语：** tuší, jak funguje deplat takovej? Super. Tak jo, je to dejme tomu třetinka, čtvrtinka lidí a teďka to
**中文：** 知道深度学习大概是怎么运作的？很好。好的，大概有四分之一到三分之一的人知道，现在……

**[08:42 – 08:56]**
**捷克语：** zkusím říct ve řeči matematiků a ve skutečnosti to nebude jako daleko od pravdy. Ve skutečnosti jakože myslím si, že to pochopíte během půl minuty a potom jako všichni byste dokázali e zvednout v
**中文：** 我用数学家的话来说，其实这也离真相不远。实际上我觉得你们半分钟就能懂，然后大家都能……举手。

**[08:56 – 09:06]**
**捷克语：** ruce. Tak e eh kdo z vás tuší, jak tuší, co to je gradient? Paráda. Super.
**中文：** 呃，你们当中谁知道「梯度」是什么？太棒了。很好。

**[09:06 – 09:22]**
**捷克语：** A to je v podstatě všechno, co potřebujete vědět na to, abyste věděli, jak funguje deep learning. Deep learning si to představte jako obrovskou funkci, která je poskládaná z nějak jako malejch funkcí, který se který se jako volaj volají po sobě. Občas jako když si
**中文：** 这基本上就是你们理解深度学习所需知道的全部。把深度学习想象成一个巨大的函数，它由许多小函数拼接而成，这些小函数一个接一个地被调用。有时候当你……

**[09:22 – 09:36]**
**捷克语：** vyklíte neuronovou síť, tak tam vidíte nějaké jako vyjete graf a ten graf to je prostě computational graf, kdy se to jako funkce za sebou za sebou skládá, jedna volá druhou a takhle se to jako propagujou ty čísla nahoru, že ta neuronová síť má na vstupu nějaký data,
**中文：** 画出神经网络，你会看到一张图，那张图就是计算图——函数一个接一个地组合，一个调用另一个，数字就这样向上传播。神经网络输入是某些数据……

**[09:36 – 09:45]**
**捷克语：** třeba obrázek, probublá probublá to těma funkcema nahoru a nahoře to má dát výstup třeba na tom, jestli na tom obrázku je kočka nebo pes. A jak to
**中文：** 比如一张图片，它「冒泡」般地穿过这些函数向上传播，在顶端输出结果，比如判断图片里是猫还是狗。它是怎么……

**[09:45 – 09:52]**
**捷克语：** funguje? Tak ze začátku inicializujeme ty funkce, tu nerovnou síť úplně náhodně. Ty ty máme tam nějaký váhy v té
**中文：** 工作的呢？一开始我们完全随机地初始化这些函数、那个神经网络。我们在里面有一些权重……

**[09:52 – 10:01]**
**捷克语：** nerovnové síti a ty funkce v podstatě něco dělaj, tak sčítaj násoběj čísla a proháněj to nějakou funkcí. Ale jsou tam teda nějaký parametry. No a ty parametry
**中文：** 在神经网络里，这些函数本质上在做一些运算——加减乘除、再过某个函数。但里面有参数。而这些参数……

**[10:01 – 10:13]**
**捷克语：** mi na něco nelze náhodně, takže ze začátku nám to v podstatě náhodně říká, jestli je to keč kočka nebo pes. A potom co děláme? My v průběhu tréninku máme nějaký data, o kterých třeba víme, jestli na obrázku je kočka nebo pes.
**中文：** 一开始是随机的，所以一开始它基本上是在随机地说这是猫还是狗。那我们做什么呢？在训练过程中，我们有一些数据，我们知道图片里是猫还是狗。

**[10:13 – 10:21]**
**捷克语：** Spočítáme si gradient. To znamená, kdybysme pohli s tou váhou doleva nebo doprava, tak jestli by nám to zvětšilo nebo zmenšilo pravděpodobnost toho
**中文：** 我们计算梯度。意思是：如果我们把那个权重往左或往右挪一点，会不会增大或减小我们想要的输出……的概率。

**[10:21 – 10:35]**
**捷克语：** výstupu, kterej nás najmá, který chceme, aby nám ta síť dala. No a v podstatě jenom v podstatě tohlencto opakujeme na velkej trénovací e trénovací množině dělat, jo? Tak deit to je v podstatě všechno, co potřebujete vědět o tom, jak
**中文：** 我们想要的输出……的概率。基本上我们就是在庞大的训练集上不断重复这个过程——这就是理解深度学习运作所需的全部。关键一点是：我们所做的，是最小化某种误差；误差定义在我们的（图片）数据集上，即网络给出的输出与我们期望它给出的输出之间的差距。强化学习和纯监督式深度学习有共同点，但也加入了新东西：共同点是，我们依然生活在神经网络的世界里，它依然是一种调整网络权重、让网络做我们想要之事的技术。

**[10:35 – 10:51]**
**捷克语：** funguje depl. Ale ta důležitá věc je, že eh to, co děláme, tak minimalizujeme nějakou chybu a ta naše chyba je prostě na tom datasetu obrázku, tak si definujeme chybu podle toho, jak hodně
**中文：** （承上）它是怎么运作的。重要的是：我们所做的，是最小化某种误差；误差定义在我们的图片数据集上，根据网络预测的输出与我们期望的输出之间的差距来定义。强化学习与纯监督式深度学习有共同点，也加入了新东西。共同点是，我们依然在神经网络的世界里，它依然是一种调整网络权重、让网络做我们想要之事的技术。

**[10:51 – 11:06]**
**捷克语：** dobře to predikuje eh ty výstupy, který bysme tak nějak doufali, že nám ta ta síť dá. Jo, super. No a reinforcement learning, tak má něco jako společnýho s čistě jako supervis nebo s supervis deep
**中文：** ……深度学习，但同时又加入了新东西。它们的共同点是：我们依然生活在神经网络的世界里，它依然是一种调整网络权重、让网络做我们想要之事的技术。


## 强化学习是什么：智能体·环境·奖励·序列决策

**SECTION_NOTE**
- 与监督学习共享同一套神经网络世界观，但任务不同：不再给定「期望输出」，而是让智能体在环境中「做得好」
- 智能体（神经网络）观察环境 → 输出动作 → 环境返回奖励(reward)与新的观测(observation)
- 目标是最大化「一段序列动作」上累积的奖励（sequential decision making），而非单步最优
- 直觉案例：国际象棋（动作=走子，奖励=终局胜/负/和）；雅达利（动作=按键，奖励=游戏分数）
**END_SECTION_NOTE**

**[11:06 – 11:22]**
**捷克语：** learningem, ale zároveň tam přidává něco novýho. Takže to, co mají společný, že pořád typicky žijeme ve světě ve světě těhletěch neuronových sítí. Pořád je to jako nějaká technika, která se snaží pošoupat ty váhy sítě, aby ta síť dělala to, co chceme.
**中文：** 再来理解深度学习是怎么运作的。把深度学习想象成一个巨大的函数，它由许多小函数拼接而成，这些小函数一个接一个地被调用。有时候当你……

**[11:22 – 11:30]**
**捷克语：** Ale ten task, v kterej se snažíme eh tu síť pošoupat, aby dělala, co chceme, je trošičku jinej. V tom klasickým deplay
**中文：** 但我们要调整网络、让网络做我们想要之事的这个「任务」，稍微有点不同。在经典的监督式深度学习里，任务很明确：我们有一些输入，也有我明确指定的输出——我清楚想要网络给出什么。

**[11:30 – 11:45]**
**捷克语：** linku supervis, tak vysloveně ten task je OK, máme nějaký vstupy a mám přesně daný výstupy, který od tý sítě chci. Právě třeba todle je kočka, todle je pes, to todle je hroinfalce malaru místo toho, co mám, je pořád to
**中文：** 比如「这是猫、这是狗」——而我有的始终是那些输入。那个神经网络，输入完全一样，但这一次在输出端，我完全不知道它该做什么。

**[11:45 – 11:53]**
**捷克语：** má nějaký vstupy. Ta ta neuronka eh jakože na vstupu úplně stejný, ale tentokrát na výstupu já úplně jako
**中文：** 这一点我想留给神奇的强化学习算法去解决。我所知道的典型情况是：我希望那个神经网络在某个环境里做出某种非常好的事情。

**[11:53 – 12:02]**
**捷克语：** nevím, co by tak měla dělat. To to chci nechat na tom kouzelným reinforcement learning algoritmu. Místo toho, co já typicky vím, je, že chci, aby ta
**中文：** 好，下一张幻灯片就会更清楚。

**[12:02 – 12:13]**
**捷克语：** neuronka v nějakým prostředí dělala něco hrozně moc dobrýho. Jo a hnedka na dalším na dalším slidu to bude to bude jasnější.
**中文：** 这就是强化学习通常所处的典型图景。我们有一个「智能体」（agent），它处在一个环境中，可以执行某些动作。

**[12:14 – 12:25]**
**捷克语：** Todle je typicky obrázek, v kterým v kterým reinforcement learning žije. Máme máme agenta, ten je v prostředí, který má k dispozici nějaký akce.
**中文：** 每当智能体执行某个动作，环境就会返回一个数字——也就是「奖励」（reward），同时也会返回对环境的某种「观测」。关键点是：这个智能体会努力在这个环境里最大化它的奖励。

**[12:25 – 12:41]**
**捷克语：** A kdykoliv, kdy ten agent udělá nějakou akci, tak z toho prostředí obdrží nějaký číslo, nějaký reboard a potom taky obdrží nějaký pozorování toho z toho z toho prostředí. Jo, hnedka hnedka si to spolu všechno vysvětlíme, ale co je co
**中文：** 回到神经网络：在这里我们会尝试调整神经网络的权重。而这个神经网络本质上就是那个智能体——它在输入端接收来自环境的「所见」，在输出端做出一个动作。

**[12:41 – 12:57]**
**捷克语：** je důležitý, že ten agent se bude snažit tady maximalizovat tu reward v tom prostředí. Takže zase zpátky k té neuronce. Tady se budeme snažit nějak eh nějak šoupat váhy té neuronky. A to neuronka je to v podstatě ten agent. Ta
**中文：** 我需要调整神经网络的权重、或者说调整智能体的策略，让它做出的动作能带来尽可能大的奖励（reward）。这大致就是整个设定。

**[12:57 – 13:08]**
**捷克语：** neuronka jakoby na vstupu dostane, co vidí z toho prostředí a na výstupu udělá akci. A já potřebuju šoupat váhy té neuronky nebo upravovat strategii toho
**中文：** 为了让大家都完全清楚，我们来看两个具体例子，看看这个简单的想法可以怎么应用。

**[13:08 – 13:17]**
**捷克语：** agenta tak, aby nám dělala takový akce, abysme dostali co největší rivot. Jo, takže tohlecto je jako zhruba ten setup.
**中文：** 比如把它应用到国际象棋上：智能体在环境中的动作，就是移动棋子。按照我们的设定，为了简单，也许我们会……

**[13:17 – 13:27]**
**捷克语：** A teďka jen, aby to bylo úplně všem jasný, tak ukažme si dva konkrétní případy, jak bysme to třeba mohli jako aplikovat takhle jednoduchou myšlenku.
**中文：** 64 个格子，对吧，再加上 64 个表示可以从哪里移动棋子的格子。这只是一种可能的表示方式；总的来说，就把它想成智能体可以执行的一组动作。

**[13:27 – 13:42]**
**捷克语：** Tady bysme, kdybysme to chtěli aplikovat na šachy, tak ty akce toho agenta v prostředí, tak bylo šoupáme prostě figurkama. Měli bysme tam zase podle toho, jak to máme eh daný, tak eh nevím, třeba pro jednoduchost by to bylo máme
**中文：** 国际象棋里的奖励会非常简单：我们在游戏结束时才会得到 +1、0 或 -1（胜/平/负）。

**[13:42 – 13:50]**
**捷克语：** 64 políček, že jo, a potom 64 dalších políček jakoby odkud můžeme třeba něco něco šoupnout. To je jako jedna možná
**中文：** 取决于我们是赢了、平了还是输了。而智能体（或神经网络）在输入端得到的观测，就是「看看棋盘现在是什么样子」。

**[13:50 – 14:05]**
**捷克语：** reprezentace, ale obecně prostě představ si to, je to nějaká jako množina akcí, kterou má ten agent k dispozici. Ten reward v Čachách by byl hrozně jednoduchej. Hold bysme až na konci hry obdrželi jedničku, nul nebo minusni.
**中文：** 这是第二个也非常简单的例子：如果智能体玩某个电脑游戏。图上这些是非常老的雅达利（Atari）游戏。

**[14:05 – 14:18]**
**捷克语：** podle toho, jestli jsme vyhráli, remizovali nebo prohráli. A ta observation toho agenta, co má jakoby ta ten agent nebo neuronka na vstupu, tak je prostě podívám se, jak vypadá ta šachovnice. Jo.
**中文：** 你们大概没人玩过这些，但也许看过相关视频。再想象一下——你们可能知道那种大机箱，投币进去就能玩，或者至少见过。

**[14:18 – 14:27]**
**捷克语：** A tady je druhej příklad taky hrozně jednoduchoučkej, když by ten agent hrál třeba nějakou počítačovou hru. Tohlecto eh konkrétně na obrázku jsou takový
**中文：** 就那样想象。智能体的动作就是按机箱上的按钮，有某种摇杆。那些就是动作。

**[14:27 – 14:35]**
**捷克语：** strašně starý eh Atary hry. Tohlencto pravděpodobně nikdo z vás eh asi asi nehrál, ale možná jste viděli nějaký
**中文：** 奖励通常是游戏里的得分——你在这款游戏上得了多高的分。而观测就是看显示器，那是我们智能体的输入。

**[14:35 – 14:50]**
**捷克语：** videa z toho. Zase představte si to. E možná znáte takový ty jako velký boxy, do kterejch se házeli házeli drobný a potom jako lidi lidi mohli na tom hrát nebo minimálně jste to viděli. Tak tak si to představte. Vysloveně ty akce toho
**中文：** 好，那我问一下：至少这个设定，大家都明白了吗？很好。但请大家随时提问，因为如果我们在最基础的设定上就迷失了，后面的内容就会讲不好。

**[14:50 – 14:57]**
**捷克语：** agenta můžou bejt mačkat čudlíky na tom boxu. Máme tam nějakej joystick. To jsou to jsou ty akce. reward je tydlety hry
**中文：** 好的。那接下来几张幻灯片，我就来让大家对「它是怎么运作的」建立一点直觉。

**[14:57 – 15:12]**
**捷克语：** typicky by jste neměli skóre jaký vysoký skóre jste nahráli na té hře a to observation tak prostě se můžeme podívat na ten monitor a to je ten vstup toho našeho agent jo tak jo, tak já se zeptám, dává minimálně tenhlecten setup,
**中文：** 现在也许有一个重要的事要点出来：在这个我们刚简单解释过的环境里，我们要做的事，就是找到这样一个智能体、这样一种策略、或者说这样一种神经网络权重，使得奖励最大化。

**[15:12 – 15:21]**
**捷克语：** v kterým eh se pohybujeme smysl? Jo, super. Ale jako prosím, e, kdykoliv se ptejte, jo, protože když, že jo,
**中文：** 而极其重要的是：我们对奖励的最大化，和经典监督学习不同——那里我们有一个目标和一个输出，只是尽量缩小目标和输出之间的误差；而这里的奖励往往要到「未来某个时刻」才出现。

**[15:21 – 15:33]**
**捷克语：** když, e, úplně basic setup, e, eh, neví, jakože když se ztratíme v tom basic setupu, tak ten zbytek bude eh bude špatnej.
**中文：** 如果我们在最基础的设定上就迷失，后面就会讲不好，所以请随时提问。

**[15:33 – 15:41]**
**捷克语：** Tak jo. A já jenom Jasně, super. Tak na dalších slidech už se pustím do toho, abysme získali trošku intuici, jak to
**中文：** 好的。接下来几张幻灯片，我就带大家获得一点关于它如何运作的直觉。

**[15:41 – 15:49]**
**捷克语：** funguje. A teďka možná ta důležitý eh důležitá věc, kterou si ještě z toho odníst, je v tomhletom prostředí, který
**中文：** 现在要强调一个重要的事：在这个我们刚解释过的环境里，我们要做的是找到一种策略或一组神经网络权重，来最大化奖励。

**[15:49 – 16:05]**
**捷克语：** jsme si teďka jednoduše vysvětlili, tak co se snažíme dělat, je snažíme se nějak najít takovýho agenta, takovou strategii nebo takový takový váhy ty neuronky pro toho agenta, abysme maximalizovali reward. A co je strašně důležití,
**中文：** 我们刚才简单解释过的环境里，我们要做的事就是找到这样一个智能体、这样一种策略，来最大化奖励。而极其重要的一点是……

**[16:05 – 16:12]**
**捷克语：** maximalizuje reward v nějakým nějaký sekvenci tahu. Neznamená to, že prostě vidíme ten jako ten monitor jednou a
**中文：** 最大化「某段动作序列」上的奖励。并不是说我们看一下显示器、按一次按钮、游戏结束就完了——不是的，非常重要的是，我们有一个动作序列。就像下棋有一连串走法一样。

**[16:12 – 16:21]**
**捷克语：** jednou zmáčkneme tlačítko a konec hry, ne? Strašně důležitá. Máme jako sekvenci tahů. Podobně jako v šachu máme sekvenci tahů. Stejně tak, když hrajeme tu počítačovou hru, tak nezmáčkneme jako
**中文：** 我们也不是只按一次键盘鼠标，而是智能体有一串动作。我们要寻找的，是一种策略，它在给定的一个回合或一段时间里，最大化游戏中累积的奖励。

**[16:21 – 16:35]**
**捷克语：** klávesnici a myš jenom jednou, ale je tam prostě sekvence eh tahu toho agenta, jo? A co se snažíme najít, je taková strategie, která přes nějaké jako specifikované epizodu nebo čas, tak maximalizuje ten nasbíranj reward ve
**中文：** 这就是我们最终关心的事。这意味着，我们有时会在局部做一件看起来不是最优的事，因为我们在那几秒里只收集到很少的奖励，但整体而言这是正确的决策——

**[16:35 – 16:50]**
**捷克语：** hře. Jo a to je to, co nás ultimátně zajímá. To znamená, že občas můžeme jako lokálně udělat něco, co vypadá so optimálně, protože jsme během třeba těch teďka těch p sekund nasbírali málo málo rewardů, ale overall to byl jako správná
**中文：** 因为当我们看一个小时长的轨迹时，它其实是最优策略，因为我们要在长长的轨迹上累积尽可能多的效用。

**[16:50 – 16:59]**
**捷克语：** správná decision to be made, protože když se podíváme jakože na hodinu dlouhou trajektorii, tak ve skutečnosti je to ta optimální strategie, protože
**中文：** 这种「序列性」极其重要——它是序列决策（sequential decision making）。我希望你们把这个印在脑子里，等你们真正理解它之后，就会看到这些方法应用起来有多简单。

**[16:59 – 17:13]**
**捷克语：** nasbírám co nejvíc co nejvíc tej utility na ty dlouhý trajektory, jo. Takže ta sequentialeta je strašně strašně důležitá, že to jako, že je to sequency decision making, to vám chci vyvoláit do hlavy, ale když když to tak nějak jako
**中文：** 最后我们会回到那些 AI 模型，以及为什么正是这些方法能很好地解数学题、为什么目前恰好是这些方法在起作用。好的，这个设定听起来应该非常简单，

**[17:13 – 17:27]**
**捷克语：** když tole člověk dostane pod kůži, tak o to hezčí a jednodušší potom bude vidět, jak strašně jednoduchý je tydlety metody aplikovat. Právě úplně na konci se vrátíme k těm EA modelům a proč to
**中文：** 但魔力在于：我们到底怎么做到这种事？怎么找到一个能最大化动作序列的好策略？我们不会完全深入算法细节，但我认为你会获得足够的直觉，理解今天的算法是怎么运作的。

**[17:27 – 17:42]**
**捷克语：** dokáže dobře dobře třeba řešit ty matematický úlohy a proč zatím jsou přesně tyhle metody, jo? Tak jo, super. Tak toleto je setup. Ten setup zní doufám strašně jednoduše,
**中文：** 好的，那我们就开始吧。第一步是大致说明，这样一幅图通常是怎么形式化的。

**[17:42 – 17:54]**
**捷克语：** ale eh teďka magie, jak sakra vůbec něco takovýho člověk dokáže dělat, jak dokážeme vůbec eh jakoby najít dobrou strategii, která teda maximalizuje tu tu
**中文：** 这些形式化可以有很多种，会因环境而异——取决于智能体所处的环境是否能完全观测，比如在象棋中，智能体看到的就给出了世界状态的全部信息。

**[17:54 – 18:07]**
**捷克语：** sekvenci akcí, jo? A zase nepůjdeme úplně super do hloubky těch algoritmů, ale myslím si, že si odnesete dostatečně dobrou intuici o tom, jak ty dnešní algoritmy fungujou.
**中文：** 其他形式化可能更有趣，比如当智能体只能部分观测世界——显示器的一部分被挡住了，看不完全。还有些形式化取决于环境里是只有一个智能体（单人环境）还是有多个玩家。


## 数学形式化：MDP、回报、折扣因子 γ、策略与最优策略

**SECTION_NOTE**
- 用图建模：顶点=状态，边=在某状态下采取某动作后可达的下一状态
- 形式化为马尔可夫决策过程(MDP)：状态集合、动作集合、转移概率、每步奖励
- 回报(return)=一段序列上（折扣）奖励之和；折扣因子 γ 让「近处的奖励」更重要
- 策略(policy)=在每个状态下对各动作的概率分布；存在使累积奖励最大的「最优策略」
- 单智能体环境下最优策略只取决于自己；多智能体时对手的策略也会影响你的回报
**END_SECTION_NOTE**

**[18:07 – 18:18]**
**捷克语：** Tak jo, tak se na to jdeme vrhnout. Super. Tak první věc je, že eh se podívat na to.
**中文：** 这些方面都可以不同。但在最简单的情况下——我们今天需要的、实际上对语言模型也够用的——基本上就是「单人、完全观测」的环境，通常建模成一个简单的图，

**[18:18 – 18:31]**
**捷克语：** První krok je si říct zhruba, jak se takovejdle obrázek typicky formalizuje. A těch formalismů je může bejt víc, ty, který se částou lišej podle toho, jestli v tom prostředí, kterej ten agent se
**中文：** 其中节点对应环境的状态、或者说智能体可能所处的状态。比如在国际象棋里，每个节点简化来说对应棋盘的某种布局。

**[18:31 – 18:41]**
**捷克语：** pohybuje, jestli má jako úplný pozorování v tom prostředí, jako třeba v šachách, tam prostě to, co agent vidí, tak mu dává veškerou informaci o tom, v jakém stavu je ten svět.
**中文：** 节点之间的边，对应智能体执行某个动作后可以转移到的位置。在象棋里这非常简单：就是「走哪一步、棋盘怎么变」。

**[18:41 – 18:55]**
**捷克语：** Jiný formalismy třeba můžou být zajímavější, když ten agent má jenom částečný pozorování o tom o tom světě. Třeba část monitoru je zakrytá, nevidíme tam přesně. A jiný formalismy, zase můžou bejt můžou bejt závajný pro to,
**中文：** 这张图借自 David Silver 的某张幻灯片，上面有个学生为了考试在学习——你顺着节点看就能发现，学习会给他短期负奖励，而去酒吧短期是正奖励；

**[18:55 – 19:10]**
**捷克语：** jestli ten agent žije v prostředí, kde je jenom ten agent samotnej. To znamená jakože je to jako eh je jsou to jednohráčový eh prostředí a nebo jestli je to v prostředí, kde těch hráčů je víc. Takže v tomhleom se to samozřejmě všechno může může lišit, ale v tom jako
**中文：** 但当我们最大化一段较长的动作序列、寻找最优策略时，在这个图里不难看出：最优的做法是忍受短期的负奖励，最后通过考试拿到那个大的正奖励。这就是它大致的形式化方式。

**[19:10 – 19:25]**
**捷克语：** nejjednodušším případě, který nám v podstatě stačí pro to, co potřebujeme dneska a i pro to, co ve skutečnosti je potřeba zrovna pro ty jazykový modely, tak jsou to v podstatě jednohráčový prostředí s s úplným pozorováním a jak se to typicky modeluje nějakým jako
**中文：** 左边那个图不重要，我们主要形式化右边那个。我们有一些节点集合、动作集合，还有一个转移函数：当我们在某个状态执行某个动作，就会以某种概率分布转移到不同状态，同时在每次转移时可能获得奖励。

**[19:25 – 19:39]**
**捷克语：** jednoduchoučkým grafem, kde vrcholy odpovídám odpovídají stavům toho prostředí nebo spíš stavům e toho agenta, e, v kterých on může bejt. Takže v těch šachách například každej vrchol
**中文：** 在象棋里这非常简单，因为奖励通常只在游戏结束时才拿到。好的，这有意义吗？很好。

**[19:39 – 19:51]**
**捷克语：** by zjednodušeně řečeno odpovídal různej konfiguraci [frknutí] té šachovnice. Hrany mezi těma vrcholama odpovíde tomu, když ten agent vydá nějakou akci, tak co
**中文：** 所以基本上它让我们能正式定义那些自然需要的东西——在图里我们需要动作、奖励、观测，这里我们也只是把它们都定义清楚。太好了。

**[19:51 – 20:06]**
**捷克语：** jakoby kam se může přesunout, jo. Takže eh pro v šachách by to bylo hrozně jednoduchočký, protože tam byl to bylo jako jedna: J to, jakou akci zahrajeme a jak se ta šachovnice změní. Jo. Eh, tady tohlencto je jako ukradenej, myslím, od
**中文：** 再来一些字母（你们肯定喜欢字母），不过我们更想讲清楚这些字母背后的直觉。

**[20:06 – 20:21]**
**捷克语：** Davida Silvera nějakej e nějakej slaj, kde má studenta, kterej se učí, eh, na zkoušku a je tam právě pěkně vidět, když si člověk prochází ty vrcholy, jaký akce může udělat, tak studovat eh nám dá krátkodobě negativní reward, mnohem jako
**中文：** 在这个形式化里，我们定义了奖励：从节点移动到节点时会得到奖励。通常我们还会定义「回报」（return），它无非就是一段时间内累积的奖励之和。

**[20:21 – 20:37]**
**捷克语：** eh lepší e do hospody, protože krátkodobě nám to dá jako pozitivní reboard, ale zase když jako maximalizujeme nějakou eh delší sekvenci akcí a hledáme optimální strategii, tak eh Eh, zhromat v tomhleom grafu, eh, není těžký vidět, že optimálně si to
**中文：** 这里具体是到无穷远，但也取决于所处环境。你可以注意到这里有个 γ（gamma）。它可有可无。它典型代表什么、为什么要用的折扣奖励（discounted reward）：直观上说，智能体 100 步之后得到的奖励，可能不如 1 步或 10 步之后的奖励那么让它关心。

**[20:37 – 20:52]**
**捷克语：** občas protrpět tu krátkodobě negativní reward, aby člověk na konci pásnul zkoušku a dostal třeba ten velkej pozitivní reward, jo, že todleto je zhruba, eh, jak se to formalizuje. Eh, tady nalevo zase není to extra důležitý,
**中文：** 我们有时会忍受短期的负奖励，好让最后能通过考试、拿到那个大的正奖励——这大致就是它的形式化方式。左边那个图不重要，我们主要形式化右边那个图。

**[20:52 – 21:04]**
**捷克语：** eh jak to vypadá, ale v podstatě jenom zformalizujeme ten obrázek napravo. Takže máme nějaké jako množiny vrcholů, akcí, máme tam máme tam přechodovou funkci. To znamená, když jsme v nějakém stavu, uděláme akci, tak máme nějakou
**中文：** （承上）我们形式化右边那个图：有节点集合、动作集合，还有一个转移函数——当我们在某个状态执行某个动作，就会以某种概率分布转移到不同状态，且在每次转移时可能获得奖励。在象棋里这非常简单，因为奖励通常只在游戏结束时才拿到。

**[21:04 – 21:18]**
**捷克语：** pravděpodobností distribuci, do kterejch různejch stavů se můžeme dostat a zároveň při každým jako přechodu ze stavu do stavu můžeme obdržet reward. Jo, v těch šachách by to bylo hrozně jednoduchý, protože ten reward bych typicky obdržel až úplně na konci e té
**中文：** 好的，有问题吗？目前说得通吧？很好。所以基本上它让我们能正式定义那些自然需要的东西——在这个图里我们需要动作、奖励、观测，这里我们也只是把它们都定义清楚。太好了。再来一些字母（你们肯定喜欢字母），不过我们更想讲清楚这些字母背后的直觉。

**[21:18 – 21:33]**
**捷克语：** party. OK. Eh, dotazy dává to zatím smysl. Super. Tak jo. Takže v podstatě nám to umožní jenom jako formálně si zadefinovat ty věci, který tak tak nějak
**中文：** 在这个形式化里我们操作、关心的东西：有定义好的奖励——从节点移动到节点时得到奖励；然后通常我们定义「回报」（return），它无非就是一段时间内累积的奖励之和。这里具体是到无穷远，但也取决于所处环境。你可以注意到有个 γ（gamma）。

**[21:33 – 21:47]**
**捷克语：** přirozeně budeme potřebovat, že jo, v tom i v tom obrázku, kterj směme úplně tady, tak potřebujeme máme nějaké akce, rewardy, observations, tak zase tady si to všechno jenom prostě zadefinujeme, co potřebujeme. Paráda. Super. Eh, další
**中文：** 它可有可无。它典型代表什么、为什么用？就是折扣奖励（discounted reward）：直观上，智能体 100 步之后得到的奖励，可能不如 1 步或 10 步之后的奖励那么让它关心。

**[21:47 – 21:56]**
**捷克语：** nějaký písmenka, protože vy máte určitě písmenka rádi, ale pojďme si spíš říct tu jako intuici, co to, co ty písmenka znamenaj.
**中文：** （清嗓）第一点动机：100 步后的奖励不如近处的奖励让智能体关心。第二点：在某些环境里我们几乎必须有 γ，否则连谈论「最优策略」都没意义——但这只是技术细节。[响指] 好。当我们把这些定义好——知道智能体所处的环境、也定义了它的策略（policy）……

**[21:56 – 22:11]**
**捷克语：** Tak ty věci, s kterýma se tam operuje a který nás zajímají, tak když máme tenhlecten formalismus, máme tam, máme tam zadefinovaný tj reward, že dostaneme reward, když se přesuneme z vrcholu do vrcholu, tak potom se typicky
**中文：** 策略无非就是：在每个节点上，对可用的动作有一个概率分布。这就是智能体的策略。我们知道它的回报长什么样，于是自然就能比较两种不同的策略——我们有两个不同的机器人、两个不同的神经网络，各自在环境里收集到不同的奖励。它不过是个数字，就是某个浮点数的和。

**[22:11 – 22:25]**
**捷克语：** deferne něco jako return a to není nic jinýho než zase eh nějaká suma těch rewardů, kterou naakumulujeme eh za danej čas. Tady, tady konkrétně je to až donekonečna, ale zase záleží, v kterém
**中文：** 一个智能体收集了 8 块钱，另一个收集了 10 块，我们就能说：好，这个智能体、这个策略大概比另一个好。漂亮且重要的是：可以证明存在某种「最优策略」——存在一个智能体、一种 policy，它的奖励基本是最大的，不会再有更大的策略。在单人环境里这相对容易证明。

**[22:25 – 22:39]**
**捷克语：** bysme byli prostředí. A můžete si tady všimnout, že je tady, že je tady gama. Zase ta ta tam může bejt, nemusí. A co typicky ta gama znamená? Proč se používá? Je to discounted reward v tom smyslu, že se snažíme nějak e
**中文：** 也很容易让人相信它会成立。稍微复杂一点的是：当环境里有多个玩家时，「最优策略」到底意味着什么——因为在多人环境里，我们的智能体收集多少奖励，不再只取决于「我怎么玩、我的策略是什么」。一旦变成多人环境，这一点就不成立了，比如我下棋还取决于对手怎么下。

**[22:39 – 22:47]**
**捷克语：** [odkašlání] za prvý ta motivace je, že ten reward, kterej ten agent dostane za 100 kroků, tak třeba ho zajímá míň, než kterej
**中文：** 它不再是单一策略的函数。但为简单起见，我们在单人环境里讨论，这个性质成立，也很容易展示。太好了。所以我们有了最初那些「积木块」——有了一个形式化框架，知道我们要找什么。但怎么找到它呢？如果环境足够小、能放进显示器或电脑，那正是你们如果选了「强化学习入门」课会学的内容。

**[22:47 – 22:56]**
**捷克语：** dostane za krok nebo za 10. To je jako první motivace. Druhá věc je, že v v některých typů prostředí to ve skoro
**中文：** 我可以强烈推荐 Traka 在小组里开的很好的强化学习课。但我的重点是：如果图足够小，我们几乎能遍历它、在电脑上跑算法，那么要有能收敛到最优解的算法并不难——它们能真正找到这种图里的最优策略。

**[22:56 – 23:10]**
**捷克语：** potřebujeme tam tu gamu mít, aby vůbec eh mělo smysl mluvit třeba o optimálních strategiích a podobně, ale to je zase jenom techniká. [frknutí] Super. No a eh když máme v podstatě eh
**中文：** 所以这是第一步。但现实中我们关心的环境、应用，永远不会小到能放进电脑。即便象棋——比起真实世界、比起语言模型，象棋听起来像个简单问题——但光是象棋（更别说围棋）的状态数，都比宇宙中的原子还多。所以我们几乎永远无法靠堆算力把它彻底解决。

**[23:10 – 23:18]**
**捷克语：** tyhlety věci zadefinovaný, víme, jak vypadá to prostředí, v kterém se na náš ten agent pohybuje, máme zadefinovaný,
**中文：** 必须另寻他法——必须做某种近似。而正因为必须近似，这恰恰是神经网络和强化学习能漂亮结合的原因。强化学习入门课里，你学的正是前两三张幻灯片的内容——形式化长什么样、有哪些理论结果、有哪些算法来解决那些小小的任务。

**[23:18 – 23:27]**
**捷克语：** co je ta strategie nebo policy toho agenta. To není nic jinýho, než že v každém vrcholu máme nějakou distribuci přes ty akci, který v tom vrcholu máme k
**中文：** 但对于那些大任务——要让它在真实世界里管用——靠的是把强化学习和深度学习结合起来。因为神经网络：我们其实并不是非得用它——如果只是小表格，跑个循环更新策略就行。

**[23:27 – 23:36]**
**捷克语：** dispozici. Decit. Tak jako to je ta strategie toho agenta. Tady víme, jak vypadá jeho return. Tak potom můžeme samozřejmě porovnávat dvě různý
**中文：** 一旦图变得极其巨大、我们没法遍历节点时，才需要神经网络——用它们来在巨大的图里做某种「泛化」。它真的会极其庞大，我们永远不可能走遍所有节点，所以神经网络让我们只走一部分节点，从中学习、改进，然后帮我们泛化。

**[23:36 – 23:45]**
**捷克语：** strategie. Máme dva různý roboty, máme dvě různý neuronky a každá z nich nasbírá v tom prostředí jinej reward. Je prostě jenom číslo, že jo. Je to prostě
**中文：** 现在把这一点和「神经网络在监督式设定里做什么」联系起来就非常简单了：在那里我们调整神经网络权重，让它能很好地识别图片里的猫、狗或河马。我们用神经网络做图像识别，是因为它们在经验上极其有效——当它看过大量猫狗图片、我们把权重调得足够好，它就能在我们给它的训练集上表现良好；而且它通常泛化得很好：当我们给它看一张它在调权重时从没见过的猫图，它其实有很高的概率能把这张没见过的图里的猫和狗区分开。

**[23:45 – 23:57]**
**捷克语：** ta suma jenom nějakej float. Tak jeden agent nasbírá jako osm peněz, další nasbírá 10 peněz, tak můžeme říct, ok, super, tak tenhlecten tenhlecten agent, tahle strategie asi lepší eh než ta druhá strategie.
**中文：** 这正是它在这里被使用的原因：我们只走图里的部分节点，希望借助大的神经网络——当我们从某个节点学到了东西，而另一个节点与之相似（类似的棋局、类似的世界状态、或者你给 ChatGPT 的类似输入），网络的泛化就能在那个状态下给出我们需要的合理输出。好。

**[23:57 – 24:13]**
**捷克语：** No a eh co je pěkný a důležitý, že se dá ukázat, že existuje něco jako optimální strategie v tom smyslu, že existuje agent, existuje policy taková, která má v podstatě ten maximální
**中文：** 这又说得通了吧？很好。我说过，随时打断我、追问细节。好，现在我们再深入一圈，建立直觉：那些在图里寻找好策略的算法，到底是怎么和深度学习结合起来的。

**[24:13 – 24:28]**
**捷克语：** reward, jo, že nebude, že nebude existovat jiná strategie, která která bude mít větší. A todle v zrovna v jednohráčovejch prostředí je relativně jednoduchý ukázat. Je to je to jako believable, proč by to asi mělo platit,
**中文：** 好。[响指] 怎么做呢？其实非常简单：我们会迭代地生成训练集，之后像监督学习一样使用它。马上解释。在监督学习里，我们通常有标注数据（猫、狗），定义某种损失函数，然后用梯度改变权重、改变网络参数，来在收集到的数据集上提升网络表现——这就是监督学习的步骤，也是它唯一在做的事。

**[24:28 – 24:36]**
**捷克语：** co je o něco složitější si vůbec zamyslet nad tím, co tak může znamenat optimální strategie e v prostředí, děti těch hráčů je víc, protože tam najednou
**中文：** 而强化学习的「区分性步骤」通常是迭代使用的：我们有一个极其巨大的图，节点数这辈子甚至宇宙里都走不完，所以我们只走一个子集，而且一开始走得很随机。比如想象下棋：我们一开始完全随机地走子。这是很糟的策略，但总得有个起点——当网络权重随机初始化、智能体随机初始化时，我们就只能随机走子。

**[24:36 – 24:51]**
**捷克语：** ten, zatímco tady platí, že kolik ten náš agent nasbírá toho rewardu, tak zavěší si jenom na tom, jak hraju já, jenom jaká je moje strategie, tak jakmile je to vícehráčový prostředí, tak už to najednou neplatí, že jo. jak já
**中文：** 这样的策略会走过巨大象棋图的某个子集。从初始糟糕策略收集到的节点（轨迹），就定义了我们的数据集，在上面跑经典的监督学习：定义要最小化的损失，跑梯度下降，调整网络权重，来提升网络在收集数据上的质量。只不过这里的损失不再对应「有没有把猫和狗分对」，而是对应「我们在训练集上收集到了多少奖励」。

**[24:51 – 25:03]**
**捷克语：** odehraju šachy, tak eh záleží na tom, jak samozřejmě bude hrát můj oponent. Není to jako funkce jenom jedné strategie, jo? Ale pro jednoduchost, když jsme tam v single hráčovým
**中文：** 所以当我们对收集到的轨迹跑梯度时，本质上是想增大那些带来更多奖励的轨迹的概率、相对减小那些只带来很少奖励的轨迹。比如随机下棋时，如果运气好走到了将死对手的终局、拿到 +1 奖励，我们就试着提高下次再走出这种序列的概率。

**[25:03 – 25:17]**
**捷克语：** prostředí, tak tole platí a jednoduchoučky jdu ukázat. Jo, paráda. Tak jo, takže eh máme ty první takový ty první building bloky toho,
**中文：** 好。一旦我们在收集到的轨迹集上改进了网络，就有了新的网络权重。把新权重再丢回环境，再下很多盘棋。这一次不再完全随机走子，策略会好一点点、不那么蠢，于是会访问图里稍微不同的节点，下稍微好一点的棋——但依然下得烂。

**[25:17 – 25:32]**
**捷克语：** který vy určitě máte rádi. To znamená je tam nějakej formalismus, víme, co chceme hledat. Eh, ale teďka jak jak to sakra najít, jo? Tak eh když když je to prostředí dostatečně malý,
**中文：** 收集新数据集，重复同样的过程。所以这是一种漂亮的迭代方法：每次把智能体改进一点，丢回环境，收集到这次稍微好一点的数据，再把智能体改进一点。好。只要我们持续得足够久、每一步都做对，就会不断进步，希望能足够接近最优策略。

**[25:32 – 25:47]**
**捷克语：** aby se nám vešlo tady na monitor a nebo aby se nám vešlo do počítače, tak to je to je přesně, co e se učili, kdybyste si zapsali nějakej kurz Rinforce Moring One
**中文：** 当然，因为图很大、我们依赖神经网络的近似和泛化，永远到不了完全最优；关键是能否找到比人类更好的策略——而事实表明可以。很好，又是提问环节，目前进展不错。

**[25:47 – 26:03]**
**捷克语：** on a já třeba můžu silně doporučit e s Trakama na malj straně skvělej skvělej kurz na Renfeling, ale můj point eh je, že pokud máme jako dostatečně malej tenhlecten graf, abysme ho v podstatě celej prošli a dokázali jsme na něm
**中文：** 在继续之前，有个有意思的问题：像我描述的那样，在象棋里，如果随机走子能赢的概率极小，我们就永远拿不到那个初始信号，也就无从 bootstrap、无从自我改进了。如果两条随机策略对弈时永远没人能赢，那信号就无从而来。


## 现实环境必须近似：神经网络遇上强化学习

**SECTION_NOTE**
- 真实环境的状态空间大到放不进计算机：仅是国际象棋/围棋的状态数就超过宇宙原子数
- 因此无法穷举求解，必须「近似」——这正是神经网络与强化学习结合的原因
- 小的环境可用精确算法收敛到最优；大的环境必须靠神经网络近似 → 深度强化学习
**END_SECTION_NOTE**

**[26:03 – 26:18]**
**捷克语：** počítači na počítači běhat nějaký algoritmy, tak není tak těžký mít algoritmy, který průve dokážou zkonvergovat k optimálnímu řešení. To znamená dokážou fakt najít optimální strategii eh v v takovémhle grafu, jo.
**中文：** 所以问你们：两个随机玩家下象棋，一方获胜（而不是和棋）的概率你们觉得有多大？

**[26:18 – 26:29]**
**捷克语：** Takže takže to je jako krůjček jedna. Eh, ale typicky ty prostředí, který nás zajímat budou v reálným světě, ty aplikace, tak
**中文：** >> 啊，明白了。>> 99.8%。>> 呃，他们下的是象棋吗？

**[26:29 – 26:38]**
**捷克语：** ty ty nikdy nebudou tak malý, aby se nám do počítače vešly. už jenom ty šachy, který pořád zněj jako, že jsou to
**中文：** 这些状态永远也不会小到能装进我们的计算机。就拿国际象棋来说，它听起来总像是……

**[26:38 – 26:52]**
**捷克语：** jednoduchčký problém oproti reálnýmu světu a oproti třeba tomu, co mu se dělat eh jako jazykový modely nebo to co vidíme e já kolem nás, tak ty šachy zně jednoduše, ale i tam třeba těch stavů eh
**中文：** ……相比现实世界、相比比如语言模型在做的事、或是我们在周围看到的东西而言是个简单问题，所以象棋听起来很简单，但即便在那里，那些状态……

**[26:52 – 27:07]**
**捷克语：** toho toho grafu, tak je víc, než je nevím, jestli v šachách v go určitě je jich víc, než je atomu ve vesmíru. Takže asi není nikdy houb, že bysme naškálovali compute tak, že bysme dokázali to vyřešit úplně. Takže musíme
**中文：** ……那个图[的状态]数量比[原子]还多——我不知道国际象棋里有多少，但围棋里肯定比宇宙中的原子还多。所以我们大概永远也无法靠堆算力把它彻底解决。所以我们必须……

**[27:07 – 27:16]**
**捷克语：** na to jinak. Musíme to vždycky nějak aproximovat. A [odkašlání] tím, že to musíme nějak aproximovat, tak to je přesně důvod,
**中文：** ……换个思路。我们总得用某种方式去近似它。而[清嗓]正因为我们必须做某种近似，这恰恰就是……

**[27:16 – 27:24]**
**捷克语：** proč jdou pěkně dohromady ty neuronový sítě a reinforcement learning, protože reforce malening jako takovej ten úvodní
**中文：** ……为什么神经网络和强化学习能配合得这么好——因为强化学习，就像那门强化学习的入门……

**[27:24 – 27:40]**
**捷克语：** kurz do reinforcement learningu, tam tak se přesně naučíte ty první dva tři slajy nebo ty předchozí dva tři slajy, co tady teďka byly, jo, naučí se tam člověk jako jak vypadají ty formalismy, eh jaký jsou jaký jsou tam ty teoretický výsledky a jaký jsou algoritmy, jak vyřešit jako eh
**中文：** ……课程里，你会精确学到前面那两三页幻灯片、也就是刚才展示过的内容——是的，在那里面人会学到这些形式化方法长什么样，有哪些理论结果，有哪些算法，以及怎么去解那些……

**[27:40 – 27:54]**
**捷克语：** tydlety malý malý malý úlohy. No, ale pro ty velký úlohy, tak co je co je přesně jako za tím, aby to fungovali ve velkém světě, tak je spojení toho rainfalme leningu a deep learningu, protože ty neuronový sítě, důvod, proč
**中文：** ……那些小之又小的习题。但是，对于那些大问题——也就是真正能在现实世界里跑起来的问题——靠的是强化学习和深度学习的结合，因为神经网络，我们之所以……

**[27:54 – 28:03]**
**捷克语：** je tam máme, jako na toleto neuronky vůbec nepotřebujeme, jo? Toleto prostě máte malou malou tabulku v počítači, běžíte si tam nějakej ford cyklus a
**中文：** ……要用它，是因为对那种小问题我们根本不需要神经网络，对吧？那种小问题你只需要在计算机里放一张小小的表格，跑一个 for 循环，然后……

**[28:03 – 28:18]**
**捷克语：** updatuje updatuje se to strategie. ty neuronky tam potřebujete, jakmile tenhlecten graf je hrozně veliký a už si nemůžeme dovolit procházet ty vrcholy a místo toho ty neuronky se používají na to, abysme dokázali nějak generalizovat
**中文：** ……策略就更新了。而一旦那个图变得无比巨大、我们再也无法承受去遍历所有节点时，才需要神经网络——它用来让我们能在那个巨大的图里做某种泛化。

**[28:18 – 28:31]**
**捷克语：** v tom obrovským grafu. To nebude takový, nebude ani takový, bude fakt obrovský. nemůžeme jakože nikdy projít všechny ty vrcholy, tak ty na rukách umožňujou to, že my projdeme jakoby jenom nějak nějakej subset vrcholů, o tom se
**中文：** 在那个庞大的图里。它不会是那种[小]样子，也不会是那样，而是真的无比巨大。我们永远不可能走遍所有节点，所以神经网络让我们能做到的，是我们只走某个节点的子集，并从中……

**[28:31 – 28:47]**
**捷克语：** dokážeme něco naučit, tam se dokážeme zlepšit a ty nám potom pomůžou generalizovat. A teďka to je jako strašně jednoduchý spojení s tím, když si uvědomí, co ty, když si uvědomíme, co ty neuronky dělaj třeba v tom supervise settingu, tak tam jsme
**中文：** ……学到一些东西，在那里得到提升，然后它们再帮我们泛化。现在这一点和下面的想法有很简单的联系：只要你想一想，神经网络在监督学习的设定里是做什么的，就会明白——在那里我们……

**[28:47 – 29:02]**
**捷克语：** řekli, že že upravujeme váhy eh ty neuronky, aby třeba dokázaly rozpoznávat dobře kočky a psy nebo hrochy na obrázku, ale že jo, ten důvod, proč to děláme, proč zase na na rozpoznání obrázku používáme neuronky, protože oni
**中文：** ……说过，我们调整神经网络的权重，让它能很好地识别图片里的猫、狗或者河马。但是，我们之所以这么做、之所以在图像识别里用神经网络，是因为它们……

**[29:02 – 29:17]**
**捷克语：** fungujou empiricky strašně skvěle v tom smyslu, že Když ono to vidělo hromadu obrázků kočekapsů. Na tom jsme ty váhy pošolichalili natolik, že to funguje dobře na tj trénovací sadě, kterej jsme mu jako ukázali, tak oni typicky
**中文：** ……在实践中表现得出奇地好——比如它看过一大堆猫和狗的图片。我们不断打磨那些权重，直到它在我们给它看的训练集上表现良好，于是它们通常……

**[29:17 – 29:32]**
**捷克语：** fungujou dobře eh generalizaci v tom smyslu, že když tomu ukázeme obrázek kočky, kterej to nikdy nevidělo při tom šolichovaní těch váh, tak ve skutečnosti to má strašně dobrou pravděpodobnost, že tu kočku od psa dokáže rozlišit i na
**中文：** ……泛化得很好：当我们给它看一张它在"打磨权重"阶段从未见过的猫的图片时，它实际上有极高的概率，也能在那张……

**[29:32 – 29:48]**
**捷克语：** obrázku, co to nikdy neviděl. Jo. No a to je přesně důvod, proč se to používá tady, protože my projdeme jenom některý ty vrcholy toho grafu a doufáme, že tím, že používáme velký neurónový sítě, tak když jsme jsme se jsme se něco dozvěděli
**中文：** ……它从未见过的图片上把猫和狗区分开。是的。而这正是它在这里被使用的原因——因为我们只走那个图里的部分节点，并希望借助大型神经网络：既然我们已经从……

**[29:48 – 30:03]**
**捷克语：** o tomhle vrcholu a tenhlecten vrchol bude třeba podobnej, bude to podobná šachová konfigurace nebo podobnej stav světa nebo podobnej vstup eh e toho toho vašeho promptu, kterej jste jste dali vašemu chat GPT, tak potom ta
**中文：** ……这个节点学到了东西，那么那个节点可能和它相似——可能是相似的象棋局面、相似的世界状态，或者相似的输入，比如你给 ChatGPT 的那个 prompt——那么……

**[30:03 – 30:19]**
**捷克语：** generalizace té sítě nám dokáže dát jako dobrej rozumnej rozumnej eh jakoby výstup tj sítě, kterej potřebujeme v tom stavu. Jo. Eh, tak jo. Dává todleto zase trošku smysl?
**中文：** ……网络的泛化能力就能给我们一个合理、靠谱的输出——我们在那个状态下需要的输出。是吧。嗯，好。这下又有点说得通了吧？

**[30:20 – 30:33]**
**捷克语：** Super. Tak jo, ale říkám, kdykoliv mě přerušte a update se na detaily. Super. Tak a teďka zase půjdeme o krouček hloubic, abysme získali intuici, jak jak
**中文：** 太好了。那好，不过我说过，你们随时可以打断我、追问细节。好。那现在我们再往深里走一圈，好让你们获得一种直觉，理解……

**[30:33 – 30:45]**
**捷克语：** to vůbec funguje, jak spojíme dohromady tydlety algoritmy, který hledají dobrou strategii v tomhletom grafu s těma s tím deplaningem jako takovým.
**中文：** ……它到底是怎么运作的，以及我们如何把那些在图里搜索好策略的算法，和深度学习本身结合起来。

**[30:45 – 30:59]**
**捷克语：** Tak jo. [frknutí] Tak tak, jak to uděláme? Ve skutečnosti je to strašně jednoduchý a my eh budeme iterativně si generovat ten trénovací
**中文：** 那好。[清嗓]那我们具体怎么做呢？其实非常简单，而且我们会迭代式地生成那个训练……

**[30:59 – 31:14]**
**捷克语：** dataset, kterej se potom používá podobně jako v Supervise learningu. Hnedka vysvětlím, jo? Zatímco v tom supervised learningu máme typicky oanotovaný data v tom smyslu, kde máme kočky, máme psy,
**中文：** ……数据集，它之后会像监督学习里那样被使用。我马上解释，好吗？在监督学习里，我们通常有所谓标注过的数据，比如我们有猫、有狗，

**[31:14 – 31:23]**
**捷克语：** zadedefinujeme si eh nějakou los, nějakou účelovou funkci eh kterou potom se snažíme minimalizovat tím, že pomocí
**中文：** 我们会定义一个损失函数、一个目标函数，然后想办法去最小化它——通过……

**[31:23 – 31:39]**
**捷克语：** gradientů měníme ty váhy, ty parametry téj sítě, abysme na tom nasbíraném datasetu zlepšili tu performance téj sítě. To je to je ten jakože eh supervised learning krok a to je celej krok toho supervised learningu, když
**中文：** ……梯度来改动那些权重、也就是网络的参数，好让我们在收集到的数据集上提升网络的性能。这就是——这就是所谓的监督学习步骤，而且如果你……

**[31:39 – 31:48]**
**捷克语：** jediný, co děláme, je supervisning, jo. A rainfal meleny tenhlecten jako eh dělčí krok typicky používá iterativně a
**中文：** ……所做的仅仅是监督学习的话，这就是全部步骤。而强化学习的这个分解步骤，通常是迭代式使用的，而且……

**[31:48 – 32:03]**
**捷克语：** děláme to tak, že máme obrovskej obrovskej graf, prostě e máme počet vrcholů, který eh jako v životě ani jako dokonce vesmíru nikdy neprojdeme, tak projdeme jenom nějakej subset a ze
**中文：** ……我们的做法是：我们有一个超级巨大的图，节点数量多到我们这辈子、甚至整个宇宙存在的时间里都走不完，所以我们只走某个子集，然后……

**[32:03 – 32:12]**
**捷克语：** začátku ten subset projdeme dost náhodně. Zase, když si to představíme v šachu, tak začneme tak, že budeme hrát úplně náhodně tahat figurkama. Jo, to je
**中文：** ……一开始我们相当随机地走这个子集。还是拿象棋举例：我们一开始会完全随机地乱走子。对，这……

**[32:12 – 32:26]**
**捷克语：** jako strašně špatná strategie, ale musíme někde začít a to jsme to je tak začneme, když máme náhodně inicializovaný váhy té neuronky, náhodně inicializoval agenta, tak budeme prostě náhodně tahat figurkama. A taková strategie nám projde nějakej subset toho
**中文：** ……是个非常糟糕的策略，但我们必须有个起点，对吧？就是这个样子：当我们的神经网络权重是随机初始化的、智能体也是随机初始化的时候，我们就只会随机走子。而这样的策略会让我们走过那个……

**[32:26 – 32:42]**
**捷克语：** toho velkýho šachovýho grafu. A na těch posbíranjých vrcholech z té iniciální špatné strategie, tak ty posbíraný vrcholy, ty trajektorie, tak ty nám definujou ten datet, na kterým budeme hold běhat ten náš klasickej supervised
**中文：** ……大象棋图的某个子集。而在那套初始的糟糕策略下收集到的节点——那些收集到的节点、那些轨迹——就定义了我们将要跑我们经典监督……

**[32:42 – 32:57]**
**捷克语：** learning v tom smyslu, že si tam zadefinujeme loss, kterej chceme minimalizovat a běžíme náš náš náš gradi and descent, šoupáme ty váhy sítě, abysme zlepšili tu kvalitu sítě na nasbíranejch dat a semanticky eh třeba
**中文：** ……学习的那个数据集：我们在上面定义一个要最小化的损失函数，然后跑我们的梯度下降，挪动网络的权重，好让我们在收集到的数据上提升网络的质量。从语义上说，比如……

**[32:57 – 33:06]**
**捷克语：** pro ty šachy nebo pro renforcem takovej, tak ten los samozřejmě tak, jak se ho zadefinuje, v tomhletom případě neodpovídá tomu, že eh že jestli jsme
**中文：** ……对于象棋或者强化学习这种情形，那个损失函数的定义，显然不再是判断我们是否……

**[33:06 – 33:21]**
**捷克语：** dobře klasifikovali kočku nebo psa, ale ten loss ho odpovídá tomu, jakej reward jsme nasbírali e na na tom na tom trénovacím datasetu. Takže ten gradient, když běžíme na těch nasbíranjch trajektoriích, v podstatě co způsobuje,
**中文：** ……把猫或狗分类正确，而是对应我们在那个训练数据集上收集到了多少奖励。所以，当我们在那些收集到的轨迹上跑梯度时，它本质上造成的结果是：

**[33:21 – 33:36]**
**捷克语：** že chceme zvětšit pravděpodobnost těch trajektorií, který nám daly více rewardů. oproti těm trajektori, který nám dali hold rewardu. Jo, takže když budeme náhodně hrát šachy, máme štěstí,
**中文：** 我们想要增大那些给了我们更多奖励的轨迹的概率，相对于那些只给了我们很少奖励的轨迹。所以，如果我们随机下棋时走运，

**[33:36 – 33:49]**
**捷克语：** že se dostaneme eh do konce do konce partie, kde jsme dali mat, tak máme reward plus 1, tak se pokusíme zvýšit pravděpodobnost toho, že takovoudle sekvenci v příštím tahu uděláme znova.
**中文：** 走到了一局棋的尽头、并且我们将死了对方，那我们就得到 +1 的奖励，于是我们就试图提高下次再走出这样一串着法的几率。

**[33:49 – 34:01]**
**捷克语：** Jo. Eh, super. Eh, no a potom jakmile jako zlepšíme tu síť na tom nasbíraném setu těch trajektorií, tak hold máme
**中文：** 对。嗯，好。而一旦我们在收集到的那批轨迹上把网络改进了，我们就有了……

**[34:01 – 34:14]**
**捷克语：** najednou nový váhy sítě. Ty nový váhy sítě znova hodíme do toho prostředí, takže budeme hrát znova hromadu partií šachu. Tentokrát už nebudeme tahat úplně náhodně. Tentokrát ta naše strategieka bude o trošičku lepší, nebude úplně
**中文：** ……一套新的网络权重。我们把这套新权重重新丢回环境里，于是会再下大量对局。这一次我们不再完全随机走子。这一次的策略会好那么一点点，它不再是完全……

**[34:14 – 34:30]**
**捷克语：** hloupá, takže navštíví trošku jiný vrcholy v tom grafu. už budeme hrát maličko lepší šachy, ale pořád budeme hrát do špatný šachy. Nasbíráme novej dataset a děláme furt to samý, jo? Takže je to jako taková pěkná iterativní metoda, kdy vždycky trošku zlepšíme toho
**中文：** ……笨的，所以它会访问图里稍微不同的节点。我们会下得稍微好一点，但依然下得很差。我们收集新的数据集，然后一直重复同样的动作，对吧？所以这是一种漂亮的迭代方法：我们每次都让那个……

**[34:30 – 34:45]**
**捷克语：** agenta, hodíme ho zrovna do prostředí, posbíráme zase jako víc tentokrát trošku lepších dat a zase toho zase toho agenta zlepšíme. Jo. A když budeme jít trvat dostatečně dlouho eh a budeme to dělat všechno dobře, tak se budeme zlepšovat a
**中文：** ……智能体提升一点，再把它丢回环境，又收集到一批这回稍微好一点的数据，再把那个智能体提升一点。对。只要我们持续足够长的时间、并且把每步都做对，我们就会不断进步，并且……

**[34:45 – 34:54]**
**捷克语：** dostaneme se hopefeli dost blízko t optimální strategie. Ale samozřejmě tím, že je ten graf velikej, spolíháme se na aproximace a generalizace těch
**中文：** ……有望足够接近最优策略。但当然，因为那个图非常大，我们依赖的是那些……

**[34:54 – 35:07]**
**捷克语：** nenorových sítí, tak samozřejmě nikdy se nedostáme k t úplné úplně optimální strategii. Spíš jde o to, jestli to dokážeme v tom prostředí najít strategii, která je lepší, než je člověk a to se ukazuje, že jo. E super. Tak jo,
**中文：** ……神经网络的近似与泛化，所以我们当然永远到不了那个百分之百最优的策略。关键更在于：我们能否在那个环境里找到比人更好的策略——而事实证明是可以的。嗯，好。那好，

**[35:07 – 35:21]**
**捷克语：** zase pauza na dotazy, takže zatím zatím dobrý. Jo, tak jo. Tak než budeme pokračovat, možná eh možná
**中文：** ……又到了提问环节，目前进展还不错。好，那好。在继续之前，也许、也许……

**[35:21 – 35:37]**
**捷克语：** zajímavý dotaz pro vás, jo, tak jak jsem to popsal, tak třeba v těch šachách by to nefungovalo, kdybysme eh měli strašně malou šanci, že když budeme náhodně hejbat figurkama, tak že dokážeme vyhrát, že jo, jako nikdy bysme
**中文：** ……先问你们一个有趣的问题。就像我刚才描述的，如果是在象棋里，要是我们随机挪动棋子而能赢的概率极小，那这套方法就不灵了，对吧？因为我们根本……

**[35:37 – 35:48]**
**捷克语：** nedostali jako ani ten iniciální signál, kterýho potom můžeme jako bootstvovat, zlepšovat se, zlepšovat se, že jo. Kdyby kdyby prostě platilo, že dva dvě náhodný strategie, když hrajou proti sobě, tak
**中文：** ……连那个可以用来自举、用来自我提升的初始信号都拿不到。假如说，两套随机策略互相对弈时，

**[35:48 – 35:57]**
**捷克语：** eh nikdy nikdo nevyhraje, tak eh nemá se ten signál, kde kde vzít. Takže možná eh zajímavej dotaz pro vás. Jakj si
**中文：** ……永远没人能赢，那这个信号就无从谈起了。所以，也许……给你们提个有趣的问题：你们觉得……

**[35:57 – 36:12]**
**捷克语：** myslíte, že je šance, když dva náhodný hráči hrajou šachy proti sobě, takže jeden vyhraje >> místo toho, aby to byla prostě plta, >> jakože vyhraje buď jeden nebo druhej.
**中文：** ……当两个随机玩家互相对下象棋时，其中一方会赢的概率是多少？——而不是简单地和棋——也就是说，要么这个赢、要么那个赢的概率？

**[36:12 – 36:21]**
**捷克语：** >> Jo. Aha. >> 99,8. >> Eh, hrají šachy?
**中文：** >> 对。啊明白了。>> 99.8%。>> 呃，他们下的是象棋？

**[36:21 – 36:35]**
**捷克语：** No teď když se nad tím zamejšn, tak >> jako co bys čekal, že se nejčastěji stane, když prostě náhodně oba hrajou figurkama? Jako jakj outcome? Jeden jeden z nich vyhraje nebo to bude spíš remíza?
**中文：** 嗯，现在你仔细一想，>> 如果双方都纯随机走子，最常发生的是什么？是哪种结果？是他们其中一个赢，还是更可能和棋？

**[36:37 – 36:46]**
**捷克语：** >> Ještě nahlas. >> Hraj šachy? [smích] Jedna jedna konec.
**中文：** >> 请大声点。>> 下的是象棋？[笑] 一上来就结束了。

**[36:46 – 36:55]**
**捷克语：** >> Jo. E a eh v eh v a co je ta jako největší pravděpodobnost, co jako skoro skoro skoro pravděpodobnost jedna, že se stane?
**中文：** >> 对。那、那、那最大概率——几乎、几乎是概率为 1 会发生的事——是什么？

**[36:55 – 37:06]**
**捷克语：** >> No prčí to v nějakým stavu, kde je složitý dát šakmat a ta hra bude jako v rámci nějaký koncovky, k bude málo ale žádnej sigá se tam nepos.
**中文：** >> 嗯，会卡在某个很难将死对方的状态里，棋局会进入某种残局，棋子越来越少，但谁也将军将不死。


## 深度强化学习的方法论与 RL 的兴衰周期

**SECTION_NOTE**
- 两大方法家族：基于价值(value-based)与基于策略(policy-based)，以及二者的混合
- 探索(exploration)与利用(exploitation)的权衡是核心难点
- RL 并非一路高歌：历史上有过低潮，后来才随算力与算法重新崛起
**END_SECTION_NOTE**

**[37:06 – 37:19]**
**捷克语：** >> No dobře, ale to ta hra nekončí ještě, že jo? Remíze před. No teda končí po 50ích, když nikdo nepohneš se nebo se nevezme figura, což >> Aha. A skončí to potom jak? Takhle.
**中文：** >> 嗯好，但那样棋局还没结束，对吧？还没到和棋。其实是到第 50 回合（如果没人动子或吃子）就判和——>> 啊哈。那它最后是怎么结束的？就像这样。

**[37:19 – 37:34]**
**捷克语：** >> Aha. Jo. Takže ano, jako ta správná intuice je eh, že když budeme úplně náhodně tahat figurkama, tak jako s velkou pravděpodobností to skončí remízou. A to je to je pravda, to je správná intuice. Ale co je jako zajímavý, kdyby ta pravděpodobnost byla
**中文：** >> 啊哈。对。所以是的，正确的直觉是——如果我们完全随机走子，那么大概率会以和棋收场。这没错，这是对的直觉。但有趣的是，如果那个概率……

**[37:34 – 37:47]**
**捷克语：** fakt jako prostě 99 celých jako a potom jako 100 109, tak tydlety algoritmy by často vůbec nefungovaly. A ta šance, že náhodou vyhrajeme jako, že dva náhodný
**中文：** ……真的是 99 点几（接近 100），那这类算法往往根本就不会奏效。而那种"随机对弈时碰巧走出将杀"的几率……

**[37:47 – 38:02]**
**捷克语：** hráči se dostanou do matové situace, je ve skutečnosti jako eh mnohem větší, než by člověk řekl, ale pořád malá. A schválně, já vás nechám se zeptat vašeho oblíbenýho jazykovýho modelu. Eh, kolik kolik to je?
**中文：** ……两名随机玩家走到将杀局面，实际上比人们以为的要大得多，但依然很小。说真的，我让你们去问问自己最喜欢的那个语言模型。呃，到底是多少？去问，然后告诉我。

**[38:02 – 38:06]**
**捷克语：** Se zeptejte a řekněte mi to.
**中文：** 去问，然后告诉我。

**[38:22 – 38:35]**
**捷克语：** >> Tak jo. Má už někdo to číslo? Když to někdo má, tak to tak to buď máměte ruku nebo to vykřikněte na mě.
**中文：** >> 那好。已经有人知道那个数字了吗？谁知道的话，举手或者冲我喊出来都行。

**[38:42 – 38:54]**
**捷克语：** Tvrdí, že prej jako neremujou skoro nikdy. >> OK. [smích] Pravděpodobnost, že asi, že jeden z nich
**中文：** （台下说）据说他们几乎从不会和棋。>> 好。[笑] 也就是说其中一个会赢的概率，据说超过 80%。所以 >> 好。[笑][清嗓]

**[38:54 – 39:06]**
**捷克语：** vyhraje prej přes 80 %. Tak >> OK. [smích] [frknutí]
**中文：** >> 其中一个会赢的概率，据说超过 80%。所以 >> 好。[笑][清嗓]

**[39:06 – 39:21]**
**捷克语：** >> Mě klad tvrdí, že mezi 1 st% a 1%. >> To je taky blbě, si myslím. [odkašlání][kašel] Já už jsem to taky zapomněl. Byly to jednotky procent. Jo, eh, mám to někde zapsaný, ale mám děravou děravou pamě.
**中文：** >> 克拉德跟我说是在 1% 到 1% 之间。>> 我觉得那也不对。[清嗓][咳嗽] 我自己也忘了。应该是个位数百分比。对，呃，我好像记在哪了，但我记性太差了。

**[39:21 – 39:29]**
**捷克语：** Každopádně eh je to jakože jak pro šachisty, tak ne šachisty je to jako překvapivý číslo, když se na tím jako je je to určitě vec, kterou by člověk se si
**中文：** 总之，无论是会下棋的还是不会下棋的人，这个数字都挺出人意料——它肯定属于人凭直觉猜不出来的那种东西。

**[39:29 – 39:44]**
**捷克语：** netipnul, ale co je jako dobrý eh spojní na todlencto, na ty algoritmy, o kterej mluvíme, je, že pokud by to byla v podstatě skoro nula, tak tolencto se jako nikdy neodpíchne, protože nikdy to nedostane ten signál, že jako náhodnou strategii ten signál dostaneme a potom už se snažíme jako [odkašlání]
**中文：** ……但和我们要讲的算法最相关的点是：如果这个数字基本是零，那这东西就永远起步不了，因为它永远拿不到那个信号——也就是从随机策略拿到信号之后，我们才去尝试[清嗓]……

**[39:44 – 39:59]**
**捷克语：** maximalizovat, zlepšovat zlepšovat tu strategii, aby co nejčastějc nejčastějc vyhrála. Jo, super. Tak jo, takčer GPT našel to jakože někde na internetu našel 15 %.
**中文：** ……去最大化、去不断改进那个策略，好让它尽可能经常赢。对，好。那么，GPT 在网上某处查到了 15%。

**[39:59 – 40:15]**
**捷克语：** >> Hele, já už si to nepamatuju, popravdě. Myslím si, že to bylo míň. >> To jenom jako předáváme. >> Jo, jo. No. Eh, OK. To co se to se divím, že to háže takhle různý čísla. >> Teďka ta odpověď na tu otázku byla to ty jednotky procent jsou tedy dostatek nebo >> stačí. Jo, jo, jakože i kdyby to bylo
**中文：** >> 嘿，说实话我也记不清了。我觉得应该更低。>> 那只是它在转述。>> 对，对。嗯。呃，好吧。我惊讶的是它给出的数字这么飘。>> 那回到这个问题——个位数百分比到底够不够？>> 够的。对，对，意思是即便它（随机策略产生胜负信号的概率）是……

**[40:15 – 40:24]**
**捷克语：** prostě eh, že jo, celý je to o tom, kolik těch partií člověk odehraje, jo. A k tomu eh
**中文：** ……说白了，一切都取决于你下了多少盘棋，对吧。而这一点，我们……

**[40:24 – 40:32]**
**捷克语：** k tomu se dostaneme za dva slajy, ale ta důležitá intuice je z tohodle, že fakt střídáme to, že sbíráme eh sbíráme ty
**中文：** ……会在两页幻灯片之后讲到，但从中得出的重要直觉是：我们确实是交替进行——先收集、收集那些……

**[40:32 – 40:47]**
**捷克语：** data, pohybujeme se to prostředí, ale začneme úplně náhodnou strategii. Ta postup ta str se postupně zlepšuje. Zase sbíráme lep lepší tradektorii a na tom nasbíra datasetu prostě běžíme běžíme jednoduchej gradient distance zjednodušeně řečeno. Jo. Tak jo, super.
**中文：** ……数据，在环境里行动，但起点是完全随机的策略。这个策略会一步步逐渐变好。我们再收集越来越好的轨迹，然后在收集到的数据集上，简化地说，就是跑一个简单的梯度下降。对，好，很好。

**[40:47 – 41:03]**
**捷克语：** A tady pokud chápeme tenhlecten obrázek, tuhletu intuici, tak ve skutečnosti chápete základ jednoho jakoby z nejpopulárnějších algoritmů dnešní doby a to je PPO nebo je i hromadou jako variant, který jsou nad tím postavený. A
**中文：** 而只要你们理解了这幅图、这个直觉，你们实际上就理解了当今最流行的算法之一的基础——那就是 PPO，以及建在它之上的一大堆变体。而且……

**[41:03 – 41:18]**
**捷克语：** zase kdybyste se zanořili do těch formalismů, tak zjistíte, že zase dělá to de věci, sbírá to trajektorie a na těch trajektoriích minimalizuje nějakou chybu. A konkrétně tadleta chyba eh
**中文：** ……如果你们再钻进那些形式化推导，会发现它做的还是那套——收集轨迹，然后在那些轨迹上最小化某种误差。而具体地，这个误差……

**[41:18 – 41:27]**
**捷克语：** míchá dohromady dvě věci. V tj v tej jako v tj funkci, co se snažíme maximalizovat nebo minimalizovat, tak dáváme dohromady to, že chceme
**中文：** ……把两样东西混在一起。在那个我们想最大化或最小化的函数里，我们同时要求：我们想要……

**[41:27 – 41:40]**
**捷克语：** maximalizovat ten reward na těch trajtorů, co jsme nasbírali. To znamená, chceme co nejčastějc jakoby zvětšit tu pravděpodobnost výhry, ale zároveň nechceme moct při tom jako jednom kroku
**中文：** ……最大化我们在那些轨迹上收集到的奖励。也就是说，我们想尽可能频繁地增大获胜的概率；但同时，我们又不希望在某一步……

**[41:40 – 41:54]**
**捷克语：** eh toho z toho, kdy zlepšujeme tu polisy, tak nechceme ji moc změnit, jo, že kdybysme jako hrozně změnili, tak najednou zase jako nevěříme tolik těm
**中文：** ……也就是在改进策略（policy）的时候，把它改得太厉害——因为如果改得太猛，我们突然就又不那么信任那些……

**[41:54 – 42:08]**
**捷克语：** nasbíraneým datům, protože by byly nasbíraný z ze strategie, která vypadá úplně jinak než tu strategii, co teďka máme, jo. Takže v tom každým kroku e ty té ty té ty jedné iterace, tak se snažíme jak tu strategii zlepšit, ale
**中文：** ……收集来的数据了，因为它们是从一套和我们现在这套完全不同的策略收集来的，对吧。所以在每一次迭代的每一步里，我们既想改进策略，又……

**[42:08 – 42:16]**
**捷克语：** zároveň ji nezměnit moc, jo? A toleto prostě pořád jenom tych. Super. Tak a teďka tady mám pro vás překvapenej
**中文：** ……同时不想把它改太多，对吧？而这就是它一直在权衡的东西。好。现在我要给你们看一个让人意外的……

**[42:16 – 42:32]**
**捷克语：** překnej příklad. Já doufám, že to bude fungovat. Jestli, tak potřebuju pomoct otevřít tole video nebo takhle vlastně tady je myška, že jo. >> Tak jo, tak to zkusíme, co se stane. To bude s reklamou.
**中文：** ……例子。我希望它能正常播放。如果需要的话，我得有人帮我打开这个视频，或者说……其实鼠标在这儿，对吧。>> 那好，我们试试看会发生什么。这开头会有段广告。

**[42:32 – 42:44]**
**捷克语：** Super. Tak jo. Eh, jo jo jo jo. OK, super. Tak teďka to, co tady vidíme, je přesně aplikovanej eh takovejdle
**中文：** 好。那好。呃，好、好、好、好。OK，好。那现在大家看到的，正是应用了刚才那种……

**[42:44 – 42:55]**
**捷克语：** iterativní algoritmus na eh takovoudle jednoduchou hru. Tohlencto je, myslím pon. Eh, viděl tohlecto někdo někdy? Máme tady dole takovou pálku. Míček běhá nahoře a snažíme se posbírat body.
**中文：** ……迭代算法的一个简单游戏。这个游戏，我想……呃，有人见过吗？底下有根球拍，小球在上面跑，我们要去收集分数。

**[42:55 – 43:04]**
**捷克语：** Super. Takže ty body máme nahoře a vysloveně je tam skóre, který se snažíme maximalizovat. Ty akce toho agenta jsou prostě šipka doleva, šipka doprava. To
**中文：** 好。所以分数在上方，那里有个分数值，我们要去最大化它。智能体的动作就只是左箭头、右箭头。这……

**[43:04 – 43:19]**
**捷克语：** je v podstatě ono. A zase používáme tady eh ten algoritmus, kterej jsme si vysvětlili. To znamená iteratemně začneme s náhodnou strategií a postupně v každé iteraci budeme zlepšovat. Jo, takže tady dole vidíme, jak to vypadá
**中文：** ……就是全部了。而我们用的还是刚才讲的那套算法：也就是从随机策略开始迭代，在每一次迭代里逐步改进。对，所以大家在下方看到的是……

**[43:19 – 43:33]**
**捷克语：** v podstatě skoro na začátku. Ono to tak nějak náhodně mačká tlačítka. Občas se to trefí, občas netrefí, ale většinou ten balón spadne dolů. Tole je po 200 těch jako velkých iteracích.
**中文：** ……几乎刚开始时的样子。它有点随机地乱按按钮。偶尔接住，偶尔接不住，但大多数时候球会掉下去。这一版是跑了约 200 次大迭代之后。

**[43:37 – 43:46]**
**捷克语：** Už to vypadá o něco líp, ale pořád nic moc. Možná zvětším.
**中文：** 看起来已经好一点了，但还很不怎么样。我把画面放大点。

**[44:03 – 44:17]**
**捷克语：** Tak po 600 iteracích už to samo zjistilo, že to prostě může odpálit míček míček nahoru. A zase eh todleto je věc, kterou která se bude opakovat v příběhu v průběhu tohodle příběhu. V podstatě tomu
**中文：** 那跑了 600 次迭代之后，它自己发现：它其实可以把球往上打。而这，正是贯穿这个故事、会反复出现的一个现象。本质上……

**[44:17 – 44:33]**
**捷克语：** agentovi jsme nic neřekli. Je to strašně obecný algoritmus. Jenom jsme mu řekli, máš k dispozici tydlety akce. hledej takovou strategii, aby si maximalizoval ten rev nahoře a co se často stane v prostředí to šachy [hudba]
**中文：** ……我们什么都没告诉那个智能体。这是个极其通用的算法。我们只告诉它：你有这些动作可用，去找一种能最大化上方那个奖励的策略。而在象棋[配乐]之类的环境里，经常会发生的是……

**[44:33 – 44:45]**
**捷克语：** a nebo právě a toí domény dneska v umělé inteligenci, tak často to dokáže najít strategii, která překvapí i doménový doménový experty.
**中文：** ……或者恰恰在如今人工智能的那些领域里，它常常能找到连领域专家都感到惊讶的策略。

**[44:45 – 44:54]**
**捷克语：** Jo, dokáže to najít tahy v šachách, ten by člověk jako, který by ho to nikdy nikdy nenapadlo. Hol tím, že to hledá strategie, který maximalizujou reward.
**中文：** 对，它能在象棋里找到人类永远想不到的着法。就因为它在寻找能最大化奖励的策略。

**[44:54 – 45:03]**
**捷克语：** Jo. Eh a tady eh eh možná k tomu dotazu, že eh co jsme
**中文：** 对。呃，这里……也许针对刚才那个问题，关于我们……

**[45:03 – 45:11]**
**捷克语：** měli předtím jakože ty ty sbírání epizod, tak e důvod, proč to dokážeš často najít mnohem lepší věci než lidi,
**中文：** ……之前讲过的收集对局/片段（episodes），它之所以常常能找到比人好得多的东西，

**[45:11 – 45:25]**
**捷克语：** tak vůbec to není o tom, že oni by to, že typicky by tyhlety algoritmy a deep learning takovej byl lepší jak lidi ve smyslu, že to z těch samejch dat dokáže vycucat lepší intuici nebo lepší strat.
**中文：** ……根本不是因为这类算法或深度学习比人"更聪明"——不是说它能从同样的数据里榨出更好的直觉或更好的策略。

**[45:25 – 45:39]**
**捷克语：** strategii. To rozhodně ne. Je to spíš tak, že eh díky množství dnešního computu to dokáže nasbírat prostě mnohem víc dat, než kolik jakýkoliv člověk jak
**中文：** 绝对不是。更主要的原因是：得益于如今的计算规模，它能收集到比任何一个人……

**[45:39 – 45:55]**
**捷克语：** za svůj život, tak veškerý třeba lidstvo dohromady vidělo. A konkrétně třeba v šachách tam potřebujem, že odehrát ty partie, nasbírat si data, udělat tu iteraci, jak jsme viděli a opakovat to. No a když se tydlety algoritmy učej hrát šachy a na
**中文：** ……一辈子、甚至全人类加起来所见过的都要多得多的数据。具体到象棋：我们需要下很多盘、收集数据、做迭代（就像刚才看到的那样）并不断重复。当这些算法学下象棋，在……

**[45:55 – 46:11]**
**捷克语：** konci tréninku to dokáže porazit nejlepší šachový hráče na světě jako s přehledem, tak to odehrálo víc partií, než všechny šakoví hráči v histori lidstva odehráli. Jo, takže to je jako jeden důvod, proč proč to dokáže být
**中文：** ……训练结束时它能轻松击败世界上最强的棋手，那它下过的盘数，已经超过了人类历史上所有棋手下的总和。对，所以这就是它能……

**[46:11 – 46:25]**
**捷克语：** lepší než než lidi v šachu. To samý, proč to dokáže být lepší jako jak spoustu expertů dneska skoro v jakýmkoliv fieldu. No protože to přečetlo všechny knížky, který kdy byly vydaný, přečetlo si to celej internet a
**中文：** ……比人强的其中一个原因。同样的原因，让它在今天几乎所有领域都能超过很多专家。因为它读完了所有出版过的书，读完了整个互联网，而且……

**[46:25 – 46:41]**
**捷克语：** zároveň to přes reinforce maleny, k tomu se dostaneme. To vyřešilo třeba víc matematicky hádanek než zase všichni matematici dohromady, jo. Takže není to tak, že prostě z toho kdo dokáže vyšťavit ze stejnýho množství dat víc, ne? Je to díky tomu, že tyhlety techniky
**中文：** ……与此同时（关于强化学习我们之后还会讲），它解出的数学谜题比所有数学家加起来还多，对吧。所以说，并不是谁更能从同样多的数据里榨出东西，对吧？关键在于这些技术……

**[46:41 – 46:55]**
**捷克语：** jsou prostě obecný, jednoduchý a když to dokážeme naškálovat, tak hold z toho dokážeme dostat mnohem výsledky. Jo, tak jo. Eh, a tady jo, tady je jak ty
**中文：** ……本质上是通用、简单的；而当我们能把它规模化之后，自然就能从中得到好得多的结果。对，好。呃，还有，这里就是那种……

**[46:55 – 47:11]**
**捷克语：** typický grafiky, když nějaký článek vidíte vypadaj, tak xová osa je nějakej jsou buď ty iterace, který jsme měli, nebo čas, jak dlouho nám to trvá trénovat. A Y osa je eh třeba reward, kolik dokážeme nasbírat v té počítačové
**中文：** ……典型的图表：当你看某篇论文里的图，X 轴通常是我们跑过的迭代次数，或者训练所花的时间；Y 轴通常是比如我们在那个电脑……

**[47:11 – 47:26]**
**捷克语：** hře. A nebo tady pro go nebo šachy, tak na epsiloné ose třeba můžeme mít elo. Aha. A dokázalo, dokázalo by to přijít na nové nápady. >> Ještě jednou, promiň. >> Dokázalo by to přijít i na nové nápady.
**中文：** ……游戏里收集到的奖励。或者像围棋、象棋这里，epsilon 轴上可以是 Elo 等级分。啊哈。而它能、它能想出新点子。>> 再说一遍，抱歉。>> 它能想出新点子。

**[47:26 – 47:36]**
**捷克语：** >> Eh, máme datase. >> Aha. >> V tom datase dokáž nějaký nápady. >> Aha.
**中文：** >> 呃，我们有数据集。>> 啊哈。>> 在那个数据集里能想到一些点子。>> 啊哈。

**[47:36 – 47:51]**
**捷克语：** >> A ty nápady třeba když člověk jako občas. >> To je skvělej dotaz a to je jako na delší diskuzi, jo? Eh a
**中文：** >> 而这些点子，比如人偶尔会……>> 这是个很棒的问题，而且值得好好讨论，对吧？呃，还有……

**[47:51 – 48:04]**
**捷克语：** možná jako já na to neodpovím, já na to odpovím otázkou, jo, nebo spíš jakože eh, protože říkám, je to naší diskuzi, ale eh obecně jakože docela fazi říct, co je vůbec eh novej nápad, jo, to jako
**中文：** ……也许我不直接回答，而是用另一个问题来回应，对吧？或者说——因为我说了，这值得讨论——但一般地，我们其实挺难说清"新点子"到底算什么，这个……

**[48:04 – 48:14]**
**捷克语：** to je strašně důležitý si uvědomit a stejně tak jako platí i i zrovna v matematice, že hromada velkejch novejch
**中文：** ……是至关重要的认识，而且恰恰在数学里也成立：大量重大的新……

**[48:14 – 48:28]**
**捷克语：** výsledků, tak ve skutečnosti eh se potom jako zpětně ukázalo, je ono je to v podstatě jako ten samej nápad, to samá myšlenka jako v e jako v týhleté části matematiky jenom tu samou myšlenku někdo
**中文：** ……成果，事后回看会发现，本质上其实和那个想法是一样的——和数学里某一分支里的同一个思想是一回事，只不过有人把同一个思想……

**[48:28 – 48:43]**
**捷克语：** někdo přenesl sem. To se to se jako děje všude a teďka jako je to novej nápad, není to novej nápad, prostě je to fazi, ale je to zrovna věc, kterým tydlencty modely dokážou bejt určitě strašně dobrý právě tím, že to posbírá všechny nápady, který byly napsaný, tak je pro ně
**中文：** ……搬到了这儿。这种事到处都在发生——现在看起来是个新点子，其实不是新点子，只是……但这恰恰是这些模型能非常擅长的地方：因为它们把所有写下来的点子都收集了起来，所以对它们来说……

**[48:43 – 48:52]**
**捷克语：** relativně jednoduchý si říct, ok, jako tadleta myšlenka, nikdo ji ještě nepoužil tady. Bůh, mám novej výsledek. Super.
**中文：** ……相对简单就能说清楚——好，比如这个想法，还没人在这儿用过。天哪，我有新成果了。太好了。

**[48:52 – 49:00]**
**捷克语：** >> Nedalo by se říct, že třeba jak jsme koukali na trénování v tý hře breakoutu, eh, že vlastně to, že třeba udržel ten týpček nahoře, je pro ten model nový
**中文：** >> 能不能说，比如我们刚才看 Breakout 那游戏的训练时，其实那个小球能一直停在上方，对模型来说就是一个新的……

**[49:00 – 49:08]**
**捷克语：** nápad nikde v tom trénování, kdyby neviděl, takže je to vlastně vymyšlení nového nápadu, když teda jako v realitě existuje, tak ten model si nikdy nezí.
**中文：** ……这个点子在训练数据里哪儿都没有出现过，所以它其实是在"发明"一个新点子——既然这个东西在现实里确实存在，只是模型从未见过。

**[49:08 – 49:17]**
**捷克语：** >> Já myslím, že to je good point, jakože je to pro ten, když to trénujeme jenom a k tomu se dostaneme, jak fungujou dneska ty jazykový modely. Kdyby to fungovalo
**中文：** >> 我觉得这是个好观点，也就是说，这适用于"只做训练"的情况——我们待会儿会讲到今天的这些语言模型是怎么运作的。如果它只是……

**[49:17 – 49:32]**
**捷克语：** jenom tak, že to posbíráme celej internet a natrénujeme na tom ten jazykovej model, tak tam by bylo jako eh hůř věřit tomu, i když možná by se tomu dalo věřit, že by to objevilo něco úplně novýho, ale eh v tom breakoutu tam je
**中文：** ……把整个互联网收集起来、在上面训练出一个语言模型，那要让人相信它能"发现"什么全新的东西就更难了——虽然也许可以相信——但在 Breakout 那个例子里，它是……

**[49:32 – 49:40]**
**捷克语：** tořitelný, protože to samo samo zkoumalo věci a našlo si to něco novýho. Tak tím, že právě dneska e i ty jazykový modely používají na konci hromadu Rainfalman
**中文：** ……可信的，因为它（智能体）是自己探索、自己找到了新东西。而正因为今天的这些语言模型，在最后也用大量的强化……

**[49:40 – 49:55]**
**捷克语：** Larningu, tak tím víc je právě BBL, že to dokáže odhalit nějaký jako nový nápady, nějakej jako novej novej jako myšlenkovej pochod, kterej to tř kterej to nikdy eh v trénovacích datech nevidělo. Jenom tím, že ten myšlenkovej
**中文：** ……学习，所以尤其通过 RLHF（基于人类反馈的强化学习），它才更有可能揭示出某些新点子、某种它从未在训练数据里见过的新思维过程。仅仅是因为那个思维……

**[49:55 – 50:07]**
**捷克语：** pochod na konci mu dá velkej reward, kde ta kde ten reward je super. Doká podařilo se mi vyřešit tuhle jako matematickej jako open problem. Aha
**中文：** ……过程在最后给了它一个大奖励——那个奖励非常棒——"我竟然解开了这个数学上的开放问题"。啊哈。

**[50:07 – 50:22]**
**捷克语：** dostě to není náš schopnej vyrábit. Aha >> existují stále, ale najít nejí >> eh
**中文：** ……不过那并不是我们人类能"生产"出来的。啊哈 >> 它们（这类问题）依然存在，只是还没被找到 >> 呃

**[50:22 – 50:36]**
**捷克语：** OK. Tak myslel jsem si, že ti rozumím, teď už ti nerozumím, protože myslel jsem myslel jsem, že ze začátku nalezíš něco jako na nerozhodnutelný problémy, ale teďka si myslím, že mluvíš o něčem jiným. >> [frknutí] >> můžeme narazit na nějakej nápad.
**中文：** OK。我刚才以为我懂你了，现在又不懂了——因为我原以为你开头说的是某种不可判定问题，但现在我觉得你在说别的东西。>> [清嗓] >> 我们可能碰到了某个点子。

**[50:36 – 50:51]**
**捷克语：** >> Aha, že jste schopní. >> Jo, takhle. Eh, eh, jasně. Fair point a možná jakože na to dostaneme odpověď za pár slajdů, kde budeme vidět o tom, jakoby tydlety herní věci se potom
**中文：** >> 啊哈，是说你们（模型）有能力。>> 对，就是这样。呃，呃，明白了。说得好，而且也许几页幻灯片之后我们就能得到答案——到时会看到这些游戏里的东西后来是怎么……

**[50:51 – 51:02]**
**捷克语：** aplikujou třeba na tu jako matematický matematický hádanky. Jo, tak jo, tak pokračujeme.
**中文：** ……应用到数学谜题上的。对，那好，我们继续。

**[51:04 – 51:14]**
**捷克语：** >> OK, super. Eh, teďka eh, asi asi dává smysl, kolik jsme začali a kolik máme končit?
**中文：** >> OK，太好了。呃，现在……大概、大概说得通了，我们从哪里开始、又要到哪里结束？

**[51:14 – 51:23]**
**捷克语：** Půlu, ale když >> dobře, tak v tom případě přeskočím tuhle sekci, protože je důležitější se dostat do tý další sekce.
**中文：** （半途插话）>> 好的，那这种情况下我就跳过这一节，因为更重要的是进入下一节。

**[51:23 – 51:31]**
**捷克语：** Eh, dobře. [odkašlání] Tak jo. Eh, tak peme udělat tuhle tuhle sekci tím pádem si
**中文：** 呃，好。[清嗓]那好。呃，那我们就做这一节，因此……

**[51:31 – 51:46]**
**捷克语：** myslím, že stíháme. Eh, tak todle jsou jako high level ty myšlenky a teďka spolu rychle prolítneme to, jak se to historicky vyvíjalo a dostaneme se k tomu, proč dneska je to strašný topik a jak [odkašlání] konkrétně se to právě
**中文：** ……我觉得我们进度 OK。呃，这些就是高层次的几个想法，现在我们一起快速过一遍它是怎么历史演进的，并讲到为什么今天它成了热门话题，以及[清嗓]它具体是……

**[51:46 – 51:58]**
**捷克语：** používá v těch AI modelech. Tak já jsem rozdělil tu historii reinforce melingu, a hlavně apekovanýho reinforcem learningu na tři období.
**中文：** ……怎么用在那些 AI 模型里的。我把强化学习——尤其是结合了深度学习的强化学习——的历史分成了三个时期。

**[51:58 – 52:13]**
**捷克语：** První období, eh, který jsem nazval neolick neolitickým obdobím, tak je zhruba od 70 let do roku 2012. A tolencto období je charakteristický s tím, že vznikaly jako takový základní
**中文：** 第一个时期，我把它叫做"新石器时期"，大概从 70 年代到 2012 年。这个时期的特点是：诞生了那些基础的……

**[52:13 – 52:27]**
**捷克语：** building bloky, eh, na kterých, e, v podstatě, že jo, ať už ty formalismy, nebo ty teoretický výsledky a a stejně tak takový ty základní algoritmy, který potom dokážeme běhat na relativně malejch prostředích, jo, takže prostě
**中文：** ……构建模块——无论是那些形式化方法、理论结果，还是那些基础算法，它们能在相对小的环境里跑起来，所以……

**[52:27 – 52:36]**
**捷克语：** postupně vznikal jako takovej jako eh eh taková prostě eh jak se tomu říká, na baráku dole. Eh,
**中文：** ……它们就逐渐积累起来，就像人们说的，是房子的地基。呃，

**[52:36 – 52:45]**
**捷克语：** >> jo, super. Díky. Eh, na kterým prostě eh se se všechno staví a že že je do budoucna. Jo. A mám tady pár několik
**中文：** >> 对，太好了。谢谢。呃，就是说所有东西都建立在它之上，而且是为了将来。对。我这里还有几个……

**[52:45 – 53:00]**
**捷克语：** korektivních příkladů, kde zase pro vás to teďka eh vám to možná nic neříká, ale potom třeba absolvujete straku straků na Falem Learning, tak najednou si na tydlety všechny výrazy vzpomenete a uvědomíte si, j, všechny tyhlety věci
**中文：** ……对照性的例子，现在对你们来说可能什么也说明不了，但之后比如你们去上某门强化学习的课，突然就会想起所有这些词，并意识到：所有这些东西……


## 游戏史上的突破：Pong、AlphaGo、扑克与规模化

**SECTION_NOTE**
- 第一波爆发(约2012–2015)：DeepMind 用 RL 在 Pong/Atari 上「魔法般」自学出策略
- AlphaGo 攻克围棋(2016)：曾被认为还需二十年才能超越人类
- 扑克是不完美信息博弈，需 CFR（反事实遗憾最小化）一类方法；DeepStack 是代表
- 规模化：把同样的思想放大到更多机器、更大网络——例如 OpenAI 的 PPO 算法
**END_SECTION_NOTE**

**[53:00 – 53:08]**
**捷克语：** vznikly ve skutečnosti relativně dávno a na potom hromadu těch věcí, který se dějou od 20 plus se dá dívat tak, že
**中文：** ……其实在相当早以前就出现了，而从 2020 年之后发生的很多事，都可以这样来看：

**[53:08 – 53:24]**
**捷克语：** jsou to v podstatě ty samý myšlenky, ale dokázaly se naškálovat eh na velkém compute a dokázali se spojit právě s Deepleringem, aby ty samý myšlenky eh jsme dokázali rozběhat na hrozně velkých prostředích a to přineslo právě ty
**中文：** ……本质上还是那些同样的想法，只是它们能在巨大的算力上规模化，并且和深度学习结合起来，于是同样的想法能在极其庞大的环境里跑起来，而这恰恰带来了那些……

**[53:24 – 53:35]**
**捷克语：** aplikace a revoluce doho světa, jo, ale ty myšlenky vznikaly v podstatě v těhletěch letech. Potom e druhý období, který tady mám, vlastně čtyři období jsou, sorry, kecám.
**中文：** ……应用和给世界带来的革命——但这些想法基本上是在那些年里诞生的。然后，呃，我列的第二个时期——其实应该是四个时期，抱歉，我说错了。

**[53:35 – 53:44]**
**捷克语：** Eh, druhý období 2012 a 920, tak to bylo období, kde přišel první boomin v osm learningu a
**中文：** 呃，第二个时期，2012 到 2019，那是深度学习第一次爆发的时期，而且……

**[53:44 – 53:53]**
**捷克语：** ten přišel právě s tím, kdy byly první výsledky těch her, který jsme si ukazovali, jo, tam ten Pong, kterej, kterej tam magicky našel tu strategii,
**中文：** ……它伴随着我们刚才展示的那些游戏的早期成果而来——比如那个 Pong，它神奇地自己找到了那个策略，

**[53:53 – 54:09]**
**捷克语：** tak když se toleto poprvý povedlo Deep Mindu, tak to byl jako velkej eh šok pro hromadu lidí. mnohem větší šop, pak, jak přišel, když tyhlety techniky prorazely právě lidi v v Go, kde dlouho se lidi mysleli, e, že bude třeba trvat dalších
**中文：** ……所以当 DeepMind 第一次成功做到这个时，对很多人来说是巨大的震撼。比后来更大的震撼是，当这些技术突破到围棋（Go）上——人们长期以为，可能还要再等……

**[54:09 – 54:18]**
**捷克语：** 20 roků, než počítače budou lepší e lepší jak lidi. Takže bylo to [odkašlání] jako bum novejch výsledků a bum toho, že konečně jde spolu
**中文：** ……20 年，计算机才能比人更强。所以那是[清嗓]新成果接连爆发、而且是终于能把……

**[54:18 – 54:28]**
**捷克语：** zkombinovat právě ten renarning, deep learning na to, aby se dokázaly vyřešit problémy, který nejen že předtím nešly vyřešit, ale lidi si mysleli, že bude trvat ještě hrozně dlouho, než je vyřešíme.
**中文：** ……深度学习和强化学习结合起来，去解决那些不仅以前解不了、而且人们以为还要很久才能解的问题。

**[54:28 – 54:43]**
**捷克语：** A eh zase já tydlety slajdu slajy projdu relativně rychle, ale do tohodle období se dá zařadit ty počítačový hry, Alpha Go, eh Poker, potom [odkašlání] tydlety i velký počítačový počítačový hry. Zase
**中文：** 呃，这些幻灯片我会过得比较快，但这个时期可以归入：电脑游戏、AlphaGo、扑克，以及[清嗓]那些大型电脑游戏。同样……

**[54:43 – 54:58]**
**捷克语：** bylo to jako e v podstatě to to samý jak ta jednoduchá hra Pongk, ale dá se to naškalovat v podstatě ty samý myšlenky. Eh, ve skutečnosti to tadleta hra, tak zatím byl v podstatě jenom naškaloven PPO algoritmus, který jsme měli spolu
**中文：** ……它本质上和那个简单的 Pong 游戏是一样的，只是这些同样的想法可以被规模化。呃，实际上刚才那个游戏，用的基本上就是我们已经一起看过的那个被规模化的 PPO 算法，

**[54:58 – 55:09]**
**捷克语：** asi na slidu 10, jo, že prostě slide 10 se od tohodle výsledku z Openia neliší ničem jiným, než že to bylo naškalovaný na hromadu počítačů a na hodně velký sítě.
**中文：** ……大概在第 10 页幻灯片。也就是说，第 10 页和 OpenAI 的这个成果之间，唯一的区别就是它被规模化的程度——用了很多台计算机和很大的网络。

**[55:09 – 55:22]**
**捷克语：** Super. Stejně tak to lidi už začínali aplikovat na nějakou jednoduchou robotiku a takovýdle sexy aplikace i v reálným světě a obecně všichni byli happy.
**中文：** 太好了。同样，人们也开始把它应用到一些简单的机器人，以及现实世界里这类很酷的应用，总的来说大家都很开心。

**[55:22 – 55:37]**
**捷克语：** Ale potom přišlo období eh který nevypadalo úplně dobře [odkašlání] a důvod, proč jsem já tole období e nazval takhle, protože zjednoduše řečeno přišel hlad a cholera. A co se stalo, že
**中文：** 但随后到来了一个看起来不太妙的时期[清嗓]——我之所以这么叫它，简单来说是因为"饥荒和瘟疫"降临了。而发生了什么呢……


## 瓶颈期：朴素规模化的极限（「饥饿与霍乱」）

**SECTION_NOTE**
- 把原有技术与深度学习简单结合、再一味堆规模，会撞上「朴素规模化」的天花板
- 这一时期并非一切顺利——需要新的方法突破才能继续前进
**END_SECTION_NOTE**

**[55:37 – 55:51]**
**捷克语：** tenhlecten jako naivní exploitation, kde se vzaly tydlet techniky, který už tady byly dlouho, splo deep learningem, začalo to fungovat a lidi to škálovali, škálovali, tak to narazilo svým způsobem na limity toho naivního škálování.
**中文：** ……就是那种"天真的扩展"——那些早已存在、又和深度学习结合的技术，开始奏效，人们就不断地规模化、规模化，结果在某种意义上撞上了这种天真式规模化的天花板。

**[55:51 – 56:05]**
**捷克语：** Nebylo jasný, ok, co získáváme tím, že řešili jsme malý hry, teďka máme pong, teďka máme jako velký počítačový hry. Eh, ale jako co co dál? Jakože to byl jako jeden velký problém, takže ten impakt na reálnej svět byl menší, než
**中文：** 当时并不清楚：我们解了小游戏，现在有 Pong，现在有大型电脑游戏，然后呢？这成了一个大问题——它对现实世界的影响，比……

**[56:05 – 56:18]**
**捷克语：** lidi doufali poom, co viděli, co to začalo dělat v počítačovejch hrách. Ale možná ten jako druhej hřebíček do raky, který byl mnohem důležitější, byl, že v roce
**中文：** ……人们在看到它在电脑游戏里的表现后所期望的要小。但也许那根钉进棺材的、更重要的钉子，是在……年

**[56:18 – 56:26]**
**捷克语：** 2019 Open AI releaslo svůj svoje GPT2 a tehdy to bylo jako obrovskej šok pro
**中文：** ……2019 年，OpenAI 发布了他们的 GPT-2，当时对所有……

**[56:26 – 56:34]**
**捷克语：** všechny lidi, který dělali NFKu, protože najednou tady byla neuronka, která vypadala hrozně chytře. Vypadala jako strašně dobrej chytrej agent, mohli jste
**中文：** ……做 AI 的人来说都是巨大的震撼，因为突然之间出现了一个看起来聪明得吓人的神经网络。它看起来像个非常聪明的智能体，你可以……

**[56:34 – 56:49]**
**捷克语：** si s tím povídat. A bylo zatím ve skodni nula reinforce melaningů. Takže najednou jak Deep Mind, tak spousty jiných reinforce melaning labů začali panikařit, že v podstatě jdou špatným směrem. Proč se tady vlastně vůbec zaobívám refsem learningem? Když
**中文：** ……和它聊天。而它里头还完全没有任何强化学习的成分。于是突然之间，无论是 DeepMind 还是其他很多强化学习实验室，都开始恐慌：我们是不是走错方向了？我到底为什么要搞强化学习？既然……

**[56:49 – 57:03]**
**捷克语：** obyčejnej deep learning, kde vezmeme celej internet, naučíme na tom Neronku predikovat další slovo, decit dokáže bejt ve skutečnosti strašně chytrý, že to byl důvod, proč proč se v podstatě
**中文：** ……普通的深度学习——把整个互联网拿来，训练神经网络去预测下一个词——就能变得实际上聪明得吓人。这就是那个让世界……

**[57:03 – 57:18]**
**捷克语：** svět změnil. A teďka k čemu se chci dostat a tím se blížíme už ke konci přednášky, tak to období, v kterým žijeme teď, tak je období renesance Renforc learningu. A co je na tom pěkný, takové ve skutečnosti to samý, co
**中文：** ……改变的原因。而现在我要说的、也接近讲座尾声的是：我们此刻所处的这个时期，是强化学习的"文艺复兴"时期。而妙的地方在于，其实正是……

**[57:18 – 57:27]**
**捷克语：** způsobilo eh jakoby temný období Rainfal Smelarinku, tak je důvod, proč je to teďka jedna z nejvíc hot topics v AI. A
**中文：** ……造成强化学习"黑暗时期"的同一个东西，现在又成了它成为 AI 最热门话题之一的原因。而……

**[57:27 – 57:41]**
**捷克语：** to jsou právě jazykový modely, protože co si lidi uvědomili v roce 2022, je, že se a zase já teďka přeskočím hromadu zajímavejch historickejch detailů, jak na to lidi přišli, proč to dává smysl,
**中文：** ……这恰恰就是语言模型——因为人们在 2022 年意识到（我这里跳过一大堆有趣的历史细节，不讲人们是怎么想到、为什么合理的），

**[57:41 – 57:56]**
**捷克语：** ale eh i vy sami, že jo, teďka eh tím, co jsme si teďka vysvětlili, tak si dokážete spojit 11 dohromady, tak máme ty metodurin forme lenu, který se eh
**中文：** ……但就连你们自己，对吧，通过我们刚才讲的，也能把点连起来：我们有那些强化学习里的方法，它们……

**[57:56 – 58:12]**
**捷克语：** sekvenčním rozhodování dokážou hledat strategii, která maximalizuje revol. Jo, ty jazykový modely v podstatě co dělaj? Jasně, jsou přetrénovaný na celým internetu a trénujeme tak, aby predikovali další token. No a potom tak, jak je používáme, oni predikuj další
**中文：** ……在序列决策中能去寻找最大化奖励（reward）的策略。对，语言模型本质上在做什么？显然，它们在全互联网上预训练，训练目标是预测下一个 token。而当我们使用它们时，它们就预测下一个……

**[58:12 – 58:28]**
**捷克语：** token. To zase dáme na vstup, potom zase predikujou další slovo, predikujou další slovo a takhle nám to takhle nám vyplivnou tu vaši odpověď. Jo, když se když když se zeptáte chat GPT na něco, takhle to jako slovo po slovu, token po tokenu vám bude odpovídat. No a na konci
**中文：** ……token。我们再把它喂回输入，然后它又预测下一个词、再下一个词，就这样一个词一个词地把你的回答"吐"出来。对，当你问 ChatGPT 什么时，它就是这样一个词一个词、一个 token 一个 token 地回答你。而在最后……

**[58:28 – 58:36]**
**捷克语：** eh se na to můžeme dívat. OK, máme nějakej reward za to, jestli nám to odpovědělo dobře. Jo, takže ta sek ta je
**中文：** ……呃，我们可以这样看。好，如果它回答得好，我们就有一个奖励。所以那个序列就是……

**[58:36 – 58:45]**
**捷克语：** to sekvence nějakejch slov, který to vyplivne a máme tam reward za to, jestli nám to odpovědělo dobře. Tak to bylo jako první seta, v kterým lidi najednou
**中文：** ……它吐出来的一串词，而我们有个奖励来判断它回答得好不好。这就是第一个"设定"（情境），人们突然……

**[58:45 – 59:00]**
**捷克语：** začali používat reinforcement learning pro jazykový modely a začalo fungovat to strašně dobře, protože když tomu začali jenom dávat reward za to, jestli vy jste spokojný s odpovědí, tak to je v podstatě to, co to, co je chat GPT. To je rozdíl mezi GPT2, který byl jen jako jazykový model, který byl trénovanj
**中文：** ……开始把强化学习用于语言模型，而且效果出奇地好——因为只要给它一个奖励，奖励的标准是"你对这个回答满不满意"，这就基本是 ChatGPT 的本质了。这就是 GPT-2（只是一个语言模型，训练数据来自……

**[59:00 – 59:16]**
**捷克语：** internetu a chat GPT, který to chat znamená, že dáváme tomu reward za to, že je to dobrej chatbot, že si s tím dobře povídáte. A ta věc, která jako nejvíc hotá, je, že lidi dokážou i těm
**中文：** ……互联网）和 ChatGPT 的区别：chat 意味着我们给它的奖励是"它是一个好的聊天机器人、你能和它顺畅地对话"。而最火的一点是，人们还能给这些……

**[59:16 – 59:29]**
**捷克语：** modelům dávat reward za to, jestli to jakože verifiable dokáže udělat nějako sekvenci, nějakou sekvenci, která odpovídá třeba matematickýmu důkazu,
**中文：** ……模型一个奖励，奖励它能否"可验证地"产出某个序列——比如某个对应数学证明的序列，

**[59:29 – 59:44]**
**捷克语：** kterej na konci dokážeme ověřit. To znamená dostaneme reward. Super. Je to jako plus J. dokázal si vyřešit třeba tenhleten otevřenej problém nebo tuhlenctu hádanku na matematické olympiádě. Eh, tak to je přesně, kde dneska ten false melaning je jako velká
**中文：** ……我们在最后能验证它。也就是说，我们拿到了奖励。太好了。这就像是"+1"（加一分）：它能自己解开了某个开放问题，或者某道数学奥林匹克竞赛的谜题。呃，而这恰恰就是今天强化学习成为……

**[59:44 – 59:53]**
**捷克语：** věc, kdy se vezmou ty přetrénovaný jazykový modely. Zadefinuje se nám v podstatě jako reor to, co nám zajímá. Je to jako je to dobrej programovací agent.
**中文：** ……一件大事的地方——把那些预训练好的语言模型拿过来，我们基本上把"我们所关心的东西"定义成奖励。比如它是一个好的编程智能体，

**[59:53 – 60:09]**
**捷克语：** Dokáže to dobře naimplementovat tenhlecten kód, dokáže to dobře vyřadřit tuhlenctu matematickou hádanku. A to je ta naše definice rewardu. Pustíme na to přesně ty algority, který jsme spolu viděli a na konci dne máme strašně chytrýho agenta, kterej nám dokáže potom nový hádánky matematický, který nikdy
**中文：** ……它能很好地实现这段代码，能很好地解开那道数学谜题。这就是我们对奖励的定义。我们把它交给刚才一起看过的那套算法，到一天结束时，就有了一个极其聪明的智能体，它能解那些它从未……

**[60:09 – 60:24]**
**捷克语：** neviděl, e, vyřešit, než lidi, který se přihlášej na matematickou olympiádu. Tak jo. A já myslím, že to je v podstatě všechno. Tady máme jenom obrázek, který ukazuje, jak v průběhu času se ze začátku nepoužívali skoro jako žádnej
**中文：** ……见过的、比那些报名数学竞赛的人解得更好的数学新谜题。那好。而我觉得基本上就这些了。这里有一张图，展示的是：一开始几乎没有人把任何……

**[60:24 – 60:40]**
**捷克语：** žádnej compute na rainforce melning. Všechno to bylo čistě o tom pritréningu a v průběhu času víc na víc flopu computu a peněz jde právě na tu reinforce m learning fázi. A toleto přeskočím. Tole taky přeskočím.
**中文：** ……算力花在强化学习上。一切都纯粹是预训练；而随着时间推移，越来越多的 FLOPs 算力和资金正流向强化学习这一阶段。这张我跳过。这张也跳过。

**[60:40 – 60:56]**
**捷克语：** Ne, tole nepřeskočím. Mám ještě 5 minut, že jo? >> Super. Tak jo. Tak tak 5 minut je úplně akorát. Tak já co teďka udělám, jsou nějaký jako crazy predictions pro reinforce learning forward.
**中文：** 不，这张我不跳。我还有 5 分钟，对吧？>> 太好了。那好。5 分钟刚刚好。那我现在要做的，是对强化学习的未来做一些"疯狂的预测"。

**[60:56 – 61:09]**
**捷克语：** A tenhlecten obrázek jenom ukazuje, berte to samozřejmě trošku s rezervou, protože dělat předpovědi o budoucnosti je samozřejmě, když se lidi kreslili eh e takovýhle takovýhle předpovědi v 50.
**中文：** 这张图只是说明一下，当然要带点保留地看它——因为预测未来嘛，就像人们在 50 年代画过这种……

**[61:09 – 61:18]**
**捷克语：** 50. letech, ale i tak budu i tak udělám nějaký functions. Tyv to první je relativně jednoduchá, eh protože si
**中文：** ……这种预测图一样。但即便如此，我还是要做几个预测。第一个相对简单，因为我觉得……

**[61:18 – 61:26]**
**捷克语：** myslím, že je dobrá šance, že se to stane a v podstatě e to, jak veškerý, eh, AI systémy dneska fungujou, dělá se
**中文：** ……它有较大概率会发生——而本质上，今天所有 AI 系统的运作方式是这样的：要做……

**[61:26 – 61:35]**
**捷克语：** tam hromadu tréninků v tom smyslu, že běžíme na hrozně moc grafickejch kartách ten gradient distance, že tam tudíme váhy těch velkejch neronovejch sítích,
**中文：** ……大量的训练，也就是在极大量的显卡上跑梯度下降，去更新那些大型神经网络里的权重，

**[61:35 – 61:51]**
**捷克语：** stojí to hromadu peněz, hromadu computu a potom, když už jsou ty sítě natrénovaný, tak se potom prostě nahrajou těm zákazníkům. Potom jsou to ty fixní síti, s kterýma vy si teďka povídáte a decit. jakože ty sítě už se dál neučej v průběhu toho, kdy jsou
**中文：** ……这要花大量金钱和算力。等网络训练好之后，就直接部署给客户。于是它们就成了那些"固定网络"——你现在正在和它对话、觉得它聪明得吓人的那些网络。也就是说，这些网络在……

**[61:51 – 62:07]**
**捷克语：** nasazeni do toho světa, jo. Ty váhy jsou fixní, takže není to jak lidi, který prostě se eh učej, jak učej pořád, jo, že nemáte prostě fixní strategii, ale tak dneska v podstatě funguje funguje moderní EA, jo, potom co prostě natréneme tu síť, tak ji nasadíme a hold
**中文：** ……被部署到真实世界里之后就不再学习了。权重是固定的，所以它不像人——人会一直学、持续学，对吧，人没有一套固定不变的策略。但今天的现代 AI 基本就是这样运作的：训练好网络，然后部署，然后……

**[62:07 – 62:16]**
**捷克语：** za půl roku vyjde nová, lepší, větší síť a nasadí nasadíme ji znova, jo? Není tam žádná notion toho online nebo continue learningu. Tak to je moje první
**中文：** ……半年后出一个新的、更好的、更大的网络，再重新部署，对吧？这里面没有任何在线学习或持续学习的概念。所以我的第一个……

**[62:16 – 62:24]**
**捷克语：** prediction, že časem uvidíme víc a víc eh eh jakoby toho, že ty sítě se adaptujou v průběhu. Eh, druhá
**中文：** ……预测是：随着时间推移，我们会越来越多地看到这些网络在运行过程中自我适应。呃，第二个……

**[62:24 – 62:33]**
**捷克语：** prediction je, že právě jak deep learning už měnilo svět kolem nás, tak reinforcement learning udělá to samý pro
**中文：** ……预测是：就像深度学习已经改变了我们周围的世界，强化学习也会对我们……

**[62:33 – 62:49]**
**捷克语：** nás. A jo, to co to, co určitě teďka platí a možná nějaký lidi to tomu nevěřej, ale prostě eh tak nemají pravdu. Eh, že AI v podstatě způsobuje největší revoluci e našeho života. Mění
**中文：** ……做同样的事。而且，有一件事现在确实成立、也许有些人不信，但他们其实就是错了。呃，那就是 AI 本质上正在引发我们生命中最大的一场革命。它正在改变……

**[62:49 – 62:57]**
**捷克语：** to ve všechny odvětí kolem nás. ten svět dneska vypadá úplně jinak, než vypadal před pěti lety a před 10 lety. A jako if
**中文：** ……我们周围的所有行业。今天的世界和 5 年前、10 年前完全不同。而且 if……

**[62:57 – 63:05]**
**捷克语：** anything, tak se to tak se jenom akceleruje e to, jakej ten vývoj je kolem nás. A stejně tak jako se to stalo
**中文：** ……anything（如果有什么的话），这种发展只会加速。而正如它（这场革命）之所以发生，是因为……

**[63:05 – 63:20]**
**捷克语：** kvůli deep learningu, tak moje prediction je, že tak jak máme deep learning, ať už si otevřeme telefon, jedeme tramvají, jedeme v autě, otevřeme si počítač, tak všude budeme mít aplikace reinforce melinku a zase prostě ani nad tím nebudeme přemýšlet a hold to
**中文：** ……深度学习，我的预测是：就像我们今天到处都有深度学习——无论打开手机、坐电车、开车还是开电脑——将来我们也会到处看到强化学习的应用，而且我们同样根本不会去想它，它……

**[63:20 – 63:33]**
**捷克语：** bude kolem nás a bude to fungovat. No a ta poslední predikce, tak to se vrátím k té analogii, kterém jsem na začátku, kde jsem říkal, ok, nejdřív byl Deep Learning Ma Stream, potom
**中文：** ……就会在我们周围、就会运转。而最后一个预测，我要回到开头那个类比：我说过，先是深度学习热潮，然后……

**[63:33 – 63:48]**
**捷克语：** za deep learning byl Touring Award, tak nakonec byl za deep learning udělaná i Nobelova cena. Tak moje predikce je, že eh za rainfalse melanin bude taky udělanána Nobelovka cena, Nobelova cena.
**中文：** ……深度学习拿了图灵奖，最后深度学习还拿了诺贝尔奖。所以我的预测是：强化学习也将获得诺贝尔奖，诺贝尔奖。

**[63:48 – 64:02]**
**捷克语：** A moje prediction je, že ji dostane Rich Saturn. Kdy ji dostane, za co ji dostane, to já nevím, ale pořád je tole moje predikce. Tak jo, tak to je v podstatě všechno a já mám poslední dva slajy,
**中文：** 而我的预测是，得奖的会是 Rich Sutton（理查德·萨顿，强化学习之父）。他什么时候得、因为什么得，我不知道，但这始终是我的预测。那好，这基本就是全部了，我还有最后两张幻灯片，

**[64:02 – 64:16]**
**捷克语：** který jenom řeknou během půl minuty, co děláme my, tak to, co jsme si tady spolu prošli, to je v podstatě, co jsme dělali posledních 15 roků, ať už to byly tydlety samoučící algoritmy, jsme dělali
**中文：** ……用半分钟讲讲我们在做什么：我们刚才一起过的内容，基本就是我们过去 15 年做的事——无论是那些自学习算法，我们曾在……

**[64:16 – 64:32]**
**捷克语：** v pokru, potom jsme dlouhý roky dělali v Deepmindu, tak pár roků zpátky jsme se rozhodli vrátit e do Prahy a řekli, jsme si, že budeme aplikovat tyhlety samoučící algoritmy v nějaký novej krazy doméně, kde budeme budovat zase vlastní
**中文：** ……扑克（poker）领域做过，后来在 DeepMind 做了很多年；几年前我们决定回到布拉格，说要把这些自学习算法应用到一个全新、很酷的领域，在那里重新建立起我们自己的……

**[64:32 – 64:46]**
**捷克语：** state of the art e algoritmy a zkusíme tady v Praze vybudovat eh eh fakt jako World Class Research, co dělá Rainfel, tedy aplikovanej v nějakj doméně a eh
**中文：** ……最前沿（state-of-the-art）的算法，并试着在布拉格建起真正世界一流的研究——做强化学习，也就是把它应用到某个具体领域，而且……

**[64:46 – 64:59]**
**捷克语：** založili jsme si equekilibre a tady máte quo, kdybyste se o tom chtěli dozvědět víc. Tak jo, tak to je všechno.
**中文：** ……我们创立了 EquiLibre（平衡公司）。这里有二维码，如果你们想了解更多可以扫。那好，这就是全部了。

**[64:59 – 65:11]**
**捷克语：** >> Děkujeme. [potlesk] Určitě máme prostor na dotazy, tak já se nejdřív zeptám někdo zč.
**中文：** >> 谢谢。[掌声] 我们肯定还有提问时间，那我先问问现场有没有人……

**[65:11 – 65:24]**
**捷克语：** >> Vy jste zmiňal takovou tu dobu temná pro reinforcement learning. Myslíte si, že se to může stát jako pro ten deep learning, že se vlastně zjistí, že už se to nedá jen tak jako dál bez hlavy škálovat?
**中文：** >> 你提到过强化学习的"黑暗时期"。你认为深度学习会不会也出现这种情况——也就是人们发现它其实不能再这么毫无节制地规模化下去了？

**[65:24 – 65:34]**
**捷克语：** Tam je to může se to stát pro ten možná v tom výzkumu, ale jako zatím to vypadá.
**中文：** >> 那种情况也许在研究层面有可能发生，但至少目前看起来……

**[65:34 – 65:44]**
**捷克语：** Tak [smích] depl už vyhrá v tom smyslu, že teďka už eh hromada věcí funguje a je aplikovanej všude možně, jo, takže tam prostě jakože aplikace už jsou jasný.
**中文：** ……[笑] 深度学习已经赢了——从这个意义上说：现在海量东西都在运作、并被应用到各个地方，所以应用层面已经很明确了。

**[65:44 – 65:58]**
**捷克语：** pořád ten vývoj letí dopředu. Zatím to vypadá, že Scalines platí, že pořád lidi můžou jako dělat větší, dražší dražší neuronky a pořád to funguje. Takže tam to zatím nevypadá, že by to mělo na cokoliv na cokoliv narazit. Co se může
**中文：** ……发展仍在向前飞奔。目前看来，规模化（scaling）依然成立——人们还能做出更大、更贵的神经网络，而且依然有效。所以在那方面暂时看不出会撞上什么墙。可能发生改变的是……

**[65:58 – 66:12]**
**捷克语：** stát, že přijde nějaká nová eh úplně nová e metoda, která bude fungovat líp, ale zase jako nic tomu nenaznačuje, takže za za zatím spíš ne.
**中文：** ……也许会冒出某种全新的方法，效果比现在更好，但目前没有任何迹象表明会这样，所以至少现在还说不上会。

**[66:13 – 66:28]**
**捷克语：** Další dotaz tam. Ano. Tak jak jste říkal, tak ono je to schopný vyprodukovat nějakej jako validní matematickej důkaz. >> Aha. >> A to už to umí docela dobře. A jakj jaký jsou plány na to, aby ty důkazy byly nějak pochopitelný?
**中文：** >> 下一个问题。好的。就像你说的，它已经能产出某种有效的数学证明了。>> 啊哈。>> 而且它现在已经做得相当不错了。那有什么计划让这些证明变得更"可理解"吗？

**[66:28 – 66:36]**
**捷克语：** >> Hele, to je taky jakože věc, na kterou se lidi dívaj, protože typicky to dělá ty jakože víc jsou dva směry, jak dělá
**中文：** >> 嘿，这也是人们在关注的一件事，因为通常它生成证明有两条路线——

**[66:36 – 66:45]**
**捷克语：** ty důkazy. Jedna věc si je čistě jako představ si to fakt jak v textu, ale pak je to problém jako když ti to vyplnectránkovej důkaz textu, tak jako kdo to sakra bude ověřovat, protože i
**中文：** ……它做证明。一种是纯粹的、就把证明当作文本来生成；但问题是，当它吐给你一段文本证明时，到底谁来验证它？因为即便……

**[66:45 – 66:52]**
**捷克语：** nějaký jako těžký matematický důkazy, který vyřešili lidi, pak trvalo jako komunitě dva roky ověřit třeba ten důkaz. Takže jako dává mnohem větší
**中文：** ……某些人解出来的艰难数学证明，整个数学界都要花两年才能验证。所以更有意义的……

**[66:52 – 67:01]**
**捷克语：** smysl a jako většina těhle modulů se snaží jít spíš tím směrem, že ten důkaz je vysloven nějakým jako formalizovaným jazyce třeba v hlínu, kde fakt jako jde
**中文：** ……是：大多数这类模型倾向于走另一条路——让证明用某种形式化语言（比如 Lean）表达，这样才真正能……

**[67:01 – 67:16]**
**捷克语：** ukázat, ok, jakože průbově tole je důkaz, jo. A pak je ten spíš ten problém toho, co říkáš ty je OK. Eh, super. Ale jako jak mi to pomůže, krom toho, že vím, že to tvrzení platí, jako jak dostanu nějakou tu intuici, jak mi to vysvětlit. A to je to jsou lidi, který
**中文：** ……展示出来，证明这就是一个证明，对吧。而你说的那个问题更关键：'啊，太好了。但这对我有什么帮助？除了知道这个结论成立，我怎么获得那种直觉、它怎么向我解释？'而这正是那些人……

**[67:16 – 67:30]**
**捷克语：** se na to dívaj a to strašně zají zajímavej zajímavj jako odvětví. >> Tak další dotaz asi asi nevidím. Í, kdyby někoho ještě
**中文：** ……在关注的、非常有趣的领域。>> 那下一个问题……我好像没看到了。嗯，如果还有谁……

**[67:30 – 67:37]**
**捷克语：** napadlo, tak se klidně ozvěte a můžeme se podívat na ty dotazy, který jsou online.
**中文：** ……想到问题，尽管提出来，我们也可以看看线上提的问题。

**[67:39 – 67:55]**
**捷克语：** >> Jo, [frknutí] těžká otázka. [odkašlání] Co tam je? [smích]
**中文：** >> 好，[清嗓] 这是个难题。[清嗓] 上面写了什么？[笑]

**[67:55 – 68:04]**
**捷克语：** >> Aha. Eh, jo. Eh, jasně. Eh, ten dotaz se mi líbí a eh já řeknu určitě, jo, já se takhle, já řeknu, v čem je Matchfix
**中文：** >> 啊哈。呃，好。呃，明白。呃，这个问题我喜欢，我肯定会回答。我来说说，Matfyz（查理大学数学物理学院）好在哪里，

**[68:04 – 68:18]**
**捷克语：** skvělej, ale řeknu taky v čem si myslím, že Matfik má co zlepšovat. Jo. Eh eh důvod, proč má studovat Matface, je přesně to, v čem jmenuje Matfis dobrej. NF si myslím, že dělá dobrou práci naučit lidi správně přemýšlet a stejně
**中文：** ……但也说说我认为 Matfyz 还有哪些可改进之处。对。呃，呃，之所以该去读 Matfyz，恰恰是因为它好在哪里。学院（指 Matfyz）我认为在教人"正确思考"这件事上做得不错，同样地……

**[68:18 – 68:30]**
**捷克语：** tak typicky lidi si smartfizu odnesou to, že jako vědí poznat, jestli jako něčemu člověk rozumí nebo nebo nerozumí, což se jako nedá říct o hodně lidí na tom světě, na tomhle světě, že jo.
**中文：** ……通常从 Matfyz 出来的人会带走一种能力：能分辨自己到底懂不懂某样东西——而这一点，对这个世界上很多人是做不到的，对吧。

**[68:30 – 68:44]**
**捷克语：** Hromada vlastně lidí si myslí jako jak něčemu rozumí a ve skutečeně tomu vůbec nerozumí. Jako na matfizu se člověk naučí dokázat dokázat jako i fakt jako do hloubky a naučí se jako občas jako rozbít si ten čumák, že zjistí, že prostě ve skutečnosti něčemu nerozumí.
**中文：** 大量的人其实以为自己懂了某样东西，实际上完全不懂。而在 Matfyz，人学会去"证明"——真正深入到骨子里地证明——并且学会时不时"撞个鼻青脸肿"，从而发现：自己其实根本没懂。

**[68:44 – 68:53]**
**捷克语：** Takže jako ten způsob přemejšlení eh jít do hloubky a poznat, čemu rozumím, nerozumím, tak to si myslím, že se tady dělá dobře a určitě užem kvůli tomu má
**中文：** 所以这种"深入思考、并认清自己懂与不懂"的思维方式，我认为这里做得很好，单凭这一点就绝对……

**[68:53 – 69:00]**
**捷克语：** absolutně smysl e matfis studovat. A to, že potom spíš [odkašlání] se to jako posunuto pořád i tydlety věci, co se
**中文：** ……有充分的理由去读 Matfyz。而（话说回来）[清嗓]……这些东西也一直在向前推进……

**[69:00 – 69:09]**
**捷克语：** jako učej na matfizu, tak jsou relevantní. Proto akorát se to je to o jeden jako level abstrakce jinde třeba místo toho, aby potom ty matematici jako
**中文：** ……就像在 Matfyz 学到的东西，其实都有关联。只是它涉及的是另一个抽象层次——比如，将来那些数学家不再亲自做数学，而是去改进那个替他们做数学的"AI"，

**[69:09 – 69:22]**
**捷克语：** teďka to přeženu pak dělali tu matematiku, tak budou zlepšovat zlepšovat to já, který za ně bude dělat tu matematiku. to jako trošku přeháním, jo, ale jako odpověď je určitě jo, ale stejně tak řeknu jako jednu věc, kterou si myslím, že Matvis typicky nedělá
**中文：** ……我这话有点夸张，对吧，但答案确实是肯定的。不过同样我要说一件我认为 Matfyz 通常做得不够好的事：

**[69:22 – 69:38]**
**捷克语：** úplně dobře a to je eh eh to je eh na matfizu se člověk dokáže dobře naučit eh jednak to, co jsem říkal a stejně tak prostě vyřešit nějakej těžkej problém,
**中文：** ……那就是在 Matfyz，人能很好地学会我刚才说的那些，也能很好地去解一个难题，

**[69:38 – 69:54]**
**捷克语：** ale neučí se moc dobře, co je ten problém, na kterým bych dokázal na který bych měl trávit ten čas, jo, že jsou jakože dvě různý věci. Mám nějaký jako problem solving a problem selection. A na matfizu mně přijde, že často je
**中文：** ……但却没怎么学会"该把时间花在什么样的问题上"——也就是说，problem solving（解题）和 problem selection（选题）是两回事。而在 Matfyz，我觉得经常是……

**[69:54 – 70:05]**
**捷克语：** hromada šikovnejch, chytnejch jako strašně chytrejch lidí, který pracujou na extrémně nezálejným problému, kterej když vyřešej, tak no a co?
**中文：** ……一大堆聪明绝顶的人，在钻研极其不重要的问题——就算解出来，那又怎样？

**[70:08 – 70:23]**
**捷克语：** >> Tak jo, co dál? [odkašlání] Eh, hele, to je super dotaz. Eh, ř řeknu na to jako klasickou odpověď, jak
**中文：** >> 那好，下一个问题？[清嗓] 呃，嘿，这是个很棒的问题。呃，我给它一个经典的回答，关于……

**[70:23 – 70:31]**
**捷克语：** se jako tomudle vyhnout a jakoby jak se pořád tvářit, že je to jako správný a morální, i když to zežere hodně resourců
**中文：** ……怎么回避这个问题，以及怎么始终摆出一副"这既正确又道德"的样子，哪怕它消耗了大量资源。

**[70:31 – 70:40]**
**捷克语：** a teďka nezávisle na tom, jestli tomu člověk jako věří nebo nevěří, je to dobrej argument, tak může dávat smysl spálit hromadu eh neekologickejch
**中文：** ……而现在，不管你个人信不信，这是个不错的论点：烧掉大量不环保的……

**[70:40 – 70:53]**
**捷克语：** resourců, na to vyrobit strašně chytrý AI, protože potom to strašně chytrý AI nám přece pomůže vyřešit to eh jakoby všechnu tu ekologii a všechny ty problémy, který tady máme. To jako jeden klasickej argument a buď jako tomu
**中文：** ……算力资源，去造出一个极其聪明的人工智能，因为这之后，那个极其聪明的人工智能就能帮我们解决所有的生态问题、以及我们面临的种种难题。这是经典的论点之一，你可以……

**[70:53 – 70:57]**
**捷克语：** můžete věřit nebo nemusíte.
**中文：** ……选择相信，也可以不信。


## 从扑克到交易：市场即不完美信息博弈

**SECTION_NOTE**
- 金融市场在结构上类似扑克：参与者隐藏信息、会「虚张声势」、要推断对手在想什么
- EquiLibre 把自学习的 RL/CFR 方法从游戏搬到算法交易；与传统量化的区别在「不预测未来，而是求不可利用的策略」
- 与 Tower Research Capital 合作；挑战在于市场非平稳、噪声大、没有固定规则
**END_SECTION_NOTE**

**[71:00 – 71:16]**
**捷克语：** [odkašlání] Taky strašně super dotaz. Eh, co je jakože co je zajímavý a to je jako dobrý vědět pro všechny, že co se jak vypadá
**中文：** [清嗓] 这也是个超棒的问题。呃，有意思的是——而且这件事值得所有人知道——今天的 AI 世界长什么样：

**[71:16 – 71:29]**
**捷克语：** dnešní AI svět, tak asi málokdy málokdy by to odhadl, že to tak bude vypadat, ale dneska v podstatě ty nejlepší modely, který jsou open sourceový a otevřený, tak jsou ve skutečnosti z
**中文：** ……大概没人会猜到它会是这个样子——但今天，那些最好、开源开放的模型，实际上来自……

**[71:29 – 71:40]**
**捷克语：** Číny, což je, což je strašně zajímavý. a naopak ty jako close modely a ty firmy, tak jsou z Ameriky. Taková je, takové je dneska realita.
**中文：** ……中国，这非常有趣。而反过来，那些闭源模型和公司，来自美国。这就是今天的现实。

**[71:40 – 71:53]**
**捷克语：** Eh, jestli jsem spíš za jedno nebo za druhý. Eh, to by bylo zase jako na hrozně hrozně dlouhou debatu, protože jako jsou jako dobrý argumenty pro jednoho, dobrý
**中文：** 呃，至于我更站哪一边——呃，这又会变成一场没完没了的辩论，因为两边都有好论据，

**[71:53 – 72:08]**
**捷克语：** argumenty pro druhý. Co si myslím, že jakože co je relevantnější je, že Evropa je na tom špatně, ať už s open source nebo closed modelama, takže to to mě aso mrzí víc než jako kdo má close doma open
**中文：** ……另一边也有好论据。而我认为更相关的一点是：无论开源还是闭源，欧洲都处境糟糕，所以比起"谁拥有闭源、谁拥有开源"，这更让我感到遗憾。

**[72:08 – 72:11]**
**捷克语：** modely.
**中文：** ……模型。

**[72:14 – 72:16]**
**捷克语：** [frknutí]
**中文：** [清嗓]

**[72:22 – 72:35]**
**捷克语：** E, jasně, chápu. Eh, eh, já si myslím, že je. Eh, já si myslím, že je, protože jde tam o peníze, lidi jsou občas racionální, občas eh jako neracionální. Je tam
**中文：** 呃，明白，我理解。呃，呃，我觉得是的。呃，我觉得是的，因为这关乎钱——人有时理性，有时又不理性。里面还有……

**[72:35 – 72:50]**
**捷克语：** stejně tak je tam hrozně šumu v tom smyslu, když vydělám peníze, tak vydělal jsem je, protože jsem dobrej parkový hráč nebo mi zrovna přišly dobrý karty. Stejně tak jako spousta lidí e jako na trhu neví, jestli obchoduje dobře nebo špatně nebo mají štěstí. Takže já
**中文：** ……同样有大量噪声：当我赚到钱，我究竟是因为是个好扑克玩家，还是因为牌好？同样，市场上很多人并不知道自己是交易得好、差，还是只是运气好。所以我觉得……

**[72:50 – 72:54]**
**捷克语：** myslím, že ta analogie hrozně moc.
**中文：** ……这个类比非常贴切。

**[72:58 – 73:14]**
**捷克语：** >> [frknutí] >> Eh jo, typicky platí, eh, že to automatizovaný obchodování ve skutečnosti eh je nejvíc happy v takovejdlech
**中文：** >> [清嗓] >> 呃对，通常的规律是：自动化交易实际上在最……

**[73:14 – 73:29]**
**捷克语：** událostech. A to je spíš kvůli tomu, že když se děje něco crazy, tak to znamená, že hromada lidí panikaří. To znamená, ty trhy vypadají hrozně špatně a neefektivně a to jsou typicky ty největší žě pro tydlety automatizovaný
**中文：** ……这类事件中最开心。这更多是因为：当发生某种疯狂的事，意味着大量的人在恐慌。也就是说市场看起来极其糟糕、低效，而这恰恰是那些自动化……

**[73:29 – 73:41]**
**捷克语：** systémy. Ale zase je to jako spíš statistickej argument v tom smyslu, že todle typicky platí, ale že jo, kdo ví, jestli to bude platit o jako o eventu n+ 1.
**中文：** ……系统最大的机会。但这更多是统计意义上的论点：通常如此，不过，谁知道第 n+1 个事件还是否适用呢。

**[73:47 – 74:02]**
**捷克语：** >> Eh, super. Todle je dobrej dotaz. Eh, [frknutí] takže první věc je uvědomit si, že už teďka platí, že v podstatě eh [frknutí] je ten trh plnej jako agentů, ne úplně
**中文：** >> 呃，太好了。这是个好问题。呃，[清嗓] 所以首先要意识到，今天其实就已经是——呃，[清嗓] 市场里满是各种各样的智能体，虽然不是完全……

**[74:02 – 74:16]**
**捷克语：** AI, ale prostě nějakej jako je plnejch [odkašlání] automatizovanejch věcí, jo, jakože to state of the art automatizované obchodí obchodování rozhod není to, co se vám jako co jsme tady spolu dělali. To je to, co my se snažíme dělat. My se snažíme eh v
**中文：** ……的 AI，但也满是[清嗓]各种自动化的东西，对吧——也就是说，当前最前沿的自动化交易，还不是我们在这里一起做的那套。那正是我们想要去做的。我们试图……

**[74:16 – 74:24]**
**捷克语：** podstatě udělat jakože první trading company, která je fakt postavená na těhletěch moderních EA metodách, jo. Eh
**中文：** ……打造第一家真正建立在这些现代 AI 方法之上的交易公司，对吧。呃，

**[74:24 – 74:33]**
**捷克语：** a ale už teďka je ten to obchodování úplně automatizovaný. Hold se tam používají eh jiný tradičnější tradičnější metody, který který fungujou
**中文：** ……不过即便现在，交易已经完全自动化了。只不过用的是其他更传统的、行之有效的方法，

**[74:33 – 74:48]**
**捷克语：** dobře. My na to hold chceme jít těma metodama, co jsme měli tady. Takže, takže moje predikce je za dalších 5, 10 roků toleto určitě bude platit, že zase všechno bude automatizovaný tak, jak je teď. Akorát všichni budou muset používat
**中文：** ……效果很好。我们则想用我们在这里讲的这套方法来做。所以，我的预测是：再过 5 到 10 年，这套一定会成立——一切又会像现在这样自动化；只是所有人都必须用……

**[74:48 – 75:02]**
**捷克语：** tydlety moderní moderní e metody hold, protože jsou o tolik lepší než ty metody, co se používají teďka. A to se mi bude platit o Waren jako Buffetech. Jako dneska Waren Buffet [odkašlání] Warren Buffetové fungujou na trhu a
**中文：** ……这些现代方法，因为它们比现在用的方法好太多了。这也适用于像巴菲特那样的人。就像今天巴菲特[清嗓]们（Warren Buffetts）在市场上运作，而……


## 问答与结语：自动化交易的未来、巴菲特式长期投资对比

**SECTION_NOTE**
- 今天市场已充满（非 AI 的）自动化 agent；EquiLibre 想做第一家真正建立在现代 AI/RL 方法上的交易公司
- 预测：5–10 年后一切都会自动化，且所有人都不得不用这些「好得多」的现代方法
- 巴菲特式是「投资」（长期视角），与毫秒级「交易」是不同目标函数
- 市场疯狂/恐慌时往往最无效，恰是系统化交易的窗口；欧洲在开源/闭源模型上整体落后
**END_SECTION_NOTE**

**[75:02 – 75:16]**
**捷克语：** akorát mají prostě úplně jinej horizont, na kterj optimalizuj Warren Buffet netraduje, on investuje a to je úplně jiná věc investovat do Coca-Coly, než tradovat v zlomkách milisekund, aby ten
**中文：** ……他们只是有着完全不同的时间视野：巴菲特不是在日内交易，而是在投资——投资可口可乐，和在几毫秒内交易、让市场……

**[75:16 – 75:31]**
**捷克语：** trh byl efektivní a nehoupal se. Asi dáme poslední dotaz, protože už se jo >> eh jo, na tu odpověď je na kvérku.
**中文：** ……保持高效、不剧烈波动，完全是两码事。我们大概该问最后一个问题了，因为已经……>> 呃对，那个问题的答案还悬而未决（pending）。

**[75:33 – 75:48]**
**捷克语：** >> To byla rychlá odpověď. >> Tak jo, >> já se zeptám, jestli teda ještě někdo nemá nějaký závěrečný dotaz tady. Není tomu tak. Tak my ještě jednou děkujeme za perfektní přednášku. Děkuju vám, že jste přišli a za to za týden.
**中文：** >> 这是个很快的回答。>> 那好，>> 我想问问现场还有没有人有最后的提问。没有人了。那我们再次感谢这场精彩的演讲。谢谢大家到来，也谢谢大家这一周。

**[75:48 – 75:51]**
**捷克语：** Děkujem. [potlesk]
**中文：** 谢谢。[掌声]
