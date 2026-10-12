# Grab 的自动驾驶打法：东南亚不要「替代人」，要「编排人机混合车队」

**Grab's Autonomous Vehicle Playbook for Singapore and Southeast Asia**

> 播客：AV Market Strategist · Autonomy Insiders | 2026-10-01 | 45:14
> 嘉宾：**Dominic Ong**（Grab 自动驾驶总经理 / GM Autonomous）
> 主持人：Daniel Abreu Marques（AV Market Strategist）
> 说明：本文为**中英对照整理版**。该期在 Substack 上**没有官方逐字稿**，YouTube 字幕源在本机网络下不可用，因此英文为**本机 Whisper 语音转写**（598 段），并按上下文对自动转写的专名误听与明显口误作了校正（如 We Write/B-Rite → **WeRide**、Pongol/Pongo → **Punggol**、Cary/Kari → **Carri**、Elos/Sailors → **Zelos**、Carta dash cams → **KartaDashcam**、Neutonomy → **nuTonomy**、comfort Delgore → **ComfortDelGro** 等）；中文为**人工翻译**，忠实原意，非逐字对译。

---

## 冷开场 · Cold open

**[00:00 – 00:47]**

**EN:** **Montage:** "Welcome to Autonomy Insiders, the show where global industry leaders in autonomous driving unpack their real-world insights." … "In heavy rain situations, when there are occurrences of flash flooding, you actually see demand spiking 9 to 10 times. And interestingly, this kind of demand shock caused by rain is actually positively correlated with autonomous ODD contraction." … "We're actually aiming to roll out about 50 autonomous vehicles in the next few months — so that's actually a step up of our existing fleet fivefold — and we intend to map the whole of Singapore."
**中文：** **预告剪辑：**「欢迎收听 Autonomy Insiders，在这档节目里，全球自动驾驶行业的领军者会拆解他们的一线实战洞见。」……「在暴雨、出现城市内涝的时候，需求会瞬间涨到 9 到 10 倍；而有趣的是，这种由降雨引发的需求冲击，与自动驾驶 ODD（运行设计域）的收缩是**正相关**的。」……「我们计划在未来几个月部署约 **50 辆**自动驾驶车辆——这相当于把现有车队规模扩大**五倍**——并且我们打算把**整个新加坡**都完成测绘。」

---

**[00:47 – 01:32]**

**EN:** **Daniel:** Welcome back to Autonomy Insiders. I'm your host, Daniel. And most conversations about autonomous vehicles are conversations about San Francisco, or Phoenix, or Wuhan — so cities with wide lanes, clear markings, and expensive drivers. And Southeast Asia is none of those things. It has some of the densest and most improvised traffic on the planet, and some of the cheapest driver labor in any middle-income region. So on paper, it should be the last place robotaxis arrive. And yet, in April this year, a residential estate in northeast Singapore became the first neighbourhood in Southeast Asia with a public autonomous passenger service. And my guest today runs that program — Dominic Ong is the General Manager, Autonomous, at Grab. And Dominic, I'm so happy to have you on the show today.
**中文：** **Daniel：** 欢迎回到 Autonomy Insiders，我是主持人 Daniel。关于自动驾驶的讨论，大多是在讲旧金山、凤凰城或者武汉——那些车道宽阔、标线清晰、司机人力昂贵的城市。而东南亚一样都不占。它拥有地球上最密集、也最「即兴」的交通流，同时又是中等收入地区里司机人力成本最低的地方之一。所以从纸面上看，它本该是 robotaxi 最后才抵达的地方。但就在今年 4 月，新加坡东北部的一个住宅区成了东南亚第一个提供**公共自动驾驶载客服务**的社区——而今天这位嘉宾正是这个项目的负责人：**Dominic Ong，Grab 自动驾驶总经理**。Dominic，非常高兴能请到你。

---

**[01:32 – 02:09]**

**EN:** **Dominic:** Thank you so much, Daniel, for having me. Really excited to be able to share our story on your platform. **Daniel:** Before we get into any of the technologies, let me start with the basics, because I think our audience knows the AV industry well, but maybe not everyone knows Grab to its full extent. So maybe give me the two-sentence version of what Grab is, and also what share of Southeast Asia's daily movement runs through it.
**中文：** **Dominic：** 非常感谢你，Daniel，很高兴能在你的平台上分享我们的故事。**Daniel：** 在进入技术话题之前，我想先从最基础的开始——我们的听众对自动驾驶行业很熟，但未必每个人都完整了解 Grab。所以能不能用两句话讲清楚 Grab 是什么，以及东南亚每天有多少出行是跑在你们网络上的？

---

## 一、Grab 是谁 · Who is Grab

**[02:09 – 02:52]**

**EN:** **Dominic:** No problem. Well, I kind of want to say that if anyone has travelled to Southeast Asia and has tried to arrange transportation on their own, you likely would have touched the Grab app. In a nutshell, Grab is a NASDAQ-listed, founder-led super app company that has businesses in mobility, food delivery, grocery delivery, digital payments and financial services. Currently we are present in over 900 cities, 8 countries in Southeast Asia, and our total transaction volume currently accounts for about 0.5% of the GDP of the entire Southeast Asian region. In fact, today I want to say we serve over 54 million monthly transacting users.
**中文：** **Dominic：** 没问题。我想说的是，如果你去过东南亚、并且自己安排过出行，你多半用过 Grab 这个 App。简单讲，Grab 是一家**纳斯达克上市、创始人主导的超级应用公司**，业务覆盖出行、外卖、生鲜配送、数字支付和金融服务。目前我们覆盖东南亚 **8 个国家、900 多个城市**，平台总交易额大约相当于整个东南亚地区 GDP 的 **0.5%**。事实上，今天我们服务的**月度交易用户超过 5,400 万**。

---

**[02:52 – 03:28]**

**EN:** **Dominic:** The company was basically founded with a mobility service as our foundation — we wanted to offer safe ride-share rides in a geography where this wasn't always readily available. And we pride ourselves on being extremely, extremely hyper-local; basically, how do we make advanced technologies work in the Southeast Asian context. And of course, we also have a mission to drive Southeast Asia forward by creating economic empowerment for everyone — so the driver-partners, the delivery-partners and merchant-partners who actually work on our platform, their earnings, how they're able to create a sustainable living for themselves on our platform, is something that's very, very important to us. So in a nutshell, that's Grab. And sorry, it took more than two sentences.
**中文：** **Dominic：** 这家公司基本上是以出行业务为根基创立的——我们想在这样一个原本并不总能便捷叫到车的地方，提供安全的共享出行。我们最引以为豪的是**极度的超本地化**：也就是「怎么让先进技术在东南亚的语境里真正跑起来」。当然，我们的使命还包括推动东南亚向前、为所有人创造经济赋权——所以那些在我们平台上工作的司机伙伴、配送伙伴和商户伙伴，他们的收入、他们能否靠平台过上可持续的生活，对我们来说非常重要。总之，这就是 Grab。抱歉，超过两句话了。

---

## 二、一个全新的岗位：GM Autonomous · The GM Autonomous mandate

**[03:28 – 04:07]**

**EN:** **Daniel:** That's impressive. And you are the General Manager for Autonomous — and I think that title exists at Grab for the first time, probably. So what are you actually accountable for? **Dominic:** Okay, well, I just want to take a bit of a step back. The role may be new, but I've actually been looking at autonomous vehicles for over a decade. In fact, before I joined Grab many years ago, I used to work for the Economic Development Board of Singapore, and back then I was responsible for developing what was then a very nascent autonomous and automotive industry. Now, I joined Grab 10 years ago, and in these last 10 years I've actually always been looking at the autonomous portfolio. In 2016 we announced the first ever autonomous on-demand ride-share partnership with nuTonomy back then in Singapore. And in 2018 we made a small investment into Andrew Ng's autonomous driving company called Drive.ai.
**中文：** **Daniel：** 很厉害。你是**自动驾驶总经理**——这个头衔在 Grab 大概是第一次出现。那你实际负责什么？**Dominic：** 我想稍微往回退一步讲。这个岗位是新的，但我看自动驾驶其实已经看了十多年。很多年前在我加入 Grab 之前，我在**新加坡经济发展局（EDB）**工作，当时负责培育一个还很稚嫩的自动驾驶与汽车产业。之后我加入 Grab，到现在正好十年，这十年里我一直都在看自动驾驶这条线。**2016 年，我们和当时的 nuTonomy 一起，在新加坡宣布了全球首个自动驾驶按需出行合作**；**2018 年，我们对吴恩达的自动驾驶公司 Drive.ai 做了一笔小额投资**。

---

**[04:07 – 04:47]**

**EN:** **Dominic:** So in fact, I've been looking at this space for a long time, despite the title being a relatively new one. I will say that as the GM of Autonomous, I do have a three-prong vision for autonomy. The first is, how do we actually make autonomous technology cost-effective, such that it is commercially deployable in our part of the world. The second mandate that I have is about how do I localize this technology properly in Southeast Asia so that customers are actually willing to pay for it — and this includes things like making sure the infrastructure surrounding autonomous technology actually supports it properly in our environment. The third mandate that I have is actually looking out for potentially interesting technologies that could be relevant five, ten years down the road for Southeast Asia — a similar philosophy to why we looked at nuTonomy back in 2016 and Drive.ai in 2018.
**中文：** **Dominic：** 所以事实上，尽管这个头衔比较新，我盯着这个领域已经很久了。作为自动驾驶总经理，我有**三根支柱的愿景**。第一，怎么让自动驾驶技术真正**具备成本效益**，从而在我们这一带可以被商业化部署。第二，怎么把这套技术在东南亚**恰当地本地化**，让用户真的愿意为它付费——这包括确保围绕自动驾驶的基础设施，在我们的环境里能真正支撑它。第三，是去**前瞻性地寻找那些可能在未来 5 年、10 年对东南亚有意义的技术**——这跟我们 2016 年看 nuTonomy、2018 年看 Drive.ai 是同一套逻辑。

---

**[04:47 – 05:30]**

**EN:** **Dominic:** Now, obviously what I'm responsible for, that led us up to this entire three-prong vision: I look after strategy, partnerships, all kinds of investment deals. I'm responsible for the unit economics. And most importantly, the entire operational setup required to make autonomy successful in Southeast Asia.
**中文：** **Dominic：** 而我在这个三根支柱的愿景下实际负责的是：**战略、合作伙伴关系、各类投资交易**；我也负责**单位经济模型**；最重要的是，让自动驾驶在东南亚跑通所需要的**整套运营体系**。

---

## 三、司机不贵也不缺，那自动驾驶解决什么？ · What autonomy actually solves for Grab

**[05:30 – 06:03]**

**EN:** **Daniel:** Super interesting. And maybe let's now get started with the premise of this whole program. I think almost everywhere, the business case for AVs starts with expensive — or also scarce — drivers. But in most of your markets, drivers are not that expensive or scarce. So what is the actual problem autonomy solves for Grab?
**中文：** **Daniel：** 很有意思。那我们来谈整个项目的前提。几乎在所有地方，自动驾驶的商业逻辑都始于**「司机昂贵、甚至稀缺」**。但在你们大多数市场，司机既不太贵、也不太缺。所以对 Grab 来说，自动驾驶真正要解决的是什么问题？

---

**[06:03 – 06:43]**

**EN:** **Dominic:** Okay, so maybe I just want to take a couple of steps back first and provide a little bit of context on Southeast Asia — which, I mean, you've kind of already started off very nicely at the beginning. Southeast Asia is a really dynamic region that comprises a mix of cultures and urban and suburban areas, and you can tell this from the GDP per capita, because it ranges from 2,000 US dollars in Cambodia to over 100,000 US dollars in Singapore. So we're actually dealing with a wide spectrum of economies and cultures here. And amidst all of this, the main philosophy of Grab is: how do we deliver technology at Southeast Asian prices? So, for example, the average ride-share fare in the US is US$14. However, if you look at two-wheel motorcycle rides in Vietnam, they're about US$1 on average.
**中文：** **Dominic：** 我想先退两步，给一点东南亚的背景——其实你开场已经讲得很好了。东南亚是一个非常动态的区域，文化多元，城市与郊区混杂；这一点从**人均 GDP** 就能看出来：从柬埔寨的约 **2,000 美元**，到新加坡的**超过 10 万美元**。所以我们面对的是一个跨度极大的经济体与文化谱系。而在这一切之上，Grab 的核心哲学是：**怎么用东南亚的价格，交付世界级的技术。** 举个例子，美国网约车的平均车费是 **14 美元**；但如果看越南的**摩托车网约出行**，平均只有大约 **1 美元**。

---

**[06:43 – 07:22]**

**EN:** **Dominic:** So the question here is: to make the economics work, do we actually try to deliver a US$14 experience and have it be 1/14th of the effect? Or do we really try to deliver the entire US$14 experience at a US$1 price? And we've basically chosen to offer the best possible technology at prices that are relevant to the region — and this, you can imagine, is not an easy technical feat. Because of everything that we've done to try to deliver a world-class technology to Southeast Asia, I think people actually see us as a reliable everyday service, akin to running water — because they rely on us for their commute to work, they rely on us for food delivery, grocery delivery. I mean, we really try to meet people where they are.
**中文：** **Dominic：** 所以这里的问题是：要让经济模型成立，我们是把「14 美元的体验」打个十四分之一折扣地交付？还是真的**用 1 美元的价格，交付完整的 14 美元体验**？我们选择的其实是后者——用与这个区域消费水平相匹配的价格，提供尽可能好的技术。你可以想象，这在技术上绝不是一件容易的事。正因为我们为了把世界级技术带到东南亚做了这一切，我认为人们其实把我们看成一种**像自来水一样可靠的日常服务**——他们依赖我们通勤上班，依赖我们点外卖、买菜。我们是真的想「在人们所在的地方，遇到他们」。

---

**[07:22 – 08:05]**

**EN:** **Dominic:** So with all of this context in mind, you can imagine that for our business, reliability is basically **P0** to us. Our mandate is really that of reliability — look at us like a public utility service, like running water. And basically, the problem that autonomy has to then solve is: how does it contribute towards this P0 priority of reliability? And actually I see autonomy as contributing to this in two different areas. First of all, by helping us solve what we call **peak-hour gaps**. I was looking at our 2026 data: basically, in a city — in a very densely urban city like Singapore — the demand can easily spike about **four to five times** during peak hours.
**中文：** **Dominic：** 带着这个背景，你就能理解：对我们这门生意来说，**可靠性基本就是 P0（最高优先级）**。我们的使命其实就是可靠性——把我们看作一种公共事业服务，像自来水一样。那么自动驾驶要解决的问题就是：**它如何为「可靠性」这个 P0 作出贡献？** 我认为它会从两个方向作出贡献。第一，帮我们解决所谓的**「高峰缺口」**。我看了我们 2026 年的数据：在一座像新加坡这样高度城市化的城市里，**高峰时段的需求很容易涨到平峰的四到五倍**。

---

**[08:05 – 08:43]**

**EN:** **Dominic:** Then there's always the question of: are the drivers available and online, and are they able to serve the demand during these intense peak-hour periods? And that's where I suspect autonomy actually has a role to play — in helping smooth out what we call these peak-hour spikes, because you don't want to run a business in which it's super spiky. At the same time, I want to say that autonomy could potentially help us solve **connectivity gaps** as well — meaning you have situations where, let's say, there are townships that are out of the city centre, sometimes they aren't always the most popular locations for our driver-partners to want to serve. Can autonomy actually help us plug that gap? So I think in helping us solve these two problems, it basically ladders up to that end goal of reliability.
**中文：** **Dominic：** 于是问题总是：**高峰那几个小时，司机是不是在线、能不能接得住这些需求？** 我认为这正是自动驾驶可以发挥作用的地方——帮我们**抹平这种「尖峰」**，因为没有人想经营一门波动极其剧烈的生意。同时我也想指出，自动驾驶还可能帮我们解决**「连通性缺口」**：比如说，有些**远离市中心的城镇（township）**，并不总是司机伙伴最愿意去服务的地方。自动驾驶能不能帮我们把这个缺口补上？我想，解决这两个问题，最终都会**汇聚到「可靠性」这个终点**。

---

**[08:43 – 09:04]**

**EN:** **Dominic:** So for now, we're looking at autonomy to help us continue our philosophy of being the most reliable platform in the region.
**中文：** **Dominic：** 所以现阶段，我们期望自动驾驶帮我们延续这条路——**做这个区域里最可靠的平台**。

---

## 四、混合模式：一张网、一个 App · The hybrid model

**[09:04 – 09:20]**

**EN:** **Daniel:** This makes sense. And also, your answer to all of this is what you call a **hybrid model** — it's a term that's also often used in the industry. But maybe let's also define it. So what actually is the hybrid model for you? And also, maybe, what is the alternative you rejected?
**中文：** **Daniel：** 这说得通。而你给出的答案是所谓的**「混合模式」**——这个词在行业里也常被使用。不过我们还是把它定义清楚：对你来说，混合模式到底是什么？以及，你们**否掉的替代方案**又是什么？

---

**[09:20 – 09:49]**

**EN:** **Dominic:** Yeah. So for the hybrid model, how I define it is: it is **autonomous vehicles and human drivers operating on one network, booked via one app, from the same pool of demand, but dispatched interchangeably.** Meaning we have the intelligence behind the scenes on the platform determining whether or not an autonomous vehicle or a human driver would best serve a customer's request. The platform will choose between them, trip by trip.
**中文：** **Dominic：** 好。我对混合模式的定义是：**自动驾驶车辆与人类司机运行在同一张网络上，通过同一个 App 下单，共享同一个需求池，但可以被互换地调度。** 也就是说，平台在背后用智能来判断：这一单到底由自动驾驶车辆接、还是由人类司机接更合适。**平台是一单一单地在两者之间做选择。**

---

**[09:49 – 10:29]**

**EN:** **Dominic:** In this situation, I would say that the hybrid model is one which really encompasses the best of both, instead of forcing a choice between human and robot. And in relation to the P0 being reliability, which is what I shared earlier: the hybrid network actually offers reliability in the most practical manner, from the perspective of wanting to administer and deliver a mobility service that is truly reliable. Now, we talked about peak-hour gaps and connectivity gaps. The other thing that I wanted to raise was that, in the context of Southeast Asia, **rain** really contributes to an extreme variance in demand. In heavy rain situations, when there are occurrences of flash flooding, you actually see demand spiking **9 to 10 times**.
**中文：** **Dominic：** 在这个意义上，混合模式其实是**把两端的好处都收进来**，而不是被迫在「人」和「机器人」之间二选一。回到我刚才说的 P0——可靠性：混合网络恰恰是**用最务实的方式**提供可靠性，从「要运营并交付一项真正可靠的出行服务」这个角度看，就是如此。我们刚谈了高峰缺口和连通性缺口。我还想再提一点：在东南亚，**降雨**会造成需求的极端波动。在暴雨、出现城市内涝的时候，需求会涨到 **9 到 10 倍**。

---

**[10:29 – 11:07]**

**EN:** **Dominic:** And interestingly, this kind of demand shock caused by rain is actually **positively correlated with autonomous ODD contraction**. And what I mean by this is: when demand spikes due to rain, you end up with autonomous vehicles that are maybe not able to support ride requests in areas of heavy rain — because the vehicles haven't been trained, or because the floods actually prohibit the smooth operation of these vehicles. So what do you do in a situation like that, when you still have to serve the customer? Because to reject the ride request means that you will end up disappointing them, and they will leave the platform.
**中文：** **Dominic：** 而有趣的是，这种由降雨引发的需求冲击，与**自动驾驶 ODD 的收缩是正相关的**。我的意思是：当降雨把需求推高时，恰恰是那些区域里的自动驾驶车辆**可能接不了单**——因为车辆没有针对这种场景训练过，或者积水本身就让它没法顺畅运行。那你怎么办？需求还在，客人还得服务。因为**拒单就意味着让用户失望，而失望的用户会离开平台。**

---

**[11:07 – 11:47]**

**EN:** **Dominic:** Now, the second reason why I feel that it also offers reliability in a very practical manner is because you don't have a situation where you're **over-scaling the fleet to meet peak demand**. Because, as we ascertained, in a densely urban environment, demand can sometimes be very spiky due to a variety of different reasons. And if you had chosen an alternative — the alternative being you only have 100% autonomous vehicles — then basically you would have to over-fleet to cover that peak demand. And during periods of low demand, you end up with a situation where a lot of the vehicles end up remaining idle, creating a **utilization problem**.
**中文：** **Dominic：** 第二个理由同样很务实：混合模式让你**不必为了扛住峰值而把车队规模撑得过大**。因为我们已经确认，在高密度城市环境里，需求会因为各种原因变得极其尖峭。如果你选了那条替代路线——也就是**100% 全自动驾驶车队**——那你就必须为了覆盖峰值而**过度配车**；而在低谷时段，大量车辆就会闲置，形成**利用率问题**。

---

**[11:47 – 12:23]**

**EN:** **Dominic:** And because of the need for us to be extremely, extremely practical and prudent in our part of the world, we really want to be very conscious of how we're utilizing capital, how we're actually buying assets. And finally, one thing that I think is very close to my heart as well: in a hybrid network, you continue to allow for room to have **white-glove services** delivered by driver-partners. So for example, if you have families with children and they have problems with the car seat, with luggage; maybe you have passengers with certain disabilities who actually need help; you have elderly folk who are trying to take the vehicle and maybe they just need a bit of help with opening the door, or walking them to the entrance of a medical facility — there will still be that dependency on having a human in the vehicle.
**中文：** **Dominic：** 在我们这一带做生意，必须极度务实、极度审慎，所以我们对**资本怎么用、资产怎么买**非常在意。最后一点，也是我个人很看重的：在混合网络里，你**始终保留了由司机伙伴提供「白手套服务」的空间**。比如带着孩子、需要处理儿童座椅和行李的家庭；比如有某些行动障碍、确实需要帮助的乘客；再比如老年人上车，可能只是需要有人帮忙开个门，或者陪着走到诊所门口——这些场景**依然依赖车里有一个「人」**。

---

**[12:23 – 12:57]**

**EN:** **Dominic:** And so I think the hybrid network allows us to cover all of these situations effectively, without disappointing the customer too much. The fact of the matter is that autonomous technology today, in 2026, isn't quite yet perfect. And hybrid allows us to continue running a trusted and reliable service. It doesn't hurt confidence when autonomous vehicles fail — because you really don't want people to try it once, twice, and then end up leaving the platform because they're like, "well, it doesn't really fit into my daily needs."
**中文：** **Dominic：** 所以我认为，混合网络让我们能有效地覆盖所有这些场景，而不至于让用户太失望。事实是，**2026 年的今天，自动驾驶技术还谈不上完美**。混合模式让我们能继续提供一个**可信、可靠**的服务。它也不会因为自动驾驶偶发失败而伤害信任——因为你最不想要的，就是用户试了一两次之后离开平台，心里想的是：「这东西其实融不进我的日常需求。」

---

**[12:57 – 13:33]**

**EN:** **Daniel:** Yeah, super interesting. And maybe one question that you cannot answer right from the spot, but it would be super interesting: how probable is it that you have such flooding or rain that you cannot drive an autonomous vehicle in Southeast Asia? Is it something that is really common, or is it more scarce? **Dominic:** Oh, yes, extremely — it's extremely common in Southeast Asia, actually. In particular, in countries like Singapore, Malaysia, certain parts of Thailand as well. I mean, these are countries that are classified as being within the **monsoon region**. Thunderstorms are actually a fairly frequent occurrence in the period between **August to December**.
**中文：** **Daniel：** 很有意思。有一个你可能没法当场回答、但会很有意思的问题：在东南亚，**「雨大到自动驾驶车根本开不了」这种情况到底有多常见？** 是很普遍，还是很少见？**Dominic：** 哦，非常常见——在东南亚其实相当普遍。特别是新加坡、马来西亚，以及泰国的部分区域。这些国家都被划在**季风区**里，**8 月到 12 月**期间雷暴相当频繁。

---

**[13:33 – 14:13]**

**EN:** **Dominic:** And then you end up with a situation like: when there is heavy rain, we have seen our demand spike easily 9 to 10 times. So imagine you have that kind of crazy spike, and yet you are constrained in being able to serve the customer because the vehicles cannot operate during those conditions. **Daniel:** Yeah, that's super interesting. Maybe let's go directly to your deployment. So as far as I can tell, **Punggol** is the first public autonomous passenger service ever deployed inside a residential neighbourhood in Southeast Asia. So maybe let's build it from the ground up.
**中文：** **Dominic：** 于是就出现这种情况：暴雨一来，我们的需求轻松就能涨到 **9 到 10 倍**。你可以想象——需求疯狂飙升，而你恰恰在那样的天气里**被限制住了**，因为车辆在这种条件下没法运营。**Daniel：** 太有意思了。那我们直接进到你们的落地项目。据我所知，**Punggol 是东南亚第一个部署在住宅区内部的公共自动驾驶载客服务**。我们就从头把它拆开讲吧。

---

## 五、Punggol：Grab、WeRide、LTA 的分工 · Punggol

**[14:13 – 14:55]**

**EN:** **Daniel:** Can you walk me through the division of labour between Grab, your autonomous vehicle partner **WeRide**, and the **Land Transport Authority** — so specifically, who is the operator of record, who owns the vehicles, and who carries the risk if something goes wrong? **Dominic:** Yeah, absolutely. So we have a very unique and great relationship with WeRide and with LTA as far as this Punggol pilot is concerned. In the case of WeRide, they are the **provider of vehicles**, they are the **L4 technology stack owner**. We have done a partnership with them in which they are offering the vehicles to us. In the case of LTA, they are the **regulator**, but at the same time, to some extent, I would say that they are the **innovator** as well — because when we did the Punggol pilot, we actually co-created a lot of what the pilot would look like with them.
**中文：** **Daniel：** 能不能讲一下 Grab、你们的自动驾驶伙伴 **WeRide（文远知行）**，以及**陆路交通管理局（LTA）** 之间的分工？具体说：谁是**登记在册的运营方**？车归谁所有？如果出了事，风险由谁承担？**Dominic：** 当然。就 Punggol 这个试点来说，我们和 WeRide、和 LTA 的关系非常特别、也非常好。WeRide 是**车辆提供方**，也是 **L4 技术栈的所有者**；我们跟他们建立了合作，由他们向我们提供车辆。LTA 方面，他们是**监管者**，但在某种程度上，我也会说他们同时是**创新者**——因为在做 Punggol 试点时，**试点长什么样，很多是我们和他们一起共创出来的**。

---

**[14:55 – 15:36]**

**EN:** **Dominic:** So I remember that the conversation took place quite — I want to say — over a year and a half ago, where we said, "hey, we have some ideas about how we want to do this. Can we really sit down with you and work through all the details?" Because back then, LTA was really seriously contemplating how to enter into service a fleet of autonomous vehicles in Singapore. **Daniel:** So they're the regulator — meaning they put all the safety frameworks, all the guidelines, all the testing requirements in place.
**中文：** **Dominic：** 我记得那次对话大概是——我想想——**一年半以前**，我们说：「嗨，我们对怎么做有一些想法，能不能跟你们坐下来，把所有细节都过一遍？」因为当时 LTA 正在非常认真地考虑：**在新加坡要怎么让一支自动驾驶车队投入服务**。**Daniel：** 所以他们既是监管者——也就是把**安全框架、指引、测试要求**全都立起来的那一方。

---

**[15:36 – 16:14]**

**EN:** **Dominic:** At the same time, I also see them as an innovator as well, being able to sit down with the private sector and say, "hey, all these requirements, all these boundary conditions — let's try to do it in a way that doesn't become prohibitive to technology innovation." Now, the role that Grab plays is that of the **operator of record**. And what this means is that for the purpose of this pilot, we actually **own the vehicles on our balance sheet**. We operate the vehicles, we integrate the vehicles onto the Grab app, such that they are available and you're able to book a ride with them.
**中文：** **Dominic：** 同时我也把他们看作创新者——他们能坐下来跟私营部门说：「这些要求、这些边界条件，我们来试着用一种**不会把技术创新直接扼杀**的方式去实现。」Grab 扮演的角色是**登记在册的运营方（operator of record）**。这意味着，在这个试点里，**车辆是记在我们资产负债表上的、归我们所有**；我们运营这些车，把它们集成进 Grab App，让用户可以叫到车。

---

**[16:14 – 16:56]**

**EN:** **Dominic:** At the same time, we have invested heavily into what I call the **localization layer**. And maybe I'll just take a little bit — 30 seconds — to describe what this means. The localization layer basically refers to Grab investing into software and hardware capabilities to actually help our autonomous vehicle partners. So imagine you could be an AV company who comes to Singapore with maybe not a full stack — but we could work with you and have our engineers sit down with you and try to make up for any gaps you have in launching the Singapore service.
**中文：** **Dominic：** 同时，我们在所谓的**「本地化层」上投入很重**。我用大概 30 秒解释一下这是什么。本地化层指的是：**Grab 在软件和硬件能力上做投入，去实际帮助我们的自动驾驶伙伴**。想象一下，你可能是一家带着「不完整技术栈」来到新加坡的自动驾驶公司——那我们的工程师可以坐下来跟你一起，**把你在新加坡落地时的短板补齐**。

---

**[16:56 – 17:34]**

**EN:** **Dominic:** But of course, you could also have AV companies who come to Singapore and maybe they have a full stack — they say, "hey, we want you to just adopt everything." And we'll say, "okay, no problem, we will build on top of your stack and try to improve efficiency and try to make this technology work in the Singaporean context." And concretely, what does this actually mean? For us, it comprises hardware. For example, we have our proprietary **KartaDashcam** — inward-facing cameras and outward-facing cameras that we install into the WeRide vehicles, so that the regulators actually have a very clear view of what the passengers are doing within the vehicle, as well as an additional pair of eyes on what the vehicle is seeing ahead of it.
**中文：** **Dominic：** 当然，也可能有伙伴带着**完整技术栈**来新加坡，说「你们直接全盘采用就好」。那我们就会说：「没问题，我们在你的栈之上再做一层，去提升效率、让这套技术在**新加坡语境**里跑起来。」具体到什么程度？对我们来说，这包括**硬件**。比如我们自研的 **KartaDashcam**——**内向摄像头 + 外向摄像头**，装到 WeRide 的车上，让监管方可以清楚地看到**车内乘客在做什么**，同时也为车辆**前方看到的东西**多增加一双眼睛。

---

**[17:34 – 18:08]**

**EN:** **Dominic:** We have what we call the **maker-checker model**, which is that, because of the type of partnership that we have with WeRide, our team also sits down with them and reviews all the edge cases, the data that comes from the car, what it's actually telling us. And we say, "hey, these circumstances are unique to Singapore — this is how you should tweak the software, this is how you should tweak the driving characteristics." So in a way, we regard them really as a partner, in that we sit down side by side to do these things — versus saying, "hey, this is entirely your responsibility as a software stack provider."
**中文：** **Dominic：** 我们还采用所谓的**「maker-checker（制作者—复核者）」模式**：因为我们和 WeRide 是这样一种合作类型，我们的团队会跟他们坐在一起，**复盘所有边缘场景、复盘从车上回传的数据、复盘数据到底在告诉我们什么**。我们会说：「这种情况是新加坡独有的——软件这里应该这么调，驾驶特性那里应该那么调。」所以在某种意义上，我们**真的把他们当成伙伴**，是并排坐着一起做这些事，而不是说「你是软件栈提供方，这全是你的责任」。

---

**[18:08 – 18:34]**

**EN:** **Dominic:** And the third aspect of this is that we also have invested into building a **fleet-management middleware** that actually plugs into different AV OEMs as well. Because what we want to do is: through this middleware, you're able to actually have oversight on all the vehicles, how they operate, and exactly how they are functioning on the Grab platform itself. So this is what I call the localization layer.
**中文：** **Dominic：** 第三块是：我们还投入建设了一套**车队管理中间件**，它可以对接**不同的自动驾驶 OEM**。因为我们想做到的是：通过这套中间件，你能够对所有车辆、它们的运行状态、以及它们在 Grab 平台上的实际表现，拥有**全局的可见性**。这就是我所说的本地化层。

---

**[18:34 – 18:47]**

**EN:** **Daniel:** That's really interesting. So basically, you then also help to tweak the AV partner's virtual driver for Singaporean edge cases. That's really cool. **Dominic:** Yes, I would say that we try our best to do that, because we also understand that in the Singaporean context, there are many local nuances that may not always be picked up automatically. And I think the philosophy here is that we just want to be a very helpful partner to you.
**中文：** **Daniel：** 这很有意思——也就是说，你们其实也帮着调校伙伴的**「虚拟司机」**，让它适配新加坡的边缘场景。太酷了。**Dominic：** 是的，我们尽力这么做。因为我们也明白，在新加坡的语境里，有很多**地方性的细微差异**，未必会被自动捕捉到。这里的理念很简单：**我们就是想做一个对你非常有用的伙伴。**

---

## 六、从固定接驳到自动驾驶叫车 · From shuttle to ride-hailing

**[19:14 – 20:06]**

**EN:** **Daniel:** That makes sense. And maybe a bit more about your first pilot: the first pilot was on a fixed route, more or less. And now you've also announced an on-demand pilot. So for a Punggol resident, what actually changes? And also, maybe, why now? **Dominic:** Well, I have to say that we're extremely excited about this step-up for Punggol. But maybe I'll just take a little bit of time to address how we started this entire Punggol pilot. We started testing in Punggol — and, as I told you, the approach had been co-created with the **Ministry of Transport** and LTA in Singapore. We wanted to actually put autonomous vehicles in a neighbourhood that had a **mix of commercial and residential**, because you wanted people of different profiles and different backgrounds to be exposed to the vehicle.
**中文：** **Daniel：** 说得通。再说说你们第一个试点：最早大体上是**固定路线**，现在你们又宣布了**按需（on-demand）试点**。对一位 Punggol 居民来说，到底什么变了？以及，为什么是现在？**Dominic：** 我得说，对 Punggol 这次升级我们**超级兴奋**。不过我还是花一点时间讲讲整个 Punggol 试点是怎么开始的。我们从 Punggol 开始测试——如我所说，这套方案是跟新加坡**交通部（MOT）**和 LTA **一起共创**的。我们想把它放在一个**商业与住宅混合**的社区里，因为这样能让**不同画像、不同背景的人**都接触到这种车辆。

---

**[20:06 – 20:46]**

**EN:** **Dominic:** We did a fixed-route shuttle because we wanted to really try out this technology using a **very phased approach**. And this was very much in line with how the Singapore government in general rolls out innovation, because I would say the approach is usually very considered, very deliberate. And it's particularly important to do so with autonomous vehicles, given that safety is obviously paramount. So we said: "okay, let's try it on a fixed-route shuttle. Let's really make sure these vehicles can actually be localized properly. And let's make sure we **socialize** this technology with the public — because so far the public has only ever seen this technology in San Francisco or in different parts of China; they haven't actually seen it in Singapore."
**中文：** **Dominic：** 我们先做**固定路线接驳**，是因为我们想**分阶段**地把这项技术试出来。这也非常符合新加坡政府推进创新的整体风格——我认为他们的做法通常都很审慎、很有步骤。放到自动驾驶上，这一点尤其重要，因为**安全显然是第一位的**。所以我们说：「好，先在固定路线上试。先确保这些车能被恰当地本地化。然后要确保把这套技术**「社会化」给公众**——因为到目前为止，公众只在旧金山或中国某些城市见过这种技术，**他们还没在新加坡见过**。」

---

**[20:46 – 21:24]**

**EN:** **Dominic:** So let's enlist their help also — try out the rides and get as much feedback as we can from them, so that they also **co-create** what the eventual rollout will look like. And in a way, this is actually crucial for **trust**. So as we look towards the ride-hailing service rollout in Punggol, we're actually aiming to roll out about **50 autonomous vehicles in the next few months** — so that's actually a step up of our existing fleet **fivefold**. And we intend to **map the whole of Singapore**, and hopefully bring the service beyond Punggol — because I feel like we've done a lot of work in Punggol, people in Punggol are already very, very familiar with our service already. We really want to bring it to more parts of Singapore.
**中文：** **Dominic：** 所以要**请公众参与进来**：请他们试乘，尽可能多收集反馈，让他们也**共创**最终的服务形态。从某种意义上说，**这对「信任」至关重要**。所以展望 Punggol 的**叫车服务**上线，我们计划**在未来几个月投放约 50 辆自动驾驶车辆**——相当于把现有车队扩大**五倍**。我们还打算**把整个新加坡测绘完成**，并希望把服务带出 Punggol——因为我们在 Punggol 已经做了很多工作，Punggol 的居民对我们的服务也非常熟悉了。我们真的很想把它带到新加坡更多地方。

---

**[21:24 – 21:48]**

**EN:** **Dominic:** Now you may ask: why are we going to ride-hailing now? This pivot was interestingly actually **due to user demand**. Because during the entire fixed shuttle service duration, we were collecting a lot of feedback from residents, and many of the residents were extremely forthcoming with their feedback. And they told us that they actually wanted **flexible bookings, direct connections** — basically, "let us book this service exactly as we would book a Grab." And that was really what gave us — and the regulators — the confidence to say, "okay, we're ready to take this bold next step forward, to go into autonomous ride-hailing."
**中文：** **Dominic：** 你可能会问：为什么现在就转做**叫车**？有意思的是，**这个转向其实是用户需求推动的**。在整个固定接驳服务期间，我们收集了大量居民反馈，很多居民都非常乐于表达。他们告诉我们，他们想要**灵活的预订、直达的路线**——基本上就是：「让我们能像叫 Grab 一样叫这个服务。」**正是这一点，给了我们和监管方信心**，去说：「好，我们准备好迈出这大胆的下一步，进入**自动驾驶叫车**。」

---

## 七、Grab 真正盯的指标 · The metrics Grab watches

**[21:48 – 22:04]**

**EN:** **Daniel:** And you went from 40,000 kilometres in early May to about 90,000 now, in miles — whatever. And also **disengagement** is what the industry always quotes publicly. But it will also be interesting to hear from you: what is the metric your team actually watches internally?
**中文：** **Daniel：** 你们的里程从 5 月初的 4 万公里涨到了现在的约 9 万公里（公制/英制先不纠结）。而**「脱离接管」**是行业对外最爱引用的指标。但我更感兴趣的是：**你们团队内部真正在盯的是哪个指标？**

---

**[22:04 – 22:39]**

**EN:** **Dominic:** Okay. So **miles per critical intervention** — that is definitely an industry standard, and it is relevant in the initial phase when we're trying to prove out the technology. And by the way, currently we are at **over 120,000 kilometres with no critical intervention so far**. So that's something that we continue to amass and to work hard on. Miles per critical intervention is important in the initial phase, where you're trying to prove the technology. Right now we're in a phase where we're trying to prove the **operations**.
**中文：** **Dominic：** 好。**「每关键介入里程（miles per critical intervention）」** 确实是行业标准，在我们要**证明技术**的早期阶段也很相关。顺便说一句，**目前我们已经超过 12 万公里、至今没有一次关键介入**——这是我们持续在积累、在努力的东西。「每关键介入里程」在**证技术**的初期很重要。而我们现在所处的阶段，是要**证运营**。

---

**[22:39 – 23:16]**

**EN:** **Dominic:** And so **vehicle uptime** — how much time in a day is usable for the ferrying of passengers — is a metric that we're actually watching very closely right now, because it tells us how efficient our **depot operations** are. And we've just set up a depot in Punggol, and this is where we're really bringing in a lot of know-how on operational efficiency: how we actually set up the entire space, how we think about the vehicles' ingress and egress. All these things have a bearing on the vehicle uptime, and so that's a metric that we're actually looking at very carefully right now.
**中文：** **Dominic：** 所以**车辆在线可用时长（vehicle uptime）**——也就是一天里有多少时间可以真正用来拉客——是我们现在盯得非常紧的指标，因为它能告诉我们**场站（depot）运营效率**到底如何。我们刚在 Punggol 建了一个场站，在这里我们投入了大量关于**运营效率**的经验：整个空间怎么布置、车辆的**进出动线**怎么设计。这些都会直接影响车辆在线时长，所以这个指标我们现在看得非常仔细。

---

**[23:16 – 23:38]**

**EN:** **Dominic:** In the next phase, when we start doing autonomous ride-hailing, that's actually when we will start being concerned with **utilization** as a metric — which is: how much of the vehicle's available time is actually occupied with a passenger. And I think eventually, when we are really comfortable and we start offering the service widespread in many, many different areas of Singapore, and we're actually running it commercially — that's also when we will look to getting a metric which is hopefully a **combination of operational efficiency, uptime and utilization**.
**中文：** **Dominic：** 到了下一个阶段，当我们真正开始做自动驾驶叫车时，我们就会开始关注**「利用率（utilization）」**这个指标——也就是：车辆的可用时间里，有多大比例**真的载着乘客**。而最终，当我们足够从容、开始在新加坡很多很多不同区域大范围提供服务、并且真正**商业化运营**的时候，我们就会去看一个**把运营效率、在线时长和利用率组合起来**的指标。

---

**[23:38 – 24:34]**

**EN:** **Daniel:** And you mentioned already the depot, and you said you built that in Punggol. So do you envision also to operate all the depots you need, and also do the fleet operations? Or do you want to outsource it to third-party providers? **Dominic:** Oh, that's an interesting question. That is actually an important strategic decision we're working through right now. I think what we see in other markets is that, in the case of Waymo — let's take Waymo as an example — they have cities in which they handle their own fleet operations and they own the fleet themselves; they have cities in which they have contracted this function. And I think it's great that in the U.S. market you actually have choice. In the Singaporean market, I would say that because this technology is still up and coming, we're still at a very early stage where you don't have a thriving ecosystem to actually support the different models.
**中文：** **Daniel：** 你刚提到了场站，说是在 Punggol 建的。那么你们是打算**自己运营所有需要的场站和车队运营**，还是**外包给第三方**？**Dominic：** 这是个好问题，而且是我们**正在认真推敲的一个重要战略决策**。我们在其他市场看到的情况是：以 **Waymo** 为例，他们有些城市是**自己管车队运营、自己也持有车队**，有些城市则把这块**外包**出去。我觉得美国市场的好处是**你有选择**。但在新加坡市场，我会说：因为这项技术还在发展当中，我们还处在一个很早的阶段——**还没有一个成熟的生态来支撑不同的模式**。

---

**[24:34 – 25:22]**

**EN:** **Dominic:** So I would say that as a start, we will look to relying on ourselves to do fleet operations. Also because, for the initial batch of WeRide vehicles that we are putting on our platform, we actually own the assets as well. So we will start with that. And I think as we start scaling up the fleet, we will also be looking at whether or not there are available fleet partners who may be prepared to actually take on this function. And I suspect that as we get closer and closer to commercialization, once there is **regulatory clarity** on the direction that we are going and the speed at which we are scaling up — that is probably the juncture at which there will be a lot more interest coming from existing fleet owners to say, "hey, I'm willing to actually take this next step." And so the work that we're doing, hopefully, will be an **encouragement and a guidance** for many of these players who might be watching the space but not ready to take the step yet.
**中文：** **Dominic：** 所以起步阶段，我们会**靠自己做车队运营**——也因为投放到平台上的**第一批 WeRide 车辆，资产本身就是我们持有的**。我们从这里开始。随着车队规模扩大，我们也会去看**有没有现成的车队伙伴愿意接下这个职能**。我倾向于认为：当我们越来越接近商业化、一旦**监管方向明确**、扩张速度也明确之后，那大概就是**现有车队业主开始产生更多兴趣**的拐点——他们会说：「嘿，我愿意迈出这一步了。」而我们现在做的这些事，希望能成为这些**「在看但还没准备好下场」的玩家**的**鼓励和指引**。

---

## 八、什么会把 AV 栈打崩 · What breaks an AV stack in Southeast Asia

**[25:22 – 25:46]**

**EN:** **Daniel:** And maybe now let us widen the lens a bit, because Punggol is Singapore, and it's only one place in your entire footprint. So you now have real mileage. Could you maybe also rank the **top three things about Southeast Asian roads that could break an AV stack** — trained in China or the United States?
**中文：** **Daniel：** 现在我们不妨把镜头拉宽一点。Punggol 只是新加坡，只是你们整个版图里的一个点。现在你们有了**真实里程**，能不能排个序：**东南亚道路上最可能「打崩」自动驾驶栈**——尤其是那些在中国或美国训练出来的栈——的**前三大因素**？

---

**[25:46 – 26:23]**

**EN:** **Dominic:** Yeah. So before we actually touch on the physical edge cases, I actually wanted to talk about an **economics edge case**, which is Singapore. I'm not sure if you're familiar, but Singapore is likely the hardest place in the world for autonomous vehicle economics to work out. And that's really because of the **taxation regime**, because the entitlement to put a vehicle on Singaporean roads actually costs **more than six figures in US dollars**. This was the approach that had been adopted by the Singapore government to moderate the level of car ownership in Singapore — because Singapore is a place of very limited land, and we don't want a situation where we end up having to build too many roads, or having the existing roads be too congested. And so this approach towards car ownership has actually been in place for decades already.
**中文：** **Dominic：** 好。不过在谈物理上的边缘场景之前，我想先讲一个**「经济上的边缘场景」**，那就是新加坡本身。不知道你是否了解——**新加坡可能是全世界最难让自动驾驶经济模型算得过来的地方**。根本原因是**税制**：**在新加坡上牌上路的资格，成本超过六位数美元**。这是新加坡政府为了**控制拥车水平**所采取的办法——因为新加坡土地极其有限，我们不希望最后不得不修太多路，或者让现有道路过度拥堵。这套拥车制度其实**已经实行几十年了**。

---

**[26:23 – 27:38]**

**EN:** **Dominic:** So in a way, this presents also a bit of an economic edge case, because you can imagine that **an idle autonomous vehicle here will be an extreme extravagance**. It's not just a small inefficiency problem — it's like, "oh my goodness, it's really costing you a lot on a per-hour basis." So I would say that **you cannot hide a badly utilized vehicle in this market**. And in a way, one of the things that we do want to test out is whether the economics actually work out. And obviously, if we're not able to get a high level of utilization in the vehicle, then that would be one of the things that would **break the entire model**. Now, but going back to the physical edge cases — which I believe is what your question was about — I would say that the top three are likely going to be **rain**, as I mentioned, because **a tropical downpour changes lane visibility, sensor return and pedestrian behaviour all at once.** In fact, we have seen situations where a tropical downpour can actually reduce visibility to near zero.
**中文：** **Dominic：** 所以这在某种程度上构成了一个**经济上的边缘场景**：你可以想象，**在这里让一辆自动驾驶车闲置，是极其奢侈的事**。它不只是一个「小效率损失」的问题——它更像是「天哪，这辆车每小时都在烧很多钱」。所以我会说：**在这个市场里，你没法藏住一辆利用率很差的车。** 从某种意义上说，我们确实想验证的一件事就是：**这套经济模型到底算不算得过来。** 显然，如果我们做不到高利用率，那就会成为**打崩整个模型**的因素之一。好，回到物理边缘场景——我想这才是你问题的重点。我认为前三名大概是：第一，**雨**——如我所说，因为**一场热带暴雨会同时改变车道可视性、传感器回波和行人行为**。事实上我们见过，一场暴雨能把能见度**压到接近零**。

---

**[27:38 – 28:17]**

**EN:** **Dominic:** So it's really difficult even for human drivers to navigate that situation, and we haven't actually put these autonomous vehicles to that kind of test yet. So rain is probably number one. The second would probably be **motorcycles**, because two-wheelers are actually a very common modality of transportation in all parts of Southeast Asia. And, for example, a lot of the Grab delivery riders actually deliver food using motorcycles. So you have situations where, at a rate, suddenly you have **a swarm of motorcycles surrounding the vehicle** — and you don't see that in the US, because motorcycles are not as cheap or as commonly relied on as a mode of transportation.
**中文：** **Dominic：** 即便对**人类司机**来说，那种情形也很难应对，而**我们还没有把自动驾驶车辆放到那种极端条件下去测过**。所以雨大概排第一。第二大概是**摩托车**——因为两轮车在东南亚各地都是非常普遍的交通方式。比如，Grab 的大量**配送骑手就是用摩托车送餐**。于是就会出现这样的场面：**突然间，车辆被一整群摩托车包围**——这在美国是见不到的，因为摩托车在美国既没那么便宜，也没那么普遍地被依赖为出行方式。

---

**[28:17 – 28:55]**

**EN:** **Dominic:** The third one, which is not so much something that will break the stack, but rather something that the stack definitely must be tuned to, is the **right-hand drive requirement**. Because in certain markets in Southeast Asia, you actually have right-hand drive vehicles, which basically means that all the traffic directions have to be tuned for a different side of the road. Even things like how the passenger enters the vehicle, exits the vehicle, how you cross a big junction and things like that, has to be recalibrated completely. And I wouldn't say that it's an obstacle — it's rather a challenge that needs to be worked through.
**中文：** **Dominic：** 第三点与其说是会「打崩」栈的东西，不如说是**栈必须被调校适配**的东西——那就是**右舵（right-hand drive）的要求**。因为在东南亚某些市场，车辆本身是右舵的，这意味着**所有行驶方向都要为「另一侧车道」重新标定**。连乘客怎么上车、怎么下车、怎么通过一个大路口这类事情，**都必须彻底重新校准**。我不会说这是一道障碍——它更像是一个**需要被攻克的挑战**。

---

**[28:55 – 29:31]**

**EN:** **Daniel:** And I know that many of the players are experiencing this for the first time in London. I read that also — I think it's also WeRide — that want to also create a **right-hand drive version of their GXR**. So some people ask, "okay, what is the point? Do you then put the steering wheel on the right-hand side, or what is the difference?" Can you talk about that? **Dominic:** I think there are two things here. First of all, I think it's really great that WeRide has decided to invest into creating a right-hand drive vehicle, because it really shows their commitment to right-hand drive markets — and I honestly want to really **salute Tony Han** for that. Basically, it underscores his commitment towards cities like London and Singapore.
**中文：** **Daniel：** 我知道很多玩家是**在伦敦第一次遇到这个问题**。我也读到——我想也是 WeRide——他们要做 **GXR 的右舵版本**。那有人会问：「这有什么意义？不就是把方向盘挪到右边吗，差别在哪？」能不能讲讲这个？**Dominic：** 我觉得这里有两件事。首先，**WeRide 决定投入做右舵车型，这非常了不起**，因为它真正体现了他们对右舵市场的承诺——说真的，我想为此**向 Tony Han（韩旭）致敬**。这突显了他对伦敦、新加坡这类城市的投入。

---

**[29:31 – 30:10]**

**EN:** **Dominic:** One thing that is also extremely helpful is the fact that the GXR vehicle that we're using **has one sliding door**. So by configuring the vehicle in right-hand drive mode, it also means that the sliding door actually opens on the **correct side** — meaning for passengers to board and get off easily — versus if we continued on with the left-hand drive vehicle, you'd end up having situations where the door has to open onto incoming traffic.
**中文：** **Dominic：** 还有一点也极其有用：我们用的这台 **GXR 有一扇侧滑门**。所以把车配成**右舵**之后，**侧滑门也会开在正确的一侧**——乘客上下车更方便；而如果继续用左舵车型，就会出现**门朝着迎面车流打开**的情况。

---

## 九、自动配送与机器人 · Autonomous delivery and robotics

**[30:10 – 30:53]**

**EN:** **Daniel:** So we've now talked a lot about the general ride-hailing part of your business, but you also have another half of your business, which is **delivery** — which you introduced also in the intro. So **Zelos** is also an autonomous logistics company; this was one of your four original **MoU** partners. Vietnam was announced as an autonomous vehicles and delivery-robots market. So in a dense Southeast Asian city, is autonomous goods movement maybe also a **better product-market fit** than moving passengers? Or where does it actually sit in your priority stack?
**中文：** **Daniel：** 我们聊了很多出行业务这一半，但你们还有另外一半——**配送**，你在自我介绍里也提到了。**Zelos** 也是一家自动驾驶物流公司，是你们最早那四家 **MoU 伙伴**之一；越南当时被宣布为自动驾驶车辆与配送机器人的市场。那么在一座密集的东南亚城市里，**货物运输是不是比载人更「产品—市场契合」**？还是说，它在你们的优先级排序里处在什么位置？

---

**[30:53 – 31:32]**

**EN:** **Dominic:** Yeah, well, I want to say that using robotics for deliveries is actually an incredibly interesting use case, and it ties in with what we term as **urban embodied AI** in general. We really do see that there is an interesting use case that is emerging, which is basically using robotics for deliveries to **complement** the actual human delivery service. There are two specific problems that robotics actually helps us solve in this situation. The first problem is actually the **first-and-last-mile problem**, because we actually find that in many situations — especially when you're doing a delivery service in very heavily built-up urban environments — you have delivery riders actually spending a lot of time trying to deliver a package or a food order within a high-rise building: you're waiting for the elevator, you're trying to locate the apartment unit.
**中文：** **Dominic：** 我想说，**用机器人做配送其实是一个极其有意思的场景**，它和我们所说的**「城市具身智能（urban embodied AI）」**整体上是连在一起的。我们确实看到一个正在浮现的场景：**用机器人配送去「补充」人类配送服务**。在这个情境里，机器人帮我们解决两个具体问题。第一个其实是**首末公里问题**：我们发现在很多情况下——尤其是在楼宇极其密集的城市环境里做配送时——**骑手会在高层建筑里耗掉大量时间**去送一个包裹或一份餐：等电梯、找门牌号。

---

**[31:32 – 32:11]**

**EN:** **Dominic:** Sometimes you have to pick up the food in a massive shopping mall as well — so it's very difficult to find where exactly you're supposed to be going to pick that up. And we find that actually there is about **10% of a delivery rider's time that is wasted** having to navigate all of this, versus being on the road in transit towards the delivery destination. So we feel that first-last mile is probably something that robotics can actually help us a lot with. And at the same time, during **supply peaks** — we talked about how demand spikes during peak periods — for food delivery, for grocery delivery, they all have separate peaks: delivery during the lunch and dinner-time crowd. We basically hope to also use robots to complement the actual delivery riders, to **smooth out that curve** a little bit.
**中文：** **Dominic：** 有时候你还得在**巨大的商场里取餐**——要找到到底该去哪里取，非常困难。我们发现，**骑手大约有 10% 的时间是被浪费掉的**——不是花在去目的地的路上，而是花在处理这些事上。所以我们觉得，**首末公里很可能正是机器人能帮上大忙的地方**。同时，在**供给峰值**方面——我们前面谈过需求在高峰怎么飙升——外卖和生鲜各有各的峰值：午餐档和晚餐档。我们大体上希望**也用机器人来补充骑手**，把这条曲线**抹平一点**。

---

**[32:11 – 32:50]**

**EN:** **Dominic:** Now, to this end, we're actually considering innovations from many different players. **Zelos** is obviously one of them, and we're trying to work through suitable use cases where we can actually use that solution in different parts of Southeast Asia. We also have an **in-house robotics team** that has a solution called **Carri**. So Carri is actually an **indoor-outdoor robot** as well, so it's very unique in that the robot can actually travel indoors and some part outdoors. And so, in a way, it kind of solves that problem of having to navigate a very, very complicated complex or campus.
**中文：** **Dominic：** 为此，我们其实在考察很多不同玩家的创新。**Zelos** 显然是其中之一，我们正在**打磨合适的用例**，看能不能在东南亚不同地方用上这套方案。我们还有一支**内部机器人团队**，做了一款叫 **Carri** 的方案。Carri 其实是一款**室内外一体的机器人**，它的独特之处在于**既能室内通行、也能在部分室外场景通行**——所以在某种意义上，它解决的正是**在非常复杂的大型综合体或园区里穿行**这个问题。

---

**[32:50 – 33:13]**

**EN:** **Dominic:** And you can imagine a situation in which a delivery rider just shows up at the **entrance of a mall**, and Carri kind of comes and he picks up the order from Carri — versus having to navigate the depths of the mall to actually find the restaurant or the cafe to pick the order up from. So these are some of the examples of emerging use cases that we're seeing, and we're actually very excited to continue experimenting to find out how best we can actually complement our existing service.
**中文：** **Dominic：** 你可以想象这样一个场景：**骑手只需要出现在商场门口**，Carri 过来，他从 Carri 那里取走订单——而不必**深入到商场内部**去找那家餐厅或咖啡店取餐。这些就是我们看到的、正在浮现的用例中的一些例子。我们也非常期待继续做实验，找出**最能补充现有服务的方式**。

---

## 十、为什么要买股权，而不是签供货协议 · Equity stakes and AV partners

**[33:13 – 33:33]**

**EN:** **Daniel:** Super interesting. And maybe let's also talk a bit more about the strategy behind all of this, because you mentioned you have an in-house solution, but you also have taken **equity in players like WeRide, May Mobility, Momenta, also Vay**. So why pay for something you could arguably probably get with a commercial supply agreement?
**中文：** **Daniel：** 很有意思。我们再多聊聊这背后的战略：你刚提到你们有内部方案，但同时你们也**在 WeRide、May Mobility、Momenta，还有 Vay 这些玩家身上持了股**。所以，**为什么要在可以签一份商业供货协议拿到的东西上，用股权去买？**

---

**[33:33 – 34:43]**

**EN:** **Dominic:** Now, that's a very interesting question. We ask ourselves this question all the time. But as I told you, I've spent quite some time looking at this space already. And I think one conclusion that I've drawn from all the different partnership deals that have happened over the years is that **it's really critical to actually drive strategic alignment with your partner**. Because autonomous technology is still a technology that is being worked out — it is not at a stage of yet being commoditized; that technology is still being refined. And **equity investment is actually really, really key for joint strategic alignment and ecosystem integration**. Because as we are finding out in the partnership with WeRide, there is a lot of work that needs to be done that traverses technology integration, operations, data, regulations — and you really need your partner to be able to **lean in with you** to solve all of these things, which are very frequently intertwined with one another. Which is why we decided that an equity investment, where both parties have their incentives aligned and their interests aligned, is the best way to really drive the **joint ownership of the deployment**, so that both parties can actually grow and mature together.
**中文：** **Dominic：** 这是个很有意思的问题——**我们自己也在不停地问自己。** 但如我所说，我已经在这个领域花了不少时间。这么多年看过各种不同的合作交易之后，我得出一个结论：**真正和伙伴建立「战略一致性」是极其关键的。** 因为自动驾驶技术**仍然是一门正在被「做出来」的技术**——它还远没到被**商品化**的阶段，技术本身还在被持续打磨。而**股权投资，恰恰是达成「联合战略一致性」与「生态整合」的真正关键**。因为正如我们在与 WeRide 的合作中发现的那样：**有大量工作要做，而且横跨技术集成、运营、数据、监管**——你真的需要你的伙伴**跟你一起把身子探进来**，去解决这些彼此高度纠缠的问题。这就是为什么我们认定：**一笔让双方激励对齐、利益对齐的股权投资，才是真正推动「共同拥有这次部署」的最好方式**，从而让双方能**一起成长、一起成熟**。

---

**[34:48 – 35:24]**

**EN:** **Daniel:** Makes sense. And maybe now flip it around — now from an AV developer's side of the table: what does Grab bring to them that they cannot build or buy themselves? And I would say **demand** is the easy answer. So give me the second and the third reason, maybe. **Dominic:** Yeah, I think that it varies from partner to partner. So I can give you a few general points that I guess hold true across many of the different partners that we've had discussions with. I will say, first of all, it is **real-world data**.
**中文：** **Daniel：** 说得通。那我们反过来站到**自动驾驶开发者**那一侧问：**Grab 能给他们什么，是他们自己造不出来、也买不到的东西？** 我想**「需求」**是最容易想到的答案。所以请给我第二和第三个理由。**Dominic：** 我认为这**因伙伴而异**。我可以给你几条**在多数伙伴身上都成立的一般性**答案。首先第一条，是**真实世界数据**。

---

**[35:24 – 36:06]**

**EN:** **Dominic:** Because basically, across **20 billion rides and deliveries since our inception, 14 years' worth of data**, we do have operating data on the different kinds of conditions in the ride-sharing domain and the food-delivery domain. So in many occasions, partners have actually found this experience very interesting and very useful in helping them **accelerate the tackling of edge cases** and understanding and predicting how exactly the stack is going to work in different situations. And for us, because we have so many driver-partners on our platform with great driving behaviours, we also **enrol our driver-partners in the process of training up the autonomous vehicle**, so that the vehicle actually performs like a really, really well-trained chauffeur driver. So you can actually see this in the **finesse of the ride** when you actually take it in Singapore versus other deployments. So we do feel that this experience, this data, is something that is very cherished by our partners.
**中文：** **Dominic：** 因为基本上，**从创立至今 200 亿单出行与配送、14 年的数据**，我们确实拥有网约车与外卖两个领域、各种条件下的运营数据。所以很多时候，伙伴们发现这些经验**很有意思、也非常有用**，能帮他们**加速攻克边缘场景**，并理解、预测这套栈在不同情境下会怎么表现。而对我们来说，因为平台上有大量驾驶行为非常优秀的司机伙伴，我们**也会把司机伙伴纳入到自动驾驶车辆的「训练」过程中**，让车表现得**像一位训练得极好的专职司机**。你在新加坡坐这台车时，能从**乘坐的细腻程度**上感受到这一点——和别处的部署不太一样。所以我们确实认为，**这些经验和数据，是我们的伙伴非常珍视的东西**。

---

**[36:06 – 36:42]**

**EN:** **Dominic:** The second thing that we could bring to the table is a **regulatory relationship**. Because as I told you earlier, one thing that we have also set in place, as a result of our many years of operating in the region, are the deep regulatory relationships that we have forged with the different regulators in the region. One of the great things about these relationships is that they allow us to **co-create** — because you call them a regulator, but the relationship that we have with them is one where we feel comfortable enough to come to the table to say, "we have these ideas, we would like to implement them, and we would like to sit down with you to actually look at how policy can accommodate this new technology." And in many occasions, I would say we have been received with **open-mindedness and collaboration** — and I think that's something that's extremely critical and important, especially when it involves the rollout of new technology and new innovation.
**中文：** **Dominic：** 第二件我们能带到桌上的东西，是**监管关系**。如我前面所说，我们在这一区域经营多年，也由此建立起**与各地监管机构之间深度的关系**。这些关系最棒的一点，是它们让我们可以**共创**——虽然你称他们为监管者，但我们和他们之间的关系，**足以让我们舒服地坐到桌前说**：「我们有这些想法，我们想把它落地，我们想跟你们一起坐下来，看看**政策怎么去容纳这项新技术**。」而在很多场合，我们遇到的是**开放的心态和协作的意愿**——我认为这一点极其关键、也极其重要，尤其是在涉及新技术、新创新的落地时。

---

**[36:42 – 37:19]**

**EN:** **Dominic:** The third aspect of this is actually **workforce capabilities**. And what I mean by this is that in certain markets, we do see that governments actually view **gig-economy workers** as a very integral pillar to the economy. In Southeast Asia, in fact, in many jurisdictions, the informal gig economy is actually a very, very important category of the workforce that the government prioritizes — because depending on the economic situation in the country, because you have different economic cycles, you have ups and downs, they actually look to it as a means of providing **transitory employment** as people move between jobs.
**中文：** **Dominic：** 第三块是**劳动力能力**。我的意思是，在某些市场，我们确实看到政府把**零工经济劳动者**视为经济中**非常核心的一根支柱**。在东南亚，事实上在很多司法辖区，**非正规的零工经济**是政府高度重视的一类劳动力——因为经济有周期、有起落，**他们会把它当作一种「过渡性就业」的手段**，让人们在工作转换之间有个去处。

---

**[37:19 – 38:00]**

**EN:** **Dominic:** So because of the contribution and how integral they are to the economy, they also do believe that whenever you bring in innovative new technologies, it's also important to **take care of this workforce**, this informal economy as well. And this is where Grab also plays a very significant role, because many of these informal gig-economy workers actually work on our platform as driver-partners or delivery-partners. So we also feel that it's very important that as we get ahead of the technology, we also **help them transition into potential new jobs** that open up as a result of these new technologies forming.
**中文：** **Dominic：** 正因为这一群体对经济的贡献和重要性，政府也相信：**每当你引入新的创新技术时，同样重要的是要照顾好这部分劳动力、照顾好这个非正规经济。** 而 Grab 在这里恰好扮演着很重要的角色——因为这些非正规零工劳动者里，**很多人就是在我们平台上做司机伙伴或配送伙伴**。所以我们同样觉得，**在技术往前跑的时候，帮他们过渡到新技术所创造出的新岗位**，非常重要。

---

**[38:00 – 38:39]**

**EN:** **Dominic:** I mean, one could say that as much as there is a lot of uncertainty about whether or not AI could actually impact jobs, you also see a world in which it helps to create a lot of new opportunities. And in the autonomous space, we actually see that in the form of **safety drivers, remote operators, fleet management specialists**. We actually do need a lot of people who are well trained in the mobility sector to come and support the entry into service of these vehicles. So those, I would say, are the areas that we would help them. And I guess in addition to that, I mentioned something earlier, which is the **physical localization layer** as well. So our invitation to partners is basically: **come as you are — we will work with you to make Singapore work.**
**中文：** **Dominic：** 有人会说，AI 会不会冲击就业，存在大量不确定性；但你**也能看到另一个世界——它创造出很多新机会**。在自动驾驶领域，我们看到的形态是：**安全员、远程操作员、车队管理专家**。我们确实需要大量在出行行业受过良好训练的人，来支撑这些车辆投入服务。所以这些就是我们能帮上忙的方面。此外，我前面还提到过一点——**物理层面的本地化层**。所以我们对伙伴的邀约其实很简单：**「你就带着你现在的样子来，我们跟你一起，让新加坡跑通。」**

---

## 十一、Vay 与「辅助式自动驾驶」 · Vay and assisted autonomy

**[39:16 – 39:53]**

**EN:** **Daniel:** That's super interesting. So one partner I mentioned earlier — one investment in this way — Vay is not necessarily autonomy; it's like a human driving remotely. And you invested **60 million dollars**, which is also a serious signal. So is remote driving for you a **bridge technology**, or is it a **permanent layer in the stack**? Or maybe also a **hedge**, in case Level 4 takes longer than everyone hopes?
**中文：** **Daniel：** 很有意思。前面提到的一个伙伴、一笔投资——**Vay**，严格说它不算自动驾驶，更像是**「人在远端开车」**。你们投了 **6,000 万美元**，这本身也是一个很重的信号。那么**遥驾（remote driving）**对你们来说，是一项**过渡技术**？还是**技术栈里长期存在的一层**？又或者，是**万一 L4 比所有人期望的都要慢时的一个对冲**？

---

**[39:53 – 40:31]**

**EN:** **Dominic:** Yeah, so earlier on, when I was sharing about the role of the GM of Autonomous, I did say that one pillar in the vision was to keep a lookout for technologies that may be relevant in Southeast Asia five to ten years down the road. **Vay** stood out as a very interesting candidate as we were considering the entire spectrum of driverless technologies — because I think Vay is an incredible company, I think they have really done a lot of great work in integrating the remote driving stack into the vehicles. So from an engineering perspective, I think they're really a great company. I would say that we are working with them to actually understand operationally where they stand in this world where autonomy is picking up. We see them as a very interesting **alternative technology** that has the means of delivering a ride-share service or car-sharing service **at a fraction of the cost** of what the incumbents are offering today.
**中文：** **Dominic：** 好。前面我讲自动驾驶总经理这个角色时说过，愿景里有一根支柱，就是**去前瞻那些五到十年后可能对东南亚有意义的技术**。在我们审视**整个「无人驾驶技术谱系」**的时候，**Vay** 是一个很突出的有趣候选——因为我认为 Vay 是一家了不起的公司，他们在**把遥驾技术栈集成进车辆**这件事上做得非常出色。所以从工程角度看，他们真的是很棒的公司。我们正在和他们一起**从运营层面理解**：在自动驾驶势头起来的这个世界里，他们处在什么位置。我们把他们看作一项**很有意思的「替代性技术」**——它有能力以**远低于现有玩家成本**的方式，去交付共享出行或共享汽车服务。

---

**[40:31 – 41:05]**

**EN:** **Dominic:** And to that end, we are working with them on many different business models to try to achieve this end goal. Now, in the area of autonomy, in fact, I will say that one interesting and emerging idea is basically what we call **assisted autonomy** — whether or not the remote driving stack that Vay has can actually be a very nice complement to help the autonomous industry. And to that end, they already have a partnership with **Kodiak**, for example — I know Vay is actually integrated into Kodiak today. At the same time, could they also be used in **vehicle recovery**, for example? Because they also happen to have a deployment in **Vegas**, where you have a lot of autonomous vehicle players that are currently running commercial services there. So I think Vay gives us an opportunity to really push the boundaries of how we're thinking about autonomy, by presenting a technology that can be very nicely complementary to the incumbents.
**中文：** **Dominic：** 为此，我们正在和他们一起试**很多不同的商业模式**，去逼近这个目标。而在自动驾驶领域，我想说一个**很有意思、正在浮现的概念**，我们叫它**「辅助式自动驾驶（assisted autonomy）」**——也就是：Vay 的遥驾栈，能不能成为**辅助整个自动驾驶产业的一个很好的补充**？在这方面，他们**已经和 Kodiak 建立了合作**，我知道 **Vay 现在已经集成进了 Kodiak**。同时，它能不能也用于**车辆救援（vehicle recovery）**？因为他们恰好在**拉斯维加斯**有部署，而那里有大量正在做商业运营的自动驾驶玩家。所以我认为，**Vay 给了我们一个机会，去把「我们如何思考自动驾驶」的边界真正往外推**——因为它提供了一项**能与现有玩家很好地互补**的技术。

---

## 十二、Waymo 进入新加坡 · Waymo enters Singapore

**[41:41 – 42:24]**

**EN:** **Daniel:** Sound exciting. And now let's come to the big news in Singapore: **Waymo** just announced they're also launching in Singapore — in 2027 they want to start, and they want to provide commercial rides in 2028. So how are you viewing this development? **Dominic:** Daniel, as someone who has looked at this industry for a long time, I want to say I am **extremely excited** about it. I am really glad that Waymo is actually joining us and **ComfortDelGro** on this joint mission of creating a thriving autonomous landscape for Singapore. There are three reasons for this. First of all, from a **consumer perspective**, Singaporean riders will now get **more choice**, because they would be able to choose from existing operators as well as the new operator Waymo, and make their own decisions on which operator actually serves them the best.
**中文：** **Daniel：** 很激动人心。现在我们来说新加坡最大的新闻：**Waymo** 刚刚宣布也要进入新加坡——2027 年启动，2028 年提供**商业载客**。你怎么看这件事？**Dominic：** Daniel，作为一个看了这个行业很久的人，我想说我**极其兴奋**。我真的很高兴 Waymo 加入到我们和 **ComfortDelGro** 的行列里，**共同为新加坡打造一个繁荣的自动驾驶生态**。理由有三点。第一，从**消费者角度**：新加坡乘客会有**更多选择**——他们可以在现有运营方和新运营方 Waymo 之间做选择，**自己判断谁服务得最好**。

---

**[42:24 – 43:00]**

**EN:** **Dominic:** Second of all, I would say that **Waymo's entry is a validation that there is a pathway to commercialization even in a market like Singapore, where the economics are difficult**. So in a way, it kind of validates all the intuition that we had about "is Singapore viable as a market?" And I feel like Waymo's entry will also end up **accelerating a lot of our thinking around the regulatory frameworks and the safety frameworks**. So all in all, I would say that it's a very positive development for autonomy in Singapore and Southeast Asia, and I'm really excited about them coming. On our end, we're staying **laser focused** on delivering our service in Singapore, and we're really excited about the expansion that we have announced already — the **five-fold fleet increase** that's coming online very soon, how we're actually going to be carrying passengers on autonomous ride-hailing services very soon. And I really look forward to being able to work in **lockstep with the Singapore government** to really work through the regulatory changes that will need to take place to accommodate all of us, while at the same time serving the Singaporean population.
**中文：** **Dominic：** 第二，我认为 **Waymo 的进入本身就是一种「验证」——证明即便在新加坡这种经济模型很难算的市场，商业化也是有路可走的**。所以从某种意义上，它**验证了我们所有的直觉**：新加坡作为一个市场到底是否可行。我也觉得 Waymo 的进入会**加速我们在监管框架和安全框架上的思考**。总而言之，我认为这对新加坡和东南亚的自动驾驶是一个非常积极的进展，我很期待他们到来。而我们这一边，会**极度聚焦**于在新加坡把服务交付好；我们对已经宣布的扩张也非常兴奋——**车队规模扩大五倍**很快就会上线，很快我们就会用**自动驾驶叫车服务**来载客。我非常期待能**与新加坡政府步调一致地协作**，把需要发生的监管变化推进下去，以容纳我们所有人，同时服务好新加坡民众。

---

## 十三、规模化时，谁持有车队？ · Who owns the fleet at scale

**[43:00 – 43:40]**

**EN:** **Daniel:** And maybe one follow-up question, because you again mentioned the five-fold increase of your fleet, and at the beginning you mentioned that you own the first WeRide vehicles. So if you look at things at scale, do you still want to **own the vehicles and carry the CapEx**? Or would you want to have **third-party fleet ownership** as well? So what would be the model at scale, at the end?
**中文：** **Daniel：** 我想追问一个问题。你又提到车队要扩大五倍，而开头你说**第一批 WeRide 车辆是你们自己持有的**。那么如果看规模化之后——你们还打算**自己持有车辆、承担资本开支（CapEx）**吗？还是也希望能有**第三方持有车队**？所以最终、规模化之后的模式会是什么样？

---

**[43:36 – 44:12]**

**EN:** **Dominic:** So Grab is actually not a stranger to owning CapEx, because in our part of the world we have actually **set up rental car companies in Singapore, Malaysia and Indonesia**, where we actually own the assets on our balance sheet. And the reason for this is simple: it's because in our part of the world, many drivers have difficulty getting access to credit to be able to purchase their own cars. And so, in having our own rental companies, we've basically made it a little bit easier for them to actually get access to a vehicle to drive on our platform. And we had made these investments in the early days when we first started the ride-hailing service — and the reason for this was because **the ecosystem hadn't yet grown**.
**中文：** **Dominic：** 其实 **Grab 对持有 CapEx 并不陌生**——在我们这一带，我们**在新加坡、马来西亚和印尼都设立了租车公司**，这些资产是**记在我们资产负债表上的**。原因很简单：在这一带，**很多司机很难获得信贷去买自己的车**。通过自营租车公司，我们**让他们更容易拿到一台能上我们平台跑活的车**。这些投资是我们在**刚做网约车业务的最早期**就做的——原因就是，**当时的生态还没有长出来**。

---

**[44:12 – 44:50]**

**EN:** **Dominic:** So we took it upon ourselves to say, "let's make this easy for our drivers to be able to come onto our platform." I see this evolution happening similarly in autonomous as well — which is that, at the onset, as I mentioned earlier, you may have fleet owners who are **waiting and watching** to see if this is actually a viable business to be had. So we happen to be in this phase where the technology and the business model are still being proven. I would say that **until we get full regulatory clearance to actually run a sustainable business in many parts of Singapore, it is likely that we will still end up owning the CapEx and operating CapEx ourselves.**
**中文：** **Dominic：** 所以我们**主动承担**了这件事，说：「让我们把司机上平台这件事变得容易。」我认为**自动驾驶会经历非常相似的演化**——如我前面提到的，起步阶段，**会有车队业主选择「观望」，看这到底是不是一门可行的生意**。所以我们恰好处在这样一个阶段：**技术和商业模式都还在被验证**。我会说：**在我们拿到完整监管许可、能够在 Singapore 的许多区域真正经营一门可持续的生意之前，很可能我们仍要自己承担持有成本和运营开支。**

---

**[44:50 – 45:14]**

**EN:** **Daniel:** Makes sense. Dominic, we're at the end, so thank you so much for taking the time today. It was really insightful to learn more about Grab, to learn more about the Southeast Asian market, and all the special edge cases you encounter over there. So thanks again for joining me today on the podcast. **Dominic:** Thanks so much, Daniel, for having me. Really enjoyed this conversation. Catch up with you soon.
**中文：** **Daniel：** 说得通。Dominic，我们到尾声了，非常感谢你今天抽时间。能更了解 Grab、更了解东南亚市场，以及你们在那里遇到的各种特殊边缘场景，收获很大。再次感谢你来上节目。**Dominic：** 非常感谢你邀请我，Daniel。这次对谈我非常享受，回头再聊。

---

*逐字稿来源：本机 Whisper 语音转写（small.en，598 段，音频取自该期 Substack/RSS 官方 mp3，时长 45:14）。英文保留转写形态并按上下文校正；中文为人工翻译。主要校正条目：WeRide（原 We Write / B-Rite / rewrite）、Punggol（原 Pongol / Pongo / Pong World）、Carri（原 Cary / Kari）、Zelos（原 Elos / Sailors）、KartaDashcam（原 Carta dash cams）、nuTonomy（原 Neutonomy）、Drive.ai（原 Drive AI）、ComfortDelGro（原 comfort Delgore）、Vay（原 Vey / VA）、Kodiak、miles per critical intervention（原 mouse per critical intervention）、ride-hailing（原 right chair / right healing / ridegaling）、MoU（原 NYU）。*
