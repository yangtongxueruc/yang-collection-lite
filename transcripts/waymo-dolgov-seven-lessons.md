# Waymo 七条物理世界 AI 经验（中英对照逐字稿）

> Dmitri Dolgov（Waymo 联合 CEO）在 Startup School 的演讲。下方为按章节排列的逐段中英对照稿，时间戳依据 YouTube 官方章节线性插值。


## 开场：把 AI 带进物理世界
*Intro: Bringing AI Into the Physical World*

**[00:00 – 00:35]**

**EN:** Good afternoon, everyone. It’s great to be here. We talk a lot about AI that lives on your screen, lives in the digital world. Today I’d like to talk to you about a different kind of AI that we’ve been building at Waymo, AI that lives in the real physical world. How many of you, by the way, have been in a Waymo? Just raise your arms. Wow. Okay. That is impressive, especially since I understand many of you are out of town. For those who are visiting and have not had a chance to check out Waymo, I hope while you’re here in the Bay Area, you’ll give it a try. Since this is a startup school, I structured this presentation as a sequence of lessons—seven lessons that we’ve learned over the years at Waymo around what it takes to build and safely ship today’s most mature application of AI in the physical world, the Waymo Driver.

**中文：** 大家下午好。很高兴来到这里。我们平时谈论的，大多是在屏幕上、在数字世界里运行的 AI。今天我想和大家聊的，是我们在 Waymo 打造的另一类 AI——活在真实物理世界里的 AI。顺便问一句，在座有多少人坐过 Waymo？举起手来。哇，好厉害，尤其是我知道你们中很多人是从外地来的。来湾区参访、还没机会体验 Waymo 的朋友，希望你们趁此机会试一试。因为这是一场创业学校的活动，我把这次分享组织成了一连串的经验——七条我们在 Waymo 多年来总结出的经验，关于如何打造并安全地交付当今最成熟的物理世界 AI 应用：Waymo Driver。

**[00:35 – 01:10]**

**EN:** Let me start with a short video. This is a clip from a ride that I recently took in a Waymo with my kids. As you see here, we’re moving forward, proceeding through an intersection, and a couple of human drivers just decide to cut in right in front of us. The Waymo Driver reacted safely, reacted smoothly. In fact, so much so that my kids, who were preoccupied in the backseat, didn’t even notice that anything happened. To me, this was a pretty powerful moment. I’ve been working on this technology and this product for close to two decades, and it just did something fairly important. It acted safely. It kept my kids safe. It kept everybody safe, and nobody noticed. That, I think, will be a bit of a theme in general when it comes to physical AI: the best AI moments will look like nothing happened.

**中文：** 我先放一段短视频。这是前不久我带着孩子们坐 Waymo 的一段行程片段。大家可以看到，我们正在向前行驶，穿过一个路口，两名人类驾驶员突然插到了我们正前方。Waymo Driver 安全、平顺地做出了反应。事实上，反应如此平顺，以至于坐在后排、正忙着别的事的孩子们，根本没注意到发生了什么。对我来说，这是极具冲击力的一刻。我投身这项技术和产品已近二十年，而它刚刚做了一件相当重要的事——它安全地行动了，它保护了我的孩子们，保护了所有人，而没有人察觉。我认为这恰恰是物理 AI 的一个普遍主题：最好的 AI 时刻，看起来就像什么都没发生。

**[01:10 – 01:46]**

**EN:** It’s just the task got done safely and smoothly.

**中文：** 任务就那样安全、平顺地完成了。

**[01:46 – 02:21]**

**EN:** These moments where the Waymo Driver kept everyone safe are happening daily across our fleet. Today, the Waymo Driver is serving around 500,000 trips per week and driving over four million fully autonomous miles every week in 15 cities across the United States. For comparison, that’s over 300 years every week of an average American driver’s annual mileage. The Waymo Driver is accomplishing that with a superhuman safety record. So what does it take to build and deploy an AI agent in the physical world at scale? In Silicon Valley, there’s a common mantra to move fast and break things. However, when you’re dealing with atoms instead of bits, breaking things is not really okay. So the thing you have to do is move fast and ship safely.

**中文：** Waymo Driver 守护所有人安全的这些瞬间，每天都在整个车队中上演。如今，Waymo Driver 每周在遍布美国的 15 座城市里，完成约 50 万次行程，行驶超过 400 万英里的全自动驾驶里程。做个对比：这相当于普通美国人年驾驶里程的 300 多年，每周都在发生。Waymo Driver 以超人的安全记录达成这一切。那么，要在物理世界里大规模地打造并部署一个 AI 智能体，究竟需要什么？硅谷有句流行口号：快速行动，打破陈规。然而，当你面对的是原子而不是比特时，'打破'就真的不可接受了。所以你要做的，是快速行动，同时安全地交付。


## 为什么物理 AI 截然不同
*Why Physical AI Is Different*

**[02:21 – 03:06]**

**EN:** That’s a much more difficult thing to do. You have to build systems that are robust from day one. You have to build AI models and you have to build training recipes where safety is the foundation and not an afterthought, not an add-on. By the way, the problem itself of physical AI is different from digital AI. There are four main gaps that you have to contend with if you’re building AI for the physical world versus the digital world. First, there is the cost-of-errors gap. If you have a language model or a chatbot or a copilot and it makes a mistake, usually it costs you a retry. In the physical world, the cost of a mistake can be measured in human lives, not tokens. There’s simply not an undo and a retry button.

**中文：** 这是一件困难得多的事。你必须在第一天就构建稳健的系统。你必须构建 AI 模型、构建训练方法，把安全作为地基，而不是事后补丁、附加模块。顺便说，物理 AI 这个问题本身，就不同于数字 AI。如果你要为物理世界而非数字世界构建 AI，必须面对四道主要鸿沟。第一，是错误代价的鸿沟。如果你的语言模型、聊天机器人或副驾犯了错，代价通常只是一次重试。但在物理世界里，错误的代价要用生命来衡量，而不是 token。这里根本没有'撤销'和'重试'按钮。

**[03:06 – 03:51]**

**EN:** Secondly, you have the latency gap. Typically, when you’re running a VLM or a digital assistant, it can take many seconds, sometimes minutes, to come back with an answer. A car traveling at freeway speeds moves about a hundred feet in one second, so milliseconds really matter. You have to run all of your inference and make all of your decisions on board a compute that fits in the trunk of your car. Next, there’s the data gap. Digital AI had the internet—this wonderful, immense cache of pre-labeled human knowledge and human thought that we’ve ever assembled. There’s no digitized version of the internet for the physical world.

**中文：** 第二，是延迟的鸿沟。通常你运行一个视觉语言模型或数字助手时，它要花好几秒、有时几分钟才能给出回答。而一辆以高速行驶的汽车，每秒会移动约一百英尺，所以毫秒级都至关重要。你必须在能塞进汽车后备箱的计算单元上，完成所有推理和决策。接下来，是数据的鸿沟。数字 AI 拥有互联网——这个人类有史以来汇集的、经过预标注的庞大知识与人思维宝库。而物理世界，并没有一个数字化的'互联网'版本。

**[03:51 – 04:36]**

**EN:** And lastly, there’s the validation gap. In digital AI, often you can ship something that’s good enough and then let your users use your product. They find the edge cases, and that allows you to deploy on day one, practically at unlimited scale. Then you can just iterate and hill climb the quality from there. In physical AI, the situation is different. Given the high cost of errors, you need to have a very high level of safety and a very high level of confidence on day one before you deploy your first robot, before you drive your first autonomous mile. At the same time, when you’re dealing with physical AI, the actual experience of having your agent in the real world is invaluable and irreplaceable. These systems are not just something that you can build in the lab, get perfect, and then deploy at full scale overnight.

**中文：** 最后，是验证的鸿沟。在数字 AI 里，你常常可以先发布一个'够用'的东西，再让用户去使用你的产品。他们帮你发现边界情况，于是你第一天就能以近乎无限的规模上线，之后不断迭代、逐步提升质量。物理 AI 的情况则不同。鉴于错误代价高昂，在部署你的第一个机器人、开出第一英里自动驾驶之前，第一天你就必须拥有极高的安全性和置信度。与此同时，在物理 AI 中，让智能体真正身处真实世界的经验是无价且不可替代的。这类系统不是你能在实验室里造到完美、再一夜之间全面铺开的。

**[04:36 – 05:22]**

**EN:** Given those two factors, you really need to super clearly and super crisply define the operating conditions and the deployment parameters of your agent, and then build a rigorous framework to guide your deployment so that you can scale in a responsible manner. This is absolutely critical. This is how you earn trust from your customers, from the communities, from the regulators, and yourself.

**中文：** 鉴于这两个因素，你确实需要极其清晰、明确地界定智能体的运行条件和部署参数，然后建立一个严格的框架来引导部署，从而以负责任的方式扩展规模。这一点至关重要。你正是这样赢得客户、社区、监管者乃至你自己信任的。

**[05:22 – 06:07]**

**EN:** At Waymo, we see these gaps, of course, in the context of autonomous vehicles, but these gaps will show up in practically any non-trivial physical agent that we deploy in some shape or form. Driving is simply the first domain where AI has crossed these four gaps at scale with the public interacting with our product. So let’s dive into those lessons that we’ve learned over the years at Waymo from working on this problem and talk about how we address those gaps. I have seven lessons in this talk. They’re all technical. There’s a lot more that goes into building a company and building a product, but today I’ll just focus on the technical aspects of building AI for the physical world. Each one of those lessons, I think, by itself will not be exactly earth-shattering. A lot of it will overlap with things you’ve likely heard elsewhere.

**中文：** 在 Waymo，我们当然是在自动驾驶汽车的语境下看到这四道鸿沟的，但它们几乎会出现在我们以任何形式部署的、任何值得认真对待的物理智能体上。驾驶，只是 AI 首次大规模跨越这四道鸿沟、并与公众交互的领域。那么，让我们深入那些我们在 Waymo 多年来从解决这一问题中总结的经验，谈谈我们如何跨越这些鸿沟。今天的分享有七条经验，全是技术层面的。打造一家公司、一款产品当然还有更多内容，但今天我只聚焦于为物理世界构建 AI 的技术维度。我认为每一条经验单独看都不算石破天惊，其中很多会与你在别处听到的内容重叠。

**[06:07 – 06:52]**

**EN:** But I hope that the grounding of these lessons in our experience and some of the nuance that I can add about how they showed up in our experience of deploying a physical agent and scaling it safely will be interesting and useful for many of you who are in the space as you build your product, as you build your startup.

**中文：** 但我希望，这些经验扎根于我们的切身实践，加上我所能补充的、关于它们在我们的物理智能体部署与安全扩展过程中如何体现的细微之处，能对在座许多正在打造产品、创立公司的你们有所启发和帮助。


## 经验一：Demo 与产品之间隔着一条鸿沟
*Lesson 1: The Gap Between a Demo and a Product*

**[06:52 – 08:02]**

**EN:** So let’s dive in. The first lesson has to do with this massive, frustrating, sometimes soul-crushing difference between a demo and a real product. A working demo is 1% at best of the work that you have to do. The many nines of performance, the many nines of reliability that follow, that’s where the real work happens. If you’re a founder in the room, chances are you are focused on getting that first prototype, that first demo off the ground. When you hit that first version of a system that works, that first 90%, when the demo actually works, it feels incredible. You feel like you solved it, the sky’s the limit, you’re extrapolating forward. In our world, we hit that first milestone, that first 90% back around 2010. When this project started in 2009, before we started building the system, we set a couple of pretty ambitious goals for ourselves.

**中文：** 那我们进入正题。第一条经验，关涉 demo 与真正产品之间那种巨大、令人沮丧、有时甚至让人心碎的差距。一个能跑的 demo，最多只占了你全部工作的 1%。随之而来的、那许许多多个'九'级的性能与可靠性，才是真正的工作所在。在座若是创始人，很可能正专注于让第一个原型、第一个 demo 落地。当你做出第一个能跑的系统版本、那最初的 90%、demo 真正跑通时，感觉无比美妙。你会觉得问题已经解决，海阔天空，于是顺着势头往前推演。在我们这里，大约在 2010 年达到了那第一个里程碑——那最初的 90%。2009 年这个项目启动时，在动手搭建系统之前，我们给自己定下了几个相当宏大的目标。

**[08:02 – 09:13]**

**EN:** One was to drive 100,000 miles in autonomous mode. The second goal was to drive 10 routes, each one a hundred miles long, chosen to cover a variety of conditions across the Bay Area. We had to do each one from beginning to end without a human intervention. At the time, we had a team of about a dozen engineers and we accomplished both of these goals in about a year and a half. Keep in mind, this was well before any of the AI breakthroughs, before ConvNets, before Transformers, before VLMs, before any of the stuff that we talk about today. Yet we got it done. By demo standards, autonomous driving was solved in 2010. We handled everything. We could drive during the day, during the night. We handled traffic, pedestrians, cyclists, traffic lights, construction zones, on freeways, on surface streets. So we were “capability complete.” At the time, we felt like we were on top of the world.

**中文：** 其中一个目标是自动驾驶跑满 10 万英里。第二个目标是跑完 10 条线路，每条长 100 英里，需覆盖旧金山湾区的多种路况。每一条都必须从起点到终点、全程无任何人工接管。当时我们只有约十几个工程师，却用大约一年半时间完成了这两个目标。请记住，这远在任何 AI 突破之前——在卷积网络、Transformer、视觉语言模型、在今天被我们挂在嘴边的任何技术出现之前。然而我们做到了。以 demo 的标准，自动驾驶在 2010 年就已经'被解决了'。我们无所不能：白天能开、夜晚能开；能应对交通、行人、骑行者、红绿灯、施工区，能在高速也能在地面道路行驶。所以我们是'能力完备'了。当时我们觉得自己站在了世界之巅。

**[09:13 – 10:24]**

**EN:** But then, as we started building towards a product, we quickly ran into a brutal reality: there’s a massive difference between doing something once or driving 10 routes once and building a scalable service with nobody behind the wheel.

**中文：** 但随后，当我们开始朝产品迈进时，迅速撞上了一道残酷的现实：把一件事做一次、把 10 条线路各跑一次，与打造一个无人值守、可规模化的服务之间，存在着天壤之别。

**[10:24 – 11:34]**

**EN:** It took us about 10 more years to begin providing a service and then five more years to scale to half a million trips per week. The demo took 18 months; the product took about 15 years, but now we’re scaling exponentially. To date, we’ve served well over 20 million fully autonomous trips and we’ve driven well over 200 million fully autonomous miles. We have rider-only vehicles operating in 15 cities across the United States, and we’re scaling exponentially. It took us 15 years to get to that first hundred million miles and about seven months to drive the next hundred million. It took us about eight years to go from the time when we started our initial rider-only operation to the time when we were serving riders in four cities. Earlier this year, we launched four cities in just one day.

**中文：** 我们又花了大约 10 年才开始提供服务，再花 5 年才扩展到每周 50 万次行程。Demo 用了 18 个月；产品用了约 15 年，而如今我们正以指数级扩展。迄今为止，我们已完成远超 2000 万次全自动驾驶行程，行驶远超 2 亿英里全自动驾驶里程。我们的纯无人车在美国 15 座城市运营，且正指数级扩张。我们花了 15 年才跑完第一个 1 亿英里，而下一个 1 亿英里只用了约 7 个月。从最初开展纯无人运营，到覆盖 4 座城市，我们用了约 8 年；而今年初，我们仅在一天之内就新开 4 座城市。


## 可靠性活在「九」的指数阶梯上
*Why Reliability Lives on an Exponential Curve*

**[11:34 – 12:28]**

**EN:** So why does bridging that gap from demo to product take so long? Well, because there’s this harsh engineering reality that you can’t really cheat: reliability and performance live on this exponential ladder of nines. Getting to that first 90% or 99% is the easy part, but every next nine you want to add takes about ten times more effort. You need to know upfront exactly how many nines your product actually needs. A demo might need one nine, an assist product or copilot might need a few, but a fully autonomous AI agent that we’re going to be putting out in the physical world, engaging with the public and with kids running around, needs a whole stack of them. At scale, the long tail is the problem space—it’s your entire problem statement. When you drive millions of miles per week, a rare event that might happen once in a million miles just becomes your daily reality.

**中文：** 那么，为什么跨越从 demo 到产品的鸿沟要这么久？因为有一个你无法真正逃避的、冷峻的工程现实：可靠性与性能，活在这架'九'的指数阶梯上。达到最初的 90% 或 99% 是容易的部分，而每多要一个'九'，所需努力大约要翻十倍。你需要提前就精确知道你的产品究竟需要几个'九'。一个 demo 或许只需要一个九，一个辅助产品或副驾或许需要几个，但一个我们将投放到物理世界、与公众和奔跑的孩子打交道的全自主 AI 智能体，需要一整叠的'九'。在规模化之下，长尾就是你的全部问题空间——它就是你的完整命题。当你每周行驶数百万英里时，百万分之一概率的罕见事件，恰恰成了你的日常现实。

**[12:28 – 13:23]**

**EN:** Getting those next nines means doing something different every time. You don’t get to six nines of performance or reliability by doing the same thing you did to achieve the first two, just for longer. You have to do fundamentally different things. It requires a fundamentally different approach. For example, with reliability, you can get to the first couple of nines by just doing proper engineering and some bug fixes. But to get to the next few, you need to invest in fundamentally different approaches. You need to build fully redundant systems, have tiered fallback architectures, and so forth. The same thing holds for the performance of AI models.

**中文：** 要拿到那些后面的'九'，意味着每次都要做不同的事。你不可能靠把实现前两个'九'的那套做法延长时间，就达到六个'九'的性能或可靠性。你必须做根本不同的事，需要根本不同的方法。举例说，可靠性上，前几个'九'靠规范工程和修 bug 就能拿到；但要再往上，就得投入根本不同的方法——构建完全冗余的系统、分层降级架构等等。AI 模型的性能也是如此。

**[13:23 – 14:17]**

**EN:** What that actually means is that in this space, it’s incredibly easy to get started, but it can be excruciatingly difficult to get to the real product. That effect is only amplified with every wave of technological breakthroughs, which naturally leads to hype cycles. Every AI breakthrough—from deep learning to ConvNets to Transformers, VLMs, you name it—makes it that much easier to get started. Your demos and prototypes get a hundred times easier. But the tail, where the hard problems are, moves much less. It moves, but the effect is muted. That’s why every hype cycle produces a wave of absolutely spectacular demos and very few real products. The recurring mistake of every cycle is spending on the demo what you should be saving for the nines.

**中文：** 这其实意味着：在这个领域，起步容易得令人难以置信，但要抵达真正的产品却可能痛苦至极。每一波技术突破都会放大这种效应，自然也就催生了炒作周期。每一次 AI 突破——从深度学习到卷积网络、到 Transformer、视觉语言模型，随便你举——都让起步变得更轻松，你的 demo 和原型容易上百倍。但藏着重难点的长尾，却移动得少得多。它在动，只是效应被稀释了。这就是为什么每一个炒作周期都产出一波令人叹为观止的 demo，却只有极少数真正的产品。每个周期都在重复同一个错误：把本该留给'九'的投入，花在了 demo 上。

**[14:17 – 15:11]**

**EN:** Now, this being a startup school, the last thing I want to do is throw too much cold water on the magic and excitement of those early days. This time is absolutely magical. It’s amazing. Cherish it, leverage it. But the key is to remain honest about the product you’re building, the number of nines in performance and reliability that product demands, and not cut corners to get there. Otherwise, you might be in for a pretty rude awakening later. So count your nines before you count your demo views. This brings us to the second lesson: once you know how many nines your product actually needs, it fundamentally dictates the architecture and the core technical approach you need to pursue. Every technology has a performance versus effort curve. They all tend to start fairly steep and go up, and then they flatten out.

**中文：** 话说回来，既然这是创业学校，我最不愿做的事，就是给那些早期日子的魔力与兴奋泼太多冷水。那段时光绝对神奇，令人惊叹。请珍惜它、善用它。但关键在于，要对你正在打造的产品、对它所需的性能与可靠性'九'的数量保持诚实，并且不要抄近道去达成。否则，你日后可能会迎来相当粗暴的觉醒。所以，先数清你的'九'，再去数 demo 的播放量。这就引出第二条经验：一旦你知道产品究竟需要几个'九'，它从根本上决定了你必须追求的架构与核心技术路线。每项技术都有一条'性能—投入'曲线，它们往往先陡峭上升，随后趋于平缓。


## 经验二：选对技术曲线
*Lesson 2: Pick the Right Technology Curve*

**[15:11 – 16:05]**

**EN:** And as I just mentioned, every other nine gets an order of magnitude more difficult. A common failure mode is picking the tech that gives you the fastest early ramp, riding that steep curve, feeling like you’re winning, projecting that steep slope into the future and feeling like the sky is the limit, and then hitting the plateau and discovering that the technology path you picked actually flattens out way before the performance required by your product. You might still choose to be on that steep curve for a while for a variety of practical reasons. Maybe you want to prototype something, demo something, or build something in service of learning, but be honest with yourself about whether you’re building for the purpose of a demo, for the purpose of learning, or towards an actual product.

**中文：** 正如我刚才说的，每多一个'九'都要难上一个数量级。一个常见的失败模式，是选了那条让你早期爬升最快的技术，乘着那道陡坡、感觉自己在赢，把那条陡斜线外推到未来、觉得海阔天空，然后撞上平台期，才发现你选的技术路线，在你的产品所需性能之前很久就早早见顶了。当然，出于各种实际原因，你仍可能选择在那条陡坡上待一阵——也许你想做原型、做 demo，或为了学习而搭建什么。但请对自己诚实：你是为了 demo、为了学习，还是在朝着一个真正的产品前进。


## 为什么 Waymo 用摄像头 + 激光雷达 + 雷达
*Why Waymo Uses Cameras, LiDAR, and Radar*

**[16:05 – 16:55]**

**EN:** Let’s take an example from our domain: autonomous vehicles and sensing. There’s been a longstanding debate about what kind of sensors you actually need for autonomous driving. Naturally, more sensors mean higher performance, but also higher cost and higher complexity. Humans, of course, can drive with just eyes, so there’s that proof of existence. If the goal were to just approximately match human performance or to build an assist product, that’s a very reasonable way to go. However, if you are targeting full autonomy and superhuman, strongly superhuman performance, you find that weak sensing leads to a safety curve that flattens out way too early. At Waymo, we’ve taken an approach where we use multiple sensing modalities. We use cameras, LiDARs, and radars, and they all complement each other. Cameras give you high resolution and color, but they’re passive and degrade in darkness and glare.

**中文：** 以我们所在的领域为例：自动驾驶与感知。关于自动驾驶到底需要什么样的传感器，长久以来都有争论。自然，传感器越多意味着性能越高，但也意味着成本更高、复杂度更高。人类当然只用眼睛就能开车，所以'存在性证明'是成立的。如果目标只是大致匹配人类表现、或打造一个辅助产品，那这很合理。然而，如果你追求的是完全自动驾驶、以及超人、乃至强超人的表现，就会发现弱感知会导致安全曲线过早见顶。在 Waymo，我们采取多模态感知方案：摄像头、激光雷达、雷达三管齐下，彼此互补。摄像头提供高分辨率与色彩，但它是被动的，在黑暗和眩光下会退化。

**[16:55 – 17:46]**

**EN:** LiDAR gives you a direct measurement of the 3D structure of the world around you. Radar is very good at punching through environmental conditions and weather like fog, rain, or snow, and it can directly measure velocity using Doppler. LiDAR and radar are active sensors, so they see just as well in pitch darkness or, for example, when driving into a blinding sunset. These different sensing modalities are not backups to each other. In our stack, each modality has an encoder, and the information from all of those sensors gets fused into a single view of the world around us that is much more precise and generally vastly superior to what you get with any one sensor. Let me show you a few examples. Here’s a scene where a Waymo is driving in a dust storm in Phoenix. What you see here is what the scene looks like to our fairly advanced high-resolution and high dynamic range camera.

**中文：** 激光雷达直接测量你周围世界的 3D 结构。雷达非常擅长穿透雾、雨、雪等环境与天气，还能用多普勒效应直接测速。激光雷达和雷达都是主动传感器，所以在漆黑一片、或迎着刺眼夕阳行驶时，它们照样看得清。这些不同感知模态并不是彼此的备份。在我们的技术栈里，每种模态都有一个编码器，所有传感器的信息被融合成单一的世界视图，比任何单一传感器都精确得多、优越得多。我给大家看几个例子。这是 Waymo 在凤凰城沙尘暴中行驶的场景。你看到的，是我们相当先进的高分辨率、高动态范围摄像头眼中的画面。

**[17:46 – 18:36]**

**EN:** It’s very close to what a human would see in the same conditions, which is not much. On the right is what the LiDAR sees for the exact same frame, and you can much more clearly see that there’s a pedestrian standing on the side of the road. If they were to step onto the road, that early detection can make a really big difference in how the situation plays out and the safety of everyone involved.

**中文：** 这和人类在同样条件下看到的非常接近——也就是看不太清。右边是激光雷达在同一帧看到的画面，你可以更清楚地看到路边站着一名行人。如果他们踏上马路，这种早期探测会对事态发展、对所有相关人员的安全产生巨大影响。

**[18:36 – 19:26]**

**EN:** Here’s another example. At night, driving along, there are a couple of pedestrians who are about to jump onto the road over a concrete construction barrier. Again, at the bottom you see the camera—it really can’t see much. And the LiDAR view at the top. Again, LiDAR versus camera. Here’s another example. There are a couple of dogs chasing a ball and a couple of kids chasing the dogs. And big difference—here’s what it looks like to the camera. Here’s the LiDAR. The early detection of the kids is off to the side, and there are no headlights, there are no lamps there. It’s complete darkness. So it makes a big difference. Or think about what happens when something physically obstructs the view of your sensors.

**中文：** 再看一个例子。夜间行驶时，有几名行人正要翻越混凝土施工护栏冲上路面。同样，底部是摄像头——它几乎什么也看不清；顶部是激光雷达视图。又是激光雷达对摄像头。还有一个例子：几只狗追着球、几个孩子追着狗。差别巨大——这是摄像头看到的，这是激光雷达看到的。孩子们在侧边被提前探测到，而那里没有车灯、没有路灯，一片漆黑。所以差别非常大。再想想，当物理障碍物挡住传感器视线时会发生什么。

**[19:26 – 20:17]**

**EN:** If you don’t have redundancy in sensing and have a single leaf land on your sensors, it can bring your robot to a full stop. So you need redundancy. Redundancy, of course, does not necessarily mean multiple sensing modalities, but if you need redundancy anyway, you might as well benefit from the complementary physics of the different sensing modalities in the nominal case. So here’s a video of one of our cars that picked up a leaf—or actually, I think a full branch of a tree—that our wipers were unable to shake, and the car detected that. Because we have sensing redundancy, it was able to safely get back to the depot for proper cleaning.

**中文：** 如果你的感知没有冗余，一片叶子落到传感器上，就可能让机器人彻底停摆。所以你需要冗余。当然，冗余不一定意味着多种感知模态，但既然无论如何都需要冗余，那在常规情况下不如顺势利用不同模态在物理特性上的互补。这里有一段视频：我们的一辆车沾上了一片叶子——或者说，我觉得是一整根树枝——雨刮器甩不掉，车自己检测到了。因为我们具备感知冗余，它得以安全返回场站进行彻底清理。

**[20:17 – 21:07]**

**EN:** Specifically, when it comes to hardware, do not anchor to today’s component prices. We are on the sixth generation of the Waymo Driver, the Waymo hardware suite today. With every generation, the hardware not only delivered amazing capability, but we were able to drastically simplify and radically reduce the cost of the hardware as well. So betting your company, betting your approach on today’s hardware prices, is just betting your company on a number that has a fairly short shelf life and is going to expire. Hardware will change. Many components will get commoditized and drop in price. So design for that future and be ready to upgrade.

**中文：** 具体而言，在硬件上，不要锚定今天的元器件价格。我们现在已经到了第六代 Waymo Driver、也就是今天的 Waymo 硬件套件。每一代，硬件不仅带来了惊人的能力，我们也得以大幅简化、并从根本上降低硬件成本。所以，把你的公司、你的路线押在今天的硬件价格上，无异于把公司押在一个保质期很短、注定会过期的数字上。硬件会变，许多元器件会被商品化、价格下跌。所以要为那个未来而设计，并随时准备升级。


## 经验三：踏准每一波技术浪潮
*Lesson 3: Ride Every Technology Wave*

**[21:07 – 22:01]**

**EN:** That brings us to the next lesson, lesson number three. Technology moves incredibly fast, especially nowadays. So you need to be ready to ride those tech waves and do that repeatedly. And when you do, you have to not only think about the wins in performance and the wins in capability, you have to be very mindful about unification and simplification. Over the years, we’ve seen a number of major breakthroughs in technology, a lot of them around AI. With every wave of innovation, we pretty much rebuild the Waymo Driver around that major wave of AI breakthroughs. We often push the state of the art in those areas forward ourselves. We leveraged convolutional networks around 2013 for computer vision and perception. Then, when transformers came about around 2017, we bet big on them both for perception and for the task of behavior prediction and decision making and planning.

**中文：** 这就引出下一条、也就是第三条经验。技术以惊人的速度发展，尤其如今。所以你需要准备好乘上那些技术浪潮，而且要反复地乘。而在这样做时，你不仅要考虑性能与能力的收益，还必须非常在意统一与简化。多年来，我们见证了多次重大技术突破，其中很多围绕 AI。每一波创新，我们几乎都围绕那次重大的 AI 突破重建了 Waymo Driver。我们往往还亲自把那些领域的前沿向前推进。大约 2013 年，我们用卷积网络做计算机视觉与感知；之后，2017 年前后 Transformer 问世，我们在感知以及行为预测、决策与规划任务上，对它下了重注。

**[22:01 – 22:55]**

**EN:** Turns out the task of driving is not that dissimilar from the task of modeling language because of the social aspects of driving. You’re having a conversation with other dynamic actors in the world, but you’re doing that in the space of body language of your agent, your car, as opposed to just the language of words. You operate in sequences, and local continuity matters, but so does global context. Today we’re leveraging the latest in VLMs and frontier world models. Now, using the latest tech for capability and performance wins—I don’t want to say it’s easy, but it can be reasonably straightforward. Doing applied research in isolation or starting a tiger team to prototype some new technology is not the most difficult part. There are many companies, many teams that are excellent in this. The much harder muscle to build is to carry that bleeding-edge research into production and deploy it in a safety-critical environment without regressions, and do it without breaking stride on the scaling of your product.

**中文：** 结果发现，由于驾驶的社会属性，驾驶这件事与语言建模并不那么不同。你是在和世界上其他动态参与者'对话'，只不过这场对话用的是你的智能体——你的车——的肢体语言，而非单纯的文字语言。你在序列中运作，局部连续性很重要，全局上下文也同样重要。如今我们在利用最新的视觉语言模型与前沿世界模型。用最新技术换取能力和性能——我不想说这很容易，但它可以相当直接。孤立地做应用研究、或组建一支突击队去原型化某项新技术，都不是最难的部分。许多公司和团队都擅长这个。真正难练的肌肉，是把那些尖端研究带进生产环境、部署到安全至上的场景中而不产生回退，并且在产品扩张的节奏上不掉链子。

**[22:55 – 23:49]**

**EN:** Adding capability, again, is not the hardest part, but adding capability while at the same time reducing fragmentation and reducing complexity—that is really important. Finally, the hard muscle to build as a company is to be able to do that repeatedly through multiple waves of technical innovation and technical breakthroughs. So on this front, I have two bits of advice. The first one: when a new technology shows up, it can be very exciting, very tempting to kick off a new effort, a tiger team to pursue it. And that’s great. You should absolutely do that. However, when you do, it’s very important that you consider what you would do after, under a success scenario. Let’s say that effort succeeds. You should be very clear on what the path of that new innovation is for your company, for your entire product, for your entire system.

**中文：** 再次强调，增加能力不是最难的部分，但一边增加能力、一边降低碎片化与复杂度——那才真正重要。最后，作为一家公司最难练的肌肉，是能在多波技术创新与突破中反复做到这一点。在这点上，我有两条建议。第一：新技术出现时，很令人兴奋，也很诱人去启动一个新项目、一支突击队去追逐它。这很好，你绝对该这么做。但与此同时，非常重要的一点是：要考虑成功后你会怎么做。假设那个项目成功了，你必须非常清楚，这项新创新对你的公司、对整个产品、对整个系统意味着怎样的前进路径。

**[23:49 – 24:43]**

**EN:** Oftentimes I’ve seen a failure mode where a project, a very difficult technical project, succeeds, and then there’s a dead end. That can be very wasteful, that can be completely deflating. The second bit of advice I have here is when pursuing new tech, again, don’t just ask, what does this new tech give me in terms of capability and performance? Also ask, has it simplified my stack? And has it led to fragmentation or unification? Set your launch bar to demand both breakthrough performance and, at the same time, radical simplification and unification.

**中文：** 我常见一种失败模式：一个非常难的技术项目成功了，然后走进了死胡同。这极其浪费，也令人彻底泄气。我的第二条建议是：在追求新技术时，同样不要只问'这项新技术在能力和性能上给了我什么'，还要问'它简化了我的技术栈吗？它带来的是碎片化还是统一？'把你的上线门槛设为：既要突破性的性能，又要彻底简化与统一，二者缺一不可。


## Waymo 基础模型：架构拆解
*Inside the Waymo Foundation Model*

**[24:43 – 25:37]**

**EN:** This exact philosophy and this muscle that we’ve built at Waymo over the years is what produced our latest core technology. The heart of it is the Waymo Foundation model. Now, the Waymo Foundation model is a multimodal world action language model. It’s kind of a mouthful, so let me unpack the ingredients. It’s a multimodal model because it is able to process these multimodal sensor inputs: cameras, LiDARs, and radar. It’s a world model because it inherently understands how the world works—the physics, the dynamics, as well as the social and semantic aspect of it. It’s an action model because we are not just passively observing how the world evolves; we’re an active participant. So the model needs to understand the effects of the actions of our agent on the world and be able to tell the good ones from bad ones. And finally, it’s aligned with language.

**中文：** 正是这种理念、以及我们在 Waymo 多年来练就的肌肉，催生了我们最新的核心技术。其核心就是 Waymo 基础模型。Waymo 基础模型是一个多模态世界—动作—语言模型。这有点拗口，让我拆开来说。它是多模态的，因为它能处理多模态的传感器输入：摄像头、激光雷达和雷达。它是世界模型，因为它从本质上理解世界如何运作——物理、动力学，以及社会与语义层面。它是动作模型，因为我们不只是被动观察世界如何演化，而是积极的参与者。所以模型必须理解我们智能体的动作对世界的效应，并能分辨好坏。最后，它与语言对齐。

**[25:37 – 26:32]**

**EN:** And that allows us to unlock general world knowledge from visual language models. That’s incredibly useful in the long tail of rare semantic situations. More specifically, this is what the architecture looks like. It’s your typical encoder-decoder architecture. The encoder part takes in the multimodal sensing and compresses or encodes it into an efficient representation that retains all of the relevant data, all of the relevant information for the generative part, or the decoder. It’s an end-to-end model, which has a couple of nice properties. It allows us to effectively backpropagate the gradient from the task that we actually care about all the way to the early layers of the model. It allows the encoder to learn the right rich representations for what the generative part needs to solve the task. It uses a system one, system two, “think fast,” “think slow” architecture, and it leverages the general world knowledge of VLMs for efficient learning of semantic tasks.

**中文：** 这让我们得以从视觉语言模型中解锁通用的世界知识——在罕见语义情况的长尾里，这极其有用。更具体地说，架构是这样的：典型的编码器—解码器结构。编码器部分接收多模态感知，将其压缩或编码成高效的表征，保留生成部分（即解码器）所需的所有相关数据、所有相关信息。它是一个端到端模型，具备一些优良特性：让我们能把真正关心的任务的梯度，有效地反向传播到模型最早期的层；让编码器为生成部分求解任务学到恰当的丰富表征。它采用系统一、系统二的'快思考、慢思考'架构，并借助视觉语言模型的通用世界知识，高效学习语义任务。

**[26:32 – 27:26]**

**EN:** Let’s dive deeper. First, the “think fast” path. That part fuses the raw data from our cameras, our LiDARs, our radars, and that allows for split-second, safety-critical decisions. You can think of it as your driving instincts. This is what allows the car to brake instantly if, for example, a pedestrian runs into the road or a cyclist nearby swerves into your path. This is, if you will, the lizard brain of your agent that deals with a lot of geometric tasks and can react in milliseconds. Second is the slow path. That’s the part responsible for the more complex semantic and scene-level understanding type tasks. These tasks don’t typically change in milliseconds, so there you can afford a bit more latency and trade that off for higher capability and higher levels of reasoning.

**中文：** 我们深入一点。首先是'快思考'路径。这部分融合来自摄像头、激光雷达、雷达的原始数据，从而做出分秒必争、关乎安全的决策。你可以把它想成驾驶本能。正是它让车能在行人冲入马路、或附近骑行者突然切入时瞬间刹车。如果你愿意，这是你的智能体的'蜥蜴脑'，处理大量几何任务，能在毫秒内反应。第二是'慢思考'路径。这部分负责更复杂的语义与场景级理解类任务。这些任务通常不在毫秒间变化，所以你可以承受多一点延迟，用它换取更强的能力和更高水平的推理。

**[27:26 – 28:20]**

**EN:** For example, if the Waymo Driver encounters a situation where there’s a vehicle on fire on the side of the road, the fast path might just see it as a generic obstacle and reason that the path ahead is clear. This is where the slow path comes in. That path can use deep semantic reasoning to understand the semantics of that object—the car being on fire—in the broader scene context. That allows our driver to decide to take a very different action or a different route entirely, even if geometrically the path ahead is clear.

**中文：** 例如，若 Waymo Driver 遇到路边一辆车着火的情况，快思考路径可能只把它当成一般障碍物，判断前方道路畅通。这时就需要慢思考路径出场。它能用深层语义推理，在更广阔的场景语境中理解那个物体——着火的车——的语义。这让我们的 Driver 即使在前方几何上畅通时，也能决定采取截然不同的动作，或干脆换一条完全不同的路线。

**[28:20 – 29:15]**

**EN:** Finally, there’s the generate component—the decoder. That’s the component that understands and can produce behavior. It understands how other actors behave and allows us to make predictions and plan our own driving decisions. Our Waymo Foundation model powers the Waymo Driver that runs on different generations of hardware and on different vehicle platforms. You have our fifth generation and sixth generation, the Jaguar I-PACE, the Ojai, and the Hyundai Ioniq. In the future, we’ll power different products and different commercial applications like trucking and personally owned vehicles. By leveraging the strategy of focusing on the high-capacity foundation forward model, we’re able to move a lot of complexity upstream to that large shared foundation. That allows us to make the specialization layer that’s running on the car pretty lightweight. In turn, that allows us to speed up the development process.

**中文：** 最后是生成组件——解码器。它是理解并能产生行为的组件：理解其他参与者如何行为，让我们得以预测并规划自己的驾驶决策。我们的 Waymo 基础模型驱动着运行在不同代硬件、不同车辆平台上的 Waymo Driver。包括我们的第五代、第六代，捷豹 I-PACE、Ojai，以及现代 Ioniq。未来，它还会驱动卡车运输、私家车等不同的产品与商业应用。通过聚焦高容量基础前向模型的策略，我们把大量复杂度上移到那个共享的大基础模型上，从而让车端运行的专门化层相当轻量。这反过来又加快了开发进程。

**[29:15 – 30:09]**

**EN:** So the most important muscle in this lesson is for your company to not just leverage the tech of the day, but have the ability and build that muscle to repeatedly ride those tech waves and pull in the results of that innovation into production without regression, without breaking stride in deployment and scaling, and without drowning in complexity. So let’s move to the next lesson.

**中文：** 所以这条经验里最重要的肌肉，是让你的公司不只是利用当下的技术，还要具备、并练出反复乘上技术浪潮、把创新成果纳入生产环境的能力——不回退、在部署与扩展上不掉节奏、也不被复杂度淹没。那么，我们进入下一条经验。


## 经验四：苦涩的教训依然成立
*Lesson 4: The Bitter Lesson Still Wins*

**[30:09 – 30:58]**

**EN:** There is a well-known lesson in the AI community that general methods that leverage massive compute and massive data will always beat methods that rely on handcrafted, engineered human knowledge. That’s the so-called bitter lesson that Richard Sutton published and formulated in 2019. We have lived this and we have seen this in every wave of technical breakthroughs. Each time, the bitter lesson holds: methods that scale best with compute and data always win out. And by the way, this is one of the reasons why we bet on the approach of building the foundation model. There is a well-known property that if you bet on a high-capacity model and you use your data and your compute on that, you just get better scaling laws, and then you distill into smaller, more efficient models that are running on your agent in real time. You just get better scaling laws as opposed to just focusing on the smaller models directly.

**中文：** AI 界有个著名的教训：能利用海量算力和海量数据的通用方法，终将击败依赖人工设计、工程化人类知识的方法。这就是 Richard Sutton 在 2019 年提出并阐述的'苦涩的教训'。我们亲身践行、也在每一波技术突破中见证了它。每次，苦涩的教训都成立：最能随算力和数据扩展的方法，总会胜出。顺便说，这也是我们押注于构建基础模型路线的原因之一。有个公认的特性：如果你押注高容量模型，把数据和算力投在上面，就会得到更好的扩展定律，然后再蒸馏到更小、更高效的、在智能体上实时运行的模型。相比直接只盯小模型，你得到的是更优的扩展定律。

**[30:58 – 31:47]**

**EN:** So one nuanced area where this lesson shows up is the use of structure in your models. Depending on how you use your structure, you can end up on either side of the bitter lesson. Essentially, structure that fights scale will always lose, and structure that channels scale always wins. In particular, this comes up around the discussion of end-to-end models. As I mentioned, an end-to-end model has some very nice properties. You backpropagate gradient from the final tasks all the way through the model, and it allows the API between the encoder and the decoder to use rich learned representations. Those are the easiest models to build and train.

**中文：** 那么，这条教训体现得微妙的一个领域，是模型中结构的使用。取决于你怎么用结构，你可能站在苦涩教训的任一侧。本质上，对抗扩展的结构终将落败，而疏导扩展的结构总会赢。这一点尤其在端到端模型的讨论中凸显。正如我所说，端到端模型有一些很好的特性：你把最终任务的梯度反向传播穿过整个模型，让编码器与解码器之间的接口得以使用丰富的学习表征。它们是最容易构建和训练的一类模型。

**[31:47 – 32:36]**

**EN:** The architectures are known. You can start with doing some imitation learning, and a black box end-to-end model will give you very rapid progress, and you will ride that very initial steep part of the curve. For some products, that’s enough. But if you need to reach superhuman levels of performance in a fully autonomous agent in a safety-critical environment, just doing that basic vanilla end-to-end is not enough. This is where structure comes in. The key question here is, does the structure boost scale or does it fight it? Does it limit and constrain your solution space, or does it help you scale without loss of generality? Let me give you an example. Let me illustrate this point with a simple thought exercise and a toy problem. Imagine you are building a robot that will play the game of Go.

**中文：** 架构是现成的。你可以从模仿学习起步，一个黑盒端到端模型就能给你飞速进展，让你乘上曲线最开头的那段陡坡。对某些产品，这就够了。但如果你要在安全至上的环境中达到全自主智能体的超人级表现，只做那种基础的原生端到端并不够。这时结构就该登场。关键问题是：结构是在助推扩展，还是在对抗它？它是在限制、约束你的解空间，还是在无损通用性的前提下帮你扩展？我举个例子，用一个简单的思想实验和玩具问题来说明。想象你在造一个要下围棋的机器人。

**[32:36 – 33:25]**

**EN:** And you want it to play the game in the physical world. So you have a camera that’s observing the board and you have an actuator that will actually move the pieces around. One way you can build such a robot is to have an end-to-end system that goes directly from pixels to actuation. Maybe you train it by giving it some videos of how humans play the game. That could be a very interesting research exercise. However, if your goal was to build the world’s best playing Go robot, that’s probably not the most efficient way to go. The reason for that is that there is a very simple intermediate representation that completely captures the state of the game, the state of the task you’re trying to solve. It’s a 19 by 19 board, and that gives you a fully observable and complete state of the world that you care about, at least for the game-playing part.

**中文：** 而且你想让它在物理世界里下棋。所以你有个摄像头观察棋盘，有个执行器真正去挪动棋子。构建这种机器人的一种方式，是做一个从像素直接到动作的端到端系统，也许你给它看些人类下棋的视频来训练。那会是个很有趣的研究练习。但若你的目标是造出世界上棋力最强的围棋机器人，这大概不是最高效的路子。原因在于：存在一个极其简单的中间表征，能完整刻画游戏状态、即你要解决的任务状态——那就是 19×19 的棋盘，它给出了你所关心的世界的、完全可观测且完备的状态，至少在'下棋'这部分如此。

**[33:25 – 34:14]**

**EN:** Leveraging that structure doesn’t limit your model. It doesn’t constrain your solution space, but it gives you a very helpful way to scale. Now, that of course was a toy example. Anything that’s not trivial that you’re trying to deploy in the physical world will not have that property. The fact that such a simple, clean engineered representation doesn’t exist in the physical world is the whole reason why we need end-to-end systems and learned representations and learned embeddings. But in the physical world, there does exist structure. You have laws of physics, you have rules of the road, you have objects that behave in reasonably predictable ways. You can use that structure in addition to the learned representations to boost your performance, simplify validation, and at the end of the day, just get better scaling laws.

**中文：** 利用这种结构不会限制你的模型，不会约束解空间，却给了你一种极有助于扩展的方式。当然，那只是个玩具例子。任何你要在物理世界里部署的非平凡系统，都不会有这种性质。物理世界中不存在那样简单、干净的工程化表征，这恰恰是我们需要端到端系统、需要学习表征与学习嵌入的全部原因。但在物理世界里，结构确实存在：有物理定律、有道路规则、有以相当可预测方式运动的物体。你可以在学习表征之外，利用这种结构来提升性能、简化验证，并最终获得更优的扩展定律。


## 结构增强端到端
*Structure-Augmented End-to-End*

**[34:14 – 35:03]**

**EN:** This is the approach that we are pursuing at Waymo, which we call structure-augmented end-to-end. We go beyond the basic vanilla end-to-end by augmenting the learned embeddings with materialized structured representations. That gives us a few very important advantages. First is validation at inference time. Because the model isn’t just a black box where sensors go in and actuation commands go out, we can create a very powerful correctness and safety validation layer that you can run in real time when the agent is deployed on our vehicles. This is really important for any agent that’s operating in the physical world.

**中文：** 这就是我们在 Waymo 所走、并称为'结构增强端到端'的路线。我们在基础的原生端到端之上，用显式化的结构化表征来增强学习到的嵌入。这带来了几个非常重要的优势。第一是推理时的验证。因为模型不再只是'传感器进、动作指令出'的黑盒，我们就能构建一个非常强大的正确性、安全性验证层，在智能体部署到车辆上时实时运行。这对任何在物理世界运作的智能体都至关重要。

**[35:03 – 35:52]**

**EN:** Secondly, we get great wins in efficiency when it comes to large-scale training and evaluation of the generative part of the model, the decoder. If all you have is a black box end-to-end system, you are forced to do all of your evaluation and all of your training in the end-to-end setup, all the way from sensors to decisions to actuation. Having that intermediate structured representation allows you to mix and match. You can do some training at larger scale and some evaluation in the space of those compact structured representations, and some in the full space of end-to-end from sensors to decisions. Finally, we get strong, verifiable feedback signals for both evaluation and for training, training recipes to support things like reinforcement learning. That additional materialized structure just gives you much more powerful tools for evaluation, for metrics, as well as crafting your loss function or reinforcement learning recipes.

**中文：** 第二，在模型生成部分（解码器）的大规模训练与评估上，我们获得了巨大的效率收益。如果只有黑盒端到端系统，你就被迫在端到端框架里完成所有评估与训练——从传感器一路到决策再到动作。而有了那个中间结构化表征，你就能混搭：一部分在更大规模上训练、一部分在那些紧凑结构化表征的空间里评估，一部分在从传感器到决策的完整端到端空间里进行。最后，我们为评估和训练都获得了强而可验证的反馈信号，足以支撑强化学习之类的训练方法。那份额外显式化的结构，只是给了你更强大的工具——用于评估、用于指标，也用于设计损失函数或强化学习方案。

**[35:52 – 36:41]**

**EN:** So the lesson here is to bet on a system that’s maximally learned and minimally constrained, and leverage structure intentionally to boost performance and scaling laws, both in training and in evaluation.

**中文：** 所以这里的经验是：押注一个最大化学习、最小化约束的系统，并有意识地利用结构，在训练和评估两端都提升性能与扩展定律。


## 经验五：每个物理 AI 公司都需要仿真器
*Lesson 5: Why Every Physical AI Company Needs a Simulator*

**[36:41 – 37:30]**

**EN:** Now that raises the question of how do you actually train and evaluate your physical AI agent? And that brings us to the next lesson. To build and safely deploy an agent in the physical world, it is absolutely critical to have a good large-scale, realistic, high-fidelity simulator. Now, there are two ways you can do training and evaluation: you can do open loop and you can do closed loop. In open loop, you are passively observing input to output pairs. You can use that for evaluation or for training—imitation learning works like that. Evaluation usually takes the shape of, if you find yourself in this situation, what would you do? And then you score that. That’s in contrast with closed loop, where you take an action, you see the effect that action has on the world, then you update through your sensors the view of the world, take another action, and so on. You evaluate and train on those sequences of actions and sequences of world evolutions.

**中文：** 这就引出问题：你究竟如何训练和评估你的物理 AI 智能体？这也把我们带到下一条经验。要在物理世界构建并安全部署一个智能体，绝对关键的是拥有一个好的、大规模的、真实的高保真仿真器。训练和评估有两种方式：开环与闭环。开环中，你被动地观察输入—输出对。你可以用它做评估或训练——模仿学习就是如此。评估通常形如：'若你身处此情境，你会怎么做？'然后打分。这与闭环相反：你采取行动，观察该行动对世界的效应，再通过传感器更新对世界的视图，采取下一个行动，如此往复。你在那些行动序列与世界演化序列上做评估与训练。

**[37:30 – 38:19]**

**EN:** Now, the ability to take an action and evaluate that counterfactual is absolutely vital for building and deploying safety-critical agents in the physical world.

**中文：** 如今，采取一个行动并评估其反事实（counterfactual）的能力，对构建和部署物理世界里安全至上的智能体而言，绝对不可或缺。

**[38:19 – 39:08]**

**EN:** So a real simulator is how you do that. And a real simulator isn’t just some lightweight tooling that sits next to your AI. It is a big AI model in and of itself. The problem of building a good, realistic simulator is just as hard as building the agent itself. The AI behind the simulator really needs to understand how the world works—the physics, the semantics, the traffic, the weather, and so on. The quality of that simulator has to be high enough so that it doesn’t only look good, but it’s sufficient to train and evaluate with high confidence an agent that you’re going to be putting in the world in a safety-critical environment. In other words, you have to build a highly accurate generative world model. At Waymo, for years we’ve been building what we called behavioral world models.

**中文：** 所以，真正的仿真器就是做这件事的途径。而真正的仿真器，不只是 AI 旁边那些轻量的工具。它本身就是个大 AI 模型。构建一个好而真实的仿真器，难度不亚于构建智能体本身。仿真器背后的 AI 真的需要理解世界如何运作——物理、语义、交通、天气等等。那个仿真器的质量必须足够高：不仅要好看，更要足以让你对即将投放到安全至上环境中的智能体，高置信度地训练和评估。换言之，你必须构建一个高精度的生成式世界模型。在 Waymo，多年来我们一直在构建所谓的'行为世界模型'。

**[39:08 – 39:58]**

**EN:** We were doing that way before the term world models even became popular. Now, in the era of end-to-end models, you also need, on top of behavioral realism, sensing realism as well. In fact, building an end-to-end model has been fairly easy for quite a while now, but evaluating it in closed loop—that was the hard part of the problem. So we’ve moved on to building sensing world models. Because we’re using that structure-augmented representation in our models, we can also leverage that structure in our simulation. Our behavior world model operates in the space of structured intermediate representations, and the tightly coupled sensor world model then produces realistic sensor simulations. Our world model leverages the great work of Google DeepMind’s Genie 3, and that gives us the ability to produce controllable and highly realistic scenarios, both in the behavioral as well as sensing aspects.

**中文：** 早在'世界模型'这个词流行之前我们就这么做了。如今在端到端模型时代，除了行为真实，你还需要感知真实。事实上，构建端到端模型已相当容易有一阵子了，但让它以闭环方式被评估——那才是问题里难的部分。所以我们进而构建'感知世界模型'。因为我们的模型用了结构增强表征，我们也能在仿真中利用那种结构。我们的行为世界模型在结构化中间表征的空间里运作，而紧密耦合的传感器世界模型随之产生真实的传感器仿真。我们的世界模型借助了 Google DeepMind Genie 3 的优秀工作，使我们在行为与感知两个层面，都能生成可控且高度真实的场景。

**[39:58 – 40:47]**

**EN:** That in turn allows us to not just evaluate our agent and train new versions of our agent in situations that we’ve previously encountered, but it allows us to train and evaluate in purely synthetic, rare scenarios that we’ve never seen in the real world.

**中文：** 这进而让我们不仅能对曾在真实中遇到过的情境评估和训练智能体、训练其新版本，还能在纯合成、且在真实世界里从未见过的罕见场景中进行训练与评估。

**[40:47 – 41:36]**

**EN:** So what you’re seeing here is not just the generated video. It’s a generative, a full generative simulation of the Waymo Driver operating in closed loop. Here we’re simulating what would happen if it came across a car that was stopped in a lane on the freeway. And you can go further than that. Here’s a plane that’s landing on a freeway in front of us, or you can simulate an elephant on the loose walking through the intersection, snow on the Golden Gate Bridge, or a dinosaur walking around. The lesson here is that closed loop simulation is absolutely required for evaluation and is extremely valuable for training your physical AI agents. You need highly realistic, large-scale simulation to train and evaluate. This brings us to lesson number six. When you’re dealing with a problem of that complexity, you can’t just build a model and call it a day.

**中文：** 所以你眼前看到的，不只是生成的视频。这是对 Waymo Driver 在闭环中运行的、完整的生成式仿真。这里我们仿真的是：若它遇到一辆停在高速车道上的车，会发生什么。而你还可以走得更远——这是一架飞机在我们前方的高速上降落，或者你可以仿真一头四处游荡的大象走过路口、金门大桥上的雪、或一只走来走去的恐龙。这里的经验是：闭环仿真对评估是绝对必需的，对训练你的物理 AI 智能体也极有价值。你需要高度真实、大规模的仿真来训练和评估。这就把我们带到第六条经验。当你面对如此复杂的问题，你不能只造个模型就收工。


## 经验六：构建 AI 飞轮
*Lesson 6: Build an AI Flywheel*

**[41:36 – 42:29]**

**EN:** You have to build an entire ecosystem. And then you also need a flywheel that powers it. Because to make this work at scale, you can’t just build the agent and one AI, you need to build three. You’re building the agent. For us, that’s the driver that drives the car. You also have the simulator, which is that virtual playground for the agent to learn in. And then you have the critic. The critic is what rigorously evaluates and judges the performance of the agent and tells it how to improve. The good news is that the fundamental reasoning and the generative capabilities of all three of those are shared. That’s why in our case, they’re based on the same foundation world model.

**中文：** 你必须构建一个完整的生态系统，然后还需要一个驱动它的飞轮。因为要让这件事在规模上跑通，你不能只造智能体和一种 AI，你需要造三个：你在造智能体——对我们而言，就是开车的 Driver；你还有仿真器，那是智能体学习用的虚拟 playground；然后你还有批评者（critic）。批评者严格评估并评判智能体的表现，告诉它如何改进。好消息是，这三者底层的推理与生成能力是共享的。所以在我们这里，它们建立在同一个基础世界模型之上。

**[42:29 – 43:22]**

**EN:** Once you have these three pillars, you can create an incredibly powerful flywheel to accelerate your progress. A deployment of your agent in the real world generates data. That data then grounds the simulator and makes it more realistic. The simulator generates harder edge cases for the critic to score and for the agent to learn from. So the agent gets smarter, gets deployed in the physical world, generates more data, and that powers the flywheel and accelerates progress. But a flywheel, of course, will spin in any direction or in place. In order to make it go in the direction you want, you need to guide it by metrics. That brings us to the final lesson: your model is really table stakes, but eval and metrics, that’s your most important, that’s your strategic moat.

**中文：** 一旦有了这三根支柱，你就能创造一个极其强大的飞轮来加速进展。智能体在真实世界的部署产生数据；数据进而夯实仿真器、让它更真实；仿真器生成更难的边界情况，供批评者打分、供智能体学习。于是智能体变得更聪明，被部署到物理世界，产生更多数据，由此驱动飞轮、加速进展。但飞轮当然可能朝任意方向转、或原地空转。要让它朝你想要的方向转，你需要用指标来引导。这就来到最后一条经验：模型其实只是入场券，而评估与指标，才是你最重要的、才是你的战略护城河。


## 经验七：评测是你的战略护城河
*Lesson 7: Evals Are Your Competitive Advantage*

**[43:22 – 44:04]**

**EN:** Build your eval before you build your technology. Build your eval and your metrics before you build your product. If you can’t quantitatively define what good enough means, you’re not really building a product, you’re just iterating on your demo. Nowadays, the best model architectures are fairly well known and new ideas tend to proliferate fairly quickly. Data is incredibly important, but without good metrics, you’re just flying blind. You aren’t leveraging the best data and you can’t really evaluate the ROI on making changes to it. So really, eval and metrics, that’s your foundation. That’s what steers your whole tech stack.

**中文：** 在造技术之前，先造你的评估。在造产品之前，先造你的评估与指标。如果你无法定量地定义'足够好'意味着什么，那你其实不是在造产品，只是在 demo 上迭代。如今，最好的模型架构已相当为人所知，新点子也往往传播得很快。数据极其重要，但没有好指标，你就是在盲飞。你既没用好最好的数据，也无法真正评估改动数据带来的投资回报。所以，评估与指标才是你的地基，才是驾驭整个技术栈的方向盘。

**[44:04 – 44:46]**

**EN:** But for physical AI agents, model-level evaluation is not enough. When you’re putting an AI agent into the physical world, your evaluation and validation need to go much deeper and much broader. You need to evaluate and validate every component of your system, from the physical layer to the behavioral layer that’s running onboard in the physical world, as well as the offboard components and all of the operational processes around it. For us, we call that the safety and readiness framework. We spent years building and refining it, and that’s what guides our development, deployment, and scaling. I consider that to be one of our most important assets.

**中文：** 但对物理 AI 智能体而言，模型级评估是不够的。当你把一个 AI 智能体放进物理世界，你的评估与验证必须更深、更广。你需要评估并验证系统的每一个组件——从物理层，到在物理世界里车载运行的行为层，再到车外组件，以及围绕它的一整套运营流程。对我们来说，这叫'安全与就绪框架'。我们花多年构建并打磨它，它指引着我们的开发、部署与扩展。我认为这是最重要的资产之一。

**[44:46 – 45:27]**

**EN:** The reason it’s important is because in the physical world, trust is everything. Evaluation and metrics are how you go about earning that trust. You don’t just win trust by talking about the clever technical solution or the state-of-the-art architecture of your models or doing a flashy demo. You earn it gradually, day by day, in the field, by relentlessly proving that your system is safe and that your system works. Of course, you can’t just prove that to yourself behind closed doors. This is exactly why we openly publish our safety data and our ongoing safety research. That earned trust becomes your ultimate business advantage. Your models can be leaked. Algorithms can be replicated, but hundreds of millions of miles of fully autonomous operations in the real world, backed by evidence-grade evaluation and publicly audited proof, is much, much more difficult to replicate.

**中文：** 它之所以重要，是因为在物理世界里，信任就是一切。评估与指标，正是你赢得信任的途径。你不能只靠谈论巧妙的技术解法、最先进的模型架构、或做一个炫目的 demo 来赢得信任。你是在现场、日复一日、通过不懈地证明你的系统安全、你的系统有效，逐步赢得它。当然，你不能只在闭门中向自己证明。这正是我们公开发布安全数据和持续安全研究的原因。那份赢得的信任，成为你终极的商业优势。你的模型可能被泄露，算法可以被复制，但依托证据级评估和公开审计证明、在真实世界里跑出的数亿英里全自动驾驶，要复制起来难得多得多。


## Waymo 如何比人类安全 17 倍
*How Waymo Became 17x Safer Than Human Drivers*

**[45:27 – 46:09]**

**EN:** When you zoom out and look at this playbook as a whole, you realize that none of these lessons works alone. The nines set your bar and ensure that you pick the right technology and the right technical approach so that you don’t get stuck on the local minimum. Then intentional use of structure to boost scaling and the ability to ride technical waves of innovation helps you get to the right level of nines. Your AI ecosystem with the agent, the simulator, and the critic guided by evaluation and metrics, that’s what allows you to build that powerful flywheel. That’s how all of these effects compound. It’s this playbook that we’ve been refining over the years that allows us to achieve the strongly superhuman safety performance of the Waymo Driver. This is a snapshot of the latest safety data we’ve released.

**中文：** 当你放大视野、整体看这份'打法'时会发现：这些经验没有一条是单独起作用的。'九'为你设定标杆，确保你选对技术和正确技术路线，从而不卡在局部最优。接着，有意识利用结构来助推扩展、加上乘上技术创新浪潮的能力，帮你达到正确的'九'级。而由评估与指标引导、包含智能体—仿真器—批评者的 AI 生态，正是让你能构建那个强大飞轮的东西。所有效应就是这样复合叠加的。正是这份多年来不断打磨的打法，让我们取得了 Waymo Driver 强超人的安全表现。这是我们最新发布的安全数据快照。

**[46:09 – 47:59]**

**EN:** It’s based on over 220 million fully autonomous miles. We’re seeing that in the areas where we operate, the Waymo Driver is about 17 times better than human drivers when it comes to crashes that cause serious injury. That really matters because today, somewhere in the world, every 26 seconds, someone loses their life on a road to a crash event. On the current scale, what that means is that Waymo is preventing a serious injury every eight days. This isn’t just a metric on a dashboard. That means that someone’s loved one got to walk through the front door at the end of the day safe and unharmed. These are just the early safety benefits of AI in the physical world, and they will only grow from there. If you look at the broader landscape, the opportunity here is absolutely massive.

**中文：** 它基于超过 2.2 亿英里的全自动驾驶里程。我们看到，在我们运营的区域，涉及到造成重伤的事故时，Waymo Driver 比人类驾驶员好约 17 倍。这很重要，因为今天，在世界的某个地方，每 26 秒就有人因车祸丧生。以当前规模，这意味着 Waymo 每 8 天就防止一起重伤。这不只是仪表盘上的一个指标。它意味着某人的挚爱，在一天结束时平平安安、毫发无伤地走进了家门。这些都只是物理世界 AI 早期的安全收益，而且只会从此增长。放眼更广阔的版图，这里的机会绝对是巨大的。


## 下一个十年属于物理 AI
*The Next Decade of AI Will Be Physical*

**[47:59 – 49:23]**

**EN:** Physical AI right now is where digital AI was a few years ago, and we have all of the right ingredients to go after it. We have generative world models, we have the architectures, we have affordable compute and sensing. We have proven scaling laws, and we have a real product operating at scale. The last decade of AI happened in the digital world. I think the next decade will also happen in the physical world. For those of you who decide to build in this space, good luck, have fun, and remember who you’re building for. Your mission and your customers—that’s what matters. Otherwise, tech is just a science project. At the end of the day, as exciting and exhilarating as the tech is, nothing really beats the joy of making a difference in people’s lives.

**中文：** 物理 AI 当下所处的位置，正是数字 AI 几年前的位置，而我们已经具备所有正确的要素去攻克它。我们有生成式世界模型，有架构，有可负担的算力与感知。我们有被验证的扩展定律，还有一个在规模上运行着的产品。过去十年的 AI 发生在数字世界；我认为下一个十年也会发生在物理世界。对在座决定投身这一领域的你们，祝好运，玩得开心，并记住你在为谁而造。你的使命和你的客户——那才是要紧的事。否则，技术只是一个科学项目。归根结底，无论技术多么令人兴奋、多么酣畅，没有什么能真正胜过'改变人们生活'所带来的那种喜悦。
