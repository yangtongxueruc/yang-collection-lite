
## 开场 · 嘉宾与研究方向

**SECTION_NOTE**
- 嘉宾 Michael Hyland，UC Irvine 土木与环境工程副教授，隶属该校交通研究所（ITS）
- 研究领域：交通系统建模与分析 —— 无人驾驶（共享车队与私人拥有）、微出行、电动滑板车与自行车、网约车、微公交
- 三条主线：如何高效运营这些系统、如何有效设计它们、以及它们对城市居民的影响
**END_SECTION_NOTE**

**[00:02 – 00:13]**
**EN:** Michael, how are you doing? I'm very good. Thanks for asking. Happy to be on. No worries. Yeah, first of all, it would be great if you could introduce yourself.
**中文：** 迈克尔，你好吗？我很好。谢谢你的询问。很高兴能上场。不用担心。是的，首先，如果您能介绍一下自己，那就太好了。

**[00:14 – 00:31]**
**EN:** Happy to do so, yes. I'm an assistant, excuse me, associate professor at UC Irvine in civil and environmental engineering. I'm affiliated with the Institute of Transportation Studies here. My research is broadly on modeling and analyzing transportation systems. I tend to focus on innovations in the transportation space.
**中文：** 很高兴这样做，是的。对不起，我是加州大学欧文分校土木与环境工程系的助理教授。我隶属于这里的交通研究所。我的研究广泛涉及交通系统建模和分析。我倾向于关注交通领域的创新。

**[00:31 – 00:47]**
**EN:** Things like driverless vehicles, whether they're in shared fleets or owned by individuals, but also technologies like micro-mobility, e-scooters, e-bikes, ride-hailing, micro-transit. My work involves how to operate these systems efficiently, how to design them effectively,
**中文：** 比如无人驾驶汽车，无论是共享车队还是个人所有，还有微型移动、电动滑板车、电动自行车、网约车、微型交通等技术。我的工作涉及如何有效地操作这些系统，如何有效地设计它们，

**[00:47 – 00:56]**
**EN:** and then also try to understand their impacts on cities and the people that live in cities and urban environments. Great. Okay, you sound like you're the man for the job.
**中文：** 然后还尝试了解它们对城市以及居住在城市和城市环境中的人们的影响。太好了。好吧，听起来你就是这份工作的最佳人选。


## 实验：禁止 robotaxi 在路缘「歇脚」

**SECTION_NOTE**
- 「staging」= 一次下客到下一次接客之间在路缘的停放，即车辆「无事可做」的那段时间；**不是**上下客
- 场景：旧金山，1,700 辆 robotaxi、68,000 次日行程；禁止 staging 后日均 VMT 增加约 **60%**
- 研究未对拥堵建模，但方向明确：会加剧旧金山最拥堵区域的拥堵
- 周末 vs 工作日、仅白天禁 vs 也禁夜间等子场景结果相近；若**策略性选择**禁用区域，影响会小得多，但仍为负
**END_SECTION_NOTE**

**[00:58 – 01:05]**
**EN:** So, you've recently conducted a pretty comprehensive study, I'd say, on managing curb usage.
**中文：** 所以，我想说，您最近进行了一项关于管理路缘使用的相当全面的研究。

**[01:08 – 01:19]**
**EN:** Can you explain the experiment and what you set out to understand? Sure, yeah. It could always be more comprehensive, you know, in retrospect when looking back at the study, but I agree this one was pretty involved.
**中文：** 您能解释一下这个实验以及您想要了解的内容吗？当然，是的。你知道，当回顾这项研究时，它总是可以更全面，但我同意这项研究非常复杂。

**[01:20 – 01:42]**
**EN:** Okay, so the idea was to test the impacts of banning robotaxis, shared automated vehicles, I'll use robotaxis throughout this call, banning them from using the curb, not for picking up and dropping off passengers, but for what we call staging or parking between one drop off and the next pickup.
**中文：** 好的，所以我们的想法是测试禁止robotaxi、共享自动驾驶车辆的影响，我将在整个通话过程中使用robotaxi，禁止它们使用路缘，不是为了接送乘客，而是为了我们所说的在一次下车和下一次上车之间的停靠或停车。

**[01:42 – 02:01]**
**EN:** So basically the time when the vehicle doesn't have anything to do, it's not serving a passenger and it's not going to pick one up yet. The experiment was, what happens if we ban this type of activity on the curb? And the main result, of course, is that it has pretty big implications on what these vehicles do with their time.
**中文：** 所以基本上，当车辆没有任何事情可做时，它不会为乘客提供服务，也不会接载乘客。实验是，如果我们在路缘禁止此类活动，会发生什么？当然，主要结果是，它对这些车辆如何利用时间有很大的影响。

**[02:02 – 02:19]**
**EN:** And when they can't stage, they just circle around the transportation network. In this case, it was San Francisco. And by circling around, they Pretty drastically increased the number of vehicle miles traveled, the kilometers traveled on the roadway network in San Francisco. We don't model congestion in our study,
**中文：** 当他们无法登台时，他们就绕着交通网络转。在这种情况下，它是旧金山。通过绕圈，他们极大地增加了车辆行驶里程数，即旧金山道路网络上行驶的公里数。我们的研究中没有对拥堵进行建模，

**[02:19 – 02:38]**
**EN:** but the implications for congestion, I think, are somewhat obvious directionally. It would make congestion worse, most likely in some of the most congested parts of San Francisco. We did some other sub-scenarios related to weekends versus weekdays, preventing vehicles from staging at night versus in the day. Most of the results were pretty similar.
**中文：** 但我认为，对拥堵的影响在方向上是比较明显的。这将使拥堵更加严重，最有可能发生在旧金山一些最拥堵的地区。我们还做了一些与周末和工作日相关的其他子场景，防止车辆在夜间和白天停靠。大多数结果非常相似。

**[02:38 – 02:55]**
**EN:** If you're strategic with where you ban the SAVs, the robotaxis, from using the curb, the size of the impact is much smaller, but there still is an impact. You increase VMT, but of course you prevent these vehicles from using the curb where maybe people want
**中文：** 如果你有策略地禁止 SAV（自动驾驶出租车）使用路缘，那么影响的大小就会小得多，但影响仍然存在。你增加了 VMT，但当然你会阻止这些车辆在人们可能想要的地方使用路缘

**[02:55 – 03:16]**
**EN:** to park near their residential homes and work. So just to be clear, staging means resting at the curve between trips. That's correct, yes. Because I think people have always probably wondered this, like, where does an AV go after they've dropped a passenger off? Do they just sort of drive around in circles?
**中文：** 将车停在住宅和工作地点附近。需要明确的是，分期意味着在行程之间的曲线上休息。这是正确的，是的。因为我认为人们可能一直想知道这个问题，比如，自动驾驶汽车在送乘客下车后会去哪里？他们只是在兜圈子吗？


## 研究的由来：Waymo 主动找上门

**SECTION_NOTE**
- 车队越大、影响越大，这个问题的分量随之上升
- Waymo 经 UC Berkeley 的 **Susan Shaheen** 团队联系 UC Irvine（他们知道 UCI 在做建模）
- Waymo 的诉求：在不载客时能使用路缘，而不是绕圈或跑长距离回离街停车场
- 实验由双方**共同设计**，但最终选择权在研究者手上
**END_SECTION_NOTE**

**[03:16 – 03:33]**
**EN:** Do they wait? So yeah, I guess, how did this come about, this study? Because I can imagine that this is going to become a really, really important topic once AVs take off. Yeah, that's right. So as these fleets get bigger, I think the question becomes more important.
**中文：** 他们等待吗？所以，是的，我想，这项研究是怎么发生的？因为我可以想象，一旦自动驾驶汽车兴起，这将成为一个非常非常重要的话题。是的，没错。因此，随着这些机队变得越来越大，我认为这个问题变得更加重要。

**[03:33 – 03:55]**
**EN:** As there's more fleets, each individual fleet gets bigger. I think the impacts will be larger. So the study actually came from Waymo reaching out to us here at UC Irvine by way of colleagues at UC Berkeley, Susan Shaheen in particular. They knew we did modeling here at UC Irvine, and probably they wanted to understand from the Berkeley side.
**中文：** 随着舰队的增加，每个舰队都会变得更大。我认为影响会更大。因此，这项研究实际上是 Waymo 通过加州大学伯克利分校的同事，特别是苏珊·沙欣 (Susan Shaheen) 联系加州大学欧文分校的我们进行的。他们知道我们在加州大学欧文分校做建模，可能他们想从伯克利方面了解。

**[03:55 – 04:08]**
**EN:** They asked those folks to interview. Stakeholders and cities to understand how they're thinking about regulating the curb and using the curb for not just robotaxis, but also Uber and Lyft type vehicles. And again, like micromobility and the like.
**中文：** 他们要求那些人进行采访。利益相关者和城市了解他们如何考虑监管路缘，以及如何将路缘不仅用于robotaxi，还用于 Uber 和 Lyft 类型的车辆。再说一次，比如微交通之类的。

**[04:10 – 04:28]**
**EN:** So yeah, they came to us and said, hey, like we think it's mutually beneficial For us at Waymo and for cities, for our vehicles to be able to use the curb when we're not serving passengers, again, as opposed to just driving around or even going a long distance back to
**中文：** 所以，是的，他们来找我们说，嘿，就像我们认为这对我们 Waymo 和城市来说是互惠互利的，我们的车辆能够在我们不为乘客提供服务时使用路缘，而不是只是开车兜风，甚至长途跋涉返回

**[04:28 – 04:44]**
**EN:** an off-street parking lot. And we kind of co-designed the experiments, Waymo and us. Well, they gave input. We made the final choices, of course. And that's kind of the backstory of how the study came to be. So is it entirely independent?
**中文：** 一个街边停车场。 Waymo 和我们共同设计了这些实验。好吧，他们提供了意见。当然，我们做出了最终的选择。这就是这项研究的背景故事。那么它是完全独立的吗？


## 独立性之辩：数据全部是合成的

**SECTION_NOTE**
- Waymo 唯一坚持要澄清的是：**别让人以为他们提供了数据**
- 停车数据来自 **INRIX**，网约车行程数据来自 **Replica**；Waymo 只给了公开可得的车队规模数量级
- Hyland 坦言方向性影响「开题时就明显」——真正有意思的是**量级**（结果 60%）
- 没有为了配合 Waymo 重跑任何场景或实验
**END_SECTION_NOTE**

**[04:44 – 05:07]**
**EN:** Because I always have this feeling that when a big company like Waymo, the largest AV company in the world, and clearly the leader in the US robo-taxi race, approaches a company to produce a study, that the results are always kind of tailored in their favor? I can see that's the impression.
**中文：** 因为我总有这样的感觉，当像 Waymo 这样的大公司，世界上最大的自动驾驶公司，并且明显是美国robotaxi竞赛的领导者，接近一家公司进行一项研究时，结果总是对他们有利的？我看得出就是这样的印象。

**[05:08 – 05:22]**
**EN:** Yeah. So, I mean, let's see, um, really the only thing Waymo was pushing back on was like, um, we were not intending to imply this at all, but when we were writing up the report,
**中文：** 是的。所以，我的意思是，让我们看看，嗯，Waymo 唯一反对的是，嗯，我们根本无意暗示这一点，但当我们撰写报告时，

**[05:22 – 05:38]**
**EN:** it was like ride hailing data, uh, parking data. They were like, well, we didn't give you any data. So don't make it seem like we did give you any data. All this data is synthetic. We got the parking data from INRIX. We got the ride-hailing trip data from a company called Replica.
**中文：** 这就像打车数据，呃，停车数据。他们说，好吧，我们没有给你任何数据。因此，不要让人觉得我们确实向您提供了任何数据。所有这些数据都是合成的。我们从 INRIX 获得停车数据。我们从一家名为 Replica 的公司获得了网约车行程数据。

**[05:39 – 05:54]**
**EN:** Waymo really didn't give us any data, which was fine with us. They gave us order of magnitude information about what their fleet size was, and it was also public information. Publicly available information on fleet size and the like. As far as the results, I mean, I hate to undercut our study,
**中文：** Waymo 确实没有给我们任何数据，这对我们来说没什么问题。他们向我们提供了有关其机队规模的数量级信息，这也是公开信息。有关机队规模等的公开信息。就结果而言，我的意思是，我不想削弱我们的研究，

**[05:55 – 06:14]**
**EN:** but the directional impact was kind of obvious going into the study. We knew that by banning these vehicles from using the curb, It was going to increase VMT. That was obvious. It was really the magnitude that was the interesting part of the question. Was it going to be a 10% increase? Is it going to be a 30% increase?
**中文：** 但在研究中，方向性影响是显而易见的。我们知道，通过禁止这些车辆使用路缘，将会增加 VMT。这是显而易见的。这个问题最有趣的部分确实是其大小。会增加10%吗？会增加30%吗？

**[06:14 – 06:30]**
**EN:** Is it going to be a large number? And we found a pretty large number, which was a 60% increase in total vehicle miles traveled, vehicle kilometers traveled. And that came directly from the results. We didn't rerun any studies or really rerun the experiments with Waymo's input.
**中文：** 会是一个很大的数字吗？我们发现了一个相当大的数字，即车辆行驶总里程增加了 60%。这直接来自结果。我们没有重新进行任何研究，也没有根据 Waymo 的输入重新进行实验。

**[06:31 – 06:51]**
**EN:** They were involved with, again, making sure we were choosing the right order of magnitude for our model inputs. But beyond that, there was not much feedback from them on those types of, they weren't questioning the outputs, we'll put it that way. So 60% increase in, to be clear, VMT is vehicle miles traveled, right?
**中文：** 他们再次参与确保我们为模型输入选择正确的数量级。但除此之外，他们对这些类型没有太多反馈，他们没有质疑输出，我们会这样说。需要明确的是，VMT 是车辆行驶里程，增加了 60%，对吗？


## 多出来的里程从哪来

**SECTION_NOTE**
- 需求全天有大量**小波峰波谷**，且在空间上分散于区域内不同地方
- 运营方必须提前把车部署在预期需求附近，还要留一点缓冲，以免错过需求
- 需求一回落，车就无处可去；不让用路缘，调度软件只能派**短的「假行程」**，在预期未来需求区绕圈
- 这种绕行在网络中**累积**，最终推高总里程
**END_SECTION_NOTE**

**[06:51 – 07:07]**
**EN:** That's correct, yes. So there was a 60% increase. Wow. Where do all those extra miles come from? Well, as I like to explain it this way, there are all these... There are peaks and valleys throughout the day in terms of the demand for robo-taxis.
**中文：** 这是正确的，是的。所以增加了 60%。哇。这些额外的里程从何而来？好吧，正如我喜欢这样解释的那样，所有这些......就robotaxi的需求而言，一天中都有高峰和低谷。

**[07:07 – 07:28]**
**EN:** So everyone knows for regular travel when the big peaks are, right? So the morning peak and then you have the afternoon peak. But for a service like whether it's Uber or Lyft or Waymo, there's even little peaks and valleys that occur throughout the day. And spatially, these peaks and valleys occur throughout different parts of the region. So the fleet operator in this case,
**中文：** 那么大家都知道什么时候是高峰期，对吗？所以早上高峰然后就是下午高峰。但对于像 Uber、Lyft 或 Waymo 这样的服务，全天甚至很少出现高峰和低谷。在空间上，这些高峰和低谷出现在该地区的不同部分。所以在这种情况下，车队运营商

**[07:29 – 07:48]**
**EN:** our fictitious Waymo fleet, Once you make sure there are enough vehicles out there in the network to serve the demand that they expect to occur, and there's going to be a little bit of buffer as well, you don't want to be, if you can avoid it, missing out on demand opportunities. But when you have these vehicles out on the road and you get a little bit of a dip
**中文：** 我们虚构的 Waymo 车队，一旦您确保网络中有足够的车辆来满足他们预期发生的需求，并且还会有一点缓冲，如果可以避免的话，您就不想错过按需机会。但是当你让这些车辆上路时，你会感到有点沮丧

**[07:48 – 08:08]**
**EN:** in demand, there's nowhere for them to go. They're not serving passengers. They need to find somewhere to go. And if you don't allow them to use the curb, what the software we use does Is just give them short trips to take throughout the network, circling around where they expect the future demand to be.
**中文：** 需求旺盛，他们却无处可去。他们不为乘客服务。他们需要找个地方去。如果您不允许他们使用路缘，我们使用的软件所做的只是让他们在整个网络中进行短途旅行，在他们预期未来需求的地方盘旋。

**[08:08 – 08:18]**
**EN:** And by future, I mean near future in five, 10 minutes to make sure those vehicles are pretty close to where the new requests are going to arrive. And that's, as the results suggest,
**中文：** 我所说的未来，是指不久的将来，在五到十分钟内确保这些车辆非常接近新请求将到达的地方。结果表明，


## 回库与地产：为什么不是答案

**SECTION_NOTE**
- 研究**没有**建立「车辆回库」场景——计算预算用尽（Hyland 直言遗憾）
- 旧金山 49 平方英里内 Waymo 的 depot 仅约 **2–5 个**；车辆变空后单程约 1.5 英里，接客还要再跑回来
- 估算：即便总是回库，也只能把 60% 压到 **40–45%**，因为往返空驶本身就是负外部性
- 要真正降 VMT 就得全城布点，但「Waymo 并不热衷地产开发」；离街停车价格**随时间剧烈波动**（商业区夜间便宜、白天贵；住宅区几乎总是贵且缺大地块）
**END_SECTION_NOTE**

**[08:18 – 08:34]**
**EN:** result in a lot of cumulative extra miles travel in the network. I think a lot of people would make the assumption that these Vehicles would just go back to like a depot or depot, whatever you like to pronounce it.
**中文：** 导致在网络中累积大量额外里程。我想很多人都会假设这些车辆会像仓库或仓库一样返回，无论你喜欢怎么发音。

**[08:36 – 08:58]**
**EN:** But did you measure that or is that not really the case? Unfortunately, we didn't create scenarios around the vehicles Whenever they're what we call idle or empty and don't have anything to serve, going back to the depot. I wish we did, I wish we would have. We just ran out of literally a computational budget.
**中文：** 但你测量过这一点吗？或者事实并非如此？不幸的是，我们没有围绕车辆创建场景，每当它们处于我们所说的闲置或空置并且没有任何服务可提供时，就返回车库。我希望我们能做到，我希望我们能做到。我们刚刚耗尽了计算预算。

**[08:58 – 09:22]**
**EN:** We use the software and I can go into some interesting stories about that. But I suspect because there are so few depots in the entire 7x7 or 49 square mile San Francisco area for Waymo, I'm not sure the exact number, but let's say somewhere between two and five of these depot locations, that might reduce the extra VMT a little bit,
**中文：** 我们使用该软件，我可以讲一些关于它的有趣故事。但我怀疑，因为在整个 7x7 或 49 平方英里的旧金山地区，Waymo 的仓库太少了，我不确定确切的数量，但假设有两到五个这样的仓库位置，这可能会稍微减少额外的 VMT，

**[09:22 – 09:42]**
**EN:** but I don't think by much because whenever a vehicle would become empty, it would travel a pretty long distance, maybe let's say A mile and a half on average, and maybe a mile and a half back to pick up customers once the request, once a person makes a request. So I think there'd be a pretty negative impact on the vehicle is always returning to
**中文：** 但我认为不会太多，因为每当车辆空了时，它就会行驶相当长的距离，也许平均一英里半，一旦有人提出请求，也许会返回一英里半来接客户。所以我认为这会对车辆产生相当负面的影响

**[09:42 – 10:01]**
**EN:** the depot as well. So maybe you could bring that 60% number down to like 40, 45%. Yeah, so to reduce the number of, to reduce the amounts of VMT, you need to have depots all over the city. And, you know, this isn't even probably their beat, is it? You know,
**中文：** 仓库也是如此。所以也许你可以将 60% 的数字降低到 40%、45% 左右。是的，所以为了减少 VMT 的数量和数量，你需要在整个城市都有仓库。而且，你知道，这甚至可能不是他们的节奏，不是吗？你知道，

**[10:01 – 10:17]**
**EN:** companies like Waymo would have to partner because it wouldn't be there, it would be private land. You know, so it's a big operation. Yeah, I mean, I don't think they're into real estate development. That would be my guess. They could partner with lots.
**中文：** 像 Waymo 这样的公司必须合作，因为那里不存在，而是私人土地。你知道，这是一个大手术。是的，我的意思是，我不认为他们从事房地产开发。这是我的猜测。他们可以与很多人合作。

**[10:18 – 10:35]**
**EN:** And I think one thing that we did learn throughout the study is, maybe it's obvious to those who know about cities, but like parking off street, the price of that is clearly time dependent. In some parts of the city, maybe a commercial district, it's very cheap to access parking at night,
**中文：** 我认为我们在整个研究过程中确实学到的一件事是，也许这对于那些了解城市的人来说是显而易见的，但就像在街边停车一样，其价格显然取决于时间。在城市的某些地方，也许是商业区，晚上停车非常便宜，

**[10:35 – 10:48]**
**EN:** very expensive during the day, and vice versa in residential areas. So actually in residential areas, it's actually usually expensive no matter what. I mean, there rarely are these large size lots for a large depot to be set up.
**中文：** 白天非常贵，住宅区反之亦然。所以实际上在住宅区，无论如何通常都很贵。我的意思是，很少有这么大面积的地块可以建立大型仓库。

**[10:50 – 11:08]**
**EN:** Yeah. So companies like Waymo, they don't want to be parking and paying parking fees, do they? They just want the cheapest alternative, the cheapest option before they can pick up the next ride. No doubt they're trying to minimize their costs in all the ways that are possible to minimize their costs.
**中文：** 是的。所以像 Waymo 这样的公司，他们不想停车并支付停车费，不是吗？他们只是想要最便宜的选择，在他们可以搭乘下一趟车之前最便宜的选择。毫无疑问，他们正试图以一切可能的方式最大限度地降低成本。

**[11:08 – 11:24]**
**EN:** So I think acquiring land is expensive, so I presume they're trying to minimize the amount of land they need to acquire, and also they're going to be strategic about where they park and whether they're going to have to pay for that parking or not pay for that parking. Can you just give me your definition of deadheading?
**中文：** 所以我认为收购土地是昂贵的，所以我认为他们正在努力最大限度地减少他们需要收购的土地数量，而且他们也会对停车地点以及是否需要支付停车费或不支付停车费采取战略性策略。你能告诉我你对无用的定义吗？


## deadheading（空驶）到底指什么

**SECTION_NOTE**
- 定义：任何**车内没有乘客**的行驶里程；即不为服务特定乘客移动的位移
- 业界常拆成两桶：① 已接到新订单、直奔接客点的空驶；② 其余空驶（去路缘 staging、回库充电、夜间回库待命或清洁）
- Hyland 提醒：两类空驶性质不同，很多分析会把它们分开处理 —— 本集特意澄清这个高频术语
**END_SECTION_NOTE**

**[11:27 – 11:31]**
**EN:** Sure, yeah. So I consider deadheading
**中文：** 当然，是的。所以我考虑死胡同

**[11:33 – 11:52]**
**EN:** Any mile or any movement of a vehicle where it doesn't have a passenger inside of the vehicle. It's not serving a particular passenger movement. Some entities like to break up this empty miles into two different pots of miles.
**中文：** 车内没有乘客的车辆的任何英里或任何移动。它不服务于特定的乘客流动。一些实体喜欢将这些空里程分成两个不同的里程。

**[11:53 – 12:14]**
**EN:** One is where the vehicle does have a new request to serve and it's going directly to pick up that request. So, you know, We don't want to say it's good or bad, but that's one part of deadheading. And there's all the other deadheading that occurs when the vehicle is going to a staging location at the curb. It's going back to the depot to charge.
**中文：** 一种是车辆确实有新的服务请求，并且它将直接接收该请求。所以，你知道，我们不想说它是好是坏，但这是无谓的一部分。当车辆驶向路缘的停靠位置时，还会发生所有其他的空头事故。它要返回车站充电。

**[12:14 – 12:28]**
**EN:** It's going back to the depot at night because it no longer needs to be in the fleet or it needs to be cleaned. So a lot of analyses will separate out these two types of deadheading. Great. Thank you. I think this is important because I hear that term flying around all over the place
**中文：** 它会在晚上返回仓库，因为它不再需要在车队中或者需要清理。因此，很多分析都会将这两种类型的空头分开。太好了。谢谢。我认为这很重要，因为我听到这个词到处流传


## 方法论与数据源

**SECTION_NOTE**
- 范围：旧金山市区 **7×7 英里**
- 仿真软件用 **Autofleet**：自建同类模型需 1.5–2 年，而它的 depot 活动与路缘停车建模能力可直接复用
- **静态数据**（INRIX）：城市停车规则（可停时段/车型/时长/是否收费）；**动态数据**：每条 curb front 未来 15 分钟有车位的概率（未独立验证，采信厂商）
- 关键参数 **supply shaping / defleeting**：低需求时段（如 23:35）把 20–40% 车队撤回 depot 充电清洁，而不是全场在线空转
- 目标生产率设为 **2.2 乘客/车/小时**（含缓冲的设定值，非最优化结果）
**END_SECTION_NOTE**

**[12:28 – 12:52]**
**EN:** and useful for our listeners. Could you give us a bit more of an understanding of the methodology and the data sources? So how they all kind of fed into each other and exactly what was the scope? It was all in San Francisco, right? Yes, we did the seven mile by seven mile area in San Francisco, which is the city itself. Simulation software we used was called Autofleet.
**中文：** 对我们的听众有用。您能否让我们对方法论和数据源有更多的了解？那么它们是如何相互融合的以及范围到底是什么？一切都在旧金山，对吗？是的，我们在旧金山进行了七英里乘七英里的区域，也就是这座城市本身。我们使用的模拟软件叫做 Autofleet。

**[12:53 – 13:06]**
**EN:** So interestingly, I build a lot of simulation models myself, but Autofleet had a lot of capabilities that would have taken me a year and a half or two years. By me, I should say my graduate students to build into our model. So we just used Autofleet.
**中文：** 有趣的是，我自己构建了很多仿真模型，但 Autofleet 的很多功能可能需要我一年半或两年的时间。对我而言，我应该说我的研究生构建了我们的模型。所以我们只使用 Autofleet。

**[13:06 – 13:25]**
**EN:** In particular, they were really good at modeling These depot activities and parking at the curb, we kind of had to make adjustments to the model for the model parking at the curb, but it was easy to do that. The main data sources, I hinted at these earlier, one was the INRIX parking data. So they have two types of data,
**中文：** 特别是，他们非常擅长对这些停车场活动和路缘停车进行建模，我们不得不对模型进行调整以用于路缘停车模型，但这很容易做到。主要的数据来源，我之前已经暗示过，其中一个是INRIX停车数据。所以他们有两种类型的数据，

**[13:25 – 13:41]**
**EN:** one they call static data, which basically encodes all of the rules for a city like San Francisco, what hours you can park, what types of vehicles, how long you can park there, whether it's paid or free parking. That's the static data, and then there's the dynamic data, which we didn't validate.
**中文：** 他们称之为静态数据，它基本上编码了像旧金山这样的城市的所有规则，可以停车的时间、车辆类型、可以在那里停车多长时间，无论是付费停车还是免费停车。这是静态数据，然后是动态数据，我们没有验证这些数据。

**[13:41 – 13:58]**
**EN:** We kind of just took them at their word. They make forecasts for every curb front. So a curb front essentially could be three or four parking spaces or 10 or 15 parking spaces. But for every curb front, what is the likelihood that there will be a parking space available in the next 15 minutes?
**中文：** 我们只是相信了他们的话。他们对每个路缘进行预测。因此，路缘基本上可以有 3 个或 4 个停车位，或者 10 个或 15 个停车位。但对于每个路缘，未来 15 分钟内有可用停车位的可能性是多少？

**[13:59 – 14:16]**
**EN:** And then we use that in our simulation to say, okay, if it's super likely that there's going to be a parking space available in general, then that means our robotaxi can park at this curb. What else to say? So there's a lot of inputs. I think one of the other key ones With this parameter called supply shaping
**中文：** 然后我们在模拟中用它来表示，好吧，如果总体上很有可能有可用的停车位，那么这意味着我们的robotaxi可以停在这个路缘。还有什么可说的呢？所以有很多输入。我认为其他关键参数之一就是这个称为供给整形的参数

**[14:17 – 14:39]**
**EN:** or defleeting is another word for it. So some of the prior simulation work on robotaxis and curb usage just assumed that throughout the entire 24, 18 hour simulation period, all the vehicles were available and driving around in the roadway network. Whereas our parameter supply shaping and defleeting said, well,
**中文：** 或转移是它的另一种说法。因此，之前关于robotaxi和路缘使用的一些模拟工作只是假设在整个 24 小时、18 小时的模拟期间，所有车辆都可用并在道路网络中行驶。而我们的参数提供整形和偏转说，嗯，

**[14:39 – 14:57]**
**EN:** if you know there's not going to be that much demand at 11.35 PM at night, you actually don't need your entire fleet of vehicles to be active. You can move 20, 30, 40% of those vehicles back to your depot, have them charge, have them get clean, get them ready for the next day. And that was a key parameter in the simulation as well.
**中文：** 如果您知道晚上 11.35 不会有那么多需求，那么您实际上不需要整个车队都处于活动状态。您可以将 20%、30%、40% 的车辆移回您的车库，让它们充​​电，让它们清洁，为第二天做好准备。这也是模拟中的一个关键参数。

**[14:59 – 15:06]**
**EN:** Okay, so trying to figure out what is the optimum amount of vehicles you need at any one time.
**中文：** 好的，所以尝试找出您在任何时候需要的最佳车辆数量是多少。

**[15:08 – 15:32]**
**EN:** Yeah, we didn't optimize for this parameter. As I said, I've done a lot of studies in the past on microtransit and robotaxis. We set the value to 2.2. So this is what we said, how many passengers on average a vehicle will serve for an hour. And I think if you look at the Results in San Francisco, you might get values like slightly lower than 2.2,
**中文：** 是的，我们没有针对这个参数进行优化。正如我所说，我过去对微型交通和robotaxi进行了大量研究。我们将该值设置为 2.2。所以这就是我们说的，一辆车一小时平均服务多少乘客。我认为如果您查看旧金山的结果，您可能会得到略低于 2.2 的值，

**[15:32 – 15:44]**
**EN:** but as I said, we wanted to build in this buffer value to make sure there were enough vehicles in the network, but not too many. Great. Okay. So you said that one of your main findings was preventing robotaxis access
**中文：** 但正如我所说，我们希望建立这个缓冲值，以确保网络中有足够的车辆，但又不能太多。太好了。好的。所以你说你的主要发现之一是阻止robotaxi访问


## 第二个发现：路缘生产率（curb productivity）

**SECTION_NOTE**
- 定义：每小时从交通系统**跨越到**土地/活动系统的乘客数（即单位路缘占用时间服务的乘客量）
- robotaxi 的路缘生产率约为私家车的 **6–8 倍**（视频口述为 6–8 倍；图文版文章写 8–10 倍）
- 私家车平均在路缘停 **1.5–2 小时**；robotaxi 少 6–8 倍，约 **15 分钟**
- 层级：**公交车 ≫ robotaxi ≫ 私家车**；robotaxi 单车载客量低（约 1.6–1.8 人/单），共乘与否影响很大
**END_SECTION_NOTE**

**[15:44 – 16:02]**
**EN:** from staging could increase daily travel by roughly 60%. Give us, are there any other major findings that we're missing here that you've found? Yeah, sure. The other one, which Waymo liked a lot, we wouldn't,
**中文：** 分期可能会使每日出行量增加约 60%。请告诉我们，您发现了我们在这里遗漏的其他重大发现吗？是的，当然。另一种是 Waymo 非常喜欢的，但我们不会，

**[16:02 – 16:27]**
**EN:** I wouldn't say we created a new metric, but there's a metric that we used that was quite useful for the study, which is something called curb productivity. And I've seen this in the context of bus usage in the past and private vehicles. So we measure curb productivity, essentially the number of Passengers that cross over from the transportation system
**中文：** 我不会说我们创建了一个新的指标，但我们使用了一个对研究非常有用的指标，这就是所谓的遏制生产力。我在过去的公交车和私家车的使用中看到了这一点。因此，我们衡量路缘生产力，本质上是从交通系统穿越的乘客数量

**[16:27 – 16:47]**
**EN:** to the land use or activity system every hour. So, okay, let me break it down a little bit more. So we found that robotaxis were about six to eight times more productive than passenger vehicles in terms of how they're using the curb. So passenger vehicle, and we got this data from the city of San Francisco,
**中文：** 每小时更新一次土地利用或活动系统。那么，好吧，让我再详细解释一下。因此，我们发现，就如何使用路缘而言，robotaxi的效率大约是乘用车的六到八倍。所以乘用车，我们从旧金山市获得了这些数据，

**[16:47 – 17:03]**
**EN:** spends about an hour and a half, two hours on average at the curb. Whereas a robo-taxi spends, well, someone else can do the math, but I don't have the result according right now, about six to eight times less than that. So probably about 15 minutes on average.
**中文：** 平均在路缘花费大约一个半小时到两个小时。而自动驾驶出租车的花费，其他人可以算一下，但我现在没有结果，大约比这个少六到八倍。所以平均大概 15 分钟左右。

**[17:03 – 17:22]**
**EN:** So if you're concerned about one of your valuable assets as a city, which is the curb, it seems that robo-taxis are using that asset much more productively than personal vehicles are. Because personal vehicles just park, stay there for a very long time. People can obviously walk around and do many things while their vehicle is parked
**中文：** 因此，如果您担心作为城市的一项宝贵资产，即路缘，那么robotaxi似乎比私家车更有效地利用该资产。由于私家车只是停放，所以会在那里停留很长时间。人们显然可以在车辆停放时四处走动并做很多事情

**[17:22 – 17:35]**
**EN:** the curb, but you still have a very valuable piece of land being used unproductively by a personal vehicle. And you're still telling me Waymo had no influence on those findings. That's right. No, in fact,
**中文：** 路缘，但你仍然有一块非常宝贵的土地被私人车辆闲置。而且你仍然告诉我 Waymo 对这些发现没有影响。这是正确的。不，事实上，

**[17:35 – 17:55]**
**EN:** so we had some initial because we wanted to show like what's the trade off right between. VMT and curb usage. And we set some initial results, which were like, this is on average how long a robotaxi spends at the curb. But it was like, that was only the average for the vehicles that actually do park.
**中文：** 所以我们有一些初步的想法，因为我们想展示之间的权衡。 VMT 和限制使用。我们设定了一些初步结果，比如，这是robotaxi在路缘平均花费的时间。但这只是实际停车车辆的平均值。

**[17:55 – 18:08]**
**EN:** A lot of them don't park between trips. And then we realized like, okay, what we really want to measure is like, how bad is it that these vehicles just sit there and wait for a long time?
**中文：** 他们中的很多人在两次旅行之间都不停车。然后我们意识到，好吧，我们真正想要测量的是，这些车辆只是坐在那里等待很长时间有多糟糕？

**[18:11 – 18:21]**
**EN:** And, you know, curb productivity was the best way to do that. And I mean, the results, we have our results from the simulation, compare those to the results of the real world for personal vehicles. And this is where we got that.
**中文：** 而且，你知道，抑制生产力是做到这一点的最佳方法。我的意思是，结果，我们从模拟中得到了结果，将这些结果与现实世界中个人车辆的结果进行比较。这就是我们得到的。

**[18:21 – 18:38]**
**EN:** It's, you know, six to eight times more productive use of the curb for SAVs compared to personal vehicles. And I should say buses are like way more productive than robotaxis, which are way more productive than personal vehicles, right? Because a bus is only at a curb for a very short period of time,
**中文：** 您知道，与私家车相比，SAV 的路缘使用效率高出六到八倍。我应该说公共汽车比robotaxi更有效率，而robotaxi又比私家车更有效率，对吗？因为公交车只在路缘停留很短的时间，

**[18:38 – 18:56]**
**EN:** has a lot of people getting on, a lot of people getting off. So, I mean, that's still much better than a robotaxi is. Yeah, because often with a robotaxi, they might only pick up one person, right? Right, yeah. So in terms of occupancy of the vehicle is really important. Indeed, yeah.
**中文：** 上车的人很多，下车的人也很多。所以，我的意思是，这仍然比robotaxi好得多。是的，因为robotaxi通常只能接一个人，对吗？对，是的。所以对于车辆的乘坐来说真的很重要。确实，是的。

**[18:56 – 19:14]**
**EN:** And there's some... Maybe on average, it's like 1.6 occupants. This is a number I'm making up, I'm guessing here, 1.6, 1.8 passengers per Waymo ride. And that's maybe slightly better, slightly worse than a personal vehicle, which also has a relatively low occupancy. And again, comparing to the bus, which can be much higher, of course.
**中文：** 还有一些...也许平均有 1.6 名乘客。这是我编造的数字，我猜每次 Waymo 行程有 1.6、1.8 名乘客。这可能比私家车稍微好一点，也稍微差一点，因为私家车的乘坐率也相对较低。再说一次，与公共汽车相比，当然可以高得多。


## 质疑：robotaxi 真的更高效吗？

**SECTION_NOTE**
- 访谈者质疑：新鲜感褪去后，自动驾驶与网约车/出租车差别有多大？同样尺寸的车若只是绕圈，只是「堵住街道」
- Hyland 认可：车辆尺寸与占地与私家车相当，仍占用宝贵城市空间（无论路缘还是车道）
- 行为研究显示相当一部分人**偏好车内无司机**；同时也有相当比例的人（他课堂上的女性学生尤为明显）对与陌生人共乘感到不安
- 这可能解释 Waymo 目前为何不开放拼车
**END_SECTION_NOTE**

**[19:14 – 19:14]**
**EN:** I
**中文：** 我

**[19:17 – 19:37]**
**EN:** have often thought about whether robo-taxis are really a more efficient solution. You know, from a passenger perspective, once the novelty wears off that the ride is autonomous, are people really going to care that it's autonomous? Or are they just going to care that they get from A to B?
**中文：** 我们经常思考robotaxi是否真的是一个更有效的解决方案。你知道，从乘客的角度来看，一旦自动驾驶的新鲜感消失，人们真的会关心它是自动驾驶吗？或者他们只是关心从 A 点到 B 点的交通情况？

**[19:37 – 19:57]**
**EN:** And are robotaxis actually doing anything to reduce congestion if the vehicle is still the same size as a normal car? You know, it's not a micro car. It's not micro mobility. And so... And then it's just kind of driving around endlessly in a loop,
**中文：** 如果robotaxi的尺寸仍然与普通汽车相同，那么robotaxi实际上会采取任何措施来减少拥堵吗？你知道，这不是一辆微型汽车。这不是微移动。所以...然后它就只是无限循环地行驶，

**[19:57 – 20:15]**
**EN:** not really doing anything and not picking up maybe one passenger, but just clogging up our streets. That's how somebody could look at it, right? Oh yeah, I think there's nothing wrong with looking at it that way. Obviously, staging suggests that you can reduce the amount of empty miles,
**中文：** 并没有真正做任何事情，也没有搭载一名乘客，只是堵塞了我们的街道。有人可以这么看，对吗？哦，是的，我认为这样看并没有什么问题。显然，分期表明您可以减少空驶里程，

**[20:15 – 20:20]**
**EN:** deadheading, being driven, but to your other points, I think everything's correct.
**中文：** 毫无意义，被驱使，但对于你的其他观点，我认为一切都是正确的。

**[20:21 – 20:27]**
**EN:** These vehicles are similar size, take up the same amount of space as a personal vehicle.
**中文：** 这些车辆尺寸相似，占用的空间与私家车相同。

**[20:29 – 20:50]**
**EN:** They're going to be using valuable urban space, whether that's at the curb or the roadways themselves. I also agree that once the novelty wears off of the automation, that we're talking about something very similar to ride, hailing, or taxi. I think there's some behavioral research that suggests that people do prefer, well not every person,
**中文：** 他们将利用宝贵的城市空间，无论是路缘还是道路本身。我也同意，一旦自动化的新鲜感消失，我们就会谈论与乘车、叫车或出租车非常相似的东西。我认为有一些行为研究表明人们确实更喜欢，但不是每个人，

**[20:50 – 21:19]**
**EN:** but a large chunk of people do prefer Not having a driver in the vehicle for these individual trips. There's a lot of concern about sharing a robotaxi with a stranger in a way that they're not as scared or afraid to be in a robotaxi or be in a vehicle with an Uber driver who might serve as a neutral party in the interaction. And I actually surveyed my students one time and maybe this will not be surprising
**中文：** 但很大一部分人确实更喜欢在这些个人旅行中车内不配备司机。人们对与陌生人共享一辆robotaxi存在很多担忧，因为他们不会那么害怕或害怕乘坐robotaxi，或者与可能在互动中充当中立方的 Uber 司机同车。我实际上对我的学生进行了一次调查，也许这并不奇怪

**[21:19 – 21:37]**
**EN:** to your listeners, but All of the male students in the class, they were not very concerned about being in a robotaxi with a stranger, but a large chunk of the female women students in the class were concerned and scared about sharing a robotaxi with a stranger. So that might give you some intuition as
**中文：** 对你的听众来说，但是班上的所有男学生都不太担心与陌生人一起乘坐robotaxi，但班上的大部分女学生对与陌生人共享robotaxi感到担心和害怕。所以这可能会给你一些直觉

**[21:38 – 21:47]**
**EN:** to why right now Waymo doesn't allow shared rides in their system. You can only book for maybe you and a friend or you and a family member to make a trip.
**中文：** 为什么现在 Waymo 不允许在其系统中共享乘车。您只能为您和朋友或您和家人预订旅行。


## 城市该如何管路缘

**SECTION_NOTE**
- 明确建议：**不要**禁止 robotaxi 使用路缘
- 城市抱怨缺乏监管抓手（加州权力几乎尽在州一级），但「用路缘禁令变相封杀」是糟糕的膝跳反应
- 主张：在与需求匹配的时段与区域设**专门接送区（pickup/drop-off zones）**，让车快进快出、不必争抢路缘
- **不支持**给 robotaxi / 网约车 / 出租车设专门的 staging 区；但应允许它们像私家车一样**短时停靠**
**END_SECTION_NOTE**

**[21:49 – 22:07]**
**EN:** Yeah, I mean, it's all a fascinating topic, isn't it? And it's all going to have such a profound impact on all of our lives and the way we travel. But let's go back to, circle back to the study then. So what can cities do in terms of regulating the curb? So what are you going to be advising to policymakers off the back of this research?
**中文：** 是的，我的意思是，这都是一个令人着迷的话题，不是吗？这一切都将对我们所有人的生活和旅行方式产生深远的影响。但让我们回到研究上来。那么，城市在监管路缘停车方面可以做些什么呢？那么，通过这项研究，您将向政策制定者提出什么建议呢？

**[22:10 – 22:19]**
**EN:** I'm not sure how many cities were considering banning robotaxis from using the curb. But if they were considering doing that, I would say Do not do that.
**中文：** 我不确定有多少城市正在考虑禁止robotaxi使用路缘。但如果他们考虑这样做，我会说不要这样做。

**[22:20 – 22:42]**
**EN:** I know one thing that cities are complaining about, and rightly so, is that they don't have many regulatory levers over robotaxis right now. In the state of California, really, the state has almost all the regulatory power. Cities have very limited regulatory power. And I think kind of a knee-jerk reaction to try to effectively ban these vehicles
**中文：** 我知道城市正在抱怨的一件事是，他们目前对robotaxi没有太多监管手段，这也是正确的。事实上，在加利福尼亚州，该州拥有几乎所有的监管权力。城市的监管权力非常有限。我认为试图有效禁止这些车辆是一种下意识的反应

**[22:42 – 22:45]**
**EN:** by not letting them use the curbs would be a bad idea.
**中文：** 不让他们使用路缘将是一个坏主意。

**[22:47 – 22:57]**
**EN:** They might be increasing congestion a little bit, but I think they're providing valuable mobility to a large number of people in urban environments. Okay, so beyond that kind of like main conclusion,
**中文：** 它们可能会稍微加剧拥堵，但我认为它们正在为城市环境中的大量人员提供宝贵的出行方式。好吧，除了主要结论之外，

**[23:00 – 23:02]**
**EN:** maybe moving beyond our study a little bit,
**中文：** 也许稍微超出了我们的研究范围，

**[23:05 – 23:23]**
**EN:** because we didn't really look into the pickups and drop-offs very much, but I am generally in favor of, at certain times of day, In areas where there is a lot of demand for passengers getting into not just robo-taxis, but taxis and ride-hailing vehicles in particular,
**中文：** 因为我们并没有真正深入研究上车和下车的情况，但我总体上赞成在一天中的某些时间，在乘客需求量很大的地区，不仅需要乘坐robotaxi，而且特别需要乘坐出租车和网约车，

**[23:24 – 23:43]**
**EN:** to have designated pickup and drop-off zones where it is easy for these vehicles to Get to the curb quickly, pick up a passenger quickly and exit very quickly. So individual vehicles are not having to fight for curb space and the vehicles are not spending much time at the curb at all. They're just getting the passenger in the vehicle and moving away quickly.
**中文：** 有指定的上车和下车区域，使这些车辆能够轻松快速到达路缘、快速搭载乘客并快速离开。因此，个别车辆不必争夺路缘空间，并且车辆根本不会在路缘花费太多时间。他们只是把乘客送上车，然后迅速离开。

**[23:45 – 23:52]**
**EN:** I don't think I'd be in favor of having like designated staging locations for robotaxis.
**中文：** 我不认为我会赞成为robotaxi指定类似的停靠地点。

**[23:54 – 24:11]**
**EN:** Or ride hailing or taxi vehicles in general. But I think just allow these vehicles to use the curb for short-term parking in the same way that private vehicles can use the curb for short-term parking. Again, not related to our study, but
**中文：** 或者乘坐一般的叫车或出租车。但我认为只是允许这些车辆使用路缘进行短期停车，就像私家车可以使用路缘进行短期停车一样。再说一遍，与我们的研究无关，但是


## 停车定价为何会失灵

**SECTION_NOTE**
- robotaxi 与网约车可以「再开远一点」，去用更便宜甚至免费的路缘车位
- 网约车司机人在车内、车辆仍运行时，目前并**不付费**；Waymo 同样如此
- 结论：停车定价作为城市管理车辆需求的杠杆，在 robotaxi 时代**会比以往任何时候都更弱**
**END_SECTION_NOTE**

**[24:14 – 24:34]**
**EN:** Parking pricing is going to be very challenging in a robo-taxi world, in a world with more Uber and Lyft, because they can always drive a little bit farther away and access the cheaper or free curbside parking. And then in the case of robo-taxis and Uber and Lyft drivers, Uber and Lyft drivers are still in the vehicle,
**中文：** 在robotaxi的世界里，在一个拥有更多 Uber 和 Lyft 的世界里，停车定价将非常具有挑战性，因为它们总是可以开得远一点，并获得更便宜或免费的路缘停车位。然后，就robotaxi以及 Uber 和 Lyft 司机而言，Uber 和 Lyft 司机仍在车内，

**[24:34 – 24:51]**
**EN:** so I don't think they're actually paying when they're sitting at the curb. As I understand it right now, Waymo is not paying when they're sitting at the curb and the vehicle's still on. So that's going to be a real challenge, I think, for cities going forward is how to manage vehicular demand when
**中文：** 所以我认为他们坐在路缘时实际上并没有付钱。据我目前的了解，当他们坐在路缘且车辆仍在行驶时，Waymo 不会付款。因此，我认为，对于未来的城市来说，这将是一个真正的挑战，即在以下情况下如何管理车辆需求：


## 私人无人车会给 VMT 带来什么

**SECTION_NOTE**
- 团队另一条研究线；本篇论文一作 **Jung & Bach** 的博士论文正是聚焦「私人拥有的无人车」
- Hyland 不预测时间表，但假设 **10–15 年**后进入家庭
- 建模结论：家庭会「送人上班 → 空车回 → 再接另一人去活动 → 再空车回」，**可能因此少买车**，但会**显著推高 VMT 与拥堵**
- 除非有政策让「开车更贵、拥堵更贵」——这是他眼中城市与州层面最重要的政策问题
**END_SECTION_NOTE**

**[24:51 – 25:06]**
**EN:** the parking pricing lever is going to be less effective than it ever has been. Yeah, I think that's a really good point about parking pricing. You also mentioned individual vehicles, but what about when those individual vehicles are personally owned driveless vehicles? Yeah.
**中文：** 停车定价杠杆将不如以往那么有效。是的，我认为停车定价的这一点非常好。您还提到了个人车辆，但是当这些个人车辆是个人拥有的无人驾驶车辆时呢？是的。

**[25:06 – 25:07]**
**EN:** That's going to have on VMT.
**中文：** 这将在 VMT 上进行。

**[25:11 – 25:22]**
**EN:** That's another area of research for my group. So, Jung and Bach, who I should have mentioned already, is the first author on this paper with Waymo, or the Waymo partially funded study, I'll put it that way. He's also,
**中文：** 这是我的团队的另一个研究领域。因此，Jung 和 Bach（我应该已经提到过）是 Waymo 这篇论文的第一作者，或者是 Waymo 部分资助的研究，我会这么说。他也是，

**[25:22 – 25:45]**
**EN:** his dissertation was focused on personally owned driverless vehicles, which I'm not going to make a forecast as to when Waymo or Toyota or another company is going to be selling these vehicles to individual households, but Let's say in 10 to 15 years they do sell them to households. I think in that scenario we have a lot of benefits to households in terms
**中文：** 他的论文重点是个人拥有的无人驾驶汽车，我不会预测 Waymo 或丰田或其他公司何时会将这些车辆出售给个人家庭，但假设在 10 到 15 年内他们确实会将它们出售给家庭。我认为在这种情况下，我们对家庭有很多好处

**[25:45 – 26:04]**
**EN:** of mobility, but we have some very big potential implications for congestion in vehicle miles traveled. What we're seeing in our modeling results there is that households absolutely will Have the vehicle drop off one household member at work,
**中文：** 流动性，但我们对车辆行驶里程的拥堵有一些非常大的潜在影响。我们在模型结果中看到的是，家庭绝对会让车辆接送一名正在工作的家庭成员，

**[26:04 – 26:13]**
**EN:** drive home, pick up another household member, take them to an activity, whether that's school or some after school activity, and then drive back home empty again. So in this case,
**中文：** 开车回家，接另一位家庭成员，带他们去参加活动，无论是学校还是放学后的活动，然后再次空车回家。所以在这种情况下，

**[26:14 – 26:38]**
**EN:** a household might actually be able to own fewer vehicles because these vehicles can travel empty and deadhead back to the household, but that's going to significantly increase VMT and congestion, unless of course there are some policies to Make it more expensive to drive and make it more expensive to congest the roadways. So I think that's a particularly important policy question for cities and states going forward.
**中文：** 一个家庭实际上可以拥有更少的车辆，因为这些车辆可以空载无偿返回家庭，但这将显着增加VMT和拥堵，当然，除非有一些政策使驾驶成本更高，道路拥堵成本更高。所以我认为这对于城市和州的未来来说是一个特别重要的政策问题。


## 「无人出租车的 Airbnb 模式」可信吗

**SECTION_NOTE**
- 访谈者类比：房子与车位都在共享，车闲着也是闲着，为什么不让它出去赚钱？
- 团队对「把 8 万–12 万美元资产交给陌生人」持**怀疑**态度
- 更看好**偶尔借给附近亲友**的模式——这可能让对方少买第二、第三辆车（加州语境）
- 对 **Tesla 设想**的「车主把车借给网约车车队运营商」模式存疑：清洁、损坏，以及「任何人、任何用途」
**END_SECTION_NOTE**

**[26:38 – 26:59]**
**EN:** Yeah, and I think it's so important that they start discussing that now rather than waiting for the companies to introduce the technology and then regulation catching up, which seems to happen every single time. It's like the Airbnb model for driver's taxis. Everything's going to become shared. We're sharing our car parking spaces already in the UK.
**中文：** 是的，我认为他们现在就开始讨论这一点非常重要，而不是等待公司引入技术然后监管赶上，这似乎每次都会发生。这就像 Airbnb 的司机出租车模式。一切都将变得共享。我们已经在英国共享停车位。

**[27:01 – 27:21]**
**EN:** It makes sense if I buy a driverless vehicle and it's just sat in the car parking space when it could be out making me money, right? That makes total sense as a business model. But the impact on VMT, as you say, is just going to be huge. Yeah. So Tesla talked a lot about this.
**中文：** 如果我购买一辆无人驾驶汽车，并且它只是停在停车位上，而它可以为我赚钱，这是有道理的，对吗？作为一种商业模式，这是完全有意义的。但正如你所说，对 VMT 的影响将会是巨大的。是的。所以特斯拉对此谈了很多。

**[27:22 – 27:39]**
**EN:** Buy one of our vehicles, use it when you want, and then give it to the fleet and we'll make money for you while you're doing other activities. We're a little bit skeptical that people will be willing to give their $80,000 to $120,000 asset to strangers,
**中文：** 购买我们的一辆车辆，在需要时使用它，然后将其交给车队，我们将在您进行其他活动时为您赚钱。我们有点怀疑人们是否愿意将自己的 80,000 至 120,000 美元资产交给陌生人，

**[27:40 – 27:45]**
**EN:** but we do think there's maybe a market, or not really a market, but an opportunity
**中文：** 但我们确实认为可能存在市场，或者不是真正的市场，而是机会

**[27:47 – 28:04]**
**EN:** To get more use out of, again, these valuable assets where, okay, let's say I own a Tesla. I don't. I own a 2016 Volvo. I own a Tesla. I have family nearby. I have friends that also have kids that maybe need to make a trip
**中文：** 为了更好地利用这些宝贵的资产，好吧，假设我拥有一辆特斯拉。我不知道。我拥有一辆 2016 款沃尔沃。我拥有一辆特斯拉。我有家人在附近。我的朋友也有孩子，他们可能需要去旅行

**[28:04 – 28:21]**
**EN:** and they don't have an extra vehicle to make this trip. I'd be willing to lend my vehicle out occasionally or semi-occasionally to friends and family that live nearby, which may be Prevent them from buying a third vehicle or a second vehicle here in California. So I think there's like a nice opportunity there for some sharing
**中文：** 他们没有额外的车辆来完成这次旅行。我愿意偶尔或半偶尔地将我的车辆借给住在附近的朋友和家人，这可能会阻止他们在加利福尼亚州购买第三辆车或第二辆车。所以我认为这是一个很好的分享机会

**[28:22 – 28:38]**
**EN:** of these personally-owned driveless vehicles, but we're a little bit skeptical of the Tesla model where it essentially reverts back to a full ride-held type service where anyone could be throwing up or using your vehicle for any type of purpose. Yeah. And I, you've also got issues of cleanliness as well.
**中文：** 这些个人拥有的无人驾驶车辆，但我们对特斯拉模型有点怀疑，它本质上恢复到完整的乘车类型服务，任何人都可以扔掉或使用你的车辆用于任何类型的目的。是的。我，你也有清洁问题。

**[28:38 – 28:53]**
**EN:** Um, you know, there's a reason why these, these robo taxis are going back to the, the, the depot to get charged and cleaned. Right. So, uh, maybe my lending out to friends and family. Um, but yeah, it's, Michael, it's been a fascinating conversation.
**中文：** 嗯，你知道，这些robotaxi要返回停车场充电和清洁是有原因的。正确的。所以，呃，也许我借给朋友和家人。嗯，但是，是的，迈克尔，这是一次有趣的谈话。

**[28:53 – 29:03]**
**EN:** Um, I've really, really enjoyed it. Is there anything else that you feel like we missed or you, you, you know, you've got got to get off your chest. Let's see here. Um,
**中文：** 嗯，我真的非常喜欢它。还有什么是你觉得我们错过的吗？或者你，你，你知道，你必须吐露心声。让我们看看这里。嗯，


## 结语：拥堵定价，对所有车一视同仁

**SECTION_NOTE**
- 城市该不该向 robotaxi 收路缘费/市区行驶费？答案：**应该，但不止 robotaxi**
- robotaxi 应与所有乘用车适用**同一套规则**：要付费停车就都付费，要付高峰通行费就都付
- 他作为交通分析师**支持拥堵定价**（伦敦、纽约经验），认为洛杉矶、旧金山等高密度城市同样可行
- **反对**只对 robotaxi 加税：那会让需求转移回私家车与 Uber，拥堵依旧；真想减拥堵，就得对所有乘用车收费
**END_SECTION_NOTE**

**[29:06 – 29:10]**
**EN:** So I've been asked the study a number of times about
**中文：** 所以我多次被问及这项研究

**[29:12 – 29:34]**
**EN:** should cities be charging robo-taxis to use the curb and to drive around in urban areas? And my answer is yes, but not just robo-taxis. In my opinion, robo-taxis should be subject to the rules of all the private vehicles or all the passenger vehicles in urban areas.
**中文：** 城市是否应该对robotaxi在城市地区使用路缘行驶和行驶时收费？我的答案是肯定的，但不仅仅是robotaxi。我认为，自动驾驶出租车应该遵守所有私家车或所有城市客运车辆的规则。

**[29:35 – 29:51]**
**EN:** If a passenger vehicle has to pay to park, a robotaxi should have to pay to park. If a robotaxi has to pay to drive in the city of San Francisco at 9 a.m. in the morning, then a personal vehicle, a ride-hailing vehicle, a regular taxi should also have to pay during those time periods.
**中文：** 如果客运车辆需要付费停车，robotaxi也应该付费停车。如果robotaxi早上 9 点在旧金山市内行驶需要付费，那么在这些时间段内，私家车、网约车、普通出租车也应该付费。

**[29:51 – 30:14]**
**EN:** So as a transportation analyst, I am in favor of congestion pricing. I think it's worked very well in London. It's worked Very well in New York City. I think it can work in other large, dense areas, including Los Angeles at San Francisco. But I wouldn't subject robo-taxis to additional fees and additional taxes that you're not subjecting personal vehicle owners to.
**中文：** 因此，作为一名交通分析师，我赞成拥堵收费。我认为这在伦敦效果很好。它在纽约市效果很好。我认为它可以在其他大而密集的地区发挥作用，包括洛杉矶和旧金山。但我不会向自动驾驶出租车收取额外的费用和额外的税款，而私人车主则不会缴纳这些费用和税款。

**[30:15 – 30:29]**
**EN:** That's not because I'm a shill for Waymo. That's because if you just charge Waymo to drive in urban areas, people are just going to They're going to shift out of Waymo, they're going to shift into their personal vehicles, they're going to shift into Ubers, and the city is just going to be as congested as it's always been.
**中文：** 这并不是因为我是 Waymo 的托儿。这是因为，如果你只是给 Waymo 充电，让他们在城市地区开车，人们就会离开 Waymo，转而使用自己的私家车，转而使用 Uber，而城市就会像以前一样拥堵。

**[30:29 – 30:45]**
**EN:** So if you actually want to reduce congestion, you need to charge all of the personal passenger vehicles for using very valuable space in urban areas. Makes sense. Yeah, the ultra low emission zone has been a phenomenal success in London. I can say that.
**中文：** 因此，如果你真的想减少拥堵，你需要对所有使用城市地区非常宝贵的空间的私人客运车辆进行收费。有道理。是的，超低排放区在伦敦取得了巨大的成功。我可以这么说。

**[30:45 – 30:55]**
**EN:** But no, that all makes sense. So Michael, we're going to have to leave it there. But thanks so much for coming on. And yeah, it's been a pleasure to have you. Thanks, Ben. I really appreciate it.
**中文：** 但不，这一切都是有道理的。所以迈克尔，我们不得不把它留在那里。但非常感谢您的到来。是的，很高兴有你。谢谢，本。我真的很感激。

**[30:55 – 30:58]**
**EN:** Great talking to you. See you later.
**中文：** 很高兴跟你说话。稍后见。
