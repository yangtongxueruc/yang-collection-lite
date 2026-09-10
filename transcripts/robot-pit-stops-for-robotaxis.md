**[00:04 – 00:23]**
**EN:** Welcome to Autonomy Insiders, the show where global industry leaders in autonomous driving unpack their real world insights. We build robotic pit stops for self-driving cars. Effectively, this is distributed depot footprint directly within the heart of the
**中文：** 欢迎收看 Autonomy Insiders，该节目将向全球自动驾驶行业领导者展示他们对现实世界的见解。我们为自动驾驶汽车建造机器人维修站。实际上，这是直接位于系统中心的分布式仓库足迹

**[00:23 – 00:43]**
**EN:** operating zone. What the vehicles need is a very dense, very widely on-demand available network directly in the pockets of demand such that you cannot just offer pit stops in the center of the city on demand. You can do micro resets because this is where the real economic outlook is.
**中文：** 操作区。车辆需要的是一个非常密集、非常广泛的按需可用网络，直接在需求范围内，这样你就不能只在城市中心按需提供停车站。你可以进行微观重置，因为这才是真正的经济前景所在。


## Introduction · 介绍

**[00:49 – 01:04]**
**EN:** Welcome to Autonomy Insiders. I'm your host, Daniel, and most conversations about autonomy are about the driver, the software, the sensors, the miles. This episode is about the other part, cleaning, inspection, getting a car ready to earn money again. My guest is building a robot
**中文：** 欢迎来到 Autonomy Insider。我是主持人，丹尼尔，大多数有关自动驾驶的对话都是关于驾驶员、软件、传感器和里程。这一集是关于另一部分，清洁，检查，准备一辆车再次赚钱。我的客人正在建造一个机器人

**[01:04 – 01:20]**
**EN:** that sits in a single parking space and does all of that so the car never has to leave the neighborhood it is earning in. George Kalligeros is co-founder and CEO of Aseon Labs. Aseon came out of stealth in May and announced a $10 million seat in June. So, George,
**中文：** 它位于一个停车位中，可以完成所有这些工作，因此汽车永远不必离开它所赚钱的社区。George Kalligeros 是 Aseon Labs 的联合创始人兼首席执行官。 Aseon 在 5 月份走出了隐秘状态，并在 6 月份宣布了 1000 万美元的席位。所以，乔治，

**[01:20 – 01:32]**
**EN:** welcome on the show and I'm so happy to have you on today. Thanks, Daniel. Thanks so much for inviting me. So, before we go anywhere, maybe in plain terms, so what is Aseon and what does a fleet operator
**中文：** 欢迎来到这个节目，我很高兴今天有你参加。谢谢，丹尼尔。非常感谢你邀请我。所以，在我们去任何地方之前，也许简单地说，什么是 Aseon 以及车队运营商是什么


## What Aseon is, and what an operator actually buys · Aseon 是什么以及运营商实际购买什么

**[01:32 – 01:52]**
**EN:** actually get from you? Yeah. So, Aseon would build robotic pit stops for self-driving cars. Effectively, this is distributed depot footprint directly within the heart of the operating zone. So, an AV operator gets from us powered ground and fully robotic operations as a service.
**中文：** 真的从你那里得到吗？是的。因此，Aeon 将为自动驾驶汽车建造机器人维修站。实际上，这是直接位于操作区域中心的分布式仓库占地面积。因此，自动驾驶操作员可以从我们那里获得动力地面和完全机器人操作作为服务。


## Inside the box: one bay, two robotic arms · 箱内：一个托架，两个机械臂

**[01:52 – 02:09]**
**EN:** And can you also describe this part as a physical option? So, maybe if I would stand next to it in a parking lot, so how big is it? What do I see? Maybe also what moves? Yeah, for sure. So, as you described, it very much looks like a box and it occupies one
**中文：** 您能否将这部分描述为物理选项？那么，也许如果我在停车场站在它旁边，那么它有多大？我看到了什么？也许还有什么动静？是的，当然。因此，正如您所描述的，它看起来非常像一个盒子，并且占据了一个

**[02:09 – 02:26]**
**EN:** typical charging bay, right? So, the product in European terms is about 6 meters long and 2.7 meters wide and you don't really see much from the outside. I'll share with you a photo that you can pull up. This is the latest version of the product that we're building currently
**中文：** 典型的充电座，对吗？因此，按照欧洲标准，该产品长约 6 米，宽约 2.7 米，从外面看不到太多。我将与您分享一张您可以调出的照片。这是我们当前正在构建的产品的最新版本

**[02:26 – 02:41]**
**EN:** in Menlo Park, California. It's going to be great in October. You can peer from the inside and you'll see our robotic system which uses two robotic arms with six degrees of freedom that pick from a range of casted tooling to do a bunch of interesting things on the autonomous vehicles.
**中文：** 在加利福尼亚州门洛帕克。十月份会很棒。您可以从内部观察，您会看到我们的机器人系统，该系统使用两个具有六个自由度的机械臂，可以从一系列铸造工具中挑选出来，在自动驾驶车辆上执行一系列有趣的操作。


## A 20-30 minute reset, bounded by charge rate · 20-30 分钟重置，受充电率限制

**[02:41 – 02:56]**
**EN:** And then from the car's point of view, so it pulls in and then what so roughly, how long is it in there before it's then back taking rides? Yeah, maybe high level for now we can get into the mechanics later, but just to get a picture of it.
**中文：** 然后从汽车的角度来看，它停了下来，那么粗略地说，在它返回乘车之前，它在那里待了多长时间？是的，也许现在我们可以稍后再深入了解机制，但只是为了了解一下它的情况。

**[02:56 – 03:13]**
**EN:** Yeah, so the concept of the product is to compress as much of the depot workflows in a single box. That's why it's called a micro depot. So, the car pulls in, the first thing that happens is after an inspection, the vehicle gets plugged into charge and then a sequence of events takes
**中文：** 是的，所以该产品的概念是将尽可能多的仓库工作流程压缩在一个盒子中。这就是为什么它被称为微型仓库。因此，汽车停下来后，首先发生的事情是检查后，车辆插入充电，然后发生一系列事件

**[03:13 – 03:26]**
**EN:** place that takes anywhere between 20 to 30 minutes. The main thing that drives the time inside the pod is the charging rates and how long we keep the vehicle into charge. Every single other operation that we do effectively falls within that window. So,
**中文：** 需要 20 到 30 分钟的地方。影响充电舱内时间的主要因素是充电速率以及车辆充电的时间。我们有效执行的所有其他操作都属于该窗口范围。所以，

**[03:27 – 03:44]**
**EN:** yeah, this is the core. So, now we have a good picture and now I want to understand what that replaces. Maybe walk me through what happens today without you and your product. So, a robot taxi, for example, in San Francisco needs a reset, a two in the afternoon. So,
**中文：** 是的，这就是核心。所以，现在我们有了一个很好的图片，现在我想了解它取代了什么。也许让我了解一下如果没有你和你的产品今天会发生什么。例如，旧金山的一辆机器人出租车需要在下午两点重置。所以，


## What it replaces: two hours out of service, several times a day · 替代内容：停运两小时，每天数次

**[03:44 – 04:00]**
**EN:** what does that actually cost the operator, maybe also in time and probably also miles? Yeah, for sure. Typically, the primary driver that takes vehicles out of service is the vehicle operates and it falls below its threshold, typically state of charge. So, the vehicle
**中文：** 这实际上给运营商带来了多少成本，也许还有时间，也可能还有里程？是的，当然。通常，导致车辆停止使用的主要驱动因素是车辆运行并且其低于其阈值（通常是充电状态）。那么，车辆

**[04:00 – 04:18]**
**EN:** runs low on battery, maybe it's 20, 25% battery. Then it needs to call into either a maintenance hub, a depot, or a pit stop location, which are smaller rapidly deployed locations near the operating zone. San Francisco actually has good infrastructure to support robot taxi
**中文：** 电池电量不足，可能还有 20%、25% 的电量。然后，它需要呼叫维护中心、仓库或维修站位置，这些都是靠近操作区的较小的快速部署位置。旧金山实际上拥有良好的基础设施来支持机器人出租车

**[04:18 – 04:35]**
**EN:** ops and it's a relatively compressed city. So, maybe depending on where you're in the city, maybe within three to five miles, the car can drive to a depot and then gets charged and serviced. The service typically takes about, I'd say, anywhere between 40 minutes to 80 minutes.
**中文：** 操作，这是一个相对压缩的城市。因此，也许取决于您在城市中的位置，也许在三到五英里之内，汽车可以开到车库，然后进行充电和维修。我想说，该服务通常需要大约 40 分钟到 80 分钟。

**[04:35 – 04:49]**
**EN:** Let's say the hour is the average and then it might need to travel another 40 minutes back and forth. So, typically, the vehicle is out of service, let's say two hours with every sort of recharge operation, but that happens multiple times in a day.
**中文：** 假设这个时间是平均时间，那么来回可能还需要 40 分钟。因此，通常情况下，车辆会停止服务，假设每次充电操作都会停止两个小时，但这种情况一天会发生多次。

**[04:49 – 05:06]**
**EN:** Makes sense. And you and also, I think, your co-founder, you visited also AV depots while researching all of this. So, what did you see there that you did not expect? Yeah, we did. I don't think we saw anything that we did not expect. They ran efficiently,
**中文：** 有道理。我认为您和您的联合创始人在研究所有这些内容时也访问了 AV 仓库。那么，你在那里看到了什么是你没有想到的呢？是的，我们做到了。我认为我们没有看到任何我们没有预料到的东西。他们高效地奔跑，


## What they found inside real AV depots · 他们在真实的 AV 仓库中发现了什么

**[05:06 – 05:26]**
**EN:** they were well equipped, they're relatively new, right? I think what became strikingly obvious is how difficult it is to run human operations and how difficult it is to incentivize the human operators to effectively carry out the repeat high-frequency tasks in the depot. And yeah,
**中文：** 他们装备精良，而且相对较新，对吧？我认为，显而易见的是，进行人工操作是多么困难，以及激励人工操作员有效地执行仓库中重复的高频任务是多么困难。是的，

**[05:26 – 05:44]**
**EN:** this effectively kicked off a lot of inspiration for why we are now building with robotics. And I think you said also that roughly a third of a fleet is offline at any given time. So, is that also a number operators recognize and accept or is it also more number that
**中文：** 这有效地激发了我们为什么现在使用机器人技术进行构建的很多灵感。我想你也说过，在任何特定时间，大约有三分之一的机队处于离线状态。那么，这也是运营商认可和接受的一个数字，还是也是更多的数字？


## A third of the fleet offline at any given time · 在任何给定时间，三分之一的机队处于离线状态

**[05:44 – 05:57]**
**EN:** surprises them maybe when you put it in front of them? Yeah. So, these figures were pulled from a public report. I think it was Harry Campbell basically doing some analysis on the Waymo fleet a year and a half ago. But the operators have a really,
**中文：** 当你把它放在他们面前时，他们可能会感到惊讶吗？是的。因此，这些数字是从公开报告中提取的。我认为一年半前 Harry Campbell 基本上对 Waymo 车队进行了一些分析。但运营商确实有一个

**[05:57 – 06:14]**
**EN:** really good grasp of their core metrics. And that number came from what's the percentage of fleet that could be servicing customers but are currently either traveling to the depot or being serviced or they're queuing or they're in inspection and cannot deliver a ride at any
**中文：** 确实很好地掌握了他们的核心指标。这个数字来自于可以为客户提供服务但目前要么正在前往车站或正在接受服务，要么正在排队，要么正在接受检查并且无法随时提供乘车服务的车队所占的百分比。

**[06:14 – 06:30]**
**EN:** point in time. We crunched a lot of these numbers to kind of understand what is the effect of the locality of the depot? If it's far from the city, what is the effect in terms of the utilization of the fleet? Because there is this antithesis where today's model of a depot,
**中文：** 时间点。我们处理了大量这些数字，以了解仓库位置的影响是什么？如果距离城市较远，对车队的利用率有何影响？因为今天的仓库模型存在这种对立，

**[06:30 – 06:44]**
**EN:** which is very human-centric, it's all about high throughput and turning the fleet around and trying to compress as much of the servicing in the late hours of the day, whereas a fleet pretty much just needs to be constantly operating utilizing and capturing rides.
**中文：** 这是非常以人为中心的，这一切都是为了高吞吐量和扭转车队并试图在一天的晚些时候压缩尽可能多的服务，而车队几乎只需要不断地利用和捕获乘车服务即可。


## Four years at Tier, and who you can actually incentivise · 在 Tier 工作四年，您可以真正激励谁

**[06:44 – 06:58]**
**EN:** And before Aseon, you also spent four years at Tier also deploying hardware into city set scales. So, what did that period teach you about the operational cost that you could not have learned from the outside, so to speak?
**中文：** 在 Aseon 之前，您还在 Tier 工作了四年，将硬件部署到城市规模中。那么，可以说，那段时期让您学到了什么关于运营成本的知识，而这些是您无法从外部了解到的？

**[06:58 – 07:14]**
**EN:** Operation cost. Tier was a very interesting case study in general. It was a company that transitioned from a growth phase to an operational, sort of like an economic sanity and a profitability phase really quickly. In terms of operating costs, I think the biggest
**中文：** 运营成本。总的来说，Tier 是一个非常有趣的案例研究。这是一家从增长阶段过渡到运营阶段的公司，有点像经济理智和盈利阶段，速度非常快。就运营成本而言，我认为最大的

**[07:14 – 07:28]**
**EN:** learning was Tier had all the companies at the time had very much their own in-house operations for everything from maintenance, rebalancing, charging. And I think Lime innovated on this model where they started outsourcing operations to local entrepreneurs, gig economy workers
**中文：** 据了解，Tier 当时的所有公司都有自己的内部运营，负责维护、重新平衡、充电等各个方面的工作。我认为 Lime 在这种模式上进行了创新，他们开始将业务外包给当地企业家、零工经济工人

**[07:28 – 07:46]**
**EN:** that were much more highly and better incentivized to turn the fleet around, right? So, I think the learning there was doing a really sort of like deep and vertical up structure. It's hard to incentivize the people that are really working with the assets.
**中文：** 他们更有动力更好地扭转舰队的颓势，对吗？所以，我认为那里的学习确实有点像深度和垂直向上的结构。很难激励真正使用资产的人。

**[07:46 – 08:00]**
**EN:** I think that was really the key learning in terms of cost. Interesting. And maybe now let's open the box. So, I want to know which parts of this are solved and which was maybe also are still hard right now. So, there's charging, there's
**中文：** 我认为这确实是成本方面的关键学习。有趣的。也许现在让我们打开盒子。所以，我想知道哪些部分已经解决，哪些部分现在可能仍然很困难。所以，有充电，有


## Which jobs version one does, and which it refuses · 第一版执行哪些工作，拒绝哪些工作

**[08:00 – 08:21]**
**EN:** exterior wash, interior clean, lost items, sensor inspection, data thing. So, that is a lot of different jobs for one machine, so to speak. Which of those is working today and which is maybe also still an open problem? Yeah, it's a good question. I'll preface this by saying
**中文：** 外部清洗、内部清洁、丢失物品、传感器检查、数据处理。因此，可以说，一台机器可以完成很多不同的工作。其中哪些目前有效，哪些可能仍然是一个悬而未决的问题？是的，这是一个好问题。我会以此作为序言

**[08:21 – 08:45]**
**EN:** we should define what a solved problem is because just in robotics, getting to a working demo, getting to a 99% maturity of a feature is let's say 10% of the work. So, we can give you a working demo. The work really is in the last 1% which is being able to correctly and repeatedly tackle edge cases
**中文：** 我们应该定义什么是已解决的问题，因为仅在机器人技术中，进行工作演示、使某个功能达到 99% 的成熟度就相当于 10% 的工作量。因此，我们可以为您提供一个工作演示。真正的工作是在最后 1% 中，能够正确且重复地处理边缘情况

**[08:46 – 09:03]**
**EN:** and building a reliable system in doing that. So, I'll preface it by saying this. Now, we've been very deliberate with selecting which features we build first. So, exterior washing, sensor detailing is not something we're going to do with the first version of the product.
**中文：** 并为此建立一个可靠的系统。因此，我将这样说作为序言。现在，我们非常慎重地选择首先构建哪些功能。因此，我们不会对第一版产品进行外部清洗、传感器细节处理。

**[09:03 – 09:17]**
**EN:** We're also going to be very deliberate about which types of events we will handle. So, the product needs a very robust sort of inspection layer that kind of decides whether we can actually service a vehicle on the edge in the heart of the city versus it needed to go
**中文：** 我们还将非常慎重地考虑我们将处理哪些类型的事件。因此，该产品需要一个非常强大的检查层，以决定我们是否可以真正在城市中心的边缘维修车辆，而不是需要去

**[09:17 – 09:35]**
**EN:** back into the depot. So, what you can expect from V1 is obviously autonomously plugging the vehicle into charge. We do the data sync and the reboot of the vehicle in our station. We inspect and clean the interior of the cabin and that includes removing items left behind. And in the case of
**中文：** 回到仓库。因此，您对 V1 的期望显然是自动为车辆充电。我们在我们的车站进行数据同步和车辆重启。我们检查并清洁机舱内部，包括清除遗留的物品。而在这种情况下

**[09:35 – 09:49]**
**EN:** lost and found, we're simply going to have a runner, a driver that takes a lost wallet, a forgotten wallet back to the depot, and we can effectively release the vehicle back into operation right in the central city. So, this is V1. Super interesting. I think
**中文：** 失物招领时，我们只需派一名跑步者、一名司机将丢失的钱包、遗忘的钱包带回停车场，然后我们就可以在市中心有效地让车辆重新投入运行。所以，这是V1。超级有趣。我认为


## Interior resets: the 90% a robot can close out · 内部重置：机器人可以关闭的 90%

**[09:49 – 10:06]**
**EN:** interior cleaning is also one that I keep coming back to. So, for example, as build coffee is one thing. Somebody may be being sick in the backseat is maybe a completely other thing. So, what share of this interior research can a robot actually close out and what it still needs a
**中文：** 室内清洁也是我经常关注的问题。因此，例如，制作咖啡是一回事。后座上有人生病可能完全是另一回事。那么，机器人实际上可以完成这项内部研究的哪些部分以及它还需要什么

**[10:06 – 10:23]**
**EN:** human? So, firstly, from our analysis, the vast majority of the cleaning operations are generally relatively routine, right? So, the vehicle collects dust. Basically, the soiling is predictable. It's only a few occurrences where you'll have a biohazard or somebody has left
**中文：** 人类？那么，首先从我们的分析来看，绝大多数的清洁操作一般都是比较常规的，对吧？因此，车辆会积聚灰尘。基本上，污染是可以预见的。只有少数情况下您会遇到生物危害或有人离开

**[10:23 – 10:42]**
**EN:** something behind. So, I think we can comfortably say 90% of it is just routine cleaning. So, this is what we're tackling with our system. We're very deliberately not trying to build such that we can cater to every single exception directly in the outskirts of the city. So,
**中文：** 后面的东西。所以，我想我们可以放心地说，其中 90% 只是例行清洁。所以，这就是我们的系统要解决的问题。我们非常刻意地不试图在城市郊区直接建造能够满足每一个例外的建筑。所以，

**[10:42 – 10:55]**
**EN:** vehicle comes in, if it's a biohazard, as you say, somebody's been sick in the back of the vehicle. It's going to be extremely difficult for robotics to ever tackle this unless the robotaxi is built specifically for really ease of cleaning. So, these cases go back to the depot.
**中文：** 车辆开进来，如果是生物危害，就像你说的，车后座有人生病了。对于机器人来说，解决这个问题将非常困难，除非机器人出租车是专门为真正易于清洁而制造的。因此，这些箱子会返回仓库。


## Getting power into a dense-city parking bay · 为人口稠密的城市停车场提供电力

**[10:55 – 11:11]**
**EN:** And power is also a constraint that a lot of people are talking about that. So, you are dropping then a charging-capable unit into the parking space in a dense city. So, how do you get the energy in? And is it also via partnership or how do you do that?
**中文：** 而权力也是很多人都在谈论的一个制约因素。因此，您需要将一个具有充电功能的设备放入人口稠密的城市的停车位中。那么，如何获取能量呢？也是通过合作伙伴关系还是如何做到的？

**[11:12 – 11:31]**
**EN:** Yeah. So, charging is not included with the core products. Effectively, what our station does is it automates the pit stop operations, right? Roboticly. And then for the charging side, there's two models. So, we either partner with charge point operators. So, these are owners and
**中文：** 是的。因此，充电不包含在核心产品中。实际上，我们的加油站所做的就是自动化进站操作，对吧？机器人地。然后在充电方面，有两种型号。因此，我们要么与充电站运营商合作。所以，这些是业主和

**[11:31 – 11:47]**
**EN:** operators of networks of DC fast charging infrastructure across the center of the city. If you go, for example, one of the largest in the US, 2.2% of their capacity is already tied into AV usage, just to give you an example. The other option is to deploy in a satellite
**中文：** 整个城市中心的直流快速充电基础设施网络运营商。例如，如果您去美国最大的之一，其容量的 2.2% 已与 AV 使用相关联，仅举个例子。另一种选择是部署在卫星上

**[11:48 – 12:00]**
**EN:** constellation and bring off-grid power in, again via partnership. So, it would be renewable property and generator, or it would be even hydrogen, battery and historic system. There is a whole host of options.
**中文：** 星座并再次通过合作伙伴关系引入离网电力。因此，它将是可再生财产和发电机，或者甚至是氢、电池和历史系统。有很多选择。


## One pod, many platforms: ID Buzz down to Cybercab · 一个 Pod，多个平台：ID Buzz 到 Cyber​​cab

**[12:00 – 12:15]**
**EN:** Makes sense. And now also every AV platform is more or less different. So, you have the Jaguar I-PACE from Waymo, you have a Zeekr vehicle from Waymo, then you have purpose-built Zoox or Cybercabs. So, maybe there are also different charge ports, different sense of
**中文：** 有道理。现在每个 AV 平台也或多或少有所不同。因此，您可以拥有 Waymo 的 Jaguar I-PACE、Waymo 的 Zeekr 车辆，然后还有专门打造的 Zoox 或 Cyber​​cabs。所以，也许还有不同的充电端口，不同的感觉

**[12:15 – 12:32]**
**EN:** placements, different interiors. So, how do you build in one part that services all of them and does that force also maybe a bit of a standardization conversation with the OEMs? Yeah, I'll answer the second part of your question first. I think there is a general trend,
**中文：** 位置，不同的内饰。那么，如何构建一个为所有这些服务提供服务的部件，这是否也迫使与 OEM 进行一些标准化对话？是的，我先回答你问题的第二部分。我认为有一个总体趋势，

**[12:32 – 12:50]**
**EN:** not of standardization, but of defining products that are fit for robotax use and fit for sort of sliding doors, easy to clean interiors, right? We're going to see a trend. Now, anybody that requires a purpose-built vehicle to operate is not going to work,
**中文：** 不是标准化，而是定义适合 Robotax 使用、适合滑动门、易于清洁内部的产品，对吗？我们将会看到一种趋势。现在，任何需要专用车辆来操作的人都无法工作，

**[12:50 – 13:05]**
**EN:** only someone like Tesla is able to really define the vehicle in such narrow depth. The other part of your question is, so how do we make a single product that does multiple vehicles at a time? So, if you look at the subset of AVs in operation today and the future
**中文：** 只有像特斯拉这样的人才能在如此狭窄的深度上真正定义车辆。您问题的另一部分是，我们如何制造一种可以同时运行多种车辆的单一产品？所以，如果你看看现在和未来运行的自动驾驶汽车的子集

**[13:05 – 13:19]**
**EN:** platforms coming online, it's a relatively small subset. So, we have a three-tiered approach. The core structure is designed to accommodate from the largest vehicle, the Volkswagen ID Buzz, down to the smallest, the Tesla CyberCab. And then we have a universal
**中文：** 上线的平台，它是一个相对较小的子集。因此，我们有一个三层方法。其核心结构旨在容纳从最大的车辆（大众 ID Buzz）到最小的车辆（特斯拉 Cyber​​Cab）。然后我们就有了一个通用的

**[13:19 – 13:37]**
**EN:** robotic system that's effectively able to interface with all of these vehicles within that 3D space, right? We can cover the entire point cloud. The last 10%, which is what we do really well, is we build bespoke tools, bespoke end-of-run tooling end-effectors,
**中文：** 机器人系统能够有效地与 3D 空间内的所有这些车辆进行交互，对吧？我们可以覆盖整个点云。最后 10%，这是我们真正擅长的，是我们构建定制工具、定制运行结束工具末端执行器，

**[13:37 – 13:52]**
**EN:** that allow our robotic system, which is the same across all vehicles, to do the specific vehicle really well. So, the vast majority of the CapEx and the hardware cost sits in the pods in the robotic system, and then we make bespoke tooling that gives you the ability to do a very specific
**中文：** 这使得我们的机器人系统（所有车辆都相同）能够很好地完成特定车辆的工作。因此，绝大多数资本支出和硬件成本都集中在机器人系统的 Pod 中，然后我们制作定制工具，使您能够执行非常具体的操作

**[13:52 – 14:08]**
**EN:** vehicle as good as a human can. Super interesting. And another question that came up in my mind is like, you have one part, one parking space, and maybe there are three cars in that zone that all need a reset at the same time. So, how does that get orchestrated,
**中文：** 车辆与人类一样好。超级有趣。我脑海中出现的另一个问题是，你有一个零件，一个停车位，也许该区域有三辆车都需要同时重置。那么，这是如何精心策划的，


## Orchestration: no queuing, just-in-time only · 编排：无需排队，只需即时

**[14:08 – 14:20]**
**EN:** and who decides also maybe the queue? Yeah, it's a good question. I can give you an answer for what it looks like in the future, but initially, two things. First of all, we're going to deploy over capacity, so we're going to make sure the network is going to be
**中文：** 谁也可以决定队列？是的，这是一个好问题。我可以给你一个关于未来的答案，但首先有两件事。首先，我们将进行超容量部署，因此我们将确保网络能够正常运行

**[14:20 – 14:36]**
**EN:** not as highly utilized, so pods need to be available on demand. But on the orchestration front, every constellation of pods will be kind of a micro-deco, and then we'll simply rely on the AV operators orchestration layer, or even directly the AV developer, to dispatch and send
**中文：** 利用率不高，因此需要按需提供 Pod。但在编排方面，每个 Pod 星座都将是一种微装饰，然后我们只需依靠 AV 运营商编排层，甚至直接依靠 AV 开发人员来调度和发送

**[14:36 – 14:49]**
**EN:** vehicles our way. We're not able to queue in the locations where we operate, so it needs to be adjusted in time. A reserve of the pod vehicle shows up, so a very basic API that exposes the pods and allows them to reserve, and then everything else is on the data exchange.
**中文：** 车辆按我们的方式行驶。我们无法在营业地点排队，所以需要及时调整。 Pod 车辆的储备会显示出来，因此一个非常基本的 API 可以公开 Pod 并允许它们进行预订，然后其他所有内容都在数据交换上。

**[14:50 – 15:04]**
**EN:** And what happens when the pod itself fails, maybe, with a car inside? So, driverless vehicle is stuck in a robot on a public adjacent land, so how do you handle that? Yeah, the initial deployments are going to be manned, so we're going to have somebody to
**中文：** 当吊舱本身发生故障时，也许里面有一辆车，会发生什么？那么，无人驾驶汽车被困在邻近公共土地上的机器人中，那么你该如何处理呢？是的，最初的部署将是有人值守的，所以我们会派人来


## When the pod fails with a vehicle inside · 当 Pod 发生故障且内部有车辆时

**[15:04 – 15:20]**
**EN:** respond on this pod immediately. Mid-long term, we're going to have our own ground ops, so we're going to have physical operations on the ground that will attend to these instances, and of course, tele-operations and customer service. Now, first of all, if an odd occurrence
**中文：** 立即对此 Pod 做出响应。从中长期来看，我们将拥有自己的地面行动，因此我们将在地面进行实际操作来处理这些情况，当然还有远程操作和客户服务。现在，首先，如果发生奇怪的情况

**[15:20 – 15:35]**
**EN:** happens, the robotic system freezes, the vehicle is safely stored passively in a box. Nobody can access the pod. If we simply are not able to complete an autonomous cycle of a pit stop, which we're accounting for, we think at least 10% of occurrences with the early version of
**中文：** 发生这种情况时，机器人系统会冻结，车辆会被动地安全地存放在盒子里。没有人可以访问该 Pod。如果我们根本无法完成进站的自主循环（我们正在考虑这一点），我们认为早期版本中至少有 10% 的情况发生

**[15:35 – 15:50]**
**EN:** the product in pilot will do this, then we can simply charge the vehicle and release it to go back to the depot if it needs a clean in this instance. Otherwise, I mean, we show up and we either reset the system or we then allow the vehicle to be released and then it goes back
**中文：** Pilot 中的产品会执行此操作，然后我们可以简单地为车辆充电并在这种情况下需要清洁时将其放回车库。否则，我的意思是，我们出现并重置系统，或者然后允许车辆被释放，然后它返回

**[15:50 – 16:09]**
**EN:** into the depot. Is it sold? Right, and you also made a deliberate choice not to sell this as a product to speak, and I would like to understand why. So, you operate the pod as a network, rather than selling it as a hardware to fleet. So, why take on that capital burden instead of
**中文：** 进入仓库。卖了吗？对了，而且你也刻意选择不把这个作为产品来销售，我想了解为什么。因此，您可以将 Pod 作为网络进行操作，而不是将其作为硬件出售给车队。那么，为什么要承担资本负担而不是


## Why Aseon runs a network instead of selling boxes · 为什么Aeon运营网络而不是卖盒子

**[16:10 – 16:27]**
**EN:** shipping the boxes, for example? Yeah, okay, two elements to the answer. And first of all, our product is a form of infrastructure and it's worth understanding how AV operators currently sort of like buy or access infrastructure. They don't necessarily hold all the
**中文：** 例如，运送盒子？是的，好吧，答案有两个要素。首先，我们的产品是基础设施的一种形式，值得了解 AV 运营商目前如何购买或访问基础设施。他们不一定拥有所有

**[16:27 – 16:42]**
**EN:** infrastructure on their balance sheet, right? They'll spec out a depot location. They need to grow a market or open a market. They'll work with a real estate developer, really, pay a deposit, and then they'll commit to a long lease of that infrastructure. So,
**中文：** 基础设施在他们的资产负债表上，对吗？他们会指定一个仓库位置。他们需要开拓市场或打开市场。他们将与房地产开发商合作，实际上，支付押金，然后他们将承诺对该基础设施进行长期租赁。所以，

**[16:42 – 16:58]**
**EN:** they're used to accessing infrastructure as a service is one point. Your second point of why don't we actually ship and sell hardware is how I understand the question. It's not that we don't do this. Look, it's worth picking this apart because
**中文：** 他们习惯于将基础设施作为一种服务进行访问，这一点是其中之一。关于我们为什么不实际运送和销售硬件的第二点是我如何理解这个问题。并不是我们不这样做。看，值得将其分开，因为

**[16:58 – 17:16]**
**EN:** a contract manufacturer makes a pod, and they sell the pod on for a margin, right? And then somebody acquires and employs it. The company that acquires this is not Aseon with our venture capital equity funded balance sheet. It will be a project company, and we will be an equity
**中文：** 合同制造商制造了一个烟弹，然后他们出售烟弹以获得利润，对吗？然后有人获得并使用它。收购该公司的公司不是 Aseon，我们的资产负债表由风险资本股权资助。它将是一家项目公司，我们将是一家股权公司

**[17:16 – 17:34]**
**EN:** participant in the project company. And then the project company will raise its own asset back financing and get its own cash flows, right? So, the SPV will acquire the asset and deploy it. The interesting conversation becomes who should be the equity participant in that vehicle because
**中文：** 项目公司的参与者。然后项目公司就会筹集自己的资产回购融资，获得自己的现金流，对吧？因此，SPV 将收购该资产并进行部署。有趣的对话是谁应该成为该工具的股权参与者，因为

**[17:34 – 17:50]**
**EN:** it shouldn't solely be Aseon. Because we're building this very much like a partnership, we want the charge point operator to participate. We in fact want the AV developer or the AV operator to be very specific. We would like them to participate. And because we're building
**中文：** 不应该只是阿森一个人。因为我们的建设非常类似于合作伙伴关系，所以我们希望充电点运营商参与其中。事实上，我们希望 AV 开发人员或 AV 运营商非常具体。我们希望他们参与。因为我们正在建设

**[17:50 – 18:06]**
**EN:** a very much a new type of infrastructure, which is sort of infrastructure as a product, it's kind of a unique opportunity to kind of pivot the model on its head and allow the AV operators to own part of the infrastructure stack. Long, wide, and answer, but I think it answers the
**中文：** 这是一种非常新型的基础设施，可以说是基础设施即产品，这是一个独特的机会，可以彻底改变模型并允许 AV 运营商拥有部分基础设施堆栈。长、宽、答案，但我认为它回答了

**[18:06 – 18:23]**
**EN:** who sells and who makes what. Yeah, super interesting. Thanks for taking this apart. And when we think about like the concrete offering, so how do you then charge a fleet operators? Then per reset, is it per subscription or guaranteed capacity commitment or something like that?
**中文：** 谁卖什么，谁生产什么。是的，超级有趣。谢谢你把这个拆开。当我们考虑具体的产品时，如何向车队运营商收费？那么每次重置，是每次订阅还是保证容量承诺或类似的东西？


## How operators pay, and what makes it bankable · 运营商如何付款，以及什么因素使其有利可图

**[18:23 – 18:43]**
**EN:** So, the model is flexible, as long as you can effectively keep the project bankable, right? So, if you charge on a per use basis, then you need a minimum utilization guarantee. Not necessarily great for the AV operator, especially for a new system. The most straightforward way
**中文：** 那么，这个模式是灵活的，只要你能有效地保持项目的可融资性，对吗？因此，如果您按使用量收费，那么您需要最低使用率保证。对于 AV 操作员来说不一定很好，尤其是对于新系统。最直接的方法

**[18:43 – 19:02]**
**EN:** is you probably decouple power. You pay for power separately, probably directly with the CPO, and then you pay for the ground and the ops on a monthly basis. Okay. I mean, these are well controllable OPEX line items. So, flexible model, as long as the agreement is bankable,
**中文：** 你可能会去耦电源吗？您单独支付电力费用，可能直接向 CPO 支付费用，然后按月支付地面费用和运营费用。好的。我的意思是，这些是可以很好控制的运营支出项目。所以，灵活的模式，只要协议是可融资的，

**[19:02 – 19:20]**
**EN:** and as long as there is equity buy-in from everybody involved, is my answer. And if we look at maybe at one part, so how many resets a day or in a specific time frame, does it need to work economically? So, what is the payback period, so to speak, for such a unit?
**中文：** 我的答案是，只要每个参与者都有股权参与。如果我们看看其中一个部分，那么每天或在特定时间范围内重置多少次，它是否需要经济地运作？那么，这样一个单位的投资回收期是多少？


## Five resets a day: the utilisation math · 一天五次重置：利用率数学

**[19:20 – 19:40]**
**EN:** Yeah, let's look at it on a utilization basis, not payback. So, the big difference here is because you do not employ human staff, which is kind of a high fixed cost with overhead. Your marginal cost of delivering a pit stop is very low. It's fixed. So, we've modeled that we can effectively
**中文：** 是的，让我们从利用率的角度来看待它，而不是回报。所以，这里最大的区别是因为你不雇用员工，这是一种很高的固定成本和管理费用。进站的边际成本非常低。它是固定的。所以，我们已经建模，我们可以有效地

**[19:40 – 19:56]**
**EN:** run a very low utilization network and still break it. So, we're talking maybe even down to five resets a day. So, something like 10% utilization suffices for us to operate the network. And the idea here is to move away from this super high throughput, well-run depot that
**中文：** 运行一个利用率非常低的网络，但仍然会破坏它。因此，我们讨论的可能是每天重置五次。因此，大约 10% 的利用率足以让我们运营网络。这里的想法是远离这个超高吞吐量、运行良好的仓库

**[19:56 – 20:13]**
**EN:** needs to pull the vehicles out of service and causes loss of utilization in the fleet. What the vehicles need is a very dense, very widely on-demand available network directly in the pockets of demand such that you cannot just offer pit stops in the center of the city
**中文：** 需要停止使用车辆并导致车队利用率下降。车辆需要的是一个非常密集、非常广泛的按需可用网络，直接满足需求，这样你就不能只在市中心提供停车站

**[20:14 – 20:31]**
**EN:** on demand. You can do micro resets because this is where the real economic outlook is. There is natural downtime for 10, 15, 20 minutes during the day of the vehicle. If you can squeeze in partial charges, partial cleanups, then you can keep the fleet running
**中文：** 一经请求。你可以进行微观重置，因为这才是真正的经济前景所在。车辆白天有 10、15、20 分钟的自然停机时间。如果你可以压缩部分充电、部分清理工作，那么你就可以保持车队运行

**[20:31 – 20:47]**
**EN:** constantly. And that might not be a problem today, but this is crucial when the city will tender out licenses with a cap number of vehicles. And if your thesis is like Tesla Cybercab thesis is, it's so cheap, it runs on its own, it's free to run, so it can drive
**中文：** 不断地。这在今天可能不是问题，但当该市将发放车辆数量上限的许可证时，这一点至关重要。如果你的论文就像 Tesla Cyber​​cab 的论文一样，它是如此便宜，它可以自己运行，它可以免费运行，所以它可以驾驶

**[20:47 – 21:01]**
**EN:** to another state to get charged. That doesn't apply because the externality of increasing traffic is not accounted for. The infrastructure has to meet the vehicle, not the vehicle taken to the infrastructure just because it drives itself.
**中文：** 到另一个州收取费用。但这并不适用，因为没有考虑到流量增加的外部性。基础设施必须满足车辆的需求，而不是仅仅因为车辆能够自动驾驶而将车辆带到基础设施上。

**[21:01 – 21:17]**
**EN:** That makes sense. And maybe one more question related to the care. So I mentioned in the intro that you raised 10 million. So what is the plan for this 10 million that you raised? Yeah. So all of the money is going to engineering, proving that the product
**中文：** 这是有道理的。也许还有一个与护理相关的问题。所以我在介绍中提到你筹集了1000万。那么你们筹集的这1000万有什么计划呢？是的。所以所有的钱都将用于工程设计，证明产品


## Where the $10M goes, and what 2027 has to prove · 1000 万美元的去向以及 2027 年必须证明什么

**[21:17 – 21:35]**
**EN:** works and proving that we can get to a reliable autonomous pit stop, at least targeting the very core of the reset. So it's all about building out the team, building out the products and supporting our first pilot deployments with the goal of being manufacturing ready with
**中文：** 有效并证明我们可以到达可靠的自动进站，至少针对重置的核心。因此，这一切都是为了建立团队、构建产品并支持我们的首次试点部署，目标是为制造做好准备

**[21:35 – 21:49]**
**EN:** a third iteration of our products by the end of 2020. And if we then think about a city scale network, so this was probably a very, very different number. So I don't know if you can gauge your number, but what does the capital stack look
**中文：** 到 2020 年底我们的产品将进行第三次迭代。如果我们考虑城市规模的网络，那么这可能是一个非常非常不同的数字。所以我不知道你是否可以衡量你的数字，但资本堆栈看起来怎么样


## $50M a metro: from venture equity to asset-backed debt · 一座地铁 5000 万美元：从风险投资到资产担保债务

**[21:49 – 22:05]**
**EN:** beyond this round? So at what point does it stop being then like the adventure and the start of being like a real infrastructure or something like that? Yeah, it's what we touched on before. So we'll soon graduate from sort of like the product
**中文：** 超出本轮？那么什么时候它不再像冒险一样，而是像真正的基础设施或类似的东西一样开始呢？是的，这就是我们之前谈到的。所以我们很快就会从类似的产品中毕业

**[22:05 – 22:21]**
**EN:** development phase and we're going to be rolling out infrastructure across multiple metros, right? Deployments of 50 million per metro. You can be doing a dozen cities at the time and each metro will be its own SPV that will draw asset back finance to finance and
**中文：** 开发阶段，我们将在多个地铁站推出基础设施，对吧？每个地铁部署 5000 万个。你可以同时做十几个城市，每个城市都将成为自己的 SPV，将资产回流到金融和金融领域。

**[22:21 – 22:35]**
**EN:** roll out the hardware. So the financing will, of course, look different to the typical startup, but you know, there is a holding company, an operating company where the IP, the team of commercial agreements on a global level sit, and then there's going to be regional
**中文：** 推出硬件。当然，融资看起来与典型的初创公司不同，但你知道，有一家控股公司、一家运营公司，其中有知识产权、全球商业协议团队，然后还有区域性的公司。

**[22:35 – 22:48]**
**EN:** some asset companies that are going to be JVs with the regional partners that are going to make this happen. They're going to bring the ground, they're going to bring the power, they're going to consume the product and bring the operations. So it's a two-tiered approach.
**中文：** 一些资产公司将与区域合作伙伴建立合资企业，以实现这一目标。他们将带来基础，他们将带来电力，他们将消费产品并带来运营。所以这是一个两层的方法。


## Movable, permittable, live in eight weeks · 可移动、可许可、八周内可居住

**[22:48 – 23:03]**
**EN:** Okay, super interesting. And what I understood is also that the pots are a temporary structure, so deployable in a day and also movable if it may be, I don't know, side underperforms or something like that. So how much of the business is then, except the robotics,
**中文：** 好吧，超级有趣。我还了解到，这些罐子是一个临时结构，因此可以在一天内部署，并且如果可能（我不知道）侧面表现不佳或类似的情况，也可以移动。那么除了机器人技术之外，还有多少业务，

**[23:03 – 23:21]**
**EN:** maybe also real estate permitting and stuff like that? Yeah, a very significant component here is to not just be a robotics product company. I'll say this, currently the hunt for permittable powered ground where you can erect an industrial
**中文：** 也许还有房地产许可之类的东西？是的，这里一个非常重要的组成部分不仅仅是成为一家机器人产品公司。我想说的是，目前正在寻找允许的供电地面，在那里你可以建立一个工业

**[23:21 – 23:37]**
**EN:** depot is scarce. You kind of, if you end up with a lander, you can deploy and you deploy. The beauty of our product, it's movable because just with a conditional use authorization and a state level certification, you can pretty much deploy across significantly more parcels of
**中文：** 仓库稀缺。有点，如果你最终得到了一个着陆器，你可以部署并部署。我们产品的美妙之处在于它是可移动的，因为只需有条件使用授权和州级认证，您就可以在更多的地块上进行部署

**[23:37 – 23:54]**
**EN:** land. So the reason it's movable and temporary has to do with the fact that we're designing it to be extremely quick to deploy. So just within eight weeks of looking into a specific city, we can apply and we can pretty much have operations live. So this is why the product
**中文：** 土地。因此，它之所以是可移动的和临时的，是因为我们将其设计得能够非常快速地部署。因此，在考察特定城市后的八周内，我们就可以申请，并且几乎可以开展运营。这就是为什么该产品

**[23:54 – 24:08]**
**EN:** itself is designed that way. And I think also there's currently a lot of focus on this layer, to be honest. So quite a lot of interest. And I want to place you inside it. So you have, for example, players like Lyft,
**中文：** 本身就是这样设计的。老实说，我认为目前人们对这一层也有很多关注。所以非常有兴趣。我想把你放进去。例如，像 Lyft 这样的玩家，


## Lyft, Avis, Move: why route into a third-party network · Lyft、Avis、Move：为何路由至第三方网络

**[24:08 – 24:26]**
**EN:** they're operating in 80,000 square foot facility in Nashville. And for Waymo, then you have Avis that is doing Dallas, Move, that does Phoenix. So why would any of those operators route vehicles then into your network instead of building the capability into developers they are already
**中文：** 他们在纳什维尔占地 80,000 平方英尺的工厂中运营。对于 Waymo 来说，Avis 正在做达拉斯，Move 正在做菲尼克斯。那么，为什么这些运营商会将车辆路由到您的网络中，而不是将功能构建到他们已经是的开发人员中

**[24:26 – 24:43]**
**EN:** paying for, for example? Yeah. So first of all, we're talking about additional capacity, right? So the cities that you mentioned, the Metros, they're running successful pilot scale. So now it's all about scaling up. Now, if you run 500 vehicles, you want to have 2,000 vehicles,
**中文：** 例如，支付费用？是的。首先，我们谈论的是额外容量，对吧？所以你提到的城市，地铁，他们正在成功进行试点。所以现在一切都是为了扩大规模。现在，如果你运行 500 辆车，你想要拥有 2,000 辆车，

**[24:43 – 25:01]**
**EN:** you need four times also the infrastructural footprint and capacities to turn the fleet around. And the current answer is more maintenance hub and also more sort of like the satellite locations and everything else. What the operators would effectively buy from us is not just
**中文：** 您还需要四倍的基础设施占地面积和能力来扭转车队的局面。目前的答案是更多的维护中心，也更像是卫星位置和其他一切。运营商实际上会从我们这里购买的不仅仅是

**[25:01 – 25:18]**
**EN:** additional powered ground via the partnerships we're going to bring in, but also the ability to deploy the decentralized locations with autonomous operations, which completely flips the economics, right? Because you cannot profitably run a two or three bay depot in the
**中文：** 通过我们将引入的合作伙伴关系提供额外的动力基础，而且还能够通过自主操作部署分散的地点，这完全颠覆了经济，对吗？因为你无法在该地区经营一个两车位或三车位的仓库来盈利。

**[25:18 – 25:32]**
**EN:** center of the city, stuff with humans. One more question related to also your partnerships, because you mentioned, for example, charging, you have partners and stuff like that. But robotics inside this box, this is wholly developed from Aseon or do you also have
**中文：** 城市中心，人烟稀少。还有一个问题也与您的合作伙伴关系有关，因为您提到，例如，收费，您有合作伙伴之类的东西。但是这个盒子里面的机器人，这是完全由 Aseon 开发的，或者你也有


## What stays in-house · 内部保留的内容

**[25:32 – 25:46]**
**EN:** there's some partners which provide the robotics as well? No, this is our own IP. So this is the core of what we build. And this is the core of what we retain over the long term. We're being very strategic with what makes sense to be developed in-house,
**中文：** 有一些合作伙伴也提供机器人技术吗？不，这是我们自己的IP。所以这是我们构建的核心。这是我们长期保留的核心。我们对内部开发的内容非常具有战略意义，

**[25:46 – 26:01]**
**EN:** because frankly, the rule of hardware is it takes multiple iterations to build a stable product. And you launch a product, it breaks, you fix what's broken, you launch it, it works, but the economics don't work. Getting to a stable hardware business is tough.
**中文：** 因为坦率地说，硬件的规则是需要多次迭代才能构建稳定的产品。你推出了一个产品，它坏了，你修复了坏掉的东西，你推出了它，它有效，但经济学不起作用。获得稳定的硬件业务是很困难的。

**[26:01 – 26:19]**
**EN:** So what we're optimizing for here is the speed with which we can deploy the stable solution. Right? So yeah, this part of the stack remains very much in-house. And this is what we've hired for. Maybe now let's zoom out a bit, talk a bit more about the layer you're also betting on. So I think
**中文：** 因此，我们在这里优化的是部署稳定解决方案的速度。正确的？所以，是的，这部分堆栈仍然在内部。这就是我们聘请的目的。也许现在让我们缩小一点，更多地讨论一下您也押注的层。所以我认为


## Are AV depots the new data centres? · AV 仓库是新的数据中心吗？

**[26:19 – 26:35]**
**EN:** a lot of people always right now draw this comparison that AV depots are like data centers or cell towers. Do you think this is a right analogy? And also maybe what does the major version of this market look like structurally and who owns it then?
**中文：** 现在很多人总是将 AV 仓库比作数据中心或手机信号塔。你认为这个类比正确吗？也许这个市场的主要版本在结构上是什么样的以及谁拥有它？

**[26:35 – 26:52]**
**EN:** Yeah. So first of all, on the analogy, yeah, it is a good analogy. Robotaxis is the biggest robotic application, physical AI in the world. It's going to remain that together with humanoids. So it's a new technology that needs its own new type of bespoke infrastructure. So in this regard,
**中文：** 是的。首先，就类比而言，是的，这是一个很好的类比。 Robotaxis 是世界上最大的机器人应用程序、物理人工智能。它将与类人生物一起保持这​​种状态。因此，这是一项新技术，需要自己的新型定制基础设施。所以在这方面，

**[26:52 – 27:09]**
**EN:** for sure, we need a build out and a significant portion of the cost of running the services more than have ties to that infrastructural integration's footprint. Now, in terms of what happens and how it forms and who owns the layer, infrastructure is a little bit fuzzy.
**中文：** 当然，我们需要扩建，并且需要很大一部分运行服务的成本，而不仅仅是与基础设施集成的足迹相关。现在，就发生的事情、它如何形成以及谁拥有该层而言，基础设施有点模糊。

**[27:09 – 27:23]**
**EN:** It's very much an original basis. You need to look at who effectively at the end of the day owns that infrastructure. I kind of pine, but it's a TBD, right? I don't think it necessarily matters as much right now. It will remain, I think, very much its own layer. And then
**中文：** 这在很大程度上是一个原始的基础。您需要了解最终谁有效地拥有该基础设施。我有点松，但这是一个待定，对吧？我认为现在这不一定那么重要。我认为，它仍将保留其自己的层面。进而

**[27:23 – 27:39]**
**EN:** the AV operators are on top. You're going to see some companies like what we do take a more product-first approach to infrastructure. And I think this very much changes what's possible in terms of owning more of that vertical stack when you're deploying the product record hours.
**中文：** AV 运营商处于领先地位。你会看到一些像我们这样的公司对基础设施采取更多产品优先的方法。我认为这极大地改变了在部署产品创纪录时间时拥有更多垂直堆栈的可能性。


## Is the cost really decided off the road? · 成本真的是由道路决定的吗？

**[27:39 – 27:58]**
**EN:** And one claim that you also made is that operations run around 70% of the cost of the service. So if that is right, then autonomy economics are already decided off the road rather than on it. What is your experience with the AV? Developers, are they recognizing
**中文：** 您还提出的一项说法是，运营成本约占服务成本的 70%。因此，如果这是正确的，那么自主经济学就已经在路外而不是路上决定了。您对 AV 的体验如何？开发商们，他们认识到了吗？

**[27:58 – 28:14]**
**EN:** that or is their attention still on developing the best driver service? Yeah. Well, that was a borrowed number. We've done our own analysis. We believe it's around 55% the contribution of infrastructure and human ops. 30% of it is the infrastructure
**中文：** 还是他们的注意力仍在开发最好的司机服务上？是的。嗯，那是借来的号码。我们已经做了自己的分析。我们认为基础设施和人力操作的贡献约为 55%。其中30%是基础设施

**[28:14 – 28:31]**
**EN:** percentage points. And I think it's a major lever, obviously, but obviously there's still fat optimization and margin across the entire stack. And work needs to happen across the entire of the stack to get to profitable robot-taxi operations across
**中文：** 百分点。我认为这显然是一个主要杠杆，但显然整个堆栈中仍然存在大量优化和余量。并且需要在整个堆栈中进行工作，才能在整个堆栈中实现盈利的机器人出租车运营

**[28:31 – 28:52]**
**EN:** every city. So Uber operates right now in 15,000 cities. We have live robot-taxi operations in 15, like Waymo's 14. We have Zug's, Vegas, and then you have another nine China and two Middle East, like 25, 26. So there is a tail end of markets that are, let's say, the tier two markets
**中文：** 每个城市。因此，Uber 目前在 15,000 个城市运营。我们在 15 个国家开展了机器人出租车业务，就像 Waymo 的 14 个国家一样。我们有楚格、维加斯，然后还有另外 9 个中国国家和两个中东国家，比如 25、26 个国家。所以有一个市场的尾部，比如说二级市场

**[28:52 – 29:05]**
**EN:** we'll need to innovate on the operating model, I'd say. Another point is that cities also probably have a say in this. So you're placing your robots in the parking space. And I think the curb space in general is also
**中文：** 我想说，我们需要对运营模式进行创新。另一点是，城市在这方面也可能有发言权。所以你要把你的机器人放在停车位上。我认为路边空间总体上也是


## Curb space, cities and the traffic externality · 遏制空间、城市与交通外部性

**[29:05 – 29:19]**
**EN:** politically contested in a way. So where has that been harder than expected? And also, what does a city get out of saying yes to this kind of micro depot? It's a good question. So full disclosure, we haven't reached that point. So we're
**中文：** 在某种程度上存在政治争议。那么到底哪里比预想的更难呢？而且，如果一个城市接受这种微型仓库，又能得到什么好处呢？这是一个好问题。如此全面的披露，我们还没有达到这一点。所以我们是

**[29:19 – 29:35]**
**EN:** not operating a network in a city at the scale where there's friction with the city. And we're also deploying our product in private land, right? So the interface with the city is, of course, on the permitting front and certification with the state.
**中文：** 不在与城市存在摩擦的规模上运营网络。我们也在私人土地上部署我们的产品，对吧？因此，与城市的联系当然是在国家的许可和认证方面。

**[29:35 – 29:51]**
**EN:** So the argument that I think might become a public argument is if we're starting to now deploy in partnership with the CPO on top of charging base that consumers like you and I that have an electric vehicle would previously use, it will now privatize that bay and give it
**中文：** 因此，我认为可能会成为公开争论的论点是，如果我们现在开始与 CPO 合作，在像你我这样拥有电动汽车的消费者以前使用的充电基地上进行部署，那么现在它将将该充电站私有化并给予它

**[29:51 – 30:06]**
**EN:** to someone with vehicles. And you've taken something back from the city dweller. But the counter argument to this is people that live in the city are the people that use the robot taxes, right? And then the person that uses the robot taxi has kind of like a right
**中文：** 给有车辆的人。你从城市居民那里拿回了一些东西。但对此的反驳是，居住在城市的人是使用机器人税的人，对吗？然后使用机器人出租车的人有一种权利

**[30:06 – 30:25]**
**EN:** to a slice of that piece of infrastructure. So maybe they chose not to drive an electric vehicle and chose to take a robot taxi. So their robot taxi needs to use that public infrastructure as such. So I think, yes, depots are more hidden and in industrial
**中文：** 到该基础设施的一部分。所以也许他们选择不驾驶电动汽车而选择乘坐机器人出租车。因此，他们的机器人出租车需要使用公共基础设施。所以我认为，是的，仓库更加隐蔽并且在工业中

**[30:25 – 30:41]**
**EN:** zones and kind of like far away and to do the dirty work. But there is a real negative externality of far away depots, which is traffic. And I think traffic is going to be a big problem, even though if we were to freeze the level of movement of people and say that needs to
**中文：** 区域之类的，有点像在很远的地方做肮脏的工作。但距离较远的车厂存在一个真正的负外部性，那就是交通。我认为交通将是一个大问题，即使我们要冻结人员流动水平并说需要

**[30:41 – 30:56]**
**EN:** be statics, et cetera, basically remain the same. Other almost vehicles reduce traffic, but every time we gave people a better and a cheaper way to move around, they just move more. So traffic will inevitably increase. For the last stretch, let's look forward. And
**中文：** 静力学等基本保持不变。其他车辆几乎可以减少交通流量，但每当我们为人们提供更好、更便宜的出行方式时，他们就会移动得更多。那么流量必然会增加。最后一段时间，让我们拭目以待。和


## Europe: why build in the US, and when Aseon arrives here · 欧洲：为什么在美国建设，以及 Aseon 何时到达这里

**[30:56 – 31:12]**
**EN:** I want to look at another part of the world, Europe. So you are Greek. I think your co-founder is British whenever I'm correct. And you also built already in Europe one time. And now you're building in the US. Europe in general has less robot taxi volume, has more regulatory processes.
**中文：** 我想去看看世界的另一个地方，欧洲。所以你是希腊人。只要我没猜错的话，我认为你的联合创始人是英国人。你们也曾在欧洲建造过一次。现在你正在美国建设。总体而言，欧洲的机器人出租车数量较少，监管流程较多。

**[31:12 – 31:34]**
**EN:** So is Aseon somehow show up here in Europe and what would have to happen first that you can also show up? Yeah, we 100% will. So yes, we're European. Yes, we've built here before. We're building Aseon out of the US because I mean, frankly, I think we as Europeans,
**中文：** 那么，Aeon 会以某种方式出现在欧洲吗？首先要发生什么，你才能出现？是的，我们 100% 会的。所以是的，我们是欧洲人。是的，我们以前在这里建过。我们正在美国建立 Aseon，因为我的意思是，坦率地说，我认为我们作为欧洲人，

**[31:34 – 31:49]**
**EN:** we take a great idea and we make it plausible. So Aseon needs to be built out of the US in the Valley. This is where the robotics talent exists. And this is where you build a global business out of. So that's my general view, unfortunately, in Europe. Now, in terms of deployments,
**中文：** 我们提出一个好主意，并使其变得合理。因此，Aeon 需要建在美国以外的硅谷。这就是机器人人才存在的地方。这就是您建立全球业务的地方。不幸的是，这就是我对欧洲的普遍看法。现在，就部署而言，

**[31:49 – 32:09]**
**EN:** Europe is extremely interesting because the architecture of our cities is such that it's much more dense, right? So there is of the big 40 global metros where robot taxi are going to be operating soon. You need that inner city penetration and our model applies immediately,
**中文：** 欧洲非常有趣，因为我们城市的建筑更加密集，对吧？全球 40 个大城市中，机器人出租车很快就会投入运营。您需要内城区的渗透，我们的模型立即适用，

**[32:09 – 32:27]**
**EN:** right? So a lot of it is Europe. And then on the additional tail end, these are cities where you'll need to be much more operationally prudent and come up with new models to operate profitably in. Then again, our model directly applies. So think Liverpool versus London kind
**中文：** 正确的？所以很多都是欧洲。然后在额外的尾端，在这些城市，您需要在运营上更加谨慎，并提出新的模式以实现盈利。话又说回来，我们的模型直接适用。所以想想利物浦与伦敦的对比

**[32:27 – 32:43]**
**EN:** of thing, right? So from this 200 city list, a lot of it actually lies in Europe. We'll see how the Munich launch goes, how London goes. Obviously like across Europe, we have more deployments. I think it's coming. And I think it's coming as quickly as it's developing across
**中文：** 的事，对吧？所以从这200个城市名单来看，其实有很多都在欧洲。我们将看看慕尼黑的发布情况如何，伦敦的发布情况如何。显然，就像整个欧洲一样，我们有更多的部署。我想它即将到来。我认为它的发展速度与它的发展速度一样快

**[32:43 – 32:59]**
**EN:** the rest of the West. And Europe is still a major portion of the global robot tax rollout. So I actually can't wait to deploy European city. Yeah, absolutely. When I heard about your brother, I also immediately thought this is perfect for the dense European cities. So really
**中文：** 其余的西方国家。欧洲仍然是全球机器人税推出的主要部分。所以我其实已经迫不及待地想部署欧洲城市了。是的，绝对是。当我听说你兄弟时，我也立即想到这非常适合密集的欧洲城市。所以真的


## The one metric for the next twelve months · 未来十二个月的唯一指标

**[32:59 – 33:13]**
**EN:** good that you're also looking into Europe. And maybe one last question to close here, if we look 12 months from now. So what is the one metric you judge yourselves on? So the number that tells you that this was a successful year.
**中文：** 很高兴您也在考虑欧洲。如果我们展望 12 个月后的情况，也许还有最后一个问题要结束。那么您判断自己的唯一标准是什么？这个数字告诉你今年是成功的一年。

**[33:13 – 33:34]**
**EN:** This year is all about proving out that we can autonomously reset. So the metric of success is what we call uptime. So what is the ratio of successfully completed autonomous reset cycles overattended? Anything over 90% allows us to deploy and operate profitably in the first
**中文：** 今年的重点是证明我们可以自主重置。因此，衡量成功的标准就是我们所说的正常运行时间。那么，成功完成的自主重置周期中过度关注的比例是多少？任何超过 90% 的事情都可以让我们在第一时间进行部署和运营并实现盈利

**[33:34 – 33:45]**
**EN:** target markets. So this is it. Well, once we get to that level of product maturity, we have a business and then we're aggressive. Yeah. All right. George, thank you so much. This was really interesting to hear more
**中文：** 目标市场。所以就是这样。好吧，一旦我们达到了产品成熟度的水平，我们就有了业务，然后我们就会积极进取。是的。好的。乔治，非常感谢你。听到更多这真的很有趣

**[33:45 – 34:01]**
**EN:** about Aseon and also your pots and your strategy and way forward. I'm looking forward to talk maybe in some months and talk about your progress and what you achieved so far. It was really pleasure to meet you today and have you on the show. Thank you so much, George.
**中文：** 关于 Aseon 以及你的底池以及你的策略和前进的方向。我期待着几个月后的谈话，谈谈您的进展以及迄今为止所取得的成就。今天很高兴见到您并邀请您参加节目。非常感谢你，乔治。

**[34:02 – 34:04]**
**EN:** Thank you, Daniel. I'd love to be back. Thank you.
**中文：** 谢谢你，丹尼尔。我很想回来。谢谢。
