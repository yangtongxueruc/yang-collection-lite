> 本期英文底稿为本地语音识别（faster-whisper `small.en`，460 段合并为 93 段），**非 Substack 官方转录**（该期官方转录为空）。中文为逐段人工翻译。
> 已按官方节目简介与上下文校正专名误听：James Bang → **James Peng（彭军）**、Jingxua → **Tsinghua**、Jianqing Liu / Tian Cheng Lo → **楼天城 Tiancheng Lou（CTO）**、Z4X → **丰田 bZ4X**、Vern(e) → **Verne**、boat → **Bolt**、the Atlantis → **Stellantis**、Zacreb → **Zagreb**、RGA → **RTA**、Mova Saleh → **Mowasalat**、railroad → **real road**、pony board → **Pony World**、unieconomics → **unit economics**、Robotech C13 → **robotaxi 约 1,200 万 / robotruck 约 1,300 万美元**。
> 所有 `[mm:ss – mm:ss]` 均为音频真实时间戳。个别句子因识别歧义在译文中以括注标出，详见《总结分析》的「存疑与局限」。


## The founder story · 从 Google、百度到小马智行

**[00:00 – 00:33]**
**EN:** Welcome to Autonomy Insiders, the show where global industry leaders in autonomous driving unpack their real world insights. So is Germany also on your list? The short answer is yes. If we only consider the whole company runs robotaxics, we need roughly 50,000 robotaxics for generating positive cash for all vehicles per mile cost is actually a lot lower in
**中文：** 欢迎来到 Autonomy Insiders，这档节目请来自动驾驶行业的全球领袖，拆解他们来自真实世界的洞察。……德国也在你们的名单上吗？简短的回答是：在。如果只考虑全公司靠 robotaxi 一条线来跑，我们大约需要 5 万辆 robotaxi 才能产生正现金流。所有车辆的每英里成本其实要低得多……（开场为预告片剪辑，句子被拼接，非完整问答）

**[00:33 – 00:56]**
**EN:** case compared with Waymo can be like three to five times cheaper. Of course, you can say, well, in 20 years, maybe everyone will be a similar and then become a commodity, maybe. But at least I think in the next many years, we'll still have a huge edge. Welcome back to Autonomy Insiders.
**中文：** ……跟 Waymo 相比，可以便宜三到五倍。当然你可以说，二十年后也许大家都差不多了，然后就变成大宗商品，也许吧。但至少我认为在未来很多年里，我们仍然有巨大的优势。欢迎回到 Autonomy Insiders。

**[00:56 – 01:18]**
**EN:** I'm your host Daniel M. Brodly. Everyone listening knows Pony.ai and my guest today is the person who started it. Dr. James Bang is co-founder, chairman and CEO of Pony.ai. He studied and Jingxua did his PhD at Stanford and spent 11 years at Google and Baidu. And in December 2016, he left to found Pony.ai and Silicon Valley together with
**中文：** 我是主持人 Daniel。各位听众都知道小马智行，而我今天的嘉宾正是创立它的人。彭军博士是小马智行的联合创始人、董事长兼 CEO。他本科就读清华，在斯坦福取得博士学位，在 Google 和百度工作了 11 年。2016 年 12 月，他离开并和楼天城一起在硅谷创立了小马智行……

**[01:18 – 01:37]**
**EN:** Jianqing Liu. And today the company's list on NASDAQ and in Hong Kong. And today we'll cover the founder story, the business model Europe, the Middle East, the number and where this whole industry is going. So James, it's an honor. Welcome to Autonomy Insiders. Yeah, Daniel, it's great to be here and have this great opportunity to
**中文：** ……如今公司在纳斯达克和香港上市。今天我们会聊创始人故事、商业模式、欧洲、中东、那些数字，以及整个行业往哪里走。James，很荣幸，欢迎来到 Autonomy Insiders。——谢谢 Daniel，很高兴来到这里，有这么好的机会……

**[01:37 – 02:01]**
**EN:** talk to you. So maybe let's start with you. So you left two of the biggest AI companies in the world to end the field where nobody had a working business yet back then. So why did you decide to leave and found Pony.ai? Well I think back to 10 years ago that was the first big wave of AI that's where the AI beats the best gold player. So we do see the potential of AI to change
**中文：** ……和你聊聊。也许先从你本人开始。你离开了世界上最大的两家 AI 公司，投身一个当时还没有任何成型生意的领域。为什么决定离开、创办小马智行？——回想十年前，那是第一波 AI 大潮，就是 AI 击败最强围棋棋手的时候。我们确实看到了 AI 改变生活的潜力，而自动驾驶……

**[02:01 – 02:28]**
**EN:** our lives and autonomous driving certainly is a big area that has a great societal and financial benefits. So just from a technical point of view it's also such a challenging area to work on because it has hardware, software, it has the distributed systems, has real-time systems. So from every angle I look at this area is such a great industry to work on and at the same time
**中文：** ……显然是一个社会效益和财务回报都很大的领域。单从技术角度看，它也是个极有挑战的方向：有硬件、有软件、有分布式系统、有实时系统。所以从每个角度看，这都是一个值得投入的伟大行业；与此同时……

**[02:28 – 02:54]**
**EN:** I think stay in a big cooperation with all the internal politics and the speed of a big group. It's certainly going to be an impediment to my contribution, so I figured might as well start afresh, working on this area, a great area in a startup environment. Although, of course, at that time, I had no idea where it's going to be, but I think it's such a great area to
**中文：** ……我觉得留在大公司里，那些内部政治、大团队的速度，肯定会成为我发挥贡献的阻碍，所以我想不如重新开始，在创业环境里做这个方向。当然那时候我完全不知道它会走向哪里，但我觉得这是这么值得做的领域，应该把全部精力投进去。

**[02:54 – 03:12]**
**EN:** work on that, I should put all my energy into it. So that's the beginning story of Pony.ai and the rest is history. Yeah, and I think that's a really, really good lead-in. And the company itself also changed a lot in those 10 years. So it started in Fremont, California. Today it's headquartered in Guangzhou.
**中文：** ……这就是小马智行的开篇故事，剩下的就是历史了。——这个引子真的非常好。公司这十年本身也变了很多：起步在加州 Fremont，如今总部在广州。

**[03:12 – 03:31]**
**EN:** So you've built this company basically in both systems, Silicon Valley and China. And I think you told also a journalist in June that you're used to complexity from China. So what does China train into an AV company that Silicon Valley maybe cannot? I think there are two angles. One is from a technical point of view, where the traffic
**中文：** 也就是说，你基本上是在硅谷和中国两套体系里把公司建起来的。我记得你六月跟一位记者说过，你已经习惯了中国带来的复杂性。那么，中国到底训练出了一家什么样的 AV 公司，是硅谷可能给不了的？——我想有两个角度。一个是技术角度，中国的交通在多数情况下确实更具挑战，因为……

**[03:31 – 03:53]**
**EN:** in China suddenly is, in most cases, more challenging, because there's a lot more pedestrians and the cyclists on the road and typically the road are more crowded. So the AI driver, to be safe, has to learn to interact with all the surrounding traffic. Also, the weather conditions can be more predictable.
**中文：** ……路上的行人和骑行者多得多，道路通常也更拥挤。所以 AI 司机要保证安全，就必须学会和周围所有交通参与者交互。另外，天气条件也可能更（不可预测 —— 此处识别有歧义）。

**[03:53 – 04:18]**
**EN:** Also, I think just from a technical point of view, it's a bit more challenging. And also, to juggle between China and the US, especially over the last several years, is increasingly more challenging because of the supply chain disruption, the data compliance, and all the other legal compliance. So I think it's the complexity that in the modern days, we have to deal with.
**中文：** 所以我觉得，单从技术角度讲，它也更难一点。还有，尤其最近这几年，要在中美之间两头兼顾越来越难：供应链中断、数据合规，以及其他各种法律合规。我觉得这就是现代环境下我们必须应对的复杂性。

**[04:18 – 04:34]**
**EN:** And I think autonomous driving is certainly not an exception or could be actually an area that face more challenges. And maybe now let's look at Pony.ai and how Pony.ai actually makes money. Because when I look at your second quarter, for example, I see free businesses with almost equal size.
**中文：** 而自动驾驶当然不例外，甚至可能是面临更多挑战的领域。现在也许该来看看小马智行到底怎么赚钱了。因为我看你们第二季度，是三条规模几乎相当的业务线……


## The business · 三条营收线、车队与谁拥有车

**[04:34 – 04:57]**
**EN:** So I think it gets you reported about $36 million in revenue, roughly 12 from Robotech C13 from Robotruck and 11 from what you call intelligent solutions. Could you walk us through what's inside those three business lines and also how each of these makes money? Yes. Pony.ai, you can think about our core business is making a virtual driver, a driver that
**中文：** ……我记得营收大约 3,600 万美元，robotaxi 约 1,200 万、robotruck 约 1,300 万、还有你们叫 intelligent solutions 的约 1,100 万。能带我们过一遍这三条线里各有什么、各自怎么赚钱吗？——可以。你可以把小马智行的核心业务理解成造一个虚拟司机，一个有能力驾驶不同车型的司机……

**[04:57 – 05:19]**
**EN:** be able to have the capacity and the capability to drive different types of vehicles. Of course, looking at the mobility industry itself, the move of people and goods are the two biggest areas. That's why we're working on those two areas. One is related with moving of people, that's robotaxi.
**中文：** ……当然，看出行行业本身，人的移动和货物的移动是最大的两块，所以我们做这两块。一块跟载人有关，就是 robotaxi。

**[05:19 – 05:40]**
**EN:** The other is the move of goods, which is the robotruck, or we actually introduced the small trucks as well. The third business line is actually, essentially think about because we are developing the virtual driver, there's a lot of hardware components, there's training systems, there's simulation,
**中文：** 另一块是运货，也就是 robotruck，我们其实还推出了小型卡车。第三条业务线，本质上是因为我们在开发虚拟司机，过程中产生了大量硬件组件、训练系统、仿真、软件，而有些客户就想要其中某些组件、某些硬件或软件系统。

**[05:40 – 06:08]**
**EN:** software and some of our customers want certain components or certain hardware or software systems. So the third business we call intelligent systems essentially you can think of that as a licensing model where we sell some of the components. Currently the fastest growing area is the robotaxi where we actually spend most of the time is the fastest growing segment among the
**中文：** 所以第三条我们叫 intelligent systems，你大致可以把它理解成一种授权模式，我们卖其中一部分组件。目前增长最快的是 robotaxi，也是我们投入时间最多的，是三条线里增长最快的板块……

**[06:08 – 06:29]**
**EN:** three. But the other two, of course, we're working on those as well. And you also mentioned in an earnings call that you share about 80% of your technology stack between RoboTaxi and Robotruck. And as you mentioned this year, you added also a driverless light truck. So can you also explain a bit how do you decide what Pony.ai builds and also what
**中文：** ……不过另外两条当然也在做。你在财报电话会上还提到，Robotaxi 和 Robotruck 之间大约共享 80% 的技术栈；今年你们又加了无人轻卡。能不能再讲讲，小马智行怎么决定做什么、以及不做什么？——好问题。上一个问题我应该展开一点：robotaxi 和 robotruck 这两个领域其实高度关联……

**[06:29 – 06:54]**
**EN:** doesn't? Excellent. Great question. I should have elaborate a bit on my in the last question, is the robot taxi and robot truck areas are actually briefly interrelated. That's exactly because most of the software and hardware systems are shared between the two. The difference you can think of is while truck is a lot larger, the dynamic model of a truck
**中文：** ……正是因为绝大多数软硬件系统是共用的。差别在于卡车大得多，动力学模型很不一样，因为通常带挂车、带车头，运动方式不同，所以我们得针对 robotruck 运动方式的差异做补偿。除此之外……

**[06:54 – 07:21]**
**EN:** is quite different because typically with a trailer and a hat. So it can move in a different way. So we have to compensate for the fact that the robot truck moves differently. Other than that, the business model and the way to drive them and how do we do perception, how do we plan for the routes are actually pretty much the same. So over the last 10 years,
**中文：** ……商业模式、驾驶方式、怎么做感知、怎么做路径规划，其实都差不多。过去十年，我想我们在大大小小的车辆上、在开放道路行驶条件下，积累了技术和运营 know-how。

**[07:21 – 07:48]**
**EN:** I think we have built technical and operational know-house on vehicles, large or small, that can deal with open road driving conditions. So that's really the core strength of the company and that's the area we're working on. So that's why we think about Robotaxi, Robotruck, Light Truck. They're all moving in a city or on a highway environment.
**中文：** 这确实是公司的核心能力，也是我们专注的领域。所以我们会考虑 Robotaxi、Robotruck、Light Truck——它们都在城市或高速环境里跑，都跑得相对快，都要面对和周围交通交互的挑战。

**[07:48 – 08:12]**
**EN:** They're all moving relatively fast. They all have the challenge of interacting with the surrounding traffic. So that's our core strength and we want to leverage our core strength. Although the challenge is very high, the potential is also huge. So the short answer to the question is we built incredible technical and operational know-hows,
**中文：** 这就是我们的核心优势，我们想把它用足。虽然挑战很高，但潜力也巨大。所以简短的回答是：我们积累了很强的技术与运营 know-how，想把它用在大领域、大应用上。

**[08:12 – 08:37]**
**EN:** and we want to leverage them for the big areas, big applications. Some of the smaller ones, for example, the last-mile delivery, for example, the L2 applications, generally, we don't work on those extensively. But as I mentioned, we have the intelligent solution systems, so we sell certain components to support those areas while we don't directly working on, but for
**中文：** 一些比较小的方向，比如末端配送、比如 L2 应用，一般来说我们不做深度投入。但如我提到的，我们有 intelligent systems，会卖某些组件去支持这些领域，只是不直接做，但对于……

**[08:37 – 09:04]**
**EN:** the core areas, we work on them directly. Makes sense. And maybe now let's also talk about the fleet and to be precise about the robotaxi fleet, because you also have a target announced for this year. You ended in June with 1,975 robotaxis and you're aiming for more than 3,500 by your end. So that's roughly 1500 more vehicles to go. So where do they go? Do you want to have
**中文：** ……核心领域，我们直接自己做。——说得通。现在也许聊聊车队，准确说是 robotaxi 车队，因为你们也公布了今年的目标：六月结束时是 1,975 辆 robotaxi，年底目标是 3,500 辆以上，也就是还差大约 1,500 辆。这些车会放到哪？你想要的是……

**[09:04 – 09:30]**
**EN:** more density in China's tier one cities or is it more like in new cities overseas? And maybe also what is the real bottleneck right now? Is it vehicle supply? Is it permits? Is it people who run the fleets then? Yeah, we actually have both. So our internal strategy of scaling up is a T-shape. Essentially the horizontal line represents more cities that we will go into,
**中文：** ……加大中国一线城市的密度，还是更多投向海外新城市？另外现在真正的瓶颈是什么？是车辆供给、牌照，还是运营车队的人？——其实两者都有。我们内部的扩张策略是 T 字形：横线代表我们会进入的更多城市……

**[09:30 – 09:57]**
**EN:** but some of the cities probably will go into with, say, a fleet of 20, 30, 50, where we will start building our capabilities in that city. Whereas the vertical line represents the core cities will already have presence, then will increase the density, will have better unit economics in those cities. So we'll continue to follow that strategy for our scale
**中文：** ……其中有些城市可能只进 20、30、50 辆，用来在这个城市把能力建起来；竖线则代表已经有布局的核心城市提高密度，单位经济会因此更好。我们会继续按这个策略推进规模化……

**[09:57 – 10:09]**
**EN:** up. In terms of the bottleneck, because autonomous driving is such a complex system, I don't think it's a single factor. Because think about any complex systems,
**中文：** ……（承上：规模化）至于瓶颈，因为自动驾驶是这么复杂的一个系统，我不认为存在单一因素。想想任何复杂系统……

**[10:10 – 10:31]**
**EN:** there are so many moving pieces, you need them all moving in the same direction, right? I think some of the core factors you already mentioned, we need to have regulatory approval, We need to have manufacturing capacity. We need to have operational know-how. Also in the city, we need parking space where we can park those cars and charge them and service them.
**中文：** ……都有太多活动部件，你得让它们全部朝同一个方向动，对吧？你刚才提到的几个核心因素都在里面：要有监管批准、要有制造产能、要有运营 know-how；在城市里还得有停车位，能停车、充电、做保养。

**[10:32 – 10:56]**
**EN:** So all those factors need to be in place. We have to acquire licenses for those vehicles. We have to follow certain trajectories. But as I see, because there's only two months left, As I see this year, I think we're a while off on target to get the 3,500 vehicles to be manufactured and deployed. And certainly we're also at the time to look at the plan for next year.
**中文：** 所有这些因素都得就位。我们得为车辆取得牌照，得遵循一定的审批流程轨迹。就我看，因为只剩两个月了，今年这 3,500 辆的制造与部署（仍在推进轨道上 / 识别有歧义），当然现在也到了看明年计划的时候。

**[10:56 – 11:14]**
**EN:** But at least at this point, I'm pretty confident about this year's progress. Sounds good. And this also leads to another question. So who actually owns those vehicles? Because more and more of them are not on your balance sheet. So, under your joint deployment model, partners can fund the vehicles, run local operation,
**中文：** 但至少在这一点上，我对今年的进展相当有信心。——听起来不错。这也引出下一个问题：这些车到底归谁所有？因为越来越多车辆不在你们的资产负债表上了。在你们的联合部署模式下，伙伴可以出钱买车、跑本地运营……

**[11:14 – 11:34]**
**EN:** and also bring the riders. And you provide the virtual driver and share the economics, at least by understanding. And Toyota was the first adopter with 1,000 Z4X vehicles. Could you maybe walk us through your joint deployment model in detail? So, how does it work? And who are your preferred partners in this type of model?
**中文：** ……还能带来乘客；你们提供虚拟司机并分享收益，至少我理解是这样。丰田是首个采用者，涉及 1,000 辆 bZ4X。能详细讲讲联合部署模式怎么运作吗？以及在这种模式里，你们偏好什么样的伙伴？

**[11:34 – 12:02]**
**EN:** Yeah, great question. Think about in the first, say, a thousand vehicles, we exclusively own them and the reason is that it's such a new business model where we need to prove that it actually works so for the initial batch we own everything right we actually acquire licenses for them we manufacture them we own them and we operate them with our own app essentially we do use
**中文：** 好问题。想想最初那一千辆车，是我们独家自有的。原因是这个商业模式太新，我们必须证明它真的能跑通——所以首批我们什么都自己来：自己拿牌照、自己制造、自己持有、自己用自有 App 运营，基本上连用户获取也自己做。

**[12:02 – 12:31]**
**EN:** acquisition as well. The main reason behind that is we need to have financial model and financial data to actually prove this is a working business model. As the beginning of this year, we launched the Gen 7 vehicle and it proved that on a vehicle basis, we will already be able to have positive margin. That means owning the vehicle itself is not losing money. Because
**中文：** 背后的主要原因，是我们需要有财务模型和财务数据，来真正证明这是一个可行的商业模式。今年年初我们发布了 Gen 7 车型，它证明了在单车层面我们已经能做到正毛利，也就是说，持有这辆车本身并不亏钱。正因为……

**[12:31 – 13:01]**
**EN:** of that confidence because that positive unit margin then we can do the joint deploy model. Joint deploy model essentially can on a high level we can think of because we have positive margin somebody else can own the vehicle service them or even do the user acquisition. So generally think about, there are typically four players on a high level involved in taxi business.
**中文：** ……有这份信心、有这个正的单车边际，我们才能做联合部署。往高层面上想：既然边际为正，别人就可以持有车辆、做服务，甚至做用户获取。一般来讲，出租车生意里有四类参与者……

**[13:01 – 13:28]**
**EN:** That's not even mentioned in robot taxi business. There's user acquisition, for example Uber. Then there's fleet owner who just owns the fleet. The third player is a driver, right, who just drives the vehicle. And the fourth is the one who does all the service of the vehicle, cleaning, charging, servicing, insurance, and all that. You can think of a pony as
**中文：** （这还没专门说 robotaxi，普通出租车就是这样）一是用户获取，比如 Uber；二是车队所有者，只负责持有车队；三是司机，只负责开车；四是做车辆全部服务的一方——清洁、充电、维保、保险等等。你可以把小马智行理解为……

**[13:28 – 13:52]**
**EN:** core strength is a driver. So we provide the virtual driver for all the vehicles. For all the other three pieces, I think we can work with partners. Certainly in different markets, in different verticals, in different cities, we might own different areas. But in all of them, we own the driver. So that's the high level. And what you mentioned specifically, the
**中文：** ……核心优势是「司机」。所以我们为所有车辆提供虚拟司机；其他三块都可以和伙伴合作。当然在不同市场、不同垂直领域、不同城市，我们可能自己承担不同的部分，但在所有组合里，司机这一块都由我们掌握。这是大框架。你具体提到的……

**[13:52 – 14:18]**
**EN:** collaboration with Toyota is that Toyota will be the owner of the vehicle but in that collaboration will still be the user acquisition. In some of the partnership for example our partnership with Uber that will be just a driver and then we have Uber as a user acquisition and somebody else as the vehicle owner. So really I think once you know there are four pieces I think
**中文：** ……与丰田的合作，是丰田作为车辆所有者，而那次合作里用户获取仍由（我们）承担。有些合作，比如我们和 Uber，我们就只是司机，Uber 做用户获取，另有第三方做车辆所有者。所以我想，一旦你知道有这四块……

**[14:18 – 14:39]**
**EN:** And they can be different combinations. And it's also a good segue to get to my home continent. So Europe, Zagreb is where you made history this year. So in April, you launched Europe's first commercial robot taxi service in Zagreb with Vernon Uber with an operator on board. And in September, you started fully driverless rides with passengers on a 22 kilometer route
**中文：** ……它们就可以有不同组合。——这也是个很好的过渡，回到我所在的大陆。欧洲，萨格勒布是你们今年创造历史的地方：四月你们与 Verne、Uber 在当地推出欧洲首个商业 robotaxi 服务，车上有操作员；九月你们开始全无人载客，跑一条 22 公里的路线……


## Europe · 萨格勒布、英国、德国、卢森堡与数据主权

**[14:39 – 14:59]**
**EN:** to the airport. So what had to be true technically, and also with the regulator before you took out the person of the car, and also what is the gate between driverless test rides today and a driverless service where people pay for it? I think the reason we were able to deploy it so fast, of course, one is because we have
**中文：** ……通往机场。那么在把人从车里拿掉之前，技术上和监管上必须满足什么？还有，从今天的无人测试乘坐，到人们愿意付费的无人服务，中间那道门是什么？——我们能这么快落地，其中一个原因当然是我们已经有……

**[14:59 – 15:26]**
**EN:** more than 100, I think now it's 110 million kilometers of railroad operation. And we have gained a lot of experience with our tech driving on the roads in China and in the US. So our core virtual drive itself is safe, reliable, comfortable, and all that. Another reason is, of course, because the great partners like Vern and Uber
**中文：** ……超过 1 亿、我想现在大约是 1.1 亿公里的实路运营里程，而且在中国和美国的道路上用我们的技术积累了很多经验。所以我们的核心虚拟司机本身是安全、可靠、舒适的。另一个原因，当然是像 Verne 和 Uber 这样的优秀伙伴……

**[15:26 – 15:51]**
**EN:** really work tirelessly with us to make it happen. Some of the challenges we face in Zagreb, from a technical point of view, of course, then it's the famous roundabouts. There are just so many roundabouts in Europe. We don't normally see that in China and in the US. So our existing operational domains, I think a couple of roundabouts at best,
**中文：** ……真的和我们一起不遗余力地把它做成。在萨格勒布遇到的挑战，技术角度当然就是出了名的环岛：欧洲的环岛实在太多，在中国和美国我们不常见到。我们既有的运营域里，最多也就几个环岛……

**[15:51 – 16:14]**
**EN:** but there are so many roundabouts and also the trams. We do have trams in our existing operation domain, but in Zagreb, they share the same road, same lane with RoboTaxi. So interacting with the tram is also a new thing. So mostly from technical point of view, those two new things we need to deal with and by working with the Vernes and Uber closely,
**中文：** ……但那里环岛特别多，还有有轨电车。我们既有运营域里也有电车，但在萨格勒布，电车和 Robotaxi 共用同一条路、同一条车道，所以和电车交互也是件新事。技术上主要就是这两样新东西要处理，而通过和 Verne、Uber 紧密协作……

**[16:14 – 16:39]**
**EN:** we were able to solve them really quickly. And another challenge, of course, is from the regulatory point of view. Because in Europe, although there's testbed initiative to support autonomous driving, some of the regulations are not really clear. And specifically for that graph, you have to adopt that for the local city. So in that area, of course,
**中文：** ……我们很快就解决了。另一个挑战当然来自监管角度。欧洲虽然有 testbed 倡议支持自动驾驶，但有些法规并不真正清晰，而且具体到萨格勒布，还得按本地城市来适配。所以在这一块……

**[16:39 – 17:03]**
**EN:** we mostly rely on various local know-how push the boundaries on the regulatory front. So I think from both sides we were able to really move fast and get those launched. And Zacreb was the first city but in August you made also clear it won't be the only one so together with Uber you plan more than 2,000 robot taxis in Europe. Zacreb is live and this
**中文：** ……我们主要依靠各种本地 know-how 去推监管的边界。我想两侧同时发力，才让我们推进得这么快、把服务上线。萨格勒布是第一座城市，但八月你们也明确了它不会是唯一一座——和 Uber 一起，你们计划在欧洲部署 2,000 多辆 robotaxi。萨格勒布已经上线，这个月你们又点名了伦敦和曼彻斯特……

**[17:03 – 17:28]**
**EN:** month you also named London and Manchester but before we go into the UK I would also like to understand the logic behind. Can you rank the criteria for picking a European city. Yes, well first and foremost we generally pick the city together with our partners. It's not one-sided story of course. Second, the city generally needs to be relatively
**中文：** ……不过在聊英国之前，我还想先弄清背后的逻辑。你能给挑选欧洲城市的标准排个序吗？——可以。首先，一般是我们和伙伴一起选城市，当然不是单方面决定。第二，城市通常要相对……

**[17:29 – 17:54]**
**EN:** sizable. We don't want to work in a very small city where the economic value is not that big. And then we want work in the city that has good regulatory approval and also has a supportive local government. A third, of course, is generally there's some support from the local residents for new technology like autonomous driving.
**中文：** ……有一定规模，我们不想去一个经济价值不大的很小的城市。然后我们希望这个城市有良好的监管许可，也有支持性的地方政府。第三，一般来说当地居民对自动驾驶这类新技术要有些支持度。

**[17:54 – 18:21]**
**EN:** I think those are the main considerations for us to decide which cities to go into. makes sense and with that I think we can now go to the UK because you moved also fast there so London on October 8th and Manchester I think six days later so two UK cities more less in one week and London and Manchester are very different cities so what role does each play
**中文：** 我想这些就是我们决定进哪些城市的主要考量。——说得通。那就可以聊英国了，你们那边动作也很快：10 月 8 日伦敦，我想六天后就是曼彻斯特，一周内两座英国城市。伦敦和曼彻斯特非常不同，各自扮演什么角色……

**[18:21 – 18:37]**
**EN:** and is Manchester maybe also a template for a more mid-sized European city for you? Yeah, I think in Europe, most of the interesting cities are relatively the meat size and Zagreb is actually meat size as well. So I think those are the majority of the cities will
**中文：** ……曼彻斯特会不会成为你们进入中等规模欧洲城市的一个模板？——我想在欧洲，多数有意思的城市都相对是中等规模，萨格勒布其实也属于中等规模。所以我认为我们会上线的大多数城市……

**[18:38 – 18:55]**
**EN:** launch and London of course is one of the few mega cities in Europe where we will launch the the service and the two UK cities, the reason generally because the UK has supported regulation.
**中文：** ……都是这一类；而伦敦当然是欧洲少数的特大城市之一，我们也会在那里上线服务。选这两座英国城市，总体上是因为英国有支持性的监管。

**[18:57 – 19:21]**
**EN:** It's the demand for mobility generally quite healthy. Those are the, especially London, those are the tourist attraction. There's a lot of demand for shared mobility. So I think that those are definitely great cities to enter and to build the confidence to the regulators and to the local residents. And the two UK cities also look different on the operating
**中文：** 出行需求总体相当健康，尤其伦敦是旅游热点，共享出行需求很大。所以这些肯定是很值得进入、也便于向监管机构和本地居民建立信心的城市。这两座英国城市在运营侧看起来也不一样……

**[19:21 – 19:42]**
**EN:** side, because in Manchester, Vern Ransofliet, you announced that, so just like in Sacrab. And in London, you have a set who will own and operate these cars. So why a different setup in London and in Manchester? And maybe also, what kind of partner are you looking for London? Yeah, as I mentioned, right, there are four players, typically. There's us, provide the driver.
**中文：** ……因为在曼彻斯特，你们宣布由 Verne 来管车队，和萨格勒布一样；而伦敦则由另一家伙伴持有并运营这些车。为什么伦敦和曼彻斯特的架构不同？你们在伦敦找的是什么样的伙伴？——如我刚才说的，通常有四个角色。我们提供司机……

**[19:42 – 20:04]**
**EN:** Uber provides the user acquisition. So we need someone who has the capacity and the know-how to own the vehicle and essentially do the cleaning, charging, servicing, and everything else. We'll go city by city. I think every city might be different. Even on the user acquisition side, it's not just exclusive with Uber. We're actually working with others.
**中文：** ……Uber 提供用户获取。所以我们需要一个有能力和 know-how 去持有车辆、并做清洁、充电、维保等全部事情的一方。我们会逐城推进，我想每座城市可能都不一样。即使在用户获取这一侧，也并不是和 Uber 独家绑定，我们其实也在和别家合作……

**[20:04 – 20:14]**
**EN:** For example, we work with boat in Luxembourg. We'll probably in different cities, we'll pick and choose the strongest player for that market and work on it.
**中文：** ……比如在卢森堡我们和 Bolt 合作。不同城市我们大概会挑当地最强的玩家来合作。——明白。四个新城市里两座在英国，那应该还剩两座。接下来是所有听众都在等的问题……

**[20:14 – 20:38]**
**EN:** Okay, makes sense. And two of the four new cities are in the UK now. So I think that leaves two more. And now the question all of my listeners have been waiting for. So Germany has also a level four law since 2021. Actually, it's one of the first in the world. Yet there's still no driverless robot taxi service at scale here. But it's building up. So is Germany also in your list?
**中文：** ……德国从 2021 年起就有 L4 法，实际上还是世界上最早的之一，可到现在这里仍没有规模化的无人 robotaxi 服务。不过正在酝酿。德国也在你们的名单上吗？

**[20:38 – 21:09]**
**EN:** list? The short answer is yes. The more elaborate answer is that the 2021 regulation on the level four is actually a bit too complex in a way that it's without going to the nitty-gritty details. On the high level, it's actually a regulation for large-scale deployment. But we can't get there until we have a small scale first.
**中文：** ……简短的回答是：在。展开一点说，2021 年那套关于 L4 的法规，在某种意义上有点太复杂了——不谈细节，高层面上它其实是一套面向大规模部署的法规。但我们不可能在没有小规模的情况下直接跳到大规模。

**[21:09 – 21:39]**
**EN:** So essentially, Germany has a regulation for large scale, so it now needs to have more simplified regulation for kicking start level four operation. So I think the good news is that there's already an initiative and efforts to start with some of the simplified regulatory framework. So I think with that in place, We're definitely looking into entering some of the German cities.
**中文：** 所以本质上，德国有了大规模的规则，现在需要一套更简化的规则来把 L4 运营启动起来。好消息是，已经有动议和努力在做简化的监管框架。我想等它到位，我们肯定会考虑进入一些德国城市。

**[21:39 – 21:59]**
**EN:** Of course, Germany is the largest economy in Europe. Of course, that's the market that we have to enter. Sounds good. And I think that's also a good segue to the next country. And you already mentioned it. So Luxembourg, it's a smaller country. But it's where Pony Eye chose to base its European business back in 2024.
**中文：** 当然，德国是欧洲最大的经济体，这个市场我们必须进。——听起来不错。这也是聊下一个国家的好过渡，你刚才已经提到了：卢森堡，国家不大，但小马智行 2024 年就把欧洲业务放在了那里……

**[21:59 – 22:18]**
**EN:** And then in June, you launched a pilot in Luxembourg with bold and also with Stellantis. The vehicle is your Gen 7 system on the Stellantis mid-sized van and built on their level for already platform and Bolt is calling it also a living deck and the stated goal is fully driverless readiness by the end of the program. Can you also elaborate a
**中文：** ……今年六月你们在卢森堡和 Bolt、还有 Stellantis 启动了试点：把你们的 Gen 7 系统装在 Stellantis 的中型 van 上，基于他们 L4-ready 的平台，Bolt 把它也叫作 living lab，公开目标是项目结束时达到全无人就绪。你能不能展开讲讲……

**[22:18 – 22:41]**
**EN:** bit what does driverless readiness means in hard terms? Yes, so well of course one of the reasons we enter Luxembourg first is because it's relatively small and so it's a bit easier to enter from a regulatory point of view. And also we have good partners. So our goal is
**中文：** ……所谓「全无人就绪」，用硬指标说是什么意思？——好，我们最先进入卢森堡的原因之一当然是它相对小，从监管角度进入稍微容易些，而且我们有好的伙伴。所以我们的目标是……

**[22:43 – 23:14]**
**EN:** really in that test bed, we'll be able to have both technical and regulatory ready to do driverless. So that's what we are working with boat and the Atlantis to really get the vehicles to be safe enough so that it can be fully driverless. Our current fleet still with a safety operator but we will I think very soon will be able to have at least from a safety standards
**中文：** ……在这个 test bed 里，让技术和监管两端都准备好做全无人。这就是我们和 Bolt、Stellantis 一起在做的事：把车辆做到足够安全，可以完全无人。我们目前的车队仍配安全员，但我想很快，至少从安全标准的角度就能就绪了。

**[23:14 – 23:30]**
**EN:** point of view will be able to be ready. Sounds good and that brings me also to a question many European listeners have. So Pony.ai has deep roots in China, as we know, and operates in Europe. And European regulators and also cities, they always pay close attention to where vehicle data
**中文：** ——听起来不错。这也带出很多欧洲听众关心的问题：众所周知小马智行根基在中国，同时又在欧洲运营，而欧洲监管机构和城市总是很关注车辆数据流向哪里、软件由谁控制。你能讲讲在欧洲业务里怎么处理数据和控制吗？

**[23:30 – 24:00]**
**EN:** goes and who controls this software. So can you also talk a bit about how do you handle data and control in your European operations? Yes, that's a great question. I think every market that we enter into will work with the local city administrators and the local authorities of our practice. Essentially, we fully respect the data solvency issue and all the critical data
**中文：** ——这是个好问题。我们进入的每一个市场，都会和当地城市管理者、当地主管部门一起工作，按我们的做法。本质上，我们完全尊重数据主权问题，所有关键数据……

**[24:00 – 24:28]**
**EN:** will be reside in the local market. It adds to some of the operational cost, but I think that has to be something that we need to put into place. In terms of the data security, network security, and all the safety on the road, we have developed a full suite of software and the systems to guarantee that. Even on the vehicle driving itself,
**中文：** ……都会留存在本地市场。这会增加一部分运营成本，但我觉得这是必须落地的东西。至于数据安全、网络安全以及道路上的各类安全，我们已经开发了一整套软件和系统来保障。甚至在车辆驾驶本身……

**[24:28 – 24:52]**
**EN:** we actually will mask all the faces and all the street signs on the vehicle itself. So on our data, we actually not even store those data. we will denormalize and mask all those features even before we store them. And all the customer datas will strictly follow the highest security requirements and all the GDPR compliance and everything else.
**中文：** ……我们会在车端就把所有人脸和所有路牌做掩码。也就是说，这些数据我们甚至根本不存储——在存储之前就做了脱敏和掩码。所有客户数据都会严格遵循最高等级的安全要求，以及 GDPR 等全部合规要求。

**[24:52 – 25:12]**
**EN:** It adds to the complexity of our system, but that has something that we need to do and we fully respect those. Sounds good. And I think now let's leave Europe and look at also your other regions and maybe starting with the Gulf because I think this is also in region where things move really fast right now.
**中文：** 这会增加系统的复杂度，但这是我们必须做、也完全尊重的事。——明白。现在我想我们可以离开欧洲，看看其他地区，先从海湾开始，我觉得那是眼下推进特别快的区域……


## The Gulf · 迪拜与多哈

**[25:12 – 25:35]**
**EN:** So you chose Dubai and Doha and in Dubai you run driverless trials with the RGA and then also a paid service with hundreds of vehicle later this year. And can you walk us through your Middle East deployments and explain why that region is so important for your international expansion strategy? Well, I think you already partly answered the question is because the
**中文：** ……你们选了迪拜和多哈：在迪拜与 RTA 做全无人测试，今年晚些时候还会有数百辆规模的付费服务。能带我们过一遍中东的部署，并解释这个区域为什么对你们的国际化战略这么重要吗？——我想你其实已经部分回答了：因为……

**[25:35 – 26:00]**
**EN:** Middle East and the GCC region is really the area where they have a great initiative to support the deployment of autonomous driving vehicles and all the regulations are fast-tracked for this industry. So I actually I think outside of China and the US, Middle East is a region where it has already have fully
**中文：** ……中东和 GCC 地区确实有很强的意愿去支持自动驾驶车辆落地，这个行业的所有法规都是走快速通道的。所以我其实认为，在中国和美国之外，中东是已经把……

**[26:00 – 26:28]**
**EN:** driverless operation regulations in place. So I think that's part of the reason. Of course, another is because it has booming economy and high demand. So especially in Dubai. Dubai has so many initiatives to support the industry. That's why I think it's not just Pony.ai. I think a lot of other autonomous driving companies now is already there or has a plan to go there.
**中文：** ……全无人运营法规落地的地区。这是部分原因。当然另一个原因是经济繁荣、需求旺盛，尤其迪拜有大量支持这个产业的倡议。所以我想不只是小马智行，很多其他自动驾驶公司现在已经在那里，或者有计划要去。

**[26:28 – 26:54]**
**EN:** Doha is a similar thing. Doha has the initiative to support autonomous driving. Also, the local company Mova Saleh, the biggest taxi operator there, essentially turned their own fleet into autonomous. So it's a great partner to have, and they essentially helped us to enter that market. So I think the Gulf will remain to be one of the key areas we're working on.
**中文：** 多哈情况类似，也有支持自动驾驶的倡议；当地最大的出租车运营商 Mowasalat 基本上是想把自己的车队改造成自动驾驶。这是个非常好的伙伴，可以说是他们帮我们进入了这个市场。所以我想海湾会一直是我们的重点区域之一。


## The numbers · 单位经济、远程协助与盈亏平衡车队

**[26:54 – 27:20]**
**EN:** And you mentioned earlier already that you reach a unit economics break even in Guangzhou and Shenzhen. And this is important for your partners to see before they take on the vehicles on their balance sheets. But can you help us read that? So what's inside this unit economics definition and maybe also what is outside of that? The only thing outside is R&D cost.
**中文：** ——你前面提到，广州和深圳已经做到了单位经济盈亏平衡，这对让伙伴把车辆放到自己资产负债表上很重要。但能帮我们读一下这个口径吗？这个单位经济定义里装了什么，也许还有什么是被放在外面的？——放在外面的只有一样：研发成本。

**[27:20 – 27:46]**
**EN:** Because, I mean, think about it, we have 10 years of development with hundreds of close to a thousand software engineers and hardware engineers working on the software and the hardware piece of those. Put R&D aside, all the other costs are counted in the unieconomics. The major cost, of course, the biggest one is the depreciation of the vehicle.
**中文：** 因为想想看，我们开发了十年，有几百名、接近一千名软件工程师和硬件工程师在做这些软硬件。把研发放到一边，其他所有成本都算进了单位经济。最主要的成本、最大的一块，当然是车辆折旧……

**[27:46 – 28:01]**
**EN:** there will be the fuel cost, all the electricity cost, essentially what powers this. It's the insurance cost, it's the cleaning and the servicing because I mean tires need to be changed
**中文：** ……然后是燃料成本、所有电费，也就是驱动这辆车的东西；是保险成本，是清洁和维保，因为轮胎总得时不时换一次。

**[28:02 – 28:26]**
**EN:** once in a while. So all those are counted and of course there's also parking and the tolls for some of the paid roads. So all the operational costs you mentioned are already included when we calculate the unit economics. Another cost, of course, is the traffic acquisition. It's actually the user acquisition, right? If we work with, say, a company like Uber, we pay them the
**中文：** 所以这些都算进去了，当然也包含停车费，以及部分收费道路的过路费。你提到的那些运营成本，在我们计算单位经济时都已经计入。还有一项成本是……（用户获取），其实是用户获取，对吧？如果和 Uber 这样的公司合作，我们要付给他们……

**[28:26 – 28:54]**
**EN:** user acquisition. So all those costs are counted. And of course, on the revenue side, that's what the riders pay per ride, for each ride. So when we do the simple math of the taxi fare, subtract all the cost remains to be positive, then that's the positive unit economic margin. Then we think about the whole company margin, all the positive cash flow. Then essentially
**中文：** ……用户获取费。所以这些成本全都算。收入端当然就是乘客每次行程付的车费。于是做个简单算术：车费减掉全部成本，剩下的还是正数，那就是正的单位经济边际。再往上算全公司的边际、全部正现金流……

**[28:54 – 29:18]**
**EN:** the calculation is simple, right? Each vehicle, if how much we can make, and then times the number of vehicles. If those are higher than our R&D cost, then the whole company will break even. And do you have a rough estimate or number of vehicles that you need to break even on company level or something like that. We have several simple calculations. We
**中文：** ……计算也很简单，对吧：每辆车我们能赚多少，乘以车辆数；如果这个数高于我们的研发成本，那全公司就盈亏平衡了。那你们有没有一个粗略估算，公司层面盈亏平衡大概需要多少辆车？——我们有几个简单的算法……

**[29:18 – 29:49]**
**EN:** have three lines of business. If we only consider the whole company runs RoboTaxi, we need roughly 50,000 RoboTaxis for generating positive cash flow. Think about it, we have robo-trucks, which each truck can make more or less three to five robo-taxis. But to make things simpler, if we only consider taxi, it's roughly 50,000. Super interesting. And I think one part
**中文：** ……我们有三条业务线。如果只考虑全公司靠 Robotaxi 来跑，大约需要 5 万辆 Robotaxi 才能产生正现金流。想想看，我们还有 robotruck，每辆卡车大致相当于三到五辆 robotaxi 的赚钱能力。但为了简单，只算 taxi 的话，大约就是 5 万辆。——非常有意思。我觉得单位经济里还有一块……

**[29:49 – 30:18]**
**EN:** of the unit economics is also remote assistance. And I'm curious to hear, is it something that you do yourself or is it something that you source out to your partners that runs the operation, for example. If it's self-owned, we run ourselves. If it's a joint deployment model, it can be our partners. But our technical status is that we can already have one remote operator
**中文：** ……是远程协助。我很好奇，这块是你们自己做，还是外包给负责运营的伙伴？——如果是自有车队，我们自己跑；如果是联合部署模式，可以由伙伴来做。但我们的技术水平是，现在已经能做到……

**[30:18 – 30:39]**
**EN:** that looks after 30 vehicles simultaneously. So that cost is also counted in the unique economics as well. Maybe now let's zoom out from Pony. I for the last part of this conversation and talk a bit about the industry, because I think also a lot of listeners are investors and other strategy people and your CTO, Tian Cheng
**中文：** ……一名远程操作员同时照看 30 辆车。所以这笔成本也计入了单位经济。——也许最后这部分我们把镜头从 Pony 拉远一点，聊聊行业，因为很多听众是投资人和战略岗。你们的 CTO 楼天城说……


## The industry · Pony World、商品化之问与 2027

**[30:39 – 31:01]**
**EN:** Lo, says that Pony World 2.0, your world model, lets you launch in several countries at once without adding engineers in the same proportion. So can you tell us a bit what this world model gives you that maybe also real world models cannot? So think about, on a high level, when we need to launch in the city, we need to deploy those
**中文：** ……Pony World 2.0 这个世界模型，让你们能同时在好几个国家上线，而不用同比例增加工程师。能讲讲这个世界模型给了你们什么、是真实道路给不了的吗？——往高层面上想，我们要在一座城市上线，就得把车部署过去……

**[31:01 – 31:31]**
**EN:** vehicles and to verify the safety, while the world model is a simulation and verification system where we can let the vehicles drive there many, many times. On the railroad, we test 10 times. In the pony board, we can run say thousands of times. So that's the reason where especially the pony board has very high fidelity, meaning
**中文：** ……并验证安全性；而世界模型是一套仿真与验证系统，可以让车在那里跑很多很多次。实路上我们测 10 次，在 Pony World 里可以跑比如几千次。这就是为什么，尤其 Pony World 的保真度非常高……

**[31:31 – 32:00]**
**EN:** that we can use that to simulate and also to really count for all kinds of edge cases that happened in the railroad. So whenever we launch in the new city, we can put some of the new scenarios. For example, as we mentioned, Zagreb, roundabouts. So in our word model used to be that there are not that many roundabouts. So now we're putting more roundabouts in our word model,
**中文：** ……意味着我们可以用它做仿真，也能真正覆盖实路上发生过的各类边缘案例。所以每当进入一座新城市，我们可以把新场景放进去——比如刚才提到的萨格勒布环岛：我们的世界模型里过去没有那么多环岛，现在就往里加更多环岛……

**[32:00 – 32:27]**
**EN:** then have the vehicles trained there with very high fidelity and high efficiency. So that's the reason. Besides that, we can have all the verification down there as well. And then we just need the vehicle to be run on the real world for the final verification. So think about this as an engineering tool and as a simulation framework where
**中文：** ……然后让车辆在里面以很高的保真度和效率训练，验证也可以在那里全部完成，最后只需要车在真实世界跑一遍做最终确认。可以把它理解为一套工程工具和仿真框架……

**[32:27 – 32:52]**
**EN:** we can greatly simplify the amount of work that needs to be done whenever we need to launch a new vehicle or a new version of the software. So it's a great tool to really make everything to be faster and simpler. Yeah, it's super interesting. And there's also one narrative I read a lot when I read about virtual driver companies and also Uber.
**中文：** ……它能大幅简化每当我们上线一款新车或一个新软件版本时所需的工作量。所以它是个能让一切更快、更简单的好工具。——确实非常有意思。还有一个叙事我读到很多次，是关于虚拟司机公司和 Uber 的……

**[32:53 – 33:12]**
**EN:** And the narrative is that Uber has partnered with a lot of companies right now, probably 30 autonomous driving companies with me, right by Waymo. And everyone is also pushing into Europe or into the Middle East. And the fear is that if the platform works with everyone, maybe the virtual driver could also become a commodity. Can you give us your views on that?
**中文：** ……这个叙事是：Uber 现在已经和很多公司合作了，大概 30 家自动驾驶公司（包括 Waymo 在内），大家也都在往欧洲或中东推。于是有人担心，如果平台和所有人都合作，虚拟司机是不是也会变成大宗商品。你怎么看？

**[33:12 – 33:39]**
**EN:** Yeah, I think the state of the art is that every company's virtual drivers still are quite different in terms of their safety, in terms of the cost and in terms of the capability. So, if everyone has relatively similar capability, safety track record, and cost, I think your statement is true. It becomes a commodity.
**中文：** ——我想，目前的技术现状是，各家公司的虚拟司机在安全性、成本、能力上仍然相当不同。所以，如果大家的能力、安全记录、成本都比较接近，你这句话是成立的，它会变成商品……

**[33:39 – 34:07]**
**EN:** Because essentially that means Uber will be able to freely choose whichever vehicle to send the request to. Because every company's cost actually are still quite different. For example, our vehicle's per mile cost is actually a lot lower in the case compared with Waymo can be like three to five times cheaper. Also, the capabilities important because the city is very diverse.
**中文：** ……因为那意味着 Uber 可以自由地把请求派给任意一辆车。但各家成本其实还差得很远。举个例子，我们车辆的每英里成本要低得多，跟 Waymo 相比可以便宜三到五倍。能力也很重要，因为城市非常多样……

**[34:07 – 34:28]**
**EN:** There's narrow road, there are, as I mentioned, roundabouts, the trams, and all that. So having the ability to go everywhere, that means I can take on all the right requests come from Uber. So I think at least in the foreseeable future, we can still see there's huge difference between different autonomous driving companies.
**中文：** ……有窄路，有我提到的环岛、有轨电车等等。所以拥有哪儿都能去的能力，就意味着我能接下从 Uber 过来的所有订单。我想至少在可预见的未来，不同自动驾驶公司之间仍会存在巨大差异。

**[34:28 – 34:56]**
**EN:** And certainly, Pony.ai has an edge on cost, on capability, and especially on safety track record. That will be able to actually take on a much bigger share. Of course, you can see, well, in 20 years, maybe everyone will be up similar and then become a commodity, maybe. But at least I think in the next many years, we'll still have a huge edge. Now, let's end with looking ahead.
**中文：** 而小马智行在成本、能力、尤其是安全记录上肯定有优势，这能让我们拿到大得多的份额。当然你可以说，二十年后也许大家都差不多了，然后变成商品，也许吧。但至少我认为在未来很多年，我们仍然有巨大的优势。——最后我们来看看前方……

**[34:56 – 35:20]**
**EN:** So we already talked about the goals for this year, more than 3,500 robot taxis and over 20 cities, and you said, you're good to hit that target at the end of the year, and let's say you hit the target. So what is Pony.ai's number one priority then for 2027 and also what milestones would make you say at the end of the next year, 27 was a great success year for Pony.ai?
**中文：** ……我们已经聊了今年的目标：3,500 辆以上 robotaxi、20 座以上城市，你说年底能达成。假设达成了，那小马智行 2027 年的第一优先级是什么？以及什么样的里程碑，会让你在明年年底说「27 年对小马智行是很成功的一年」？

**[35:20 – 35:48]**
**EN:** I think for us, as I mentioned in several occasions, the most important goal is still the scale up. So as you already mentioned, the size of our fleet will be one of the important factors that we track. Our goal is hopefully we'll be at least maintaining a doubling speed every year or hopefully we could be even bigger or higher than that.
**中文：** ——我想，正如我在好几个场合说过的，最重要的目标仍然是规模化。你刚才也提到，车队规模会是我们追踪的重要指标之一。我们的目标是希望至少维持每年翻倍的速度，或者最好比这更快、更高。

**[35:48 – 36:17]**
**EN:** So that is one of the factors we're tracking. Of course, at the same time, what's the unit economic margin is another important indicator. Because one of the cases we can flop the market, but then the margin becomes squeezed. That won't be a good case to enter into. So I think the scale and the unit margin will be the most important factors that I'm looking at. Sounds good.
**中文：** ……这是我们在追踪的因素之一。当然与此同时，单位经济边际是另一个重要指标。因为有一种情况是我们把市场冲下来了，但边际被挤薄了，那就不是一个值得进入的好局面。所以我认为规模和单位边际，是我最看重的两个因素。——说得通。

**[36:17 – 36:33]**
**EN:** We are at the end and James, I thank you so much for taking the time today and sharing all your insights into Pony.ai. It was a pleasure to have you on and I'm really looking forward to see what Pony.ai's next announcements are and I'm really following closely because I think it's a great
**中文：** 我们到最后了。James，非常感谢你今天抽出时间，分享关于小马智行的这些洞察。很高兴请到你，我也真的很期待小马智行接下来的公告，会一直密切关注，因为我觉得这是一家很……

**[36:33 – 37:02]**
**EN:** company so thank you so much and see you soon. Daniel, thanks for having me and certainly as I mentioned, Europe is a great market to be into and each year I have at least two to three trips in Europe to many cities. Actually, I just got back from Europe and it's a great continent to be in and hopefully some of the listeners will have the opportunities to ride in our vehicles
**中文：** ……棒的公司，非常感谢，回头见。——Daniel，谢谢邀请。当然正如我说的，欧洲是一个非常值得投入的市场，我每年至少会去欧洲两三趟、跑很多城市。其实我刚从欧洲回来，这是个很棒的大陆，希望有些听众很快就有机会坐上我们的车……

**[37:02 – 37:10]**
**EN:** very soon and we are really working on that very hard to hit that goal. Yeah, really looking forward to that. Thank you.
**中文：** ……我们真的在非常努力地朝这个目标推进。——是的，非常期待。谢谢。

