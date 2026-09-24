## 开场：小行星、Python 与海滩上的那位老师

**SECTION_NOTE**
- 主持人 Ron Minsky（Signals and Threads），嘉宾 Aaron Bauer：Jane Street 软件工程师，也是公司为数不多的「开发者教育者」（developer educator）之一。
- 高中前的暑期科学项目：去新墨西哥六周，学数学、天文、物理和一点 Python，用望远镜观测小行星并写代码算轨道——从此确定「编程才是我的事」。
- 小镇高中没有 AP 计算机课，于是通过北卡州的线上课程项目，跟一位「在海滩上」的退休老师学 AP CS。
- 大学暑期回该项目当助教，第一次写习题、讲二叉搜索树，就此想清楚要做和教育相关的事。

**END_SECTION_NOTE**

**[00:01 – 00:51]**
**EN:** [music] All right. Well, it's my great pleasure to have Aaron Bauer with me. Aaron is a software engineer and one of Jane Street's proud but few developer educators. We'll talk a little bit more about what that means in a bit, but thanks for joining me. I'm very excited to be here. So, I like to always hear a little bit about how people started out. You've done a lot of work which is kind of on the overlap of both software engineering and computer science and teaching. And I'm kind of curious like how did you get there? Sure. So kind of my origin story, you might say, is I was sort of fascinated with computers from a child. Computer programming always felt kind of intimidating. And then I did this summer program before my senior year of high school, creatively named the summer science program, [laughter] where I went to New Mexico for six weeks
**中文：** 好的，非常荣幸请到 Aaron Bauer。Aaron 是一位软件工程师，也是 Jane Street 为数不多但引以为傲的「开发者教育者」之一——这个头衔具体意味着什么，我们待会儿再展开，先谢谢你来做客。我很高兴能来。我一向喜欢先听人们是怎么起步的。你做的很多事情正好落在软件工程、计算机科学和教学三者的交集上，我很好奇你是怎么走到这里的？可以这么说，我的「起源故事」是我从小就被计算机吸引，但一直觉得编程有点令人望而生畏。后来在高四之前的那个暑期，我参加了一个项目——名字起得很有创意，叫「暑期科学项目」（Summer Science Program）——[笑声] 我去新墨西哥待了六周。

**[00:51 – 01:41]**
**EN:** and they taught us a bunch of math, astronomy, physics, and some Python. We took telescope observations of an asteroid and then wrote some Python code to take those measurements and compute an orbit for the asteroid. So really fun and interesting program, but I came out of it — or went into it — being like, all these things seem interesting. And I came out of it being like, wow, the programming was just way more [laughter] fun and like really my thing. So at that time, my small town high school didn't offer AP computer science, but found a retired teacher on a beach in North Carolina who could take it from. And then sort of from there — how did you find a retired teacher on the beach? So it's North Carolina had a like online course program that you didn't have to live in North Carolina to use. And it just turned out the guy
**中文：** 他们教了我们一大堆数学、天文、物理，还有一点 Python。我们用望远镜观测一颗小行星，然后写 Python 代码处理这些测量数据、算出它的轨道。这个项目非常有意思，但我进去的时候觉得「这些看起来都挺有趣」，出来的时候却想：哇，编程好玩太多了，[笑声] 这才是我的菜。当时，我所在小镇的高中没有开 AP 计算机科学课，但我们找到了北卡罗来纳州一位「在海滩上」的退休老师来教我。那么——你是怎么找到一位在海滩上的退休老师的？是这样的，北卡州有一个线上课程项目，你不需要住在北卡也能用。结果发现教这门课的那位老师

**[01:41 – 02:30]**
**EN:** teaching this course was not currently working in a school, but instead was on the beach. Oh, amazing. And then the teaching side comes in that the summer before I go into grad school, I go back to the summer science program as a TA. And that's sort of my first exposure to writing an exercise for students to do and giving a little lecture on binary search trees. And I was hooked and sort of from then knew that I wanted to do something with teaching. It's funny, by the way, just like the kind of science and physics hook in programming. That's actually like a deep thing in the history of computer science, right? A lot of the early programming and programming languages and work was all about like, you know, high-end physics simulations. I always, every now and then when I run into someone who's like gathering
**中文：** 当时并不在学校任职，而是在海滩上。哦，太有趣了。然后教学这一面就来了：在我进研究生院之前的那个暑假，我回到「暑期科学项目」当助教。那大概是我第一次为学生写习题、并且讲一堂关于二叉搜索树的小课。我一下就上瘾了，从那时起就知道自己想做一些和教学有关的事。顺便说一句很有意思的是，编程里那种「科学／物理的钩子」，其实是计算机科学史上很深的一条脉络，对吧？早期很多编程、编程语言和工作，全都围绕着高端物理模拟。我每次偶尔遇到那些在采集

**[02:30 – 03:19]**
**EN:** telescope data — just the hardcore computer science of weird FPGA exploits and stuff that people are doing there — I always find very impressive. There's just a lot of interesting pushing of the state-of-the-art and also a lot of messy not understanding a lot about computer science that I feel like comes out of that scientific computing world. Yes. Something I did in undergrad was work with a Fortran simulation of impacts — asteroids or comets hitting the surface — and this came out of code that was used to simulate atomic explosions in the early days of computing, because the physics of those two situations are not that different, it turns out. Oh wow. [laughter] Yeah. And there's a bunch of super cool stuff in the early Fortran work like that. You know, we care a
**中文：** 望远镜数据的人——那种硬核的计算机科学，各种奇怪的 FPGA exploit 之类的东西——我一直觉得非常了不起。那里面既有大量把技术推到最前沿的有趣工作，也有大量「其实并不太懂计算机科学」的凌乱做法，我觉得这些都出自科学计算那个圈子。是的。我本科时做过的一件事，是用一个 Fortran 模拟程序研究撞击——小行星或彗星砸到地表——这份代码最早来自计算早期用来模拟原子爆炸的程序，因为这两种情形的物理其实差别不大。哦，哇。[笑声] 对。早期 Fortran 的工作里有不少超酷的东西。你知道，我们现在

**[03:19 – 04:09]**
**EN:** lot about automatic differentiation these days, right? Because we write all these machine learning models and you need gradient descent and for that it's nice to have derivatives. But automatic differentiation goes back to the early Fortran days, where there was a bunch of Fortran compilers that could do this. It was messy. They could do first derivatives but not second derivatives. Like you would take the derivative of one program, you get another program, and if you tried to take the derivative of that second program, God help you. Nothing good would happen there. Yeah. It's very much computer science is a means to an end. It's like I'm not programming because I love programming. I'm using it just as a tool because it beats a slide rule, I suppose. Right. [laughter] Okay. But you loved programming then? Yes, I certainly did.
**中文：** 非常在意自动微分，对吧？因为我们写这些机器学习模型，需要梯度下降，那就最好能求导。但自动微分可以追溯到早期 Fortran 时代，当时已经有一批 Fortran 编译器能做这件事。做得很乱：能求一阶导，但求不了二阶导。你对一个程序求导，得到另一个程序；如果你还想对第二个程序再求导，那就自求多福吧，不会有什么好结果。对。这很像「计算机科学只是手段不是目的」——我编程不是因为我热爱编程，我把它当工具用，因为它总比计算尺强吧，我猜。对。[笑声] 好。但你当时是热爱编程的？是的，当然。

## 研究生院：渲染、游戏设计与 Foldit

**SECTION_NOTE**
- 本科最后一年上计算机图形学课，被渲染迷住 → 决定读博（「想一辈子做一件事，就去读那件事的博士」）。
- 进项目后发现渲染研究已成熟、剩余工作多在产业界，于是「惯性」读下去：做过游戏设计研究、CS 教育研究。
- 博士论文研究「人机问题求解」：以科学发现游戏 Foldit 为对象，看玩家如何解题、协作、与自动化工具配合。
- Foldit 的关键洞见：人类贡献大尺度的几何直觉，计算机负责「反复微调找局部能量最低点」，两者结合解出了实验室多年未解的蛋白结构。

**END_SECTION_NOTE**

**[04:09 – 04:59]**
**EN:** And then you went to grad school. Like why did you go to grad school and what did you study there? So I didn't know I was going to grad school until I took a computer graphics course my last year of undergrad and got incredibly excited about rendering and was like, I would like to do this — this is something I could do for the rest of my life. What's a way that you get to do one thing for the rest of your life? You go get a PhD in that thing. So I applied to some programs, got into them, and then as I was talking to people realized that people weren't so much doing research in rendering anymore. A lot of the field had sort of moved on. It was very mature. The remaining work was largely in industry. So I kind of inertia carried me into grad school anyway and kind of did some game design research, some computer science education research, and then ended up writing a dissertation on what you
**中文：** 然后你去读了研究生。为什么读研，研究的是什么？我其实到本科最后一年上了一门计算机图形学课才知道自己要去读研——我被渲染（rendering）彻底迷住了，心想：我想做这个，这是我可以做一辈子的事。那怎么才能一辈子只做一件事？就是去读那件事的博士。于是我申请了几个项目、也被录取了，但在和人聊的过程中发现，大家已经不太做渲染方面的研究了，这个领域整体已经往前走了，非常成熟，剩下的工作主要都在产业界。所以我就这么被惯性推着读了研，做过一些游戏设计研究、一些计算机科学教育研究，最后写的博士论文是关于所谓

**[04:59 – 05:48]**
**EN:** might call human computer problem solving, studying how players of the scientific discovery game Foldit solved problems and collaborated and sort of worked with the automated tools available there. All right. Foldit. It was the early version of "here's how we're going to solve protein folding by having people go off and try and solve protein folding as a game." Exactly. It was humans have some big picture geometrical insight of "oh, I sort of know how these amino acids tend to fold up" and "oh, what if we took this part and flipped it over here" — and at that time computers were really good at the "I'm just going to wiggle the protein a lot to find the lowest energy local optima," and those two things together were able to resolve proteins that had gone unresolved in the lab for many years. People playing this game often had no biochemistry background
**中文：** 可以称之为「人机问题求解」的题目：研究科学发现游戏 Foldit 的玩家如何解题、如何协作、如何与其中可用的自动化工具配合。好，Foldit——就是早期那个「我们靠让人把蛋白质折叠当游戏来玩，以此解决蛋白质折叠问题」的思路。没错。人类提供的是大尺度的几何直觉，比如「我觉得这些氨基酸大概是这么折的」「如果把这一块翻过去会怎样」；而当时计算机非常擅长「我就把蛋白质反复扭来扭去，找局部能量最低点」。这两者结合起来，解决了一些在实验室里多年未解的蛋白质结构。玩这个游戏的人往往完全没有生物化学背景

**[05:48 – 06:38]**
**EN:** found. So it was very successful and eventually moved on to people actually designing novel proteins in the game. But I think AlphaFold and other things have sort of eaten their lunch. Do you know if some of the data that went into AlphaFold and the like came out of Foldit? I assume AlphaFold was trained on all known structures, in which case absolutely. So there's a little bit of an educational point in that, right? You're talking about how do you get a bunch of people who do not know a domain to learn it, and how does that process work, and the kind of gamifying the education process essentially? Yeah. A lot of my work in grad school had this sort of cognitive psychology element to it, of trying to understand how people think or
**中文：** 却把结构解出来了。所以这个项目非常成功，后来还发展到玩家在游戏里设计全新的蛋白质。不过我觉得 AlphaFold 之类的东西后来把它的饭碗抢了。你知道 AlphaFold 之类的模型，训练数据里有一部分是来自 Foldit 的吗？我猜 AlphaFold 是用所有已知结构训练的，那答案是肯定的。这里面其实有一点教育学意味，对吧？你刚才讲的是：怎么让一群完全不懂某个领域的人学会它，这个学习过程是怎么发生的——本质上就是把教育过程游戏化？对。我在研究生阶段很多工作都带有认知心理学的成分，就是试图理解人是怎么思考或者

## 卡尔顿学院：疫情与翻转课堂

**SECTION_NOTE**
- 从研究生院毕业后明确了「教学是第一责任」，于是去了明尼苏达的卡尔顿学院（Carleton College）：先当面教两个学期，然后 2020 年春季起连续四个学期线上教学。
- 线上初期照搬自己高中那门「纯文本、无视频」的线上 AP CS 模式，因为要对网络条件差的学生公平；但立刻收到反馈：这种模式对一部分人非常不友好。
- 试验了翻转课堂（flipped classroom）、同步授课、拆成小组等形式。翻转课堂并非疫情产物，而是教育界长期存在的理念，只是疫情让它突然普及。
- 他自己最终的做法不是严格翻转，而是让「在一起的课堂时间」混合互动活动与少量讲授。

**END_SECTION_NOTE**

**[06:38 – 07:26]**
**EN:** learn and then how they apply those skills. Okay. And then where did you go from grad school? So I knew that I wanted to go somewhere where teaching was my primary responsibility. And so that's how I ended up at a small liberal arts college, Carleton College in Minnesota. I went there and taught two quarters in person and then it was spring 2020 and then I taught four quarters online. So this is like a hard introduction to teaching. Yes, it was challenging for me, very challenging for the students, but also involved a lot of trying new things and experimenting and different formats, which I think is an important part of succeeding in
**中文：** 学习，以及他们之后如何运用这些能力。好。那从研究生院之后你去了哪里？我知道我想去一个以教学为主要职责的地方，于是就去了明尼苏达州一所小型文理学院——卡尔顿学院（Carleton College）。我在那里当面教了两个学期，然后就到了 2020 年春季，接着我线上教了四个学期。所以这算是很hardcore的教学入门了。是的，对我很有挑战，对学生更是如此；但同时也涉及大量尝试新东西、做实验、试不同形式——我认为这是做好教育很重要的一部分。

**[07:26 – 08:16]**
**EN:** education. So how well do you feel like Carleton did at adapting to these new online constraints, and how well — forget Carleton, I guess, like your own classes — how successful do you feel like you were actually able to be at this? I think I eventually got to the point where I was fairly successful. I started out taking the model of that online AP computer science course that I had taken in high school, which was entirely text-based. There were no video lectures. You just read some stuff and you did some exercises. So I started out on that in part due to guidance of like, people were at home, not everyone had good internet connections, want to make this very accessible. But I just immediately got feedback that this really does not work for all. It worked great for me, does not work for all students, right? So then
**中文：** 你觉得卡尔顿在适应这种新的线上约束上做得怎么样？或者说先不管卡尔顿——就你自己的课，你觉得你实际上做得有多成功？我最后达到了一个还算成功的状态。一开始我照搬了自己高中学过的那门线上 AP 计算机科学课的模式：完全纯文本，没有视频课，就是读点材料、做点习题。我这么做，部分是因为当时的建议：大家都待在家里，不是每个人网络都好，希望尽可能低门槛。但很快就收到反馈——这种方式对所有人都不管用。对我很好用，但不是对所有学生都管用，对吧？于是

**[08:16 – 09:04]**
**EN:** accessible in some way, deeply inaccessible in others. Yes. So I experimented with sort of flipped classroom approaches, with synchronous courses, synchronous classes, splitting out into kind of small working groups. There's a bit of jargon that I bet not everyone understands. Can you say a little bit more about what a flipped classroom is? Yeah. So a flipped classroom is instead of the class time being when the professor would deliver a lecture, the professor prepares a lecture — a recorded video — ahead of time. Students watch that before class, and then you use class time to do exercises or discussions, something more interactive, right? And this is not a new idea that came up in COVID. People have been talking about flipped classrooms for a long time. Yes, this is a
**中文：** 在某些方面很低门槛，在另一些方面却门槛极高。对。所以我试了翻转课堂的思路、同步课程、同步课堂、拆成小组工作。这里有点术语，我猜不是所有人都懂——能不能解释一下什么是翻转课堂？可以。翻转课堂就是：课堂时间不再用来讲授，老师提前准备好一节录好的视频课，学生课前看；然后课堂时间用来做练习、讨论，做更互动的事情，对吧？而且这不是疫情才有的新想法，翻转课堂已经被讨论很久了。是的，这是教育领域

**[09:04 – 09:53]**
**EN:** long-standing idea in education that has been implemented in different ways, but it gained a sudden relevance and I think widespread adoption when classes had to move online, right? And I guess part of the point of the flipped classroom is the in-person time, right? Being able to leverage the in-person time to do things that are better than just giving a lecture. Yes. So you take the time where students are, say, passively receiving some content or seeing worked examples, and you say that does not need to be done in person, and we're going to leverage the instructor's ability to tutor someone one-on-one or to lead a discussion — things that can only happen when you have time together in the classroom. Kind of where I sort of personally ended up was just trying to make — not doing the flipped classroom, but trying to make
**中文：** 一个长期存在、以不同方式被实践过的理念；但在课堂必须搬到线上时，它突然变得高度相关，我猜也因此被广泛采用。我理解翻转课堂的关键之一在于「面对面的时间」，对吧？能够利用面对面时间去做那些比单纯讲课更好的事。对。你把学生被动接收内容、看例题的那部分时间拿出来，判断它并不需要在场完成；然后把老师的能力用在别处——一对一辅导、带着讨论，这些只有面对面同在课堂时才可能发生。我个人最后走向的做法，不是完全翻转，而是试图让

**[09:53 – 10:43]**
**EN:** the time together more of a mix of interactive things and some instruction. Yeah. Like I'm curious how much you buy the kind of argument behind the flipped classroom, cuz like my instinct about this has always been that people underrate the power of lectures — that lectures are kind of a form of performance that is actually really compelling, and like, really being in person with the person doing the lecture. Even though in some sense it seems dumb and how could you possibly need it and surely you should just record the best lecture that has been given on the topic and watch it — that with real human beings in real environments this just kind of isn't true, and there's just something more compelling about being there in person. It's not like I think the flip
**中文：** 课堂时间更多是互动活动加一点讲授的混合。对。我很好奇你对翻转课堂背后的论证买账多少——因为我的直觉一直是：人们低估了讲座（lecture）的力量。讲座其实是一种表演形式，真的很有吸引力；真的和讲的人在同一个现场，这件事……虽然从某种角度看它显得很蠢——你怎么可能需要它？你当然应该把该主题下最好的那堂课录下来看就行了——但在真实的人、真实的环境里，这并不成立，现场就是有种更打动人的东西。我不是说翻转课堂

**[10:43 – 11:32]**
**EN:** classroom idea is totally wrong, but I do feel like it — like the whole thing of "oh there's just the passive lecture" is just missing something about human psychology there. Yes. So I would tend to say that lines up with my experience: that there is something about having a person, as you say, perform live in front of you that I think has a sort of focusing effect on your attention. And because it is live, I think you're more likely to try and take notes, which I think is good for people's understanding — which is not to say you couldn't do that when you're watching a video in your dorm room, but I think it's less likely. And also I think a solid hour of someone just talking at you starts to lose the engagement and become counterproductive. So another bit of jargon: active learning is very important
**中文：** 这个想法完全错，但我确实觉得，把讲座一概说成「被动的」这一整套说法，漏掉了人类心理上的某些东西。是的。我倾向于说这符合我的经验：让一个人当着你「现场表演」，我认为会有一种聚焦注意力的效果。而且正因为是现场，你更可能去记笔记——我认为这对理解有帮助。这不是说你在宿舍看视频就不能记笔记，只是可能性更低。另外，一个人对着你连着讲整整一小时，参与感会开始流失，反而起反作用。再说一个术语：「主动学习」（active learning）非常重要，

**[11:32 – 12:21]**
**EN:** for these sort of in-person things, where throughout the lecture I want to stop and pose a question and have people talk to their neighbors, or have people stop and do a little problem on their own to check their understanding, things like this. By the way, note-taking is another great example of a super weird and also strangely effective learning technique, where like just being in the classroom and taking notes and then if you walk out you just like light them on fire, like you never look at them again. There's actually, as I understand it, pretty good evidence that this actually helps retention in a serious way even though the notes themselves are totally useless. Having to process things and then sort of distill them down to something that you write down — and then some, I agree — the evidence seems to be
**中文：** 对这种面对面的教学尤其重要：讲到一半我会停下来问一个问题，让大家和邻座讨论，或者停下来自己做一道小题检查理解，诸如此类。顺便说，记笔记是另一个绝佳例子——一种非常奇怪却又出奇有效的学习技巧：你人在教室里记了笔记，走出门就可以把它们一把火烧了，再也不会看一眼。但据我理解，有相当好的证据表明，这确实能显著帮助记忆保持，即便笔记本身完全没用。你得先处理信息、再把它浓缩成写下来的东西——我也同意——证据似乎是

**[12:21 – 13:10]**
**EN:** that the act of writing it down helps set it in your memory in some qualitatively different way than just hearing it, even if you understood it, right? And apparently writing is better than typing for this — maybe I'm getting that, this is what I thought was true about the research, although it's not like I remember the study or anything. That sounds familiar to me. I would say my own experience in the classroom is it's maybe less about the typing per se than someone having a screen with all the information and distraction that humanity has created sitting between them and the presenter — that tends to undermine one's ability to pay attention. That seems very believable. This is also why I have generally tried to avoid teaching in computer labs, which is
**中文：** 写下来这个动作，会以一种质上不同的方式把它刻进记忆里，而不只是听见——哪怕你当时听懂了。而且据说手写比打字效果更好——也许我记得不准，这是我对相关研究印象中的结论，不过我也没记住是哪篇论文。这个说法我听着耳熟。就我自己的课堂经验而言，关键也许不在于打字本身，而在于人面前多了一块屏幕——人类创造出来的一切信息与干扰夹在他和讲者之间——这会削弱注意力。这听起来很可信。这也是我一般尽量避免在计算机实验室里上课的原因，

**[13:10 – 13:58]**
**EN:** something that people often do in CS courses, but I just can tell as soon as there's a screen in front of people, like 50% of people — even if they want to pay attention — they just can't. Yeah, exactly. This echoes a little bit my own experience just like teaching my kids how to program. One of the things I did a lot of was have them think about programs on paper, right? In fact, one of the things I conned my kids into thinking was like an acceptable distraction like when food arrived at a restaurant was like I would write a little Scheme program on a piece of paper with like obfuscated names and then they would have the puzzle of trying to figure out like what did flub do and [laughter] somehow I convinced them this was like an acceptable way to spend time. But I do think like the thing of like talking
**中文：** 而 CS 课里人们常常这么干。但我一眼就能看出来：只要人面前有一块屏幕，大概 50% 的人——哪怕他们想专注——就是做不到。对，完全同意。这也呼应了我自己教我孩子编程的经验。我做得很多的一件事，就是让他们在纸上思考程序，对吧？事实上，我骗孩子们把一件东西当成「可接受的消遣」：在餐厅等菜上来的时候，我会在纸上写一小段 Scheme 程序，把名字都混淆掉，然后他们就有一个谜题要解——「flub 到底干了什么」。[笑声] 不知怎么就说服了他们，这算是消磨时间的正当方式。但我确实认为，和他们聊

**[13:58 – 14:47]**
**EN:** to them about what a program means, and starting out by being like, I'm going to write down on the board or on a piece of paper, here's an expression, what does this evaluate to? I think the moment you gave them a computer to type it in and try to evaluate it, they were playing the game of getting the computer to do the thing, and not thinking about the question of what is actually happening. And I think there were ideas you could get across much more easily when you got the computer out of the way. Yeah. And there is definitely a thing that people just learning programming will tend to do, which is: this is arcane instructions for the machine, I will perturb it arbitrarily until it does what I want. And this is very easy to do when it's on a screen and you can run it. But if I ask you to write out a
**中文：** 一段程序是什么意思的时候，一开始就是这样：我在黑板或纸上写一个表达式，问它求值等于什么？我认为一旦给他们一台电脑去敲进去、跑出来，他们就在玩「让电脑做成一件事」的游戏，而不再思考「究竟发生了什么」这个问题。有些事情，把电脑挪开之后传递起来容易得多。对。而且刚开始学编程的人确实会倾向于这么做：这是给机器的神秘指令，我就随便乱改，直到它做出我想要的结果。在屏幕上能直接跑的时候，这样做太容易了。但如果我让你把一段程序

## 反馈循环与掌握式学习

**SECTION_NOTE**
- 疫情期间的大实验之一是「自动反馈」：多选自动判分、填空、自动判题作业，目标是缩短「交作业 → 拿反馈」的延迟。
- 学习离不开反馈；但传统模式下批改要一两周，学生早已往前走、甚至不看反馈。
- 引入「掌握式学习」：同一知识点可无限次重试，取最好成绩，直到真正做对；同时用不断变化的题序／选项顺序阻止硬刷。
- LLM 生成即时反馈潜力很大，但要收窄场景（如代码风格而非议论文），并警惕误导性误报。

**END_SECTION_NOTE**

**[14:47 – 15:37]**
**EN:** program on paper and then decide when you think it's correct, it's more likely to force you to think about what it's actually doing. For sure. Okay. So you were at Carleton during this very complicated and disruptive COVID pandemic. You did a bunch of experiments and learned things. What happened when you got back to the classroom and people could be there? Are there things that you took away from that experience that you kept? Like what was persistent that you learned there? Yeah, I think one of the persistent things was I just find it very useful to have a lecture recording. I think this varies by institution. I've heard from other instructors that if they record the lecture, no one shows up to class because they can watch it. This wasn't the case at Carleton. Students wanted to come to class. And I tried to make being in class with this sort of
**中文：** 写在纸上、然后自己判断什么时候它是对的，这更可能逼你去想它究竟在做什么。确实。好。所以疫情期间你就在卡尔顿，经历了这段非常复杂、充满打断的时期。你做了很多实验、学到不少东西。当你回到能面对面上课的教室时，发生了什么？有没有哪些东西是你从那段时间里保留下来、一直沿用的？哪一些是持续有效的？我认为持久保留下来的一点是：我确实觉得有一份课堂录像非常有用。我想这因学校而异。我听别的老师说，他们一旦录课就没人来上课了，因为可以直接看录像。在卡尔顿不是这样，学生愿意来上课。而我也努力让「来上课」因为这套

**[15:37 – 16:25]**
**EN:** interactive stuff actually useful. But — it might be institution dependent. It also might be lecturer dependent. This is fair. [laughter] This is fair. The classrooms at Carleton were not equipped generally with video equipment. So I was carrying around a webcam on a tripod to each of my classes and plugging into my laptop and recording the lectures and posting them online. And as I would get questions throughout the semester like, oh, I have this track meet or this obligation, I have to miss this class, what should I do? And if I have a recording, it's like, well, it's there, you can watch it. Or someone asks a question, I can send them a link with the timestamp of the lecture — here's where I explain this thing. So that carried over. I think I may have arrived at this
**中文：** 互动内容而真的有用。但这也可能因学校而异，也可能因讲授者而异。这话有理。[笑声] 有道理。卡尔顿的教室一般没有配视频设备，所以我拖着一个架在三脚架上的网络摄像头去每一堂课，插到笔记本上录课，再传到网上。学期中不断有人来问：我要参加田径赛／有别的事，得缺一次课，怎么办？如果有录像，答案就是：在那儿，你可以自己看。或者有人提问，我可以发一个带时间戳的链接——「我就是在这一段解释的」。所以这一点被保留了下来。我想我即使没有经历

**[16:25 – 17:15]**
**EN:** even without COVID lockdown. But during that I experimented a lot with sort of automated feedback in various ways. So weekly quizzes that were multiple-choice and auto-graded, or different sorts of fill-in-the-blank kind of things, different autograding software where students could submit homework and get immediate feedback on whether it passed tests, that sort of thing, and carried that forward into my courses and found it — because getting feedback on your work is an essential part of learning and I was always dissatisfied with: okay, you do the homework, you turn it in, a week or two later an instructor or TA has graded it and you give back some feedback, but at that point you've moved on and you may not
**中文：** 疫情封控，也会走到这一步。但在疫情期间，我在各种形式的自动反馈上做了很多实验：比如每周一次的多选自动评分小测，或者各种填空形式；各种自动判题软件，学生交作业后可以立刻知道是否通过测试；诸如此类。这些都被我带进了自己的课程，而且我发现——因为得到对自己作业的反馈是学习中不可或缺的一环——我一直对下面这件事不满意：你做了作业、交上去，一两周后老师或助教批改完，给你一些反馈；但那时候你早就往下走了，你可能

**[17:15 – 18:05]**
**EN:** even read the feedback you get. Also that incorporated a technique that is sometimes called mastery learning, though I didn't do it in its fullest extent. But the idea is you have to demonstrate sort of mastery or competence at a thing before you can move on, where you can attempt it any number of times, and you keep getting feedback and you sort of reattempt until you actually have kind of gotten it right. And so in some of this automated assessment I let me take more of that approach. Interesting. My first instinct about the mastery thing is I would have done very poorly without — when I took math classes in college, because I felt like the experience of taking high-end math classes was like I was holding on, barely keeping up, trying to understand what happened, and then 6 months later
**中文：** 连反馈都不会看。这里面还融进了一种有时叫「掌握式学习」（mastery learning）的方法，虽然我没有做到最彻底。它的思路是：你必须在某件事上展示出掌握或胜任，才能往下走；你可以尝试任意多次，持续获得反馈，反复重来，直到你真的把它做对。所以我在一部分自动测评里采用了这种思路。有意思。我对「掌握式学习」的第一反应是：如果当年大学数学课用这种方式，我大概会表现得很糟——因为我觉得上高阶数学课的体验就是勉强吊着、将将跟上、努力搞懂发生了什么；然后六个月后

**[18:05 – 18:54]**
**EN:** someone else was taking the class and asked me about it, be like, oh yeah, I know how that works. But like, just somehow I couldn't quite get my arms around it at the time, but somehow just the passage of time after, and then you look back you're like, oh yeah, I know how that fits together. But I'm probably under-imagining — probably I could have demonstrated some local mastery. This is like, I think the demonstration of mastery and also feeling really confused are probably like consistent experiences. Yeah, I think this is often applied in a sort of maximal extent with much younger students. Like in elementary school math class, it's sort of self-paced in a way where the class might be at different points through the material, and you have to master addition or the long division algorithm before you move on to the next unit. I think as you get higher level, you start needing to apply this
**中文：** 别人上这门课来问我，我就说：哦对，我知道那是怎么回事。但当时我就是抓不住它；就是时间过去之后，回头一看，你才觉得「哦，我懂它是怎么拼起来的」。不过我很可能是低估了自己——大概我当时也能展示出某种局部的掌握。我认为「展示掌握」和「感到极度困惑」大概本来就是经常并存的体验。对，这种做法常常在年龄小得多的学生身上被用到极致。比如小学数学课，某种程度上是自定进度的：全班可能处在材料的不同位置，你必须先掌握加法或长除法算法，才能进入下一个单元。我认为到了更高阶段，你就需要用更有针对性

**[18:54 – 19:44]**
**EN:** in more targeted ways, and that the flexibility is not there to the same extent in, say, a college course. Did you actually do the thing of having people stay on older topics until they demonstrated mastery, or is it more like there's a thing that you should do which is keep on iterating until you pass, but that happens at a fixed time and you kind of have to do it at a particular point in time in the semester. Yeah. It would not have worked for people to progress through at different rates. Not least of which because students can procrastinate — it is a thing people do. And I think it would have been a disservice to let people pile up all the work until the very end. So you do have to give people deadlines throughout for
**中文：** 的方式去应用它，而在大学课程里，那种灵活性并不存在。你实际上真的让人停留在旧主题上直到展示出掌握吗？还是说更像是：确实有一件应该做的事——不断迭代直到通过——但它发生在固定时间点，你必须在学期中某个特定时点完成？对。让人按不同速度推进是行不通的。更何况学生会拖延——这是人会做的事。而且我认为让人把所有作业堆到最后一刻，是一种失职。所以你必须全程给大家设截止时间，

**[19:44 – 20:33]**
**EN:** their own good, and force people to move on. And so it was a model of: you have this short quiz to do this week, you can attempt it any number of times, but you're just going to get the best result of the times that you take it. And the questions are set up in a way such that it's pretty annoying to brute force. Like the order of them keeps changing, the order of the answers keeps changing. So it's just going to be faster if you actually try and understand all of it and then get 100% that way. Have you thought much about whether in the modern world some of this feedback — the kind of instant feedback that you think would be more useful for students — can be generated by LLMs? Yes, I think there is quite a lot of potential for that, particularly because when you have say a more
**中文：** 为了他们自己好，也逼着人往前走。所以那套模式是：这周有一份小测要做，可以尝试任意多次，但取你所有尝试里的最好成绩。题目的设置方式让人很难硬刷：题目顺序一直在变、选项顺序也一直在变。所以如果你真的试图把它全部理解、然后拿到 100%，反而会更快。你有没有认真想过，在当下这个世界里，这类反馈——你认为对学生更有用的那种即时反馈——能不能由 LLM 来生成？能，我觉得潜力相当大。特别是当你有一个更

**[20:33 – 21:21]**
**EN:** structured thing to narrow the focus of the LLM. So for example, feedback on code style as opposed to an essay. I think I see a lot more promise in — in addition to some automated grading of test cases and maybe some linter to give students feedback of like, you need to follow these rules — some additional kind of code style pass I can see being very useful. That being said, in my experience, there's also plenty of false positives of LLMs giving feedback that is misleading. And so I think at the very least you would want to frame it
**中文：** 结构化的东西来收窄 LLM 的关注范围时。比如，针对代码风格的反馈，而不是针对一篇论文。我觉得更有前景的是——除了对测试用例做自动判题、以及用 linter 告诉学生「你得遵守这些规则」之外——再补一层代码风格检查，我认为会非常有用。话虽如此，就我的经验而言，LLM 也会给出大量误报式的、具有误导性的反馈。所以至少你得把它

## 开创「开发者教育者」这个岗位

**SECTION_NOTE**
- 从明尼苏达搬到布鲁克林，恰好碰上 Jane Street 在招「教育者＋程序员」的奇怪组合岗位。
- Jane Street 长期重视教育：交易知识没人在入职前就会，技术栈（自有语言、自有版本控制、自有编辑器）也足够「怪」，因此需要长期投入教育。
- 岗位设计成 50/50：一半写代码，一半做教育（直接授课、做课程，以及培养其他人成为更好的老师）。
- 「教学者必须是实践者」是刻意选择：不在同一个生态里做同一件事，教不出有说服力的内容。
- 这个岗位很难招：教学经验多的人多在学术界且不愿离开；同时既是优秀教育者、又是可信的 Jane Street 工程师，这个交集很小。

**END_SECTION_NOTE**

**[21:21 – 22:11]**
**EN:** carefully to students, at least, or find ways to really reduce the rate at which it's kind of leading them astray. Sure. Somehow you ended up here. How did that happen? Right. So I was living and teaching in Minnesota, and my brother and his wife had moved to Brooklyn. She's from Bay Ridge, and I decided that I wanted to live near them — my brother and I are close. So I decided to move to Brooklyn. Was not going to be able to keep teaching in Minnesota while living in Brooklyn. And it was very fortunate that at that exact time, Jane Street was trying to hire for this weird educator-programmer combo. I had just assumed like there were some things I liked about academia, but I was ready to
**中文：** 向学生说清楚，或者想办法真正降低它把人带偏的概率。明白。后来你不知怎么就来到这里了。这是怎么发生的？是这样：我当时在明尼苏达生活、教书，而我弟弟和他太太搬去了布鲁克林——她来自湾脊区（Bay Ridge）。我很想住得离他们近一些，我和弟弟关系很好，所以我决定搬到布鲁克林。而住在布鲁克林就不可能继续在明尼苏达教书。非常幸运的是，就在那个时候，Jane Street 正在招这个很奇怪的「教育者＋程序员」组合岗位。我原本的想法是：学术界有一些我喜欢的地方，但我已经准备好

**[22:11 – 22:59]**
**EN:** try something new and didn't really want to go through the academic job market. So I figured I would go be a software engineer somewhere. But it's been amazing to continue doing education stuff in addition to doing some programming. Yeah. And it's maybe worth saying a little bit about the idea that we had in creating this job, right? We really wanted — I mean, to take a step back, teaching has been an important part of what we do at Jane Street for a very long time. In part this is because we do some weird stuff that we've not done so much in the outside world. Some of that is just subject matter stuff of like, nobody kind of comes in knowing much about trading. And so there's a big effort in teaching people to understand how to think about trading. And then also our tech stack is in a bunch of ways weird. And so there's a lot of things that we want to educate
**中文：** 尝试新东西，也不太想走学术求职市场那条路。所以我当时的想法是：那就去某处当个软件工程师吧。但结果是——除了写点代码，还能继续做教育，这件事太棒了。对。关于我们设立这个岗位时的想法，也许值得说一说。我们真的很想——退一步说，教学长期以来一直是 Jane Street 很重要的一部分。部分原因是我们做的事情有些很「怪」，外面做得并不多。有些纯粹是主题层面的：没有人进来就懂交易，所以需要花很大力气教人怎么去理解交易。另外我们的技术栈在很多方面也很怪，所以有很多东西需要我们教大家，

**[22:59 – 23:49]**
**EN:** people about to understand the specifics of the programming language and the environment and the tools, a lot of which are very different from what you see on the outside. And so we've spent a lot of energy on education for a long time now. And at some point we're like, it's great to have people who are on the ground involved in things, diving in and doing the educational work, but maybe we could get some people who have some expertise in the area and have actually done it for a material period of time and try and leverage that effectively. So well, let's just actually create a job that's just for this. And it seemed clear to us that we wanted the people who were doing the teaching to also be people who were practitioners, right? Again in part because there's lots of things that are unique about our environment, and if the people involved don't directly experience and work in
**中文：** 让他们理解这门编程语言、这套环境和这些工具的细节——其中很多和外面看到的东西差别很大。所以我们在教育上已经投入了大量精力、持续了很久。到某个时点我们想：让一线的人参与进来做教育工作很好，但也许可以找一些在这个领域有专长、并且已经实打实做过相当一段时间的人，把这部分能力更有效地用起来。那好，就干脆为这件事专门设一个岗位。而且我们很明确：做教学的人本身也必须是实践者。同样，部分原因在于我们的环境有很多独特之处；如果参与的人并不直接身处

**[23:49 – 24:38]**
**EN:** the same ecosystem, they're just not going to be effective or compelling teachers there. And so we designed this as a kind of 50/50 split, where the idea is you're going to spend half your time programming and half your time focusing on educational work. Some of which is going to be directly teaching classes or creating curriculum, and some of which will be helping other people grow as teachers — because we actually don't want there to be a small number of developer educators who do all of the teaching work, but to help grow the practice and make people better at it. I guess the other thing that I find interesting and a little frustrating about your description is that this putting up this job ad did not at all work in the way I wanted it to. [laughter] Which is to say I just sort of thought this was an obviously awesome job and we will advertise it and great candidates will fall from the sky
**中文：** 同一个生态，他们就不会是有效、有说服力的老师。所以我们把它设计成一种 50/50 的分配：一半时间写代码，一半时间专注教育。其中一部分是直接上课、开发课程，另一部分则是帮助别人成长为更好的老师——因为我们其实不希望有一小撮「开发者教育者」包办所有教学工作，而是要培育这门手艺，让大家做得更好。关于你的描述，我还有一点觉得既有意思又有点沮丧：当初把招聘启事挂出去，完全没有按我想要的方式起作用。[笑声] 也就是说，我原以为这显然是份很棒的工作，我们一发广告，优秀候选人就会从天而降。

**[24:38 – 25:27]**
**EN:** because it's a cool and unique job opportunity, and it turns out like if we had put this out like 3 months differently or something we would have not gotten you at all. And in fact, as an ongoing thing, it's actually been pretty hard to find the right people for this spot. I think it's less the case that people in general — people don't fall from the sky. I think hiring people is really hard. Yes. And I think that this job is, as you say, very cool, but also very unusual. And the kind of person that would be looking for this job is also therefore kind of unusual. In particular, most people with a lot of teaching experience are in academia, and most people chose academia because they are passionate about what they get to do
**中文：** 因为这是个很酷、很独特的职业机会。结果发现，如果我们晚三个月、或者换个方式发这个启事，我们根本招不到你。而且事实上，作为一件持续进行的事，要找到合适的人真的挺难。我想与其说是「人不会从天而降」，不如说：招人真的很难。是的。而我认为这份工作正如你所说，非常酷，但也非常不寻常。因此会来找这份工作的人，本身也不太寻常。特别是：大多数有大量教学经验的人都在学术界，而多数人选择学术界是因为他们热爱自己

**[25:27 – 26:16]**
**EN:** there and often are not looking to leave academia and work at a place in industry. The job is also a kind of unusual marriage of skills. Like if I'm teaching courses at a university, I'm not necessarily doing a lot of day-to-day software engineering, and I may or may not even be interested in that being a significant fraction of what I do, right? And we really want, at least in the ideal case, to find people who are really good educators, who have a love for the craft and have spent a lot of time doing it, and really think hard about what kind of things might you do and want to experiment in the space and learn how to be really better, and are also just like fully credible Jane Street software
**中文：** 在那里能做的事，往往并不想离开学术界去产业界某个地方工作。这份工作还是一种很不寻常的技能组合。比如，如果我在大学里教课，我未必会做大量日常的软件工程；甚至我可能对「让软件工程占我工作中很大一块」并不感兴趣，对吧？而我们至少在理想情况下，真的想找到这样的人：非常出色的教育者，热爱这门手艺、投入过大量时间，会认真思考「可以怎么做」、愿意在这个领域做实验、想变得更好；同时又是完全过硬、可信的 Jane Street 软件

**[26:16 – 27:05]**
**EN:** engineers. And that's the intersection of two things where that intersection is relatively small. It's maybe worth saying that we're really excited with how having people in this role has turned out. There's some amount of taking some internal people and kind of converting them into this role, which is another path. But we're also excited to get more people from the outside to do this, and I think there are just more and more domains where we want it. Maybe it's worth talking through some of the other spots that we are trying to find developer educators for. Yeah. One thing I would add about the role itself is that I think one reason it has been successful — despite Jane Street having been doing a lot of education before this role existed — is having someone where that is a sort of first-class focus
**中文：** 工程师。这就是两个集合的交集，而这个交集相对很小。也许值得说的是：让这个岗位上有人，效果让我们非常满意。其中一部分做法是把内部的人转岗到这个角色，这是另一条路径。但我们也希望从外部招到更多人来做这件事，而且我认为需要我们这么做的领域只会越来越多。也许值得聊聊我们正在为哪些其他方向寻找「开发者教育者」。好。关于这个角色本身，我想补充一点：它之所以成功，一个原因就在于——尽管在这个岗位出现之前，Jane Street 已经做了大量教育工作——有了一个人把这件事当成

**[27:05 – 27:55]**
**EN:** of their job, as sort of a step change in how they're going to be able to engage and the sustained attention on education. But yeah, somehow there's just more and more stuff we need to teach. [laughter] And not just to new people who need to learn OCaml, but it turns out we're changing the OCaml language. And everyone at the company, no matter how long they've been [laughter] here, needs to learn about it. There are all these new AI tools. We want to teach everyone how to engage with these effectively. And it's sort of the case that the more we have put into this and expanded and refined it, the more places we go like, oh, we should make that better, too. And so the kind of
**中文：** 自己工作的第一优先级，这会带来一种台阶式的变化——他们能以不同的方式投入，并对教育保持持续的关注。但确实，我们要教的东西就是越来越多。[笑声] 不只是要教需要学 OCaml 的新人；结果我们还在改动 OCaml 这门语言本身。公司里的每个人，无论来了多久，[笑声] 都得学它。还有这些新出现的 AI 工具，我们想教每个人怎么有效地使用它们。而且情况似乎是：我们投入得越多、扩展和打磨得越深，就发现越多地方想「哦，这个也该做得更好」。

## 越来越多的东西要教：OxCaml、Python 与 ML 教育者

**SECTION_NOTE**
- 对「专注教育专长」的需求只增不减：OxCaml 教育者岗位、机器学习教育者岗位，以及通用型开发者教育者。
- 他担心「人被困在自己的工具里」：语言少的时候大家随处可去；语言一多就会分层，各自只精通一种。他更希望公司里只有「软件工程师」，而不是「OCaml 程序员」「Python 程序员」。
- 未来形态可能类似设计师嵌入各团队：教育者嵌入 AI 助手团队等，既服务该方向的教育需求，也让教育者积累多样化的技术经验，而不是都挤在同一个角落。

**END_SECTION_NOTE**

**[27:55 – 28:45]**
**EN:** appetite for this kind of focused educational expertise seems to have only grown, right? And so on the OCaml side, we've posted this OxCaml educator spot for people who have a strong PL background and are also excited about teaching, and we've actually had some good luck there. We're still looking for great people to do a kind of machine learning educator role, where focusing on — you know, we're doing all this exciting new generation and training of ML models, and people who understand that space and can teach more people to do it is a very valuable thing. And just a kind of the general version of this role that hits all sorts of things like you mentioned: having to teach everyone how to use the exciting new corners of OCaml as they come into
**中文：** 这种对「专注的教育专长」的需求，看来只会增长，对吧？在 OCaml 这条线上，我们挂出了 OxCaml 教育者的岗位，找那些编程语言（PL）背景很强、同时热心教学的人，在这一块我们运气还不错。我们还在找优秀的人来做机器学习教育者的角色——我们正在做各种令人兴奋的新模型生成与训练，而理解这个领域、并且能教更多人来做事的人，价值极高。还有就是这种角色的通用版，覆盖面很广，就像你说的：每当 OCaml 出现新的、令人兴奋的角落，就得教所有人怎么用。

**[28:45 – 29:34]**
**EN:** existence is one thing. Also, we now do a bunch of Python, right? And we kind of want everyone to know something about Python. In fact, one of the things I worry about is people getting captured by their tools. One of the things that's nice about having a small number of programming languages is you can kind of go anywhere into any codebase and do stuff. And once you have like two or three or four programming languages, there's a kind of natural striation where people get good at the one thing. And I'd really love to be more in a world where there are no OCaml programmers and Python programmers — they're just software engineers, and they know how to use many tools and can figure out what's the right tool to use given the particular circumstance. But for some of that we actually have to teach people. There are people who have been here for a long time who — I mean everyone knows some Python, but there are lots of people who don't, who aren't any good at
**中文：** 这是一件事。另外，我们现在也大量使用 Python，对吧？我们希望大家多少都懂一点 Python。事实上，我担心的其中一件事，就是人被困在自己的工具里。语言数量少的一个好处是：你可以走进任何代码库做事情。而一旦有两三种、四种语言，就会出现一种自然的分层，人们各自精通其中一种。我非常希望能更多地活在这样的世界里：没有「OCaml 程序员」和「Python 程序员」，只有软件工程师；他们懂得使用多种工具，并能在具体情境下判断该用哪个工具。但要做到这一点，有一部分确实得教。这里有些人待了很久——大家多少都懂点 Python，但也有很多人不

**[29:34 – 30:23]**
**EN:** it, and there are real things to learn to be good at it. So that's another corner where I think there's more teaching. Plus we also invent our own programming languages in spots and teach people about that, yeah, and like a million other things. So yeah, I do think that there's just more surface area to cover, more technology for people to understand, and therefore more opportunities to create real value by teaching people stuff. Yeah. And to say another thing about this sort of general dev educator role, I think a model that I feel like we're heading toward, and that sort of mimics some of the ways that, say, designers have been incorporated into different teams and spots throughout the firm. I think that may be where we're headed for educators as well. So I mentioned AI tools. I think
**中文：** 太行，而要真正做好它是有实打实的东西要学的。所以这是另一个需要更多教学的角落。再加上我们在某些地方还会自己发明编程语言，也得教别人；还有很多很多其他事情。所以是的，我认为需要覆盖的「面积」就是更大了，需要人们理解的技术更多了，因此也多了很多「靠教别人东西来创造真实价值」的机会。对。关于这种通用型开发者教育者角色再说一点：我觉得我们正走向一种模式，它有点类似设计师被嵌入到公司各个团队和位置里的做法。我认为教育者大概也会往这个方向走。我提到过 AI 工具，我

**[30:23 – 31:11]**
**EN:** think we would love to have an educator sitting on our AI assistance team to focus on the education work that they're doing, and I think more and more places will want an educator embedded there for all the teaching materials that need to come out of that part of the world. Right. And I actually feel like there's two benefits there. One is the thing you're saying of like, there are education needs that are focused on what's happening in a particular area. And then also I think you want the people who are doing the education work to have a variety of different technical experiences, so that they have sort of more of a body of experience. If you poke them all in the same corner of the firm, they'll kind of have all the same context and that's just less of a robust foundation. Yeah. Let's pivot for a second to talk about the technical work that you do. So
**中文：** 觉得我们会很希望有一位教育者坐在 AI 助手团队里，专注他们那部分的教育工作；而且我认为会有越来越多的地方希望嵌入一位教育者，因为那个方向需要产出大量教学材料。对。我其实觉得这里有两个好处。一是你说的：教育需求会聚焦在某个特定方向上发生的事情。二是：我认为应该让做教育工作的人拥有多样化的技术经历，让他们有更厚实的经验积累。如果你把他们全塞进公司的同一个角落，他们的背景就都一样了，那是一种更不牢靠的基础。对。我们稍微换个话题，聊聊你做的技术工作。

## 编辑器团队，以及什么是一个「feature」

**SECTION_NOTE**
- 他在 tools and compilers 组下的 editors 团队：维护公司内部大家写代码用的文本编辑器（VS Code、Emacs、Neovim）以及相关服务，如代码索引服务、OCaml language server。
- 他早期做过 feature 管理软件 Iron 的一个扩展，让「把工作拆成多块、按关系链组织、分别过评审」这件事从手工繁琐变成顺手的工具。
- 在 Jane Street，「feature」大致介于外界的 commit 与 PR 之间。
- 25 年来他们走出了一条和外界的开发工具很不一样的「平行宇宙」路线：Iron 在「堆叠式 PR（stacked PRs）」等基础能力上非常好，但在编辑 diff、来回搬动等环节又很差——同一个大目标，技术路径不同，最终得到的能力集合完全不同，并由此塑造了整套工程文化。

**END_SECTION_NOTE**

**[31:11 – 32:01]**
**EN:** like where in Jane Street's technical organization are you, and what kind of engineering problems do you think about there? Yeah, so I'm on the editors team within the tools and compilers group. So our team maintains the text editors that folks at Jane Street use to write code — VS Code, Emacs, Neovim — as well as some related services like the code indexing service that we have, the OCaml language server. And I have sort of worked across various things in the dev tools space. I started out working on an extension to our feature management software Iron, to make it much easier to split up work into different pieces of code
**中文：** 你在 Jane Street 的技术组织里处于什么位置，在那里思考什么样的工程问题？我在 tools and compilers 组下面的 editors 团队。我们团队维护 Jane Street 同事写代码用的文本编辑器——VS Code、Emacs、Neovim——以及一些相关服务，比如我们自己的代码索引服务和 OCaml language server。我在开发者工具这块做过不少不同的事情。一开始我做的是公司 feature 管理软件 Iron 的一个扩展，让「把工作拆成不同块的代码

**[32:01 – 32:50]**
**EN:** review and organize it in a way that was sort of awkward and manual before, but giving people a nice tool to be like, take this and split it over here and arrange it in this nice chain of relationships that all get reviewed separately. Right. It's maybe worth saying when we say the word feature at Jane Street, we mean something that's roughly analogous to — sometimes analogous to commit and sometimes analogous to PR in the outside world's dev tooling. I think the thing that really strikes me about all of the tooling we've built in this code review and feature management area is just, it's actually made a very different set of choices. We've been off on a 25 year alternative universe adventure of building development tools that just look pretty different. And if you
**中文：** 评审」变得容易得多——过去这件事既别扭又全手工。现在给人一个好用的工具，你可以把这块拆出来、挪到那边，排成一条漂亮的关系链，每一环都单独过评审。对。也许值得说明一下：在 Jane Street，我们说「feature」这个词，大意相当于外面开发工具里的 commit，有时又相当于 PR。我觉得我们在代码评审和 feature 管理这块造的所有工具，最让我有感触的一点是：我们其实做出了非常不同的一组取舍。我们花 25 年走上了一条「平行宇宙」式的开发工具之路，做出来的东西看起来就是很不一样。如果你

**[32:50 – 33:39]**
**EN:** look at Iron, which is the tool that's responsible for code review and releasing features and all of that, it's like way better than everything in the outside world and also way worse, depending on exactly which thing you want to look at. And the thing you're talking about, this having nice ways of carving up and breaking down a larger collection of changes into a sequence of smaller changes, is a good microcosm of — first of all, it has really good support for what we sometimes call stacked PRs in the outside world. And that's built in, in a really nice foundational piece. And also the process of really editing diffs and moving things back and forth was awful — like slow and painful. And the tooling wasn't very good. And you would have been much happier using, I don't know, the Emacs Magit
**中文：** 看 Iron——负责代码评审、发布 feature 等等的那套工具——它比外面所有东西都好得多，同时在某些具体方面又差得多，取决于你想看哪一点。而你刚才说的「把一大堆改动优雅地切分、拆解成一系列更小改动」是个很好的缩影：首先，它对我们在外面叫「堆叠式 PR」的做法支持得非常好，这是内建在一套很漂亮的基础能力里的。但另一方面，真正去编辑 diff、来回搬动东西的过程却很糟糕——又慢又痛苦，工具也不好用。你甚至会更愿意用——比如，Emacs 的 Magit

**[33:39 – 34:28]**
**EN:** extensions or whatever in git than using the stuff that we've had. It's just interesting that there are lots of different technical paths you can take towards the same big picture goal and end up with really different sets of choices and really different functionality as a result. Yeah. And there's a whole engineering culture that flows from that. How you do code review, how you think about giving people feedback on their work is entirely shaped by the underlying technical system, right? And actually I think this comes to the question of why does Jane Street have an editors team? Exactly. Like, you know, text editors — can't you just use one of them? And I think it's just the case that editors are much more central to how we work and how we review code than you might imagine.
**中文：** 扩展之类的东西，也不愿意用我们已有的那套。有意思的是：通往同一个大目标可以有很多不同的技术路径，最后会得到非常不同的取舍组合，以及由此而来的、非常不同的功能。对。而且由此会流淌出一整套工程文化。你怎么做代码评审、怎么看待「给别人的工作提反馈」，完全被底层的技术系统塑造，对吧？其实我觉得这就引到了那个问题：Jane Street 为什么需要一支 editors 团队？没错。文本编辑器——你用市面上某一个不就行了？我想实际情况是：编辑器在我们的工作方式、以及代码评审方式里的中心程度，远超你想象。

## 编辑器作为软件工程师的「主场」

**SECTION_NOTE**
- Jane Street 把文本编辑器当成工程师的 home base：代码评审、版本控制等所有交互都发生在编辑器内，全部可键盘导航，不需要在多个应用／页面之间跳。
- 因为「不走寻常路」（不用 git 用 Iron 等），反而必须有一支团队把各种集成做进编辑器，让人真的能「住在里面」。
- Jane Street 明显不是 web-first 的组织：与把所有交互塞进浏览器的大厂不同，这里改代码、理解代码、讨论代码都发生在编辑器里。
- 早期设计选择：对改动的反馈以特定格式写在编辑器里（称为 CR），而不是去某个网页 UI 里给别人的 PR 留言；因为人在编辑器里，有时干脆直接帮对方改掉，而不只是留评论——这对外来者会感到「不卫生」，但它是另一种协作模态。

**END_SECTION_NOTE**

**[34:28 – 35:15]**
**EN:** It's worth saying a little bit how are editors here different than maybe people have seen in the outside world, in terms of the role that they play in our software development process? Yeah. So there are a few different things. One is at a fundamental level, Jane Street has approached the text editor as the software engineer's home base. All the interactions with Jane Street's code review and version control and all these other systems live within the editor. You do everything there. It's all easily keyboard navigable, and you're not jumping between different applications or pages. And so that means that because Jane Street does a lot of weird
**中文：** 值得说一下，就编辑器在你们软件开发流程中扮演的角色而言，这里的编辑器和外面大家见过的有什么不同？好。有几点。首先在根本层面上，Jane Street 把文本编辑器当作软件工程师的「主场」。与代码评审、版本控制以及其他所有系统的交互都发生在编辑器里，你在这里做一切事情，全部可以用键盘轻松导航，不需要在不同应用或页面之间跳来跳去。这意味着，正因为 Jane Street 做了很多奇怪的

**[35:15 – 36:04]**
**EN:** different stuff like not using git but using Iron, we actually need a team to build all this integration into the editors so that people can actually live there and not, you know, do some things in the command line and some in the browser and then write code in the editor and sort of jump between these different surfaces. Yeah. And despite the fact that we've built a lot of, I think, quite cool web UIs over the last few years and tooling for building web UIs, Jane Street is just a much less web-focused place certainly than the big tech firms, which I think have all ended up leaning quite heavily in terms of taking all of these interactions and sticking them into a web browser. And for us, it's just like you're in the editor, you make the changes, and the editor becomes both the place in which you interact with all these tools and also the central
**中文：** 事情——比如不用 git 而用 Iron——我们反而真的需要一支团队把这些集成全都做进编辑器，好让人真的能「住在里面」，而不是有些事在命令行做、有些在浏览器做、代码在编辑器里写，然后在不同界面之间来回跳。对。而且，尽管过去几年我们做了不少我觉得相当酷的 web UI、也有做 web UI 的工具链，Jane Street 相比大厂显然是一个「web 比重低得多」的地方；而大厂最后都相当重地把这些交互全都塞进了浏览器。对我们来说就是：你在编辑器里，你做出改动；编辑器既是与所有这些工具交互的地方，也是理解代码、讨论代码的

**[36:04 – 36:52]**
**EN:** location for understanding code and for communicating about code. Like I think another interesting early design choice, which has ups and downs, but I think has certainly cemented the importance of editors, is that the way in which you give feedback on a change is in the editor, right? There's specialized comments that you write with a particular format to mark a piece of feedback, rather than going off into some separate web UI and clicking a button and leaving a note on a kind of PR that somebody else owns. And part of it is this formal feedback comes through the editor, but also because you're in the editor, some of what you do when working on a feature with someone is you just collaborate on the feature. Instead of leaving a CR, which is the name for these comments that we put in, you might just fix the thing. You might just make
**中文：** 中心地点。我觉得另一个有趣的早期设计选择是——它有好处也有坏处，但确实巩固了编辑器的重要性——你给一个改动提反馈的方式，是在编辑器里，对吧？你要用特定格式写一种专门的注释来标记一条反馈，而不是跑到某个独立的网页 UI 里、点个按钮、在别人拥有的 PR 上留一条留言。一部分是这种正式反馈通过编辑器传递；但同时，因为你在编辑器里，当你和某人一起做一个 feature 时，你做的事之一就是直接协作。你可能不去留一条 CR（我们给这种注释起的名字），而是直接把问题修掉，直接

**[36:52 – 37:40]**
**EN:** a change, which I think is a great — it's certainly, I think, a great part of how development works here. It's also weird and unsettling, I think, for people who are used to the other thing. It's like someone else is reaching in and modifying my PR. It feels unsanitary. But for good or ill, or maybe as one should say, for good and ill. It's just a different modality, a different way of interacting within thinking about code, and the editors just have a really central piece in all of that. Yeah. And as you're saying, this really biases us to keep the editor as the home base, because if you're interacting with these systems in a surface where you can't just as easily jump in and edit the code, you then are sort of losing that
**中文：** 改一处代码。我认为这很好——它确实是这里开发方式中很棒的一部分。对习惯了另一种模式的人来说，这也会显得奇怪、令人不安：就像别人伸手进来修改我的 PR，感觉不太卫生。但无论好坏，或者说，好坏兼具。它只是另一种模态、另一种在思考代码过程中互动的方式，而编辑器在这一切里占据着非常中心的位置。对。正如你所说，这一点强烈地让我们倾向把编辑器继续当作主场，因为如果你是在一个无法顺手跳进去改代码的界面里与这些系统交互，你就失去了

**[37:40 – 38:30]**
**EN:** property of this code review system and property of a code review culture that I think we see is pretty positive. What is challenging about this at a technical level? Like what are the things that make it hard to make the editors do the things that we want them to do? So one aspect is that the editors that we're using are things that exist in the outside world — VS Code, Emacs. And for example, one problem that we're at work solving in VS Code right now is that in Jane Street's work we sometimes have incredibly large diffs — so a giant configuration file or just a massive OCaml file. And it turns out that the diff algorithm in VS Code has some
**中文：** 这个代码评审系统的特性，以及我认为相当正向的那套代码评审文化的特性。从技术层面看，这里的难处是什么？是什么让你很难让编辑器做出你想让它做的事？一个方面是：我们用的编辑器是外部世界存在的东西——VS Code、Emacs。举例来说，我们现在正在 VS Code 里解决的一个问题是：在 Jane Street 的工作里，有时会有极其巨大的 diff——一个超大的配置文件，或者一个体量惊人的 OCaml 文件。结果发现，VS Code 的 diff 算法一旦遇到一定规模的 diff，就会有严重的

## 巨型 diff 与规模带来的问题

**SECTION_NOTE**
- 典型痛点：超大 diff 让 VS Code 的 diff 算法性能崩掉；更糟的是，打开一个巨大 diff 卡住后关掉，会把查看 diff 的队列整体锁死，后面所有 diff 都看不了。
- 另外还有「把 Iron 的 code view 集成进编辑器」带来的冲突：缓冲区的 URI 假设被打破，导致内置搜索行为异常，需要逐个排查修复。
- 编辑器之间的共享基础设施（OCaml language server、底层 Merlin 提供的类型查询与跳转定义）也有大量性能问题与数据结构取舍。
- 一个典型「规模」故事：为了让索引能更好地查找 module，编译器产物里加了额外信息，结果这个索引多用好几 GB 内存，机器上已经建不出来了。

**END_SECTION_NOTE**

**[38:30 – 39:18]**
**EN:** serious performance [laughter] problems once you have diffs of a certain size. And furthermore there's an issue of, if you try and open a large diff and it hangs and you close it, it's now locked up the queue for viewing diffs at all and you can't look [laughter] at any others. And so there are just things like this where either there's some functionality that we want internally that isn't accommodated by this external tool that we're building in. There are also challenges where we have implemented some integration with the Iron code view system that messes with some assumptions that, say, VS Code makes about what a buffer is going to be
**中文：** 性能问题。[笑声] 而且还有一个麻烦：如果你试着打开一个巨大的 diff，它卡住了，你把它关掉，此时查看 diff 的队列就被整体锁死了，你之后任何 diff 都看不了。[笑声] 就是这类事情：要么是我们内部想要的某些功能，这个我们正在往里做集成的外部工具并不支持。还有些挑战来自我们做的 Iron code view 系统集成，它打破了 VS Code 的一些假设，比如关于一个缓冲区会是什么样子、

**[39:18 – 40:07]**
**EN:** what the URI for that buffer is, and that makes the built-in editor search misbehave in a strange way and we have to track that down and fix it. I think that there are also challenging things about the kind of shared infrastructure between the editors, like the OCaml language server and the underlying system Merlin that provides type lookups and jump to definition for OCaml. And there's kind of lots of interesting performance problems and questions about what are the optimal data structures, and if we want to build an index of the entire monorepo. Oh — someone has added extra information
**中文：** 那个缓冲区的 URI 是什么。这会让编辑器内置的搜索以奇怪的方式出问题，我们得把它查出来再修掉。我认为编辑器之间的那类共享基础设施也有很多难处，比如 OCaml language server，以及底层为 OCaml 提供类型查询和跳转定义的系统 Merlin。这里有大量有趣的性能问题，以及关于「什么才是最优数据结构」的问题；还有，如果我们想给整个 monorepo 建一个索引——哦，有人为了

**[40:07 – 40:57]**
**EN:** to do better — to the files that the compiler produces, to do better lookups of modules using this index. Well, now this index uses many gigabytes more of RAM and we can't actually build the index on [laughter] our boxes anymore. So, as I'm saying this, I'm realizing a lot of the problems we're trying to solve relate to the scale of certain things that we're doing at Jane Street and making these general purpose tools perform really well at these kind of idiosyncratic use cases, right? Right. And I think one thing that comes out of what you're describing here is that the editor has this kind of central role where it's like the surface through which many other things come at the users. And so maybe the problems you run into are problems about like the type
**中文：** 更好的查找——给编译器产出的文件加了额外信息，好利用这个索引更好地查找 module。那么现在，这个索引要多占好几 GB 内存，我们已经没法在自己的机器上把它建出来了。[笑声] 说着说着我意识到：我们想解决的很多问题，都和 Jane Street 某些事情的「规模」有关，也和「让这些通用工具在非常特殊的用例下也跑得很好」有关，对吧？对。我觉得从你描述里能看出一件事：编辑器有这样一种中心角色——它像是许多其他东西到达用户面前的界面。所以你遇到的问题，可能其实是关于类型

**[40:57 – 41:45]**
**EN:** lookup system or this indexing system — things that are not literally part of the editor, but the editor is the place where you see the issues. And so you're kind of driven to fix things sometimes in the code review system and sometimes off in the kind of OCaml language stuff. Increasingly the Python world is another place where we're spending a bunch of time actually. Maybe it's worth saying what has changed as we've needed to do more support for Python. I'm kind of curious what kind of pressures that puts on the editors, because in some ways it should all be easy, right? The whole world uses Python. Now we can just do what everybody else does. I think the main surface for folks in trading and research who are interacting with Python is the
**中文：** 查询系统，或者这个索引系统——它们严格来说并不是编辑器的一部分，但编辑器是你看到这些问题的地方。所以你有时被迫去修代码评审系统里的东西，有时又跑到 OCaml 语言那一块去修。而越来越频繁地，Python 世界成了我们花大量时间的另一处。也许值得说说：当我们需要对 Python 提供更多支持时，什么发生了变化？我很好奇这给编辑器带来了什么样的压力——因为某种程度上，这本该都容易，对吧？全世界都在用 Python，照别人做的做就行了。我认为交易与研究部门的人与 Python 打交道的主要界面是

## Python notebook 的难题

**SECTION_NOTE**
- 交易／研究同事用 Python 的主要界面是 notebook，而这块一直非常棘手。
- 各种 notebook 方案各有明显缺陷：甚至连「人们为什么用 A 而不是 B」都难以搞清楚；还出现「新方案本想取代旧方案、却缺了旧方案的功能，结果同时维护好几套」的不幸趋势。
- notebook 里的代码不易共享：想把代码抽成 repo 里的 Python 库、供多个 notebook 导入复用，就需要一个「编辑 .py 文件和编辑 notebook 一样方便」的环境，而 VS Code 在内部 notebook 场景下性能与可用性都很吃力。
- 于是他们开始自己造方案——这也是 Jane Street 工具工作的一大主题；他同时担心「过度偏好自建」。

**END_SECTION_NOTE**

**[41:45 – 42:34]**
**EN:** Python notebook. And this has been, I think, the area that's been very challenging. There are different notebook solutions; they all have different significant flaws or limitations. And I think one of the pressures is even understanding what the different use cases are and why people use one over the other. And a sort of unfortunate trend of spinning up a new one that we hoped would replace the old one, except it has — it's missing some functionality that the old thing has, and so now we're maintaining multiple of them. And one other pressure is that for
**中文：** Python notebook。而我认为这块一直非常棘手。市面上有各种 notebook 方案，它们各自都有明显的缺陷或局限。压力之一，甚至连「不同的使用场景是什么、人们为什么用一个而不用另一个」都还没搞明白。还有一种不幸的趋势：新起一个方案，本希望取代旧的，结果它缺了旧方案有的某些功能，于是现在我们同时维护好几套。另一个压力是，对

**[42:34 – 43:24]**
**EN:** people who are writing a lot of code in Python notebooks, that code is not always easily sharable. For example, you might want to take it and put it in a Python library that lives in the repo, that can be imported and shared between multiple notebooks. And for that, you'd really want people in a surface like VS Code, where it's just as accessible to edit Python files as it is notebooks. But at least for the kind of Python notebooks work that people do here, VS Code has been very challenging and has had a lot of performance and usability problems — to the point where we're now starting to work on just building our own solution to this,
**中文：** 那些在 Python notebook 里写大量代码的人来说，这些代码并不总是容易共享。比如你可能想把它抽成一个放在 repo 里的 Python 库，可以被多个 notebook 导入、共享。而要这样做，你会非常希望人们处在一个类似 VS Code 的界面里——在那里编辑 .py 文件和编辑 notebook 一样方便。但至少就这里人们做的这类 notebook 工作而言，VS Code 一直非常吃力，有大量性能和可用性问题——以至于我们现在开始自己动手造方案，

**[43:24 – 44:14]**
**EN:** which is, I would say, a theme of a lot of the tools work at Jane Street. And I do worry a lot that we overlean in the direction of building our own things. At the same time, there's a lot of power in having control and having everything built in an ecosystem that you understand from top to bottom. So I actually feel like you see work happening, especially in the editor space, that's shearing in both directions. There's some places — like in the notebook work — where we're like, ah yeah, now we're going to, instead of these multiple things on the outside world, none of which exactly work in the way that we want, none of them have quite the design goals that we want, some of the ones that look closer aren't maintained anymore, whatever — there's a whole bunch of problems with the notebook stuff in the outside world. We're like, we're going to write a nice little OCaml thing, use our
**中文：** 我会说这是 Jane Street 很多工具工作的主题。我也确实很担心我们会过度偏向「自建」。但与此同时，完全掌控、并且所有东西都建在一个你从上到下都理解的生态里，本身有很大力量。所以我其实觉得，特别是在编辑器这块，你能看到两股方向相反的力量在互相剪切。有些地方——比如 notebook——我们会想：行吧，外面这些方案没有哪一个完全按我们想要的方式工作，没有哪一个的设计目标和我们一致，有些看起来更接近的已经不维护了，总之外面的 notebook 方案问题一大堆。那我们就用 OCaml 写个小巧漂亮的，用我们

**[44:14 – 45:04]**
**EN:** own web UI stuff, and it's just going to work smoothly. And we have a prototype that's pretty good, and I feel pretty optimistic about this being both not that hard to land and also giving us a huge amount of control to be able to adapt the notebook to the very specific things that we want to do internally and have a much better experience. At the same time, I feel like a lot of the other work that you guys have been doing is about de-weirdifying various aspects of our setup. Like we have 25 years of weirdo special-case Emacs stuff that we've built up over time. And we've just been spending a lot of time funding work on Emacs — figuring out how can we take the weird custom thing that we've done internally and replace it with the standard open source thing. So I feel like actually both of these directions are good. You just kind of have to pick your spot.
**中文：** 自己的 web UI 那一套，它就会顺畅地跑起来。我们有一个还不错的原型，而且我相当乐观：这件事既不会太难落地，又能给我们极大的控制力，让 notebook 适配我们内部非常具体的需求，体验好得多。同时，我觉得你们在做的另外很多工作，是在「去怪化」我们环境里的各种方面。比如我们积累了 25 年的、各种特例式的怪 Emacs 东西。我们花了大量时间资助 Emacs 相关的工作——研究怎么把我们内部做的奇怪定制替换成标准的开源方案。所以我其实觉得这两个方向都是好的，你只需要挑好你的落点。

## 自建还是回馈上游？

**SECTION_NOTE**
- 反过来的一股力量：如果能让上游工具做你想要的，那要好得多——别人的代码是最好的代码；有大量人在使用、报 bug、并被修复，你不必自己把所有坑踩一遍。
- 上游 Emacs 社区真正懂 Emacs 的设计美学，很多时候比自建得到的结果更好；外部扩展包也更容易和「按原生方式写的」内部扩展和平共存。
- 反方向的力量：他们大量扩展是用 OCaml 写的（跨 Neovim／Emacs／VS Code），非常不「标准」；部分代码又必须用宿主语言写。
- Emacs 的 elisp 与 ecaml（他们用的 OCaml 方言）之间的边界、尤其异步部分很别扭，长期目标是把这块重新架构，减少互相等待造成的奇怪死锁；本质困难是「把两种语言的并发原语联姻」。

**END_SECTION_NOTE**

**[45:04 – 45:51]**
**EN:** If you can find a way to make the upstream thing do what you want, that's just so much nicer, right? Other people improve it for you. The code that you don't have to write is the best code of all. Not only you not writing, but lots of other people are using it and reporting problems and those are getting fixed. So we don't have to find all the problems ourselves by running into them. And it turns out the upstream Emacs people really understand Emacs well and they know how the system works and they have the design aesthetic down, and in many ways you just get better stuff than you would get from our custom creations. Yeah. All the different pieces work together better, that some external
**中文：** 如果你能让上游工具做出你想要的效果，那真是好太多了，对吧？别人会替你改进它。你不用写的那部分代码，才是最好的代码。而且不只是你不用写——还有大量其他人在使用它、报告问题，而这些问题会被修掉。所以我们不必靠自己去踩出所有坑。而且事实证明，上游 Emacs 社区真的很懂 Emacs，他们知道系统如何运作、把握着设计美学；很多时候你从他们那里得到的东西，比我们自己定制出来的更好。对。各个部分之间的配合也更好——某些外部

**[45:51 – 46:37]**
**EN:** package will play much more nicely with our internal extension if our internal extension does it the sort of native Emacs way, as opposed to some totally different approach that then breaks when it comes into contact with the outside world. Right? Although a thing that pushes in the opposite direction is like a bunch of the extensions that we've done we've written in OCaml, which is like super not the standard way. In fact, we do this across multiple editors — for Neovim and Emacs and VS Code. We have OCaml as at least one of the major implementation languages. You also have to use the kind of more native language to do some of the pieces. So how does that play into the kind of technical tension? Yeah, it definitely
**中文：** 外部包，只要我们的内部扩展按「Emacs 原生方式」来写，就能与它融洽得多；而如果用了完全不同的做法，一旦和外部世界接触就会出问题，对吧？不过有一股反方向的力量：我们做的很多扩展是用 OCaml 写的，这非常不「标准」。事实上我们在多个编辑器上都这么做——Neovim、Emacs、VS Code。OCaml 至少是我们主要的实现语言之一，但有些部分你也必须用更「原生」的语言来写。那这又如何参与进这种技术张力里？它确实

**[46:37 – 47:27]**
**EN:** complicates the story. And in Emacs in particular, we have some ideas — we haven't sort of put the boundary between elisp, the sort of native Emacs implementation language, and ecaml, the flavor of OCaml that we use to write Emacs things. Like the boundary there, particularly for asynchronous things, is pretty awkward. And so I think a long-term goal would be rearchitecting that to have fewer potential for weird deadlocks when these two sides are waiting on each other, or things like this. Is part of the issue here just that Emacs is super ancient and does not have a great concurrency story at all?
**中文：** 让情况更复杂。尤其在 Emacs 上，我们有一些想法——我们还没有真正划清 elisp（Emacs 原生的实现语言）和 ecaml（我们用来写 Emacs 东西的那个 OCaml 方言）之间的边界。那条边界，特别是涉及异步的地方，相当别扭。所以我想一个长期目标是把这一块重新架构，减少两边互相等待时产生奇怪死锁的可能，诸如此类。这里的一部分问题是不是就在于：Emacs 太古老了，并发这块的故事一点都不好？

**[47:27 – 48:17]**
**EN:** Yes. So I think to some extent that's true. I think upstream Emacs is actually working on this. In particular there were some changes to the garbage collector that I think may play more nicely with asynchronous things, but unfortunately that wasn't ready for the current cut of Emacs that we're working on upgrading to. And Emacs and Vim were both tools that have been around for a while and have some limitations in terms of the kinds of interactions that they were intended to support, right? And even beyond that, just marrying the concurrency primitives of two different languages is really hard. We actually have run into very similar challenges around Python and OCaml, where I think we have now
**中文：** 是的，某种程度上是这样。我认为上游 Emacs 其实正在做这件事，特别是垃圾回收器有一些改动，我猜会和异步场景配合得更好；但很遗憾，那些改动在我们正准备升级到的那一版 Emacs 里还没就绪。而 Emacs 和 Vim 都是存在了很久的工具，在「它们本来打算支持什么样的交互」这件事上都有局限，对吧？而且再进一步说，把两种不同语言的并发原语「联姻」，本身就非常难。我们在 Python 与 OCaml 之间其实也遇到过非常相似的挑战，我觉得我们现在

**[48:17 – 49:07]**
**EN:** maybe started to work out a story that makes more sense. But it's a tricky thing even when you have pretty good concurrency stories on both sides. So to kind of pivot a little bit, I think a thing that has affected everything about developer tools is the emergence of actual good agentic AI for programming. And I'm curious how that has affected the way you think about work in the editor and what you prioritize and what are the things that you want to build. Yeah, there are a few different pieces to this one. And I think it hasn't really affected our belief that the editor can still serve as an excellent home base for the software engineer, and that we want to make the
**中文：** 或许已经开始理出一套更说得通的方案。但即便两边都有相当不错的并发方案，这依然是件棘手的事。我们稍微换个话题：我认为有一件事影响了开发者工具的一切，那就是真正好用的「智能体式 AI」（agentic AI）在编程上的出现。我很好奇它如何影响你对编辑器工作的思考、你的优先级，以及你想造什么。这件事有几块不同的内容。我认为它并没有真正动摇我们的信念：编辑器仍然可以是软件工程师极好的主场；我们也希望让

## 智能体 AI 给编辑器带来什么变化

**SECTION_NOTE**
- 信念未变：编辑器仍是工程师的主场，新出现的工作流应当像以前的工作方式一样自然、可及地通过编辑器完成。
- 变的是「怎么写代码」，不变的是「读代码」：很多工程师已经不太亲自敲代码，更多是在写提示词；但他们仍在读代码、看类型、看定义——所以「看 diff、做评审、读懂代码」的需求不但没消失，反而不变或更强。
- 这给做编辑器的人带来巨大的不确定性：现在该造什么？一年后还有用吗？
- 他们正在加强编辑器遥测与可观测性，用真实数据判断工作方式到底怎么变了：例如「跳转定义」次数不降反升，可能与人们需要读、理解的代码变多有关——因此「该不该优化跳转定义速度」这类问题要靠数据回答，而不是靠猜。

**END_SECTION_NOTE**

**[49:07 – 49:57]**
**EN:** new workflows that are emerging just as natural and accessible via the editor as the ways people were working before. And then there are also some things that seem like they aren't going to necessarily change about what people are doing in the editors. This is looking at diffs, doing code review, working to understand and read code, whereas how people write code may be changing and is changing significantly. There are certainly plenty of engineers all over the place, but also at Jane Street, who just don't type code very much anymore, and most of the typing — they type more in the way of prompts. But they're still reading code and they're still looking at the types of things and looking at the definitions of things. So they're doing lots of things you do in the editor, but
**中文：** 新出现的工作流，像以前的工作方式一样自然地、可及地通过编辑器完成。另外，有些事情看起来并不会改变人们在编辑器里做的事：看 diff、做代码评审、努力理解和阅读代码。而「人怎么写代码」可能正在变，而且变化很大。各地当然有很多工程师，Jane Street 也是，已经不太亲手敲代码了；大部分键入变成了写提示词。但他们仍在读代码，仍在看各种类型、看各种定义。所以他们做的是许多你在编辑器里会做的事，只是

**[49:57 – 50:45]**
**EN:** maybe less editing. Yes. And this, I think, has created quite a lot of uncertainty for people working on editors, in terms of what is it that is useful to build now, what is it that is going to be useful a year from now — will anything [laughter] — and one thing that I've gotten quite interested in recently, particularly because the editors team has been investing in improving the telemetry and observability of what people are doing in editors and how they're interacting with the OCaml language server, is trying to use this telemetry to understand how it is that people's work is actually changing. You know, I looked the other day — I had a
**中文：** 可能「编辑」得少了。是的。而我认为这给做编辑器的人带来了相当大的不确定性：现在造什么才是有用的？一年之后什么还会有用？还会有什么用吗？[笑声] 我最近很感兴趣的一件事——特别是因为 editors 团队一直在投入改善编辑器遥测（telemetry）与可观测性，看人们在编辑器里做什么、如何与 OCaml language server 交互——就是试着用这些遥测数据去理解：人们的工作到底是怎么变的。你知道，前几天我看了一下——我原本有个

**[50:45 – 51:33]**
**EN:** hypothesis that, well, if I look at the number of times per user that people jumped to definition in OCaml: if the LLMs are producing good code and people aren't writing and having to look up APIs as much, they'll be jumping to definition less on a per user basis. But then in the telemetry, it seemed if anything they're doing it slightly more, which was quite surprising, but also maybe relates to people actually needing to read and understand more code than they were before. And so I'm excited for this kind of data to help us understand what it is that people are actually doing in editors, because it's kind of been quite amorphous as things have been changing
**中文：** 假设：如果看「每用户跳转定义的次数」——如果 LLM 产出的代码很好、人们不再需要写代码、也不再需要频繁查 API，那么人均跳转定义应该减少。但在遥测数据里，看起来反而是略微增加了。这相当出人意料，但也可能是因为人们实际上需要读、需要理解的代码比以前更多了。所以我很期待用这类数据帮我们理解：人们到底在编辑器里做什么——因为在这快速变化的过程中，这件事一直相当模糊。

**[51:33 – 52:22]**
**EN:** very quickly. And using that to help us decide what is important to invest in and what are the workflows to make better, because questions like "should we try hard to make jump to definition faster" — that depends if people are using it more or less. Yeah. No, it makes a ton of sense. And the thing you're proposing of using the data to drive seems more right than my instinct, which is like theorizing the air about it. But on the theorizing the air part, it does feel like understanding is at the moment the thing that's most important, right? You know, what's the cost of creating a plausible looking PR? I think this is — I'm stealing something from Charlie Marsh. I think the cost of making a plausible PR has dropped nearly to zero, and the cost of verifying it is about the same
**中文：** 非常快。用数据来帮我们判断该重点投入什么、该改进哪些工作流；因为像「我们该不该努力把跳转定义做快」这种问题，答案取决于人们是更多还是更少地在用它。对，这非常有道理。你提出的「用数据驱动」比我本能的做法更对——我本能是想「凭空推理」。但就凭空推理那部分而言，我确实觉得当下最重要的事情就是「理解」，对吧？你想，造出一个看起来像样的 PR 要多少成本？这一点——我这是从 Charlie Marsh 那里借来的说法——我认为造出一个看似合理的 PR 的成本已经几乎降到零，而验证它的成本基本没变，

**[52:22 – 53:11]**
**EN:** or maybe worse, right? I think notably there's something kind of uncanny about a lot of the features generated by LLMs, in that they're very smooth. They look very nice. A lot of tells — things that you might think of as indications of a problem — just kind of aren't there. But they're often still super broken, right? And so the process of reading through and understanding is at a minimum different and in some ways certainly harder. And so the idea that we need to spend more energy and engineering work making it easy for people to understand what is happening seems really important. I think some of that understanding should come from further leveraging of LLM. I think LLMs are a really powerful explanatory tool. But I think it's easy to
**中文：** 甚至可能更高，对吧？我觉得特别值得注意的是，LLM 生成的很多 feature 有种说不出的诡异感：它们非常平滑，看起来非常漂亮；许多「破绽」——那些你会当成问题征兆的线索——就是不存在。但它们往往还是坏得一塌糊涂，对吧？所以阅读和理解的过程，至少是与过去不同，在某些方面确实更难。因此，「我们需要投入更多精力和工程工作，让人更容易理解正在发生什么」这件事，看起来非常重要。我认为其中一部分理解应该来自进一步利用 LLM——LLM 是非常强大的解释工具。但我觉得人们很容易

**[53:11 – 54:00]**
**EN:** underrate the value of traditional, hard ways of extracting data from code and surfacing it — I think things like go to definition and inferred types and test results and things like that are all really exciting. Yeah. I've also been thinking more about people's actual workflows when getting LLMs to write code, and how that relates to understanding it at the end result. So, one thing that I have played around with in some of my education work is Claude Code's learning output style, which changes the system prompt to tell it to stop sometimes and leave a to-do human sort of comment in the code and
**中文：** 低估传统那些「硬办法」的价值——从代码里抽取数据并把它呈现出来。我认为像「跳转定义」「推断出的类型」「测试结果」这类东西，都非常令人兴奋。对。我也在想更多关于：当人们让 LLM 写代码时，他们真实的工作流是什么样的，以及这与最终「理解」之间的关系。我在自己一些教育工作里玩过的一个东西，是 Claude Code 的 learning 输出风格：它会修改系统提示词，让模型有时停下来，在代码里留一条给人类做的 to-do 注释，

## Claude Code 的 learning 模式与心智模型

**SECTION_NOTE**
- Claude Code 的 learning 输出风格：让模型中途停下、留下「请人来补」的 to-do，逼你先读懂已写出的部分。他的体验是：产出过程更愉快，最终也确实更理解代码。
- 关键反思：问题不只是「产出端」加解释工具，而是「在人机共同产出代码的过程中」怎么交互，才能最终形成扎实理解——「让它全写完、我最后再读」是否最优，他现在持怀疑态度。
- 类比：写代码时你在逐步建立理解、发现错误时你在修正心智模型；而评审别人的代码时，对方直接给你成品，你只能笨拙地重建心智模型——这恰恰就是与 LLM 协作的处境。
- 「造一个看似合理的 PR 的成本趋近于零，验证成本不变甚至更糟」；LLM 生成的代码很「顺滑」，没有破绽线索却常常是坏的。软件开发的重心因此从「写」转向「读与验证」，成为新的瓶颈环节。

**END_SECTION_NOTE**

**[54:00 – 54:48]**
**EN:** ask the human to go fill in that piece. And in using this myself, I found that having it stop partway through and then I had to read what it had written so far and understand it enough to fill in this piece — I felt like I came out at the end both having had a more pleasant experience of producing this code, but also a more pleasant experience and I think effective at actually understanding what it had produced. And I'm curious to explore not just on the output end adding more explanatory power and tools to the code that's already produced, but thinking about how do people interact with these models as they're
**中文：** 让人类去把那一块补上。我自己用下来发现：让它中途停下来，然后我不得不读它已经写出的部分、并且理解到足以补上这一块——最后我觉得，整个产出代码的过程更愉快，而且我更有效地真正理解了它产出的东西。我很想探索的不只是在「产出端」为已生成的代码加上更多解释能力和工具，而是在模型产出代码的过程中，

**[54:48 – 55:37]**
**EN:** producing the code to most effectively end up with a solid understanding of it at the end, and not just be guided by "well, it feels more efficient to have it write everything and then read it at the end." I've become a little skeptical that that is actually the optimal way to approach it. It's interesting. It reminds me a little bit of the thing we were talking about, about the utility of taking notes while writing with a pencil. The idea that you are involved in the production function will cause you to better understand the thing at the end, and there's maybe a kind of infelicity in the current way the tools are set up, in that everything is tilted in the direction of "the model generates the code and then you decide whether or not to accept it." And maybe that's wrong. That's a fascinating idea. Yeah. I was giving a talk to a group of
**中文：** 人应该怎么与这些模型交互，才能最终对它形成扎实的理解，而不是被「让它全写完、最后我再读」这种「感觉更高效」的路径牵着走。我现在有点怀疑，那是否真的是最优做法。有意思。这让我想起我们前面聊的、用铅笔做笔记的效用：你亲身参与「生产过程」，会让你最后更好地理解它。而当前工具的搭建方式可能有一种「不合适」之处：一切都偏向「模型生成代码，然后你决定要不要接受」。也许这是错的。这个想法很有意思。对。我最近给一群

**[55:37 – 56:27]**
**EN:** interns about code review, and had a slide: code review is hard. When you're writing code, you're incrementally building your understanding. And when you're catching mistakes, you're correcting your mental model. And when you're reviewing someone else's code, they're just presenting you with the finished result. And you kind of have to awkwardly build your own mental model of it. And it immediately struck me: wait, this is exactly what working with LLMs is like, in the way that it makes it harder to have a mental model of the code you are authoring. That sort of started me more firmly down this path of, yeah, maybe we should be interacting with these things differently, at least some of the time. That's really interesting. There's just a lot of space for innovation here and new methods of
**中文：** 实习生讲代码评审，有一页幻灯片是：代码评审很难。你写代码时，你在逐步建立理解；当你发现自己犯错时，你在修正自己的心智模型。而你评审别人的代码时，对方直接把成品摆在你面前，你只能别扭地自己去重建一套心智模型。我当场就意识到：等等，这正是与 LLM 协作的样子——它让你更难对「自己在编写的代码」形成心智模型。这让我更坚定地走上这条路：也许我们至少在某些时候，应该用不同的方式与这些东西交互。这非常有意思。这里创新空间很大，方法论也是新的，

**[56:27 – 57:16]**
**EN:** approaching — like LLM suddenly make the things that you can do very different. It's a very different cost structure and there's a very different opportunity set. And so the thing you're talking about with the Claude Code learning mode is something where you can integrate a kind of tutor-like behavior into the automation, and that's just dramatically cheaper than it used to be, where you had to go off and talk to another person to get that experience to happen. I also feel like in the editor space in general, there's a lot of room for custom integrated visualizations and ways of understanding the data, and that the models are really good at ginning these things up. And the idea that we should be able to ship along with a feature a custom visualization that you made for understanding that diff — like, that just kind of shows up in the middle of
**中文：** LLM 突然让你能做的事变得完全不同了：成本结构不同，机会集合也不同。你刚说的 Claude Code learning 模式，就是可以把一种「导师式行为」集成进自动化流程里，而这比过去便宜太多了——过去你得去找另一个人，才能得到这种体验。我也觉得，在编辑器这个领域，定制化的内嵌可视化、以及理解数据的方式有很大空间；而模型非常擅长把这些东西快速生成出来。还有，「我们应该能随着一个 feature 一起交付一个你为理解那个 diff 而做的定制可视化」——它就出现在

**[57:16 – 58:06]**
**EN:** review. Like that's a thing that we could plausibly do now that would have made no sense three years ago. Yeah. And one thing that I'm excited to explore that connects to your point about these things being very good at explaining is that you could also bake into a feature some precomputed segmentation of the code into logical chunks, and then a pre-baked explanation of each of those chunks that you can just call up with a single keystroke as you're reviewing the code. I mean, as you're doing it, you can highlight it and ask a model to explain the piece, but that's some additional friction. The response doesn't necessarily come back that quickly. And
**中文：** 评审中间。这是我们现在有可能做到、而三年前完全说不通的事。对。我很想探索的一点——和你说这些模型非常擅长解释有关——是你还可以把某些东西「烤」进一个 feature：预先计算好的、把代码切成逻辑块的切分，以及每一块预先写好的解释；你在评审代码时按一个键就能调出来。当然，你也可以在评审过程中选中一段、让模型解释它，但那有额外的摩擦，而且响应未必很快回来。

**[58:06 – 58:56]**
**EN:** if for any given piece, you could sort of call this up, I think that might also be a sort of powerful tool for helping people more easily understand the increasing volume of code they're being asked to review, right? And I think this is just the modern condition of a software engineer. And by modern I mean for the last eight months or something, is that there's just a lot more review to do as a proportion of your time. You're just spending much more time reading and understanding, and so suddenly the value of making that better just shoots up by a lot. I mean, it was already a lot of work so it was already somewhat valuable to do it, but it's now much more clearly the rate limiting step in all of this work. So, we're talking a bunch about how AI affects the experience of developing code and
**中文：** 而如果对任何一段代码都能这样随手调出来，我认为那也会是一种很有力的工具，帮助人们更容易理解他们被要求评审的、越来越多的代码，对吧？我认为这就是软件工程师的「当代境况」——我说的「当代」是指最近八个月左右——作为你时间占比的一部分，要做的评审多得多。你在阅读和理解上花的时间明显更多，于是「把它做得更好」的价值突然大幅飙升。它本来就工作量很大，所以改进它本来就有价值；但它现在更明确地成了这整件事的瓶颈环节。我们聊了很多 AI 如何影响「开发代码」与

## 当 LLM 能做掉练习时，如何教学

**SECTION_NOTE**
- 核心张力：教人用一个陌生测试库时，LLM 直接就能把这个写出来——那这门库到底有什么是「人必须懂」的？哪些又只是可以丢给模型的样板？
- 目前的选择：让人自己动手、至少亲手实现一遍，这是后续能评判 LLM 产出的前提。
- 同时要重新划线：过去那些「因为不得不做」的繁琐劳动，也许不必再让人学着做；真正难的是「教什么」——怎么有效使用这些工具、如何融入工作流、哪些做法会让你被带歪。
- Ron 的担忧：学习的核心之一是「与材料搏斗」；当随时有个精灵待命，学习会被掏空。而「小到适合学习者、又大到 LLM 一次做不掉」的问题集合，如今已接近空集。因此有时必须「刻意收走某些可供性（affordances）」——就像当年让人在纸上做题目。

**END_SECTION_NOTE**

**[58:56 – 59:46]**
**EN:** understanding code. And this resonates, I think, a lot with the question of how does AI affect the process of teaching people stuff? So, I'm kind of curious what that has felt like, as you've been helping to run education programs here amidst the middle of this AI revolution. Yeah. So this is, I would say, quite a thorny problem, because you're faced with this tension of — one of the things that I help work on, and maybe we can talk more about this, is this workshop for early career engineers at Jane Street focused on techniques for software testing. And we call these workshops teach-ins. So this testing teach-in teaches people
**中文：** 「理解代码」。而我认为这很多地方也呼应了「AI 如何影响教人东西的过程」这个问题。所以我很想知道，在这场 AI 革命正中间，你在帮忙运营这里教育项目时，是什么感受？我想说这是个相当棘手的问题，因为你面对这样一种张力：我参与推进的其中一件事——也许我们可以多聊聊——是给 Jane Street 早期职业工程师办的一个工作坊，聚焦软件测试技术。我们把这些工作坊叫 teach-in。这个测试 teach-in 教大家

**[59:46 – 60:36]**
**EN:** how to interact with various libraries for property-based testing or for deterministic control of time in tests. And when you're teaching someone how to use an unfamiliar library, well, an LLM could just write that for them. So what is it about this library that someone actually needs to know in practice, and what might you consider sort of boilerplate that you don't need? The initial scaffolding can be made really easy, right? The models can do a decent job of that, but what's the understanding that you have to give to people? Yes. And so I think so far we've come down on the side of people having to think through these sorts of
**中文：** 如何与各种库交互，比如基于属性的测试（property-based testing）、或者在测试中对时间做确定性控制。而当你在教人使用一个陌生的库时，LLM 其实可以直接替他写出来。那么这门库到底有什么是人真正需要知道的？又有哪些你会认为是「样板」，不必学？最初的脚手架可以弄得很简单，对吧？模型能做得不错。但你真正必须给人建立的「理解」是什么？对。所以到目前为止，我们的选择是：人得把这些

**[60:36 – 61:26]**
**EN:** problems and implement them themselves — at least once — is actually pretty important for coming out of it with a sufficient understanding. And even if what they are doing subsequent to that is reading applications of this technique initially authored by an LLM, building that understanding by having done it themselves once is a critical input to then being able to evaluate those things. That is one piece of it. And I think we are actively thinking about where to draw the line, in terms of: there's some stuff that we were probably asking people to do in the past because it was stuff that they had to do — even though it was somewhat toilsome — that yeah, we should probably not have people try and learn how to do those pieces.
**中文：** 问题想清楚、并且自己实现一遍——至少一次——对于最终形成足够的理解其实相当重要。即便他们之后做的事情只是阅读由 LLM 初写的、这项技术的应用，那「自己亲手做过一次」所建立的理解，也是后续能评判这些东西的关键输入。这是其中一块。同时我认为我们正在积极思考该在哪里划线：过去有些事我们大概会要求人做，因为那是他们不得不做的——尽管有些繁琐——但现在这些部分，也许不该再让人去学着做了。

**[61:26 – 62:14]**
**EN:** But there's also, I think, the challenging question of how do we teach people, and even what do we teach people, about using these tools effectively; about how to integrate them with their workflow; about how to understand the ways in which they can be effective or lead you astray. And I think this is still in very early days. I don't think we have settled answers to this, and the tools are changing very quickly. But you can already see problems, right? There are definitely people who run into problems where they just kind of vibe it up too much and use the LLM to generate stuff and do not think. And that's a real problem. You still need to think. I actually worry more generally about what it means for
**中文：** 但还有一个我认为很有挑战的问题：怎么教人、甚至教人什么，才算「有效地使用这些工具」——如何把它们融入工作流，如何理解它们在哪些地方有效、在哪些地方会把你带偏。我认为这还处在非常早期的阶段，我们没有定论，而工具变化极快。但你已经能看到问题了，对吧？确实有人栽跟头：他们「氛围编程」得太狠，用 LLM 生成东西却不动脑子。这是个真问题——你仍然需要思考。其实我更担心的是，这对

**[62:14 – 63:04]**
**EN:** the overall education system means what. I think a kind of critical component of learning is struggling with the material. And the world where you always have a genie at your beck and call that you can just summon up to solve the problem is itself a real problem. And the overlap of problems that are easy enough that they are suitable for someone who is learning to do, and hard enough that an LLM can't just one-shot it, is like close to the empty set now. [gasps] So it's a really challenging problem. I mean, it really does make me think back to doing stuff on paper without a computer. Sometimes an important thing about making the educational process work is withholding certain affordances. And I worry that we
**中文：** 整个教育体系意味着什么。我认为学习中一个关键的组成部分，就是「与材料搏斗」。而一个你随时有个精灵随叫随到、可以直接召唤来解决问题的世界，本身就是个真问题。而「简单到适合学习者去做、又难到 LLM 无法一次搞定」这两类问题的交集，现在已经接近空集。[吸气] 所以这是个非常棘手的问题。它真的让我回想起「不用电脑、在纸上做题」的做法。有时候，让教育过程奏效的关键之一，就是「收走某些可供性」。我担心我们

**[63:04 – 63:54]**
**EN:** have a whole generation of people who are learning in this new environment where we don't know what to do. We don't know what affordances to provide and which ones to withhold. And I worry that we're not building a good educational system for people in this world. Yeah. I think you and pretty much everyone else [laughter] involved in education is deeply worried about this. To your first point about how do you get something that's small enough to be tractable for students and large enough to not be trivial with an LLM: we have [snorts] run into this exact problem multiple times with new curriculum we've built, and we've repeatedly ended up with the thing we're asking people to do is too large for the time we have. Like we are asking them to do something
**中文：** 面对的是一整代在全新环境里学习的人，而我们自己都不知道该怎么办：不知道该提供哪些可供性、该收走哪些。我担心我们并没有在为这个世界里的人搭建一个好的教育体系。对。我想你、以及几乎所有做教育的人，[笑声] 都对此深感忧虑。关于你第一点——怎么让任务小到对学生可操作、又大到对 LLM 不平凡——我们在新做的课程里已经[哼笑] 反复撞上这个确切的问题：我们让人做的事，相对于我们有的时间来说太大了。我们在要求他们做的事，

**[63:54 – 64:44]**
**EN:** where they do have to put a lot of work into the LLM code to make it good and actually do what they want, but that just takes too much time to do well, given the amount of time we have on the education piece. And I think it's going to take more experimentation to figure out where that lands. But yes, I think that figuring out where to slot using these tools into traditional education — it feels inevitable that we're going to end up with some sort of structure where you do this piece or this set of activities without the aid of LLMs, and then you do some with. And I think figuring out how to make that
**中文：** 确实得花很多功夫打磨 LLM 写出的代码、让它真的做他们想要的事；但考虑到我们在教育环节能投入的时间，这样做实在耗时太长。我认为要搞清楚这个平衡点，还需要更多实验。但没错，我认为「把使用这些工具这件事插进传统教育的哪个位置」——最终我们几乎必然会得到某种结构：某些环节或某组活动不用 LLM，另一些则用。而我认为，搞清楚如何把这两者

**[64:44 – 65:33]**
**EN:** pairing work, and what you're trying to get out of each of them, is something that a lot of people are going to be experimenting with and figuring out. Yeah. And I think it'll be interesting over the next few years, as we're doing this increasingly with cohorts of people who have not spent that much time typing code themselves. Right — there's a core learning mechanism that maybe they haven't had enough experience with. And I wonder if that will change what we have to teach people in the end. There's been a lot of conversation about things along the lines of that Claude Code learning mode — where what LLM tools, if any, should we provide to folks going
**中文：** 配对、以及你希望从每一部分得到什么，会是很多人去实验、去摸索的事。对。我觉得接下来几年会很有意思：我们越来越多地面对那些自己没花多少时间敲代码的人。对吧——有某种核心的学习机制，他们也许体验得不够。我也在想，这是否最终会改变我们必须教给人的东西。围绕 Claude Code learning 模式这类做法，已经有很多讨论：对那些正在

**[65:33 – 66:23]**
**EN:** through OCaml Boot Camp, learning OCaml for the first time, what LLM tools, if any, should we provide? And if they're just having LLMs write all the code, well, doesn't seem like they're going to learn anything. Yep. But it also feels a bit odd if people are going to leave this and then LLMs are going to be a core part of their day-to-day work. And so not having those be at all a part of this also feels like maybe not a great match for what we want to teach them. And so can we come up with a mode where the LLM will just ask you questions to check your understanding, or leave you large pieces to do yourself — set up a skeleton but actually ask you to do most of the implementation? And I think there's going to be a lot of experimentation with that as well. And maybe the thing that's
**中文：** 参加 OCaml Boot Camp、第一次学 OCaml 的人，我们该给他们哪些（如果有的话）LLM 工具？如果代码全让 LLM 写，他们显然学不到什么。对。但如果他们离开这个项目之后，LLM 会成为他们日常工作的核心，那么在整个训练里完全不让接触，似乎也不匹配我们想教的东西。那能不能设计出一种模式：LLM 只向你提问以检查理解，或者把大块的实现留给你自己做——搭个骨架，但把大部分实现交回给你？我认为这里也会有大量实验。也许还有一件

**[66:23 – 67:13]**
**EN:** been talked about a lot in educational circles: setting up the LLMs to be effective tutors, so that there's a part you're supposed to write yourself and maybe you get stuck and maybe you can get the LLM to give you a hint but not to go off and write the code for you — so that you do have the opportunity to actually do the hard thinking yourself. Yeah, this is actually a category of thing that I did research on in grad school: an automated tutor that could walk you through an arbitrary example problem, where you had some algorithm that you wanted to teach people to follow to solve this kind of problem. And with the idea that, sure, you had the one hour where you could go talk to a TA and get one-on-one help, and that was the most effective thing you could do; but if you were at other times studying for an exam, it might be really useful to have this help — not as effective, but still
**中文：** 在教育圈被热烈讨论的事：把 LLM 配置成有效的导师——有一块你必须自己写，卡住了也许可以让 LLM 给你一个提示，但不让它直接替你把代码写完，这样你确实有机会自己去啃那块硬骨头。对，这其实正是我研究生阶段做过研究的一类东西：一个自动导师，可以带你走任意一道例题——你有一个想教人掌握、用来解这类问题的算法。背后的想法是：你当然有那一小时可以去找助教一对一，那是最有效的方式；但你在其他时间复习备考时，能有这样一个帮助会很有用——效果不如助教，但仍然

**[67:13 – 68:02]**
**EN:** helpful, sort of tutor that is infinitely patient and can walk you through any example. Yeah, I think that is likely going to become a large part of at least higher education. Makes sense. So, we just talked about this testing teach-in, which is part of the formal educational program that we have for new engineers. Maybe it's worth walking through what do we do to onboard people and teach them about our world? Right. So a new software engineer joins, and the first thing that they're likely to do is OCaml Boot Camp — a sort of cumulative series of exercises, building up a little client-server app in OCaml, and learning the different core libraries, and
**中文：** 有帮助的、无限耐心的导师，能带你走任何例子。对，我认为这很可能会成为至少高等教育中很大的一部分。有道理。我们刚聊了这个测试 teach-in，它是我们给新工程师的正式教育项目的一部分。也许值得走一遍：我们是怎么让新人入职、并教他们理解我们这套世界的？好。一位新软件工程师入职后，第一件很可能做的事是 OCaml Boot Camp——一系列递进式的练习，用 OCaml 搭一个小型的客户端／服务器应用，学习各种核心库，

## 训练营、teach-in 与「课程目录」

**SECTION_NOTE**
- 入职路径：OCaml Boot Camp（累计式练习，搭一个小型 client-server 应用，学核心库，由导师评审代码，开始理解 Jane Street 的风格）→ Production Boot Camp（学应用如何部署、监控、配置），构成入职头两周；现在前者约一周就能走完。
- OCaml Boot Camp 的早期版本已有约 20 年历史，近年被大幅打磨。
- 教学法要点：新概念要「在语境中」引入——由具体应用／要加的功能来驱动，而不是先拿一个工具再去找它能解决什么问题；这样才能给人「挂理解」的钩子。
- 第一年还有一系列 teach-in：测试、高性能 OCaml 及性能分析工具、系统调试、高级函数式编程；更专门的还有 Bonsai（OCaml 写 web UI 的库）、market data 等。整体越来越像一份「课程目录」，由新人与其经理／团队一起挑出第一年的学习路径；材料也被设计成支持自学。

**END_SECTION_NOTE**

**[68:02 – 68:52]**
**EN:** getting their code reviewed by a mentor and starting to understand some of Jane Street's style. And from there we have something called a production boot camp, where you go through a series of exercises to learn how applications are actually deployed and monitored and configured at Jane Street. And that forms, say, the first two weeks someone is on the job. And I think that's really been refined a lot over the years. I think the OCaml Boot Camp itself — early versions of that are something like 20 years old. But there's been a lot of work; in fact you've been involved in a bunch of the recent stuff to refine and hone and make that better. And the fact that nowadays someone can arrive and get through that in about a week, and then a little more for
**中文：** 由导师评审他们的代码，并开始理解一些 Jane Street 的代码风格。然后有一个叫 production boot camp 的东西：一系列练习，学习应用在 Jane Street 究竟是怎么部署、监控和配置的。这构成了一个人上岗的头两周。我认为这些年来它被大大打磨过。OCaml Boot Camp 本身——它的早期版本大概有 20 年了。但做了很多工作；事实上你参与了不少近期的工作，把它精修、打磨得更好。而且现在一个人来了，大约一周就能走完，生产训练营再多一点时间。

**[68:52 – 69:42]**
**EN:** the production boot camp — is already a really good improvement. I think we've been able to make that process more efficient. And I don't know, people who come in to Jane Street — there are good and bad things. People aren't, for example, always super enthused about the overall state of all of our documentation, which has its ups and downs, but I feel like I've gotten, especially in the last few years, really positive reviews from people about these early boot camps — that they really do a really good job of setting people up with the basics that they need and doing it in a really efficient way. So I think that's been a nice piece of progress. Yeah. One thing that we've worked hard on, which I think is important when teaching this kind of material, is introducing new concepts in context — where it's motivated by some specific application, some feature you want to add to this system you're working on. And I always frame this as: the
**中文：** 这已经是很好的改进了。我认为我们让这个过程更有效率了。至于来 Jane Street 的人——有好有坏。比如说，人们对公司文档的整体状况并不总是特别热情，这一块有起有伏；但我觉得，特别是最近几年，我收到了很多关于这些早期训练营的正面评价——它们确实很好地把人需要的「基础」铺垫好，而且方式非常高效。所以我认为这是一段不错的进展。对。我们努力做过的一件事——我认为教这类材料时很重要——是「在语境中引入新概念」：由某个具体的应用、你要在这个系统上加的某个功能来驱动它。我总把这件事

**[69:42 – 70:32]**
**EN:** mistake people make is they introduce a tool and then go in search of a problem that it solves, rather than: we're working on this thing now, we want to do this, we don't have a good way to do this, but wait — here's this thing. [laughter] Why don't we use this? And yeah, I think that makes it smoother. That helps people have hooks that they can hang their understanding on. And so that's been a lot of the work, to rework these intro materials. Cool. From there, in someone's first year or so at the firm, they'll go through this series of teach-ins. So I mentioned the testing one. There's one on writing performant OCaml code and the tools to analyze the performance of OCaml code. There's one on
**中文：** 说成：人们犯的错误是先引入一个工具，然后再去找它能解决的问题；而不是——我们现在在做这件事，我们想实现这个，但没有好办法；等等，这里有这么个东西，[笑声] 我们为什么不用它？对，我认为这样更顺，能帮人找到可以「挂着」自己理解的钩子。所以把入门材料重做这件事占了很大一部分工作。很好。从那之后，在公司第一年左右，他们会走一系列 teach-in。我提到了测试那门；还有一门是关于写出高性能 OCaml 代码、以及分析 OCaml 代码性能的工具；

**[70:32 – 71:20]**
**EN:** systems debugging, all the different tools we have for understanding what might be going wrong with some system. There's one on advanced functional programming, a bunch of the advanced features of OCaml and cool ways to apply them. And then there are also some more specialized concepts. A teach-in on Bonsai, the library for writing web pages and web UIs via OCaml. There's one on market data — how the systems for market data work at Jane Street, which is very important to some people but other desks not so much. And I think as we add more, we're going to be even more in the mode of it's sort of a course catalog. And you and your manager or folks on your team sit down when you start and think about which of these are relevant
**中文：** 还有一门是系统调试，讲我们用来理解某个系统可能出什么问题的一整套工具；还有一门是高级函数式编程，讲 OCaml 的一堆高级特性以及它们的巧妙用法。此外还有一些更专门的概念：一门关于 Bonsai 的 teach-in——那是用 OCaml 写网页和 web UI 的库；还有一门关于 market data——Jane Street 的行情数据系统怎么运作，这对某些人极其重要，对其他 desk 则未必。我认为随着课程增加，我们会越来越像一份「课程目录」：你和你经理、或者团队同事在你入职时坐下来，

**[71:20 – 72:10]**
**EN:** to you to do, and almost devise a sort of course of study for your first year at the firm. And we also try and create these materials in a way that's amenable to self-study, and you could also go and work through them on your own at the point where you actually need to learn and apply the material. Yeah. One of the interesting things about the teach-ins and about how those have evolved over time: they were initially built as a kind of reflection of a trading-side education program, also called teach-ins, where that was mostly organized around going from trading desk to trading desk, learning the core concepts that were important for that desk. And my mental model of it early on was like: there's some specific technology you want to teach people about, but the more important thing is
**中文：** 判断其中哪些和你相关、什么时候做，几乎为你第一年量身规划出一条学习路径。我们也努力把这些材料做得适合自学——你也可以在自己真正需要学、需要用它的时候，自己去过一遍。对。关于这些 teach-in 以及它们多年演变，有意思的一点是：它们最初是照着交易侧一个也叫 teach-in 的教育项目做的，那个项目大体是「一个交易 desk 到另一个交易 desk」，学那个 desk 最重要的核心概念。我早期对它的心智模型是：你要教人某项具体技术，但更重要的东西是

**[72:10 – 73:00]**
**EN:** the conceptual layer of — Bonsai is a web framework, but it's also an introduction to incremental computing, right? And market data is a particular domain you need, but it's also about thinking about handling complex streaming data and building modular and efficient protocols for consuming those in a good way. There are a bunch of architectural lessons from each one of these. And I feel like that initial vision sounds good and has been less successful than I expected it to be. And we've over time gone in a direction that's been more about giving people the practical tools that let them go do things. I'm kind of curious how do you think about that? Like how does the conceptual piece fit in? When and where should we be focusing on that, and to what degree should we just be giving people what feel
**中文：** 概念层面——Bonsai 是个 web 框架，但它同时也是对「增量计算」的入门，对吧？market data 是你需要的特定领域，但它也是在思考如何处理复杂的流式数据、如何构建模块化且高效的协议来良好地消费这些数据。每一个里面都有一堆架构层面的教训。我觉得最初这个愿景听起来很好，但实际效果没有我预期得那么好。多年下来，我们更多走向了「给人实用的工具，让他们能去做事」。我很好奇你怎么看这件事？概念那一块的位置在哪？什么时候、在哪些地方该聚焦概念，又在多大程度上应该直接

**[73:00 – 73:49]**
**EN:** like the most practically useful tools? Yeah, this is a very interesting difference in the Jane Street context, compared to say college courses — where in a college degree, maybe I'm teaching a databases course, and there's some domain knowledge about databases I want to impart, but as part of their university education I also want to teach them to be capable problem solvers, and how to work through ambiguity or try out different solutions — a lot of these general skills. And one of the great things about working at Jane Street is that my colleagues are very smart and capable, and I don't really need to use their time to teach
**中文：** 给人「感觉最实用」的工具？对，这在 Jane Street 的语境里是个很有意思的差异。相比大学课程——比如我在大学教一门数据库课，有些关于数据库的领域知识我想传授；但作为他们大学教育的一部分，我还想教他们成为有能力的问题解决者、如何在模糊中推进、如何尝试不同方案——很多这类通用能力。而在 Jane Street 工作的好处之一是，我的同事都非常聪明、能干，我并不真的需要花他们的时间

**[73:49 – 74:38]**
**EN:** them problem solving skills. They're already really good problem solvers. It turns out there's some selection effect there. And so this, I think, has biased the education away from what you might see in university — of "we're going to have you spend a bunch of time grappling with this tricky problem and figuring out a solution" — because actually when people are at their desk in their day-to-day job, that tends to be what they are doing. And it therefore can feel pretty unsatisfying to do that on a kind of canned educational thing, as opposed to something that's more directed at "here are useful tools that we're going to have you work through and understand," which you would
**中文：** 去教他们解决问题的技能。他们本来就是很强的问题解决者——这里面显然有筛选效应。所以我想，这使这里的教育偏离了大学里常见的那种「我们让你花大量时间去啃一个棘手的问题、并找出解法」——因为实际上人们在日常工位上做的事，往往就是这个。因此，在一件「罐装」的教育材料上做这件事，会让人觉得相当没有满足感；而更受欢迎的是「这里有一些有用的工具，我们会带你过一遍、弄懂它们」，然后你

**[74:38 – 75:27]**
**EN:** then go apply to the truly tricky problems. So I think you're right that there are some core conceptual things — like incremental computing and things like this — which we do want people to be exposed to and think about, but we tend not to do that by asking them to take on some particularly thinky piece of it and spend several hours having to come up with a novel solution to it. What you're saying here is even if a big part of your goal is to convey the conceptual lessons, it will work better if the way you do that is by teaching them concrete useful tools and focusing on those. And
**中文：** 再把它应用到真正棘手的问题上。所以我认为你说得对：确实有一些核心概念性的东西——比如增量计算之类——我们希望人们接触并思考；但我们往往不会通过「让他们接下一个特别烧脑的部分、花几个小时想出一个新颖解法」来做这件事。你这里说的意思是：即便你的目标很大一部分是传递概念性课程，只要你的做法是「教他们具体有用的工具、并聚焦在这些工具上」，效果会更好。

**[75:27 – 76:17]**
**EN:** like some lessons will sneak in that way, but not because you shaped it explicitly about that, but because understanding the tool and being able to use it required the understanding of those lessons. Yeah, I think that's right. And also teaching this conceptual knowledge just in a different way than you would in a say a university setting. And doing it more often in ways that look like a walkthrough of "let me take you through this kind of problem and how you would solve it." And you'll do some pieces, but how you will build the more complete understanding is when you actually go and apply this to the problems you're solving on the desk. So this is a little bit about some ways
**中文：** 有些课程会以这种方式「悄悄混进来」——不是因为你有意围绕它设计，而是因为「理解这个工具、并且会用」本身就要求你理解那些课程内容。对，我认为是这样。而且教这些概念性知识的方式，也和大学里不同：更常见的形式是「来，我带你走一遍这类问题、以及你会怎么解」。你会做其中一部分；而你形成更完整的理解，是在你真的把它用到工位上要解决的问题时。这就大致是

## 什么是「学习目标」？

**SECTION_NOTE**
- 做任何较大项目，都该先把「想达成什么」写下来。学习目标是一种特定写法：描述「因为你做的这件事，学生发生了什么改变」。
- 具体格式：「完成这门 teach-in 后，学生将能够……」再跟一串**主动动词短语**。
- 反面例子：「理解 property-based testing」——太含糊、无法衡量。正面例子：「能针对嵌套 record 类型的输入写出一个 property-based 测试」——具体、可界定复杂度。
- 它逼你想清楚：我到底想达成什么，以及**我不想达成什么**（哪些不是对学生的好安排）。
- 目标写清后，课程设计自然流出：先确定学生最终要能做的事 → 学生就该在课程里练习这些 → 再倒推需要什么背景材料／讲义／代码。
- 学习目标也让「评估」有了对象：Jane Street 更关心评估**课程本身有没有教会人**，而不是评分学生。它还有第二层意义——一种「学生最后会有什么不同」的心态，这也是他在面试潜在开发者教育者时很好用的提问。

**END_SECTION_NOTE**

**[76:17 – 77:07]**
**EN:** in which teaching at Jane Street is different from teaching the outside world. I feel like a thing I learned from you early on is about some of the ways in which lessons from the outside world apply here. So we talked a bunch about the testing teach-in. This was actually the first real project that you did here. And the way I remember it is we were trying to organize this testing teach-in before you started, and it was going badly [laughter] — a little bit because of this problem of it was hard to quite get enough of anyone's time. People were doing good work and focusing on various parts of it, but there wasn't a real effort to bring the whole thing together and make the whole thing good and land it. And I remember you asking me early on — because the shape of it was a thing I had come up with. And so you asked me, "So what are the learning goals?" And I was like, fascinating. What are learning goals? Like it sounds
**中文：** Jane Street 的教学与外面世界的教学不同的一些地方。我觉得我从你身上早期学到的一件事，是外面世界的某些经验在这里同样适用。我们聊了很多关于测试 teach-in 的事——这其实是你在这里做的第一个真正的项目。我记得的情形是：在你加入之前，我们正试着把这个测试 teach-in 组织起来，进展很糟，[笑声] 一部分原因就是这个「很难聚齐每个人足够时间」的问题。大家都在做不错的工作、各自盯着其中某些部分，但没有一个真正把整件事拢起来、把它做好、落地的努力。我记得你早期问我——因为它的整体形态是我提出的——你问我：「那么学习目标是什么？」我当时觉得：有意思。「学习目标」是什么东西？听起来这些词

**[77:07 – 77:57]**
**EN:** like English words that kind of make sense together, but clearly you mean it in a more specific way. And I found that to be, in the end, a very useful and insightful way of thinking about teaching. Maybe can you say a few more words about what are learning goals, and how should that affect how you design curriculum and build courses? Yeah. So when starting off on any larger project, it's good to write down what you are trying to accomplish. [laughter] And in this case, learning goals are a specific way of writing down what you want to accomplish, in terms of what is changing about the students as a result of the thing that you're doing. And specifically I find it very useful to write them in the form "after completing this teach-in, students
**中文：** 像都是英语词、凑在一起也说得通，但你显然是更特定的意思。最后我发现，这是一种非常有用、很有洞见的思考教学的方式。能不能再多说一点：什么是学习目标，它应该如何影响你设计课程、搭建课程？好。开始任何较大的项目时，都该把你「想达成什么」写下来。[笑声] 在这个场景里，学习目标是一种特定的写法：描述因为你要做的这件事，**学生身上发生了什么改变**。具体来说，我很喜欢用这种句式：「在完成这门 teach-in 之后，学生

**[77:57 – 78:46]**
**EN:** will be able to..." and then write down a bunch of active verb phrases. So for example, "understand property-based testing" is not a great learning goal, because that's very vague. It's not a specific thing that they're going to be able to do. How would you measure it? It's hard to know how you would measure it. But "students will be able to write a property-based test on, say, a nested record type input" — something concrete, scoping what is the complexity and the sort of thing they're going to be able to do. One that really forces you to structure your thinking about what am I actually trying to accomplish here, and importantly, what am I not trying to accomplish — like, what is not a good use of students' time
**中文：** 将能够……」然后写下一串**主动动词短语**。比如，「理解 property-based testing」不是一个好的学习目标，因为它非常含糊，不是一件他们「能做出」的具体事情。你要怎么衡量它？很难知道怎么衡量。但「学生将能够针对例如嵌套 record 类型的输入写出一个 property-based 测试」——这就具体了，界定清楚了复杂度、以及他们能做到的那类事情。这种写法会逼你把自己的思考结构化：我究竟想达成什么？而且同样重要的是：**我不想达成什么**——哪些并不是对学生时间的好安排？

**[78:46 – 79:36]**
**EN:** because it's not actually a goal to have them do this thing. But then in terms of the overall design of the educational program, once you have written down pretty specifically what you want people to do, or what you want people to be able to do afterward — well, it follows pretty directly what you should have them do in the thing that you're running, because they should practice the things that they're going to be able to do when they're at the end. And okay, now I know the exercises or activities I'm going to have them do. Okay, what is the background that they need to know for this? So what lectures or other materials or what parts of code would we want to provide them, for which writing those is not relevant to these goals? And so the whole process of developing some new piece
**中文：** 因为让他们做这件事本身并不是目标。而在整体的教育项目设计上，一旦你相当具体地写下了「你希望人们做什么」，或者「你希望他们之后能做什么」，那么「你在课程里该让他们做什么」就直接推导出来了——因为他们在课程里应当练习的，正是最后要能做到的那些事。好，现在我知道要让他们做哪些练习或活动了。那么接下来：为了做这些，他们需要什么背景知识？我们要给他们提供哪些讲义、其他材料或代码片段——而哪些部分的编写与这些目标无关（那就不用白写）？所以，开发一门新课程

**[79:36 – 80:26]**
**EN:** of curriculum sort of flows nicely out of having been disciplined in writing down these goals. And I feel like, to some extent, my education work at Jane Street has been going into different rooms with different people and saying the word "learning goals." [laughter] We should do this. Right. And the other thing that I found interesting about the learning goal idea is it tells you something about how you should think about evaluation. And here, we mostly are not so interested in our teaching stuff to evaluate the students. But you really want to evaluate the program — of, did the thing you do actually teach people anything useful? And so the idea that you could see whether or not at the end that people are able to do the thing that you wanted them to do is a way of evaluating yourself in your own work as an educator. Mhm. And I guess the other thing that I think
**中文：** 的整个过程，就会很顺畅地从「把目标写清楚」这个纪律动作里流出来。我觉得某种程度上，我在 Jane Street 的教育工作就是走进一个又一个房间、对不同的人说「学习目标」这个词，[笑声] 「我们应该做这个」。对。关于学习目标这个想法，我发现的另一件有意思的事是：它会告诉你该怎么看待「评估」。在这里，我们对教学这件事其实不太关心评估**学生**；但你非常需要评估**项目本身**——你做的这件事，到底有没有教给人有用的东西？所以，「你能看到最后人们是否能做到你希望他们做的事」，就是一种作为教育者对自己工作的评估方式。嗯。还有一件事我觉得

**[80:26 – 81:16]**
**EN:** was striking about it is that learning goals has now showed up for me as, in some sense, two different things. One is there's this somewhat more specific way of writing them out and thinking them through and using them to structure the program. And then there's also just the frame of mind of: how are the students going to be different at the end? Just, what are you even doing here? Why did you show up to work today? What are you trying to achieve? And I found actually that framing to be very useful in talking to potential developer educators — talking to people who we want to hire to do education work. I think some people have really thoughtful answers about what they were trying to achieve in the classes that they taught. And sometimes it was like, "oh, I just like this material, so I taught a course about it." And I don't want to complain too much. I think a lot of great classes are just like, someone is
**中文：** 很打动我的是：学习目标对我来说现在呈现出两层不同的东西。一层是那种更具体的写法：写出来、想透彻、用它来搭建整个项目。另一层则是一种心态：**学生最后会有什么不同？** 你到底在这里做什么？你今天为什么来上班？你想达成什么？我发现这层「心态」在与潜在的开发者教育者交谈时特别有用——就是和那些我们想招来做教育工作的人聊的时候。我觉得有些人对自己教过的课想达成什么，有非常深思熟虑的答案；而有时则是：「哦，我就是喜欢这个材料，所以开了一门课讲它。」我不想抱怨太多——我认为很多好课就是这样：

**[81:16 – 82:05]**
**EN:** excited about material and they teach it. And an enormous amount of good education is not about process, but is about charisma and ideas and being able to carry the performance through and really caring about the end results. But I do feel like the structure helps, and especially helps people who haven't done it before — people who are trying to figure out how to teach classes for the first time. I think it's a very helpful way of organizing your work and your thought. Mhm. And it forces you to focus on things that are not just in the students' head, to some extent — of, what am I trying to accomplish here, that isn't just "I tell the student a thing and now they know it." But yeah, how are
**中文：** 某个人对材料很有热情，然后他去教它。大量好的教育并不关于流程，而关于魅力、想法、能不能把这台「演出」撑下来、以及是否真的在乎最终结果。但我确实觉得这套结构有帮助，尤其是对没做过的人——第一次琢磨怎么开课的人。我认为它非常有助于组织你的工作和思考。嗯。而且它逼你把注意力放在某种程度上不只是「在学生的脑子里」的事情上——即：我到底想达成什么？而不只是「我讲给学生一个东西，于是他们就懂了」。而是，他们如何以

**[82:05 – 82:55]**
**EN:** they changed in some sort of observable way. So are there other aspects of the outside learning curricula and approach — the whole world of education, the whole world of research on education is complicated and messy, and also includes lots of conclusions that probably aren't true, and also lots of conclusions that we've known for a while that somehow don't get applied. Like there's all this crazy stuff about ways of teaching reading, where we had pretty good research telling us what to do and then a lot of not doing it for all sorts of messy reasons. And yet I think the learning goals is a nice example of there being real insight that comes out of the kind of whole intellectual stew of the educational world. Are there other pieces that you think of as really important and valuable that
**中文：** 某种可观测的方式发生了变化。那外面的学习课程与教学方法里，还有哪些方面——整个教育世界、整个教育研究界既复杂又凌乱，包含很多大概并不成立的结论，也包含很多我们早就知道、却不知为何没有被应用起来的结论。比如教阅读的方式有一堆离谱的东西：我们有相当不错的研究告诉我们该怎么做，然后因为各种乱糟糟的原因，很多都没有被实践。但我觉得「学习目标」正是一个好例子，说明教育界这锅「思想大杂烩」里确实能捞到真知。还有哪些东西你认为非常重要、有价值，

**[82:55 – 83:43]**
**EN:** you try and leverage here? Yeah, one that I've tried very deliberately to apply to the OCaml boot camp is what is sometimes called cognitive load, or you might call it working memory. Just, when you are trying to learn something new, there's actually a limit to how many new things you can handle at the same time before it becomes harder to learn any of them. And so in an older version of the OCaml boot camp, right away you were learning OCaml. You were learning an editor that perhaps you hadn't used before. And you were learning a version control and code review system that you also hadn't used before. And you were doing all of these from the jump. And one thing that I did was split these apart. So
**中文：** 会尝试在这里用起来？有。我有意应用到 OCaml boot camp 上的一个概念，叫「认知负荷」，或者你也可以叫「工作记忆」。就是：当你在学新东西时，你同时能处理的新事物数量其实是有限的；超过某个量，任何一项都变得更难学。所以在旧版的 OCaml boot camp 里，你一上来就要学 OCaml，同时还要学一个你可能没用过的编辑器，同时还要学一套你同样没用过的版本控制与代码评审系统——所有这些从第一天同时压上来。我做的一件事就是把它们拆开：

**[83:43 – 84:32]**
**EN:** you start off just learning OCaml syntax in Utop, the sort of command-line REPL, and now we have nice in-browser text editor boxes where you can run little snippets of OCaml. And then you go to a piece where you get introduced to your editor and you do some activities just with the version control system. And only after you've done each of these introductory pieces do you get to the part where you're bringing them all together. So kind of applying this cognitive load idea in that way. And I think the other thing that comes to mind, which I mentioned before, is this idea of active learning — of trying to make the educational activities not just someone telling you things, but as interactive as possible.
**中文：** 一开始你只在 Utop（那个命令行 REPL）里学 OCaml 语法，现在我们有很好用的浏览器内文本编辑框，可以跑小的 OCaml 片段；然后进入一个环节，认识你的编辑器，并只围绕版本控制系统做一些练习；只有把这些入门环节都做完之后，才会进入「把它们合在一起用」的阶段。这算是把认知负荷这个思路落地。另一件我想到的、前面提过的事，是「主动学习」这个理念——努力让教学活动不只是「有人跟你讲」，而是尽可能互动。

**[84:32 – 85:22]**
**EN:** And I think some of the new material that we have developed for the internship this summer is really applying this in some interesting ways: lots of small group discussions, or interactive activities around design, or practicing talking to stakeholders. Yeah, applying this idea of people actually interacting with other students as an important part of the educational process. Right. Again, leading into — this isn't just about conveying information. There's a big psychological element to people learning and retaining. That's right. So, maybe it's worth actually talking for a second about this point about the internship. So, you've been involved in what has been a pretty serious rework of the educational intro that people get to the firm. Can you
**中文：** 我认为今年夏天我们为实习项目开发的一些新材料，就很有意思地在落地这件事：大量小组讨论，围绕设计的互动活动，或者练习与「需求方」对话。对——把「学生彼此之间真的互动」当成教育过程中重要的一环。对。再强调一次，这不只是「传递信息」；人的学习和记忆里有很大一块心理因素。没错。所以也许值得花一点时间聊聊实习这件事。你参与了对新人入职教育的一次相当大规模的改造。

## 为 AI 重建实习生课程

**SECTION_NOTE**
- 触发点很直接：AI 工具现在太强了。过去给实习生安排四周项目、一个提示词就做完了，这样的项目既无法评估实习生、也不是有意义的产出。
- 于是把项目改成更开放、包含设计与需求收集等元素，也就是更「难」、更贴近真实工作；「能写出一批不错的代码」过去也许是最重要的信号，现在重要度下降。
- 新增训练：测试（为数据库应用写高质量测试套件）。测试一直重要，现在更重要——因为模型依赖反馈，超出简单范围后它不会一次给出好答案，你必须给它判断对错的方式。
- 新增设计文档评审练习、「角色扮演需求方」的需求收集活动；并首次让实习生做代码评审（加了三天专门培训：看预制 feature、写评审意见、对照参考答案、小组讨论，再互相评审）。
- 复盘：主要挑战来自任务范围过大——如果要求产出远超打磨时间的代码量，就无法传达「你拥有这段代码、必须仔细审」这一课。节奏与预期沟通同样重要；也发现「一上来强调多任务并行与 vibe coding」定错了基调，现在改为从「测试与高质量测试套件」入手。小规模「四人小组」的频繁讨论被证明非常有效。

**END_SECTION_NOTE**

**[85:22 – 86:11]**
**EN:** say a little bit more about what motivated that and what we've tried to do in that space? Yeah, so the sort of precipitating motivation was: wow, AI tools are really good now. [laughter] And you know, maybe the four-week project we used to have interns start off by doing — that's one prompt and you're done. And so that's not a useful way to evaluate an intern, or like productive work to ask an intern to do. And so okay, we're going to change the nature of the projects that interns are going to do, to be more open-ended, to maybe involve more elements of design or gathering requirements, things like this. Well, basically making them harder and more realistic.
**中文：** 能不能多说一点：改造的动机是什么，你们在那个方向上试图做什么？最直接的动因是：哇，AI 工具现在真的强了。[笑声] 你想，过去我们让实习生一上来做的那种四周项目——一个提示词就做完了。那既不是评估实习生的有用方式，也不是让实习生做的有意义的产出。所以，好，我们要改变实习生项目的性质：更开放，也许包含更多设计、需求收集之类的元素。基本上就是让它们更难、更贴近现实。

**[86:11 – 87:01]**
**EN:** Yes. And more going beyond "can you produce a reasonable amount of good code." Just producing the code used to be maybe among the most important signals, and it's less important now, I would say. And so aligning the projects with — these are the things we want to see people do successfully. And well, to set them up for success, we should try and teach them some more about how to approach this, how we think about this at Jane Street. And in addition, not just dump them into the deep end of "you have access to LLMs, good luck," but actually try and train them some on what to keep an eye out for, what are effective ways of working with these
**中文：** 对。而且不再只是问「你能不能产出合理数量的好代码」。单纯产出代码过去也许是最重要的信号之一，而现在我认为它没那么重要了。所以要把项目对齐到「这些是我们希望看到人们顺利完成的事」。而要让他们有成功的条件，我们就该多教他们一些：怎么着手这类事、在 Jane Street 我们怎么思考它。此外，不是把他们直接扔进深水区说「你有 LLM 使用权，祝好运」，而是真的训练他们一些东西：该警惕什么、和这些工具

**[87:01 – 87:50]**
**EN:** tools, what tools even exist at Jane Street and how do people use them. So the new materials have been a combination of giving people — and this is the balancing act that I was talking about earlier — tasks that are sufficiently complicated or large so the LLM doesn't just give you a perfectly fine version on the first try, but not too large that it's going to take you a week to work through all the code that's produced. And also taking this as an opportunity to focus on some new software engineering topics that maybe didn't get a lot of formal training at the start of the internship — like testing, kind of writing a very good test suite for this database-backed application, is
**中文：** 有效协作的方式是什么、Jane Street 到底有哪些工具、人们怎么用它们。所以新材料的组合是：给人足够复杂或足够大的任务——这就是我前面说的那种平衡——让 LLM 不会第一次就给出一个完全能用的版本，但也不至于大到你要花一周去读完它产出的所有代码。同时，也借此机会聚焦一些新加入的软件工程主题——这些在实习开始时也许没得到多少正式训练，比如测试：为这个背后有数据库的应用写一套非常好的测试套件，

**[87:50 – 88:40]**
**EN:** part of the new curriculum. And testing has always been important, but like in many ways more important now, because the models thrive on feedback — right, you really need to give them ways of figuring out whether or not the thing they are doing is right. They're not going to — when you get beyond relatively simple things, they're just not going to one-shot good answers. For sure. Yeah, it's been important, but there's always a balance of, well, we could spend half of the internship teaching people things, but we actually want them to spend most of their time working on a project. So, in this new world, we're like, okay, we're going to definitely invest more in education, but we still at some point need to get them starting to work on their projects. So there's also been new exercises around looking at design docs and judging what is a good design doc, looking at some bad ones and
**中文：** 这是新课程的一部分。测试一直很重要，但现在在很多方面更重要了——因为模型靠反馈活着：你确实需要给它们判断「做的对不对」的方式。超出相对简单的问题之后，它们就是不会一次给出好答案。确实。测试一直重要，但总要平衡：我们可以把实习的一半时间用来教学，但我们其实希望大家大部分时间在做项目。所以在这个新世界里我们说：好，教育上肯定要投更多，但某个时点还是得让他们开始做项目。此外还有一些新练习：看设计文档、判断什么是好设计文档，看一些糟糕的文档

**[88:40 – 89:29]**
**EN:** discussing the flaws, and more on this planning side of things. We developed a new activity where various full-timers role-play different stakeholders for this app that the interns are working on, and they talk to them and try and gather what are the requirements for what I would design. And then the final piece that I would mention is that we've talked about code review becoming a more central part of the job. And so we traditionally have not had interns review other people's code — at least that would be pretty uncommon. But this summer this is something that we're going to ask interns to do, and that we want to actually understand how well they perform at it. But to that end, we
**中文：** 并讨论其中的缺陷——更多落在「规划」这一侧。我们还设计了一个新活动：由若干全职同事扮演这个实习生正在做的应用的不同「需求方」，实习生去和他们谈，试着收集「如果我来设计，需求是什么」。最后要提的一块是：我们聊到代码评审判在变成工作中更中心的部分。传统上我们不安排实习生评审别人的代码——至少相当少见。但今年夏天，我们要请实习生做这件事，而且我们想真正了解他们做得怎么样。为此，我们

**[89:29 – 90:18]**
**EN:** actually have three additional days of training in the middle of the internship on code review, where the interns will see pre-made features actually adding functionality to the same application that they were doing the testing and design work on earlier in the system. And they are leaving code review comments, and then they are seeing a reference of "here is the answer key, here's a set of code review comments that someone might have left," and discussing as a group what they saw there, the ones that they disagree with. And then also implementing their own features and in turns reviewing each other's code, to give them some reps doing this, with the idea that then their
**中文：** 在实习中期安排了额外三天的代码评审培训：实习生会看到预先做好的 feature——给同一个应用（他们此前在测试和设计环节做的那个）加功能。他们要写代码评审意见，然后对照一份「参考答案」——也就是别人可能留下的那组评审意见——并小组讨论他们看到了什么、哪些他们不同意。接着他们还要实现自己的 feature，并轮流互相评审代码，以积累一些练习量。用意是之后

**[90:18 – 91:06]**
**EN:** mentors and their actual project will send them some features for review. So, this is a really big change both to the educational part of the internship and really to how the internship as a whole runs. How do you think it's gone? I think we're learning a lot. [laughter] I think a lot of the challenges that have come up are related to the scope of what we're asking people to do. So if we want people to generate code with LLMs and really hammer the message in "you own this code, you need to review it carefully, you need to get it into a good state, you don't just stamp whatever the LLM produced" — well, if we ask people to produce much more code than they have
**中文：** 他们的导师和真实项目会发一些 feature 让他们评审。所以这对实习的教育部分、乃至整个实习的运作方式，都是非常大的改变。你觉得效果如何？我觉得我们学到了很多。[笑声] 我认为出现的很多挑战都和「我们要求人做的事」的范围有关。比如，如果我们希望人用 LLM 生成代码，并且把「这段代码归你所有，你得仔细评审、把它带到良好状态，不能 LLM 产出什么你就盖章通过」这个信息真正砸进去——那么，如果我们让人产出的代码量远超他们

**[91:06 – 91:55]**
**EN:** time to polish, some sense that doesn't quite line up, and we're not communicating the lesson that we want. So I think we've learned a lot about what is the right scope for these different pieces, and similar with the code review — sending people too large a feature with too many problems, and it's hard for people to spot the issues that we actually want them paying attention to. It maybe goes to the cognitive load issues you were talking about before. Yes. So, I think there's been some challenges there. But I also think it has been really great to see this more interactive
**中文：** 打磨的时间，那在某种意义上就说不通了，我们也没有传达出想要的那一课。所以我认为我们学到了很多关于「各个环节合适的范围」是什么，代码评审也一样——给一个人一个过大、问题过多的 feature，他就很难识别出我们真正希望他注意的那些问题。这大概又回到了你之前说的认知负荷问题。对。所以那里有一些挑战。但我也觉得，看到这种更互动的

**[91:55 – 92:44]**
**EN:** form of education compared to, say, the OCaml boot camp the interns went through, is really great — because in that they're going at their own pace. They're getting code reviewed by a full-timer and discussing with them, but they're not necessarily doing a lot of talking to other interns about the material. But this new curriculum, interns are in these pods of four people, and it's explicitly structured with these small group discussions frequently throughout it — both "how are you using the LLM tools?" and "what problems are you seeing with the tests that it's spitting out to you?" And I think those discussions, including with full-time mentors, have been really productive, and I'm excited about anchoring a lot of our, at least
**中文：** 教育形式，对比实习生经历过的 OCaml boot camp，真的很好——因为在 boot camp 里他们是自定进度，由一位全职同事评审代码并讨论，但未必会和别的实习生就材料聊很多。而这个新课程里，实习生被分成四人一组，并且明确在全程频繁安排小组讨论：既有「你是怎么用 LLM 工具的？」，也有「它吐给你的测试里你看到什么问题？」。我认为这些讨论——包括有全职导师参与的——非常有成效，我也很期待把我们至少

**[92:44 – 93:34]**
**EN:** intern education in that sort of model. So, it sounds like next time you run this, you'll want to reduce the scope of some of the tasks people get. Are there any other changes you think you should make? So I think reducing the scope, but also there are adjustments to emphasis and pacing. So one thing that is always a challenge with programs like this is that people go through them at very different paces. How do you accommodate someone who's racing way ahead? You want useful things for them to do. And for people who are going through it more slowly, what do you actually have them focus on? So some of this is about being careful with the
**中文：** 很大一部分实习生教育建立在这种模式上。所以听起来，下次再办的时候，你会想缩减一部分任务的范围。还有其他你认为该做的改动吗？我认为要缩减范围，同时还要调整重点和节奏。这类项目永远的一个挑战是：人们走完它的速度差别很大。对跑得飞快的人，你怎么安排？你希望有对他们有用的事可做。对走得慢一些的人，你到底让他们把注意力放在哪？所以一部分是排期要谨慎，

**[93:34 – 94:24]**
**EN:** schedule, and also how we are messaging about what the expectations are — such that people are actually taking the time to learn from the things that we think are most important, and not trying to rush ahead to keep to some schedule. And I think there was — at least there are different groups of interns, and this whole curriculum has been evolving rapidly and significantly between each batch of interns as they start throughout the summer. But in an early one, we had an issue of starting out with a lot of emphasis on multitasking and sort of vibe coding stuff. I think we felt afterward that that was not the right place to start — to sort of set a bad tone for the rest of the exercise. And there's been some rearranging to it. We're actually going
**中文：** 以及我们怎么传达对预期的说明——好让人们真的花时间去学习我们认为最重要的东西，而不是为了赶某个进度表而抢着往前冲。还有一点：实习生分不同批次，整个课程在夏天每一批人开始时都在快速、显著地演进。但在早期某一批，我们的问题是：一上来就大量强调多任务并行、以及「氛围编程」那类东西。事后我们觉得，那不是正确的起点——它会为后面的整个练习定下不好的基调。于是做了一些重新安排。我们现在实际上

**[94:24 – 95:10]**
**EN:** to start with the testing focus piece and making this testing suite really high quality, and framing it around that, rather than "oh, you can have an LLM do three different things at once and it's cool." It is cool. [laughter] Yes. And I would want — I was talking earlier about thinking about different ways of working with these models and having people sort of checking in with what they're doing more often. And I think by next summer we might have a lot more considered ideas about this, or people have tried different things. I think it's very possible that we'll want
**中文：** 要从「以测试为重点」的那部分开始，把这个测试套件做到非常高水准，并围绕它来组织，而不是「哦，你可以让 LLM 同时做三件不同的事，很酷」。确实很酷。[笑声] 对。而且我希望能——我前面说过，要思考与这些模型协作的不同方式，让人更频繁地「检查一下自己在做什么」。我想到了明年夏天，我们对这件事可能会有更多经过深思的想法，或者大家已经试过不同做法。我觉得很有可能我们会想要

**[95:10 – 95:59]**
**EN:** to build more guidance into it — like, here are specific workflows to follow — whereas I think now it was, yeah, we have some things to know about ways in which these systems can misbehave and things to keep an eye out for, but not a lot about "we think this is the good way to prompt or interact with these systems." And this is another reason why these small group discussions were great, because people were sharing the different techniques that they were playing around with, and what was working well and what wasn't serving them, right? And I guess one of the challenges of this particular aspect of the world is it's just changing fast, and so knowing what advice to give — we can give some advice now, next year might need to be different advice.
**中文：** 往里加入更多指导——比如「这些是具体该遵循的工作流」——而我认为现在的情况是：我们有一些关于「这些系统会怎么出格」的注意事项和要警惕的东西，但没有太多关于「我们认为这是一种好的提示／交互方式」的结论。这也是小组讨论之所以很棒的原因之一：人们在分享自己试过的不同技巧、哪些效果好、哪些对他们没用。而且我想，这个世界这一块的一个挑战就是它变化太快；所以「该给什么建议」很难说：我们现在可以给一些建议，明年可能就得是另一套建议了。

**[95:59 – 96:35]**
**EN:** Not only is it changing fast, but two people using it in the same way might have it do different things. So when you give people an exercise that involves using an LLM, it just introduces much more uncertainty into what is going to happen when they do it than you would have had in the past. Right. All right. Well, maybe that's a good place to stop. Thank you so much for joining me. This is great. Thanks so much. You'll find a complete transcript of the episode along with show notes and links at signalsandthreads.com.
**中文：** 不仅变化快，而且两个人用同样的方式使用它，得到的结果可能也不一样。所以当你给人一个涉及使用 LLM 的练习时，它给「他们做的时候会发生什么」引入的不确定性，比过去大得多。对。好，那也许这里是个不错的收尾点。非常感谢你来做客，聊得非常好。非常感谢。你可以在 signalsandthreads.com 找到本期的完整逐字稿，以及 show notes 和相关链接。
