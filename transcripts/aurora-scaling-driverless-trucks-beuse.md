# 中英对照逐字稿 / Bilingual Transcript

**Episode:** Scaling Driverless Trucks Safely with Aurora CSO Nat Beuse **节目：** 与 Aurora 首席安全官 Nat Beuse 谈无人卡车如何安全规模化 **Source / 来源：** The Driverless Digest · Substack **Guest / 嘉宾：** Nat Beuse（Aurora 首席安全官；前 Uber ATG 安全负责人、前 NHTSA 车辆安全研究副局长）；主持人 Harry

> 说明：英文为音频全文听写稿（机器识别后经人工校对专有名词与断句），中文为逐段翻译。时间戳为音频位置，章节划分依据访谈内容。

## 一、开场：行业的问题变了 / Cold open

**[00:00]**
**EN:** **Nat Beuse 0:00** Crashes have become normalized here in the US and we're actually in a crisis. And the sad thing about all of this is it's mostly preventable.
**中文：** **Nat Beuse 0:00** 在美国，车祸已经被常态化了，我们其实处在一场危机里。而这一切最让人难过的地方是——它**大部分是可以预防的**。

**[00:13]**
**EN:** **Nat Beuse 0:13** The AV companies are actually collaborating in a way that is quite, quite impressive. The questions that they used to have — like, how do you know that you've done it enough — have now shifted more towards scale, and like how many trucks are coming and when. So it's really interesting to see that transition, from "can you guys actually really do this" to "hey, when are we going to see some more trucks."
**中文：** **Nat Beuse 0:13** AV 公司之间的协作程度其实相当、相当惊人。他们过去会问"你怎么知道你做够了"，现在这个问题已经转向「规模」了——「你们有多少台卡车、什么时候到」。从"你们真能干成这事吗"到"嘿，我们什么时候能看到更多车"，这个转变很有意思。

**[00:00 – 00:32]**
**EN:** [Sponsor read 0:32 – 1:37 — Terawatt, AV fleet charging. Content omitted.]
**中文：** **主持人 0:32** （赞助商口播：本期由 Terawatt 赞助，为自动驾驶车队提供专用充电枢纽，98% 充电桩可用率。内容略。）

## 二、嘉宾背景：从碰撞假人到 NHTSA，再到 Aurora / Background

**[01:38]**
**EN:** **Harry 1:38** Nat Beuse is the Chief Safety Officer at Aurora, the company delivering the benefits of self-driving technology safely, quickly and broadly. Nat leads the development and implementation of Aurora's holistic safety approach and played a primary role in the launch of Aurora's commercial autonomous trucking service. Prior to Aurora, Nat led the safety team at Uber Advanced Technologies Group, or ATG, and he also served as the Associate Administrator for Vehicle Safety Research at the National Highway Traffic Safety Administration, or NHTSA. Nat, how are you doing today?
**中文：** **主持人 1:38** Nat Beuse 是 Aurora 的首席安全官。Aurora 的使命是"安全、快速、广泛地交付自动驾驶技术的价值"。Nat 负责 Aurora 整体安全方法的制定与落地，并在 Aurora 商用无人卡车服务的上线中起了主导作用。在 Aurora 之前，Nat 在 Uber ATG 领导安全团队，也曾在 NHTSA（美国国家公路交通安全管理局）担任车辆安全研究副局长。Nat，今天感觉如何？

**[02:09]**
**EN:** **Harry 2:09** You've got a long and interesting tenure in the self-driving and auto mobility space. I feel like a lot of executives in autonomous vehicles come from either Waymo or other trucking or Uber or Lyft, and I guess you have a little bit of that. But let's talk a bit about your background before we dive into Aurora. You were 11 years with the US DOT and NHTSA, and then you were with Uber and now at Aurora. So talk to me about your background and how you finally found yourself in the AV trucking space at Aurora specifically.
**中文：** **主持人 2:09** 我注意到自动驾驶行业的高管大多来自 Waymo、卡车公司、Uber 或 Lyft，你身上有一点这些。但先聊聊你进入 Aurora 之前的背景——你在美国交通部（USDOT）和 NHTSA 待了 11 年，然后去了 Uber，现在在 Aurora。说说你是怎么走到 AV 卡车这条路上的。

**[02:44]**
**EN:** **Nat Beuse 2:44** Harry, great question, and again thanks for having me. What I would start to say is I've been a safety guy basically my entire career, and I took a bit of a tortured path to actually end up in self-driving.
**中文：** **Nat Beuse 2:44** Harry，好问题，谢谢你邀请我。我想说，我基本上**整个职业生涯都是个"搞安全的"**，走到自动驾驶这条路算是有点曲折。

**[02:59]**
**EN:** **Nat Beuse 2:59** As you pointed out, I spent a fair number of years in the federal government after I left grad school. One of the interesting things for me was my whole training and education was really on "assume someone got injured and is broken in a very bad way." I was actually pursuing a career more on the prosthetic side — making people whole again and repairing them. And so when I got to the agency, to NHTSA, I actually started my career working on crash test dummies — basically pieces of metal, plastic and sensors that we were building to try to replicate human injury in crashes, to try to figure out how to mitigate those. It was a great job and I did that for a couple of years.
**中文：** **Nat Beuse 2:59** 我研究生毕业之后在联邦政府待了不少年。有意思的是，我受的全部训练其实是围绕"假设有人受伤了、而且伤得很重"——我本来想走假肢方向，把人修复完整。所以刚进 NHTSA 的时候，我职业生涯的第一站是**做碰撞假人**：一堆金属、塑料和传感器，我们造它们来复现人体在碰撞中的伤害，然后想办法减轻伤害。那份工作很棒，我做了几年。

**[03:53]**
**EN:** **Nat Beuse 3:53** And then there was this little new technology — and I should put "new" in air quotes — called electronic stability control, where, much like the seatbelt, it was going to have this huge dramatic effect on crash reduction and fatalities. So I transitioned out of basically protecting people in crashes and assuming the crash is going to happen, to "hey, maybe there's a world where these crashes don't happen at all." I started to get super deep into crash avoidance technologies and then went into what we all now call ADAS — but back in the day we didn't really know what to call them, we just gave them all these little individual names.
**中文：** **Nat Beuse 3:53** 然后出现了一个"新"技术——我得给"新"加引号——叫**电子稳定控制（ESC）**。它像安全带一样，当时被认为会对减少碰撞和死亡产生巨大的效果。于是我从"假设碰撞一定会发生、去保护人"，转到"嘿，也许存在一个碰撞根本不发生的世界"。我开始深入做碰撞避免技术，后来就是我们现在说的 ADAS——当年我们甚至不知道该叫什么，只能给它们起一堆各自的小名字。

**[04:35]**
**EN:** **Nat Beuse 4:35** And then there was this group of folks — one guy named Chris Urmson in particular — who were working on this self-driving car out in California. I was still at the agency back then, and it was really an aha moment for me to say, wow, we actually might be able to do self-driving in a real way. Part of my journey there was helping the nation prepare for it.
**中文：** **Nat Beuse 4:35** 后来有一群人——特别是 **Chris Urmson**——在加州搞自动驾驶汽车。我当时还在政府里，那对我来说是一个真正的顿悟时刻：哇，我们也许真的能把自动驾驶做出来。所以我那段旅程的一部分，是帮这个国家为它做好准备。

**[05:14]**
**EN:** **Nat Beuse 5:14** But then I decided that maybe there was some good I could do on the outside, so I left the government and went over to Uber ATG to really help them after they had their crash.
**中文：** **Nat Beuse 5:14** 但后来我觉得在外面也许能做更多好事，就离开政府去了 Uber ATG——尤其是在他们出了那起事故之后去帮忙。

**[05:15]**
**EN:** **Nat Beuse 5:15** And then things come full circle — we acquired Uber ATG. I couldn't be happier to work with Chris and the team. It's kind of like being part of the dream team of self-driving at the time, because the three co-founders were still here and it was just a great place for me to land.
**中文：** **Nat Beuse 5:15** 然后事情就圆回来了：Uber ATG 被收购（注：被 Aurora 收购），我特别高兴能和 Chris 和团队一起工作。三位联合创始人当时都还在，对我来说那是个很棒的落脚点。

**[05:39]**
**EN:** **Harry 5:39** That's very cool. I just watched an interview with Chris Urmson and Dave Ferguson from Nuro — old buddies talking about their early days at Waymo. I like the way you put it, that dream team of self-driving; I'm thinking Avengers now. But it's interesting because you came at it from the regulator's side — you were probably chatting with Waymo in those early days.
**中文：** **主持人 5:39** 很酷。我刚看了 Chris Urmson 和 Nuro 的 Dave Ferguson 的一场对谈，两个老友聊他们早年在 Waymo 的日子。你刚说的"梦之队"这个说法很有意思——我脑子里现在想的是复仇者联盟。不过有趣的是，你是**从监管方走过来**的，早期大概还在跟 Waymo 打交道。

**[01:38 – 05:39]**
**EN:** One thing you said stood out to me: early on you were working on crash test dummies and mitigating injuries, but AV is actually about avoiding crashes in the first place. So tell me how you think about crashes versus just your general safety philosophy, and what you've learned over the years from your time in government and Uber and now at Aurora.
**中文：** 你说你早期做碰撞假人、做伤害减轻，我觉得你是我听过的第一个把这段经历带到 AV 语境里的人。但 AV 其实是**从一开始就避免碰撞**。说说你怎么看"碰撞"这件事，以及你这么多年在政府、Uber、Aurora 积累下来的安全哲学。

## 三、安全哲学：车祸被常态化了，而它本可预防 / Safety philosophy

**[06:37 – 09:18]**
**EN:** **Nat Beuse 6:37** I would say crashes have become normalized here in the US and we're actually in a crisis. **Nat Beuse 6:47** We lose something like 40,000 people a year — and when I say lose, I mean fatal crashes. There are many more traffic crashes, something like over 6 million a year. **Nat Beuse 6:57** And I think what we're not good at understanding in all of that is the toll that comes not just to the human body but to the humans involved. When it's a fatality, that's a sudden loss of light, unexpected, and families suffer, there's mental anguish. **Nat Beuse 7:17** I know a lot of people who have been in injuries — it's recurring medical costs, having to go to the doctors, maybe you don't even get your full range of motion back. And the sad thing about all of this is it's mostly preventable. When you look at the numbers, the numbers tell a story: we as humans get distracted, some of us drink and drive, some of us speed, and all of those things are preventable. **Nat Beuse 7:52** And when you think about AV and AV safety, the computer doesn't do any of those things. It's just focused on the tasks at hand — which is, looking around. In our case it's got near 360-degree view, it's looking in all directions to watch what other actors are doing, and it's just driving. **Nat Beuse 8:13** That's something I would like to see: a future world where the number of crashes is greatly reduced. I mentioned electronic stability control — that was 12,000 fatalities a year, give or take, that we were estimating would be mitigated. AVs have so much more potential to do that in a much, much different way. **Nat Beuse 8:38** I think one of the things I've learned along the way is you have to approach this particular technology in a completely different way. This technology is going to be interacted with every day, unlike something like electronic stability control. So there's a burden that comes with it: being more transparent in what you're doing on safety, being more holistic in what you're doing about safety. **Nat Beuse 9:00** Because the public will see it doing its thing in the wild, whereas other technologies are very simple and hang around in the background and only occur when the bad event happens. This has to do the driving all the time. So I think there is a higher bar here in terms of what you have to do. **Harry 9:18** That's a good point. Airbags and seatbelts are within the car; they keep the passenger or the driver safe, they don't really affect other road users. But obviously with AVs, if there's a crash or an incident it affects everyone around it and maybe society at large. So definitely important topics, and a lot of potential here for safer streets. Before we start diving into the nitty gritty around safety in your day to day, let's talk about Aurora, starting with your driverless trucking rollout today. I think you're one of the few companies in the space that have actually removed the driver — and for people who read my newsletter, they know that's a big bar for me. I always like to talk about it because I'm not an expert on the tech, but I know when there's a driver or not a driver. So I'd love to talk about your operations and what you guys have done so far.
**中文：** **Nat Beuse 6:37** 我会说，在美国，车祸已经被常态化了，我们确实处在一场危机中。 **Nat Beuse 6:47** 我们每年失去大约 **4 万人**（指致命事故），还有多得多的交通碰撞——一年超过 **600 万起**。 **Nat Beuse 6:57** 我认为我们不太擅长理解的是：这一切对人付出的代价，不只是身体的，也是人的。如果是死亡，那是"灯突然灭了"，是意料之外的，家庭会承受巨大的精神痛苦。 **Nat Beuse 7:17** 我认识很多人受过伤，是那种反复发生的医疗支出、要不停看医生、可能再也恢复不到完整的活动范围。 而这一切最让人难过的是——**它大部分是可以预防的**。看那些数字，它讲的故事是：我们人类会分心，有些人喝酒开车，有些人超速——**这些都是可预防的**。 **Nat Beuse 7:52** 当你想到 AV 和 AV 安全：计算机不做这些事。它就是专注于手上的任务——在我们的例子里，是接近 360 度的视野，看着各个方向、观察其他交通参与者在做什么，然后就是开车。 **Nat Beuse 8:13** 我希望看到一个碰撞数量大幅下降的未来。我提过 ESC 那个故事：每年大约 1.2 万人的死亡被估算能被它减轻。AV 在这件事上的潜力要大得多，而且是以一种完全不同的方式。 **Nat Beuse 8:38** 但我一路学到的其中一件事是：你必须用一种**完全不同的方式**来对待这项技术。它每天都和人发生交互，不像 ESC。所以这里有一种负担：你必须**在安全上更透明、在安全上更整体**（holistic）。 **Nat Beuse 9:00** 因为公众会看到它在真实世界里"干活"，而其他技术很简单、待在背景里，只在坏事发生时才出现。而这项技术必须**一直**在开车。所以这里的门槛更高。 **主持人 9:18** 说得好。安全气囊、安全带是在车内的，保护乘客或司机，不影响其他人。但 AV 一旦出了事故或事件，会影响周围所有人，甚至整个社会。所以这个话题很重要，这里的潜力也很大——更安全的街道。 在深入安全的日常细节之前，先聊 Aurora，从你们的无人卡车落地讲起。你们是这个行业里少数**真的把司机撤掉**的公司之一。对我的读者来说，这是个很高的门槛——我不是技术专家，但我知道车上有司机还是没司机。所以想听你讲你们的运营和到目前为止做了什么。

## 四、安全案例：把"什么时候可以撤人"变成可证明的东西 / The safety case

**[10:17]**
**EN:** **Nat Beuse 10:17** Yeah, it's been awesome. When I think about the journey I've been on — I've been in this space a long time — for me this is really things coming full circle, in the sense that we came up with a framework that allowed us to determine when it was okay to remove that safety driver from that driving seat. That's something we call the safety case.
**中文：** **Nat Beuse 10:17** 很棒。想到我走过的这段路——我在这个领域很久了——对我来说这真是"圆满"。因为我们确实做出了一套框架，用来判断**什么时候可以把安全员从驾驶座上撤掉**。我们把它叫做**安全案例（safety case）**。

**[10:48]**
**EN:** **Nat Beuse 10:48** You can think of the safety case as all of the pieces of evidence that need to be put together to make the ultimate argument that we're safe to be on public roads without somebody behind the wheel. So you can imagine all the engineering work, all the operational work that people tend to overlook, all the work around what needs to happen when an incident does occur — all of those things have to be part of your overall safety case framework.
**中文：** **Nat Beuse 10:48** 你可以把安全案例理解成：把所有证据拼在一起，最终论证"我们在没有人在方向盘后面的情况下上公共道路是安全的"。所以你可以想象，所有工程工作、所有运营工作——人们常常忽略这部分——所有"一旦发生事件该怎么办"的工作，都必须成为这套安全案例框架的一部分。

**[11:36]**
**EN:** **Nat Beuse 11:36** We closed ours in April of last year, so for well over a year now we've been operating in driverless mode on public roads. Today we have 10 routes that are driverless validated, and we also just announced not that long ago our new fleet of International trucks that have no human behind the wheel, and they're starting to ramp up in numbers.
**中文：** **Nat Beuse 11:36** 我们在**去年 4 月**关闭了（closed）我们的安全案例。所以到现在，我们已经以无人模式在公共道路上运营一年多了。今天我们已经有 **10 条通过无人验证的路线**，而且不久前刚宣布了我们新的国际卡车车队，车上完全没有人类，数量也开始往上走。

**[11:37]**
**EN:** **Nat Beuse 11:37** Overall things are going quite well. I'm sleeping very good at night — the truck is doing what it's supposed to be doing. We are very proud of our safety record. And my conversations, whether with government or even with our insurance carriers or members of the public — the questions they used to have, like "how do you know that you've done it enough," have now shifted more towards scale and "how many trucks are coming and when."
**中文：** **Nat Beuse 11:37** 整体进展相当不错。我晚上睡得很好——卡车在做它该做的事。我们对自己的安全记录很自豪。而且我发现，无论是和政府、和我们的保险承保方、还是和公众的对话，他们过去会问"你怎么知道你做够了"，现在更多转向**规模**和"多少台车、什么时候"。

**[12:07]**
**EN:** **Nat Beuse 12:07** So it's really interesting to see that transition, from "can you guys actually really do this" to "hey, when are we going to see some more trucks." It's been a fantastic journey, and this is a great team that's been delivering release after release. Now we're kind of oiling up the machine to meet [demand] — software releases have to go out on the road, we have to put new product features in — and watching that machinery turn over and over has been really awesome to see.
**中文：** **Nat Beuse 12:31** 所以这个转变特别有意思。这是一支很棒的团队，一个版本接一个版本地交付。现在我们在给这台机器"上油"，让软件版本能上路、把新功能装进去，看着这套机械装置一遍又一遍运转，真的很棒。

**[12:42]**
**EN:** **Harry 12:42** That's cool to see, and it must be rewarding for you and the team. So 10 routes — are they all in Texas and on public roads? What are some of the stats, how many vehicles, what are they carrying? What can you share there?
**中文：** **主持人 12:42** 听起来很有成就感。那 10 条路线都在德州吗？都在公共道路上？能分享一些数据吗——多少台车、运什么？

## 五、事实与数字：10 条路线、跨州、运什么的都有 / Facts and figures

**[12:56]**
**EN:** **Nat Beuse 12:56** All sorts of things. It's one of the interesting things about being in this space — there's not just one type of goods to carry. There's everything from frac sand that we're carrying in the Permian Basin to berries.
**中文：** **Nat Beuse 12:56** 什么都运。这是这个领域有意思的地方——不是只有一种货。我们在二叠纪盆地（Permian Basin）运**压裂砂**，也运**浆果**。

**[12:56 – 15:32]**
**EN:** And you mentioned where these routes are — that's one of the misconceptions, that people think we're only in one place. We're actually not; we're in a couple of different states now with approved driverless routes, whether that be New Mexico, Texas, Arizona.
**中文：** 关于路线在哪，有一个常见误解是"你们只在一个地方"——其实不是。我们现在在**好几个州**都有获批的无人路线：墨西哥（注：指新墨西哥州，或跨墨西哥边境路线）、德州、亚利桑那。

**[13:30]**
**EN:** **Nat Beuse 13:30** In fact I was having breakfast this morning with a colleague who went down to Phoenix for a family thing, and he said, "Hey Nat, I saw one of your trucks down there" — and it really shocked him because he didn't expect to see it. So it's kind of cool to have that validation that people are seeing our trucks.
**中文：** **Nat Beuse 13:30** 事实上，今天早上吃早饭时，一个同事说他去凤凰城探亲，说"嘿 Nat，我在那儿看到你们一台卡车"，他特别震惊，因为他没预期会看到。这种"人们真的看到我们的车在路上跑"的验证感很酷。

**[14:00]**
**EN:** **Nat Beuse 14:00** I would say a year from now, or even six months from now, if you go anywhere down in the southern belt, you'll be hard pressed not to see one of our trucks just doing good in the world. We're continuing to expand the type of goods — they're wide and varied — and it's been really great to see the product do its thing in the wild.
**中文：** **Nat Beuse 14:00** 我想说，从现在起六个月、一年之后，如果你去南方的阳光地带（Sun Belt）任何地方，你很难不看到我们的一台卡车在那儿跑。我们在持续扩展承运的货物类型，种类非常宽、非常杂，看到产品在真实世界里干活，真的很棒。

**[14:15]**
**EN:** **Harry 14:15** Do all of these routes have no one behind the wheel? Do some of them have what I think are called safety observers in the cab? What's the breakdown?
**中文：** **主持人 14:15** 那这些路线是不是都是车里没人？有些是不是有所谓的"安全观察员"坐在驾驶室？

**[14:25]**
**EN:** **Nat Beuse 14:25** When we say driverless, we truly mean driverless. Nobody in the cab, no one behind the wheel.
**中文：** **Nat Beuse 14:25** 当我们说无人，我们就是**真的无人**——驾驶室里没有人，方向盘后面没有人。

**[14:32]**
**EN:** **Nat Beuse 14:32** For some of the routes there is something we call a rapid recovery person — that's more of an operational facility kind of thing, because we're working on some bigger contracts to allow at scale. Everything has to operate at scale.
**中文：** **Nat Beuse 14:32** 对某些路线，我们有一个叫"快速恢复（rapid recovery）"的人员——但那更多是运营设施层面的事，因为我们在谈一些更大的合同、要支持规模化。所有事情都要能规模化地运转。

**[14:51]**
**EN:** **Nat Beuse 14:51** That person, that center, is doing no safety function at all. That's the whole purpose of closing the safety case. And those International trucks I mentioned actually have nobody in there at all.
**中文：** **Nat Beuse 14:51** 那个人、那个中心**不承担任何安全功能**——这正是"关闭安全案例"的意义所在。而我刚提到的那些国际卡车，车上根本没有人。

**[15:03]**
**EN:** **Nat Beuse 15:03** The Tesla Cybercab has a safety driver in the [cab], though they have a stop and a start button, so they don't have a lot of functionality but they do have something. It can be confusing sometimes, because every company — and there's a marketing aspect on the more consumer-facing robotaxi applications too.
**中文：** **Nat Beuse 15:03** 相比之下，特斯拉 Cybercab 的驾驶座上是有安全员的，虽然他们只有一个启动和停止按钮、功能不多，但确实有东西——有时候这会造成混淆，因为每家公司在面向消费者的 Robotaxi 应用上都有营销层面。

**[15:20]**
**EN:** **Nat Beuse 15:20** We've been very transparent about what we're doing and very clear about the roles of those folks. I go back to what it takes to close the safety case. When we closed the safety case, there was none of this "oh well, this is good enough, but wink wink, nod nod, we have somebody in there." We did not allow ourselves to go down that path. It was really truly — we put our CEO in the back of the truck.
**中文：** **Nat Beuse 15:20** 但我们一直非常透明，也非常明确地说明那些人的角色。回到"关闭安全案例需要什么"——我们关闭的时候，没有那种"差不多就行了吧，眨眨眼我们其实留了个人在里面"。我们不允许自己走那条路。真的是——我们把我们的 CEO 放进了卡车后厢（指首次无人运行的演示）。

**[15:46]**
**EN:** **Nat Beuse 15:46** People might remember that on that first inaugural run. People would have come after me if we were just doing that, just hoping that it gets there.
**中文：** **Nat Beuse 15:52** 你知道，如果我们只是那样做、只是"希望它能到"，人们会来追着我打的。

## 六、怎么关闭安全案例：需求 → 测试 → 政策 → 运营 / Closing the safety case

**[15:56 – 19:16]**
**EN:** **Harry 15:56** What did it take to close the safety case, and what were the objective measures you were looking at? **Nat Beuse 16:04** A couple of things. We had to make sure we understood the environment we were going to deploy the product in — the industry jargon is the ODD, the operational design domain: where is this truck going to operate in the wild. **Nat Beuse 16:18** You decompose that into requirements, and then requirements have associated tests to show that you meet those requirements. So there was a lot of work on building those requirements, building those tests, and of course the Aurora driver has to pass those tests. **Nat Beuse 16:41** But there were other aspects. We had to make sure we had the right safety policies in place to enable issues to be raised and adjudicated. We had to make sure we had the operational aspects nailed down — I've been known to say a self-driving truck can't do any good if it doesn't know how to operate, doesn't have the operational piece around it. So you look at it as an accumulation of different aspects of safety to close that overall safety case. **Nat Beuse 17:16** To me the more interesting question then is: OK, how do you do that for the next version of software? There we got very sophisticated and are able to look at the claims that are impacted every time we change a piece of code or go to a new route, so that we don't have to repeat all the things all over again. You can start to get very surgical with what needs to change in that safety case, because every time you do a new version it's essentially a new safety case — you'll have new requirements, new tests, new things happen. **Nat Beuse 17:48** One of the things we did that you might find interesting: we recently had someone look at and evaluate our safety case from an independent lens, and they also looked at it from the lens of the guidance that I and some other folks wrote way back when we were in government. They said these folks have a really good safety case — it's comprehensive, it's complete, it has all the right pieces, and it also exceeds the guidance that the government has handed out. **Nat Beuse 18:52** So that's an extra version of validation to show there was no cutting corners — safety is built in from the foundation, from the early days of the company when Chris, Sterling and Drew founded it, to make sure safety is in every part of what we do. **Nat Beuse 18:53** Industry was full of demos way back in 2016 and 2017. **Nat Beuse 19:00** You can't scale a demo. You can only scale a product. And that's what the safety case actually allows us to do — it's not like we did it one time and then we're going to put the driver back in and hope everything works. No, when we closed that thing it was like: we're doing this. Real. It's done.
**中文：** **主持人 15:56** 关闭安全案例需要什么？你在看哪些客观指标？ **Nat Beuse 16:04** 几件事。首先，我们必须搞清楚要把产品投放到什么环境里——行业术语叫 **ODD**，运行设计域，这台卡车要在真实世界的哪里跑。 **Nat Beuse 16:18** 然后你把它**分解成需求**，需求对应**测试**，用来证明你满足这些需求。所以这里有大量工作：建立需求、建立测试，然后车必须通过这些测试。 **Nat Beuse 16:41** 但这只是一个方面。还有别的：我们必须有正确的**安全政策**，让问题能被提出、被裁定；我们必须把**运营**层面敲定——我常说，一台自动驾驶卡车如果不知道怎么运营，就毫无价值。 **Nat Beuse 17:16** 所以你是从多个不同的安全层面累积起来，最终关闭整个安全案例。对我来说更有意思的问题是：**下一个软件版本怎么办？** **Nat Beuse 17:16** 在这件事上我们变得非常成熟——每次改一段代码、或去一条新路线，我们能看出哪些"主张（claims）"会受影响，这样就不必把所有事情重做一遍。你可以非常精准地做外科手术式的调整。 因为每个新版本本质上都是一个新的安全案例——会有新的需求、新的测试、新的情况发生。 **Nat Beuse 18:15** 还有一件事你可能会觉得有意思：我们最近请人**独立评估**了我们的安全案例，他们同时用"我当年在政府时和一些人写的指导文件"这个视角来看。他们的结论是：这些人有一套 realmente 完整、全面的安全案例，包含所有正确的组成部分，而且**超出了政府给出的指导要求**。 **Nat Beuse 18:52** 这算是额外的验证——证明我们没有走捷径，安全是从地基里就建进去的，从 Chris、Sterling、Drew 创立公司的最早期就是如此。 **Nat Beuse 18:53** 而且你大概会认同这一点：2016、2017 年那会儿，这个行业到处是 Demo。 **Nat Beuse 19:00** **Demo 是没法规模化的。能规模化的只有产品。**而安全案例恰恰让我们能做到这件事——不是"我们做了一次，然后就把司机放回去、希望一切正常"。不，当我们关闭它的时候，就是"我们在做这件事，是真的，完成了"。

## 七、ODD：从"白天、单路线、好天气"到逐步解锁 / ODD and business model

**[19:16 – 22:11]**
**EN:** **Harry 19:16** What is the ODD that the Aurora Driver is validated for, and that has to line up with the business model too — where these trucks are going to be operating. Can you talk about that intersection? **Nat Beuse 19:31** Great question. I'll describe it in three different ways. The first is: what does the technology need to do? When we first started we were following a crawl, walk, run approach — we only did daytime, we only did one route, it had to be clear conditions. Very good product, but maybe not very useful for a customer. **Nat Beuse 19:55** (Harry: though in some places that describes every day.) But very few places — definitely not here in Pittsburgh. Over the course of time we've added new capabilities: night, weather. And again, we were driving in all those things before, but we hadn't validated it for driverless operations. So that's been the transition — keep unlocking all of these features for driverless application. **Nat Beuse 20:27** The second is the model we're in: what's called transportation as a service. In that model Aurora is doing all of the things. The reason we need to do that, frankly, is so we can learn the hard parts of the business, so that when we implement the product in the customer's hands, it's not something they have to make a lot of adjustments to accommodate. **Nat Beuse 20:43** So we're running routes for customers, but we're the trucking company essentially, at our terminals. And what we need to transition to — where we are transitioning to — is what we call driver as a service. There the truck is actually owned and operated by the customers, and we already have customers signing up for that right now. **Nat Beuse 21:27** The use case you talked about is the second pillar: a customer says, hey, I like you Aurora, it seems you're doing good things, I'd like to unlock this particular route or this particular thing. We look at it and say, does this make sense? Can we actually do it? How much engineering effort is it? Then we can add on to the product to meet that customer's use case. **Nat Beuse 21:47** Then there's the third piece: where do you expand. That's where it makes a lot of sense for us to expand geographically east to west, and then we'll move toward the north — and that's exactly what you see us doing. **Nat Beuse 21:57** One of the awesome things about Aurora is we tend to do the things we say we're going to do. There isn't this "we're going to do a thing" and then we do something else. We've been very consistent with doing the things we say we're going to do, and doing them well.
**中文：** **主持人 19:16** Aurora Driver 目前验证的 ODD 是什么？这显然也要和商业模式对齐——这些车要在哪里跑？ **Nat Beuse 19:31** 好问题。我想用三种方式来描述。 第一种是**技术需要做什么**。我们一开始是"爬、走、跑"的路径：只做白天、只做一条路线、必须是晴朗天气。产品很好，但对客户可能没太大用。 **Nat Beuse 19:55** （主持人：不过有些地方这其实描述的是每一天。） 对，但这样的地方很少，至少在匹兹堡不是。随着时间推移我们加了新能力——夜间、恶劣天气。其实那些我们之前也在跑，但**没有为无人运营做过验证**。所以这个转变就是：不断把这些功能"解锁"到可以无人应用。 **Nat Beuse 20:27** 第二是**我们所在的模式**——所谓"运输即服务（TaaS）"。这个模式下，Aurora 做所有的事。老实说，我们需要这样做是为了**学会这门生意里难的部分**，这样等把产品交到客户手里时，客户不需要为它做大量调整。 **Nat Beuse 20:57** 所以我们在为客户跑路线，但某种意义上我们自己就是那家卡车公司——用我们自己的场站。而接下来我们要转向的，是我们说的**"司机即服务"（DaaS）**：卡车由客户自己拥有和运营，现在已经签了客户。 **Nat Beuse 21:27** 然后是第三个支柱：**往哪里扩张**。对我们来说，从东往西沿阳光地带扩张很合理，然后再往北——你看到的正是我们在做的。 **Nat Beuse 21:57** 我觉得 Aurora 有一点很棒：我们倾向于**做我们说要做的事**。没有那种"我们打算做 A，结果做了 B"。我们一直很一致。

## 八、运营极限：龙卷风、飓风、佛州下午四点的雷暴 / Operating limits and edge cases

**[22:11]**
**EN:** **Harry 22:11** Is there a number or a percentage? You mentioned daytime, one route, clear — then you add night and weather. What's the number that you and your customers decided on — these trucks need to hit 95% of the time they need to be able to go out and provide service? Obviously during a tornado or a hurricane you wouldn't plan for that, but there's got to be maybe a subjective threshold. How do you think about that line of uptime and reliability?
**中文：** **主持人 22:11** 有没有一个数字或百分比？你提到白天、一条路线、晴朗，然后加夜间和天气。你和客户有没有定一个门槛，比如 95% 的时间必须能出车、能提供服务？龙卷风或飓风显然不用规划，但总得有个主观阈值。你怎么看可用率和可靠性的这条线？

**[22:40]**
**EN:** **Nat Beuse 22:40** Both have to be very high. Ninety-something percent kind of thing, not seventies and sixties.
**中文：** **Nat Beuse 22:40** 两个都必须非常高。是**九十几个百分点**那种，不是七十、六十几。

**[22:11 – 24:00]**
**EN:** And to your point about hurricanes — we actually do have to plan for hurricanes. We have to be able to know operationally. This is one of the things a lot of people underestimate around the point I made earlier about operationalizing a product — making it more than just "this is cool self-driving technology."
**中文：** 关于飓风——我们**确实**必须规划。我们必须能在运营上知道该怎么办。这就是我之前说"把产品运营化"时，很多人低估的部分：让它不只是一项很酷的自动驾驶技术。

**[23:05]**
**EN:** **Nat Beuse 23:05** If you have — make up some number — 300 trucks, 500 trucks deployed on the Sun Belt, guess what: weather is the thing. I grew up in Florida, we have our fair share of four o'clock rainstorms — every single day, you can time your watch by it. Some of those thunderstorms are pretty ugly. Can you drive through those? Some of them you literally cannot, because roads are flooded. So we actually have to know how to deal with these things and how the product has to deal with them.
**中文：** **Nat Beuse 23:05** 假设你有——随便编个数——300 台、500 台车部署在阳光地带。那天气就是那个关键变量。我在佛罗里达长大，我们对下午四点的雷暴很有"份额"，你几乎可以拿表对着它校准。有些雷暴很难看——你能开过去吗？有些你**根本**开不过去，因为路被淹了。所以我们必须知道怎么处理这些，产品必须知道怎么处理。

**[23:35]**
**EN:** **Nat Beuse 23:35** Things like a hurricane: you've got to have a business plan for when the weather service says there's a category three coming in and it'll be here between this time and this time. We've got to be smart enough to understand how we're going to deploy those trucks during that particular event. Road closures is another thing. All of these speak to operationalizing the product in a way that makes it useful to the customer.
**中文：** **Nat Beuse 23:35** 再比如飓风：当气象部门说"三级飓风要来，会在这个时间段到"，你得有一个商业计划，聪明到知道那段时间这些车该怎么部署。**道路封闭**是另一件事。所有这些都指向"把产品运营化，让它对客户真正有用"。

## 九、指标：要匹配甚至超过人类司机 / Uptime and reliability

**[24:01 – 25:45]**
**EN:** **Harry 24:01** Is there a number or percentage of uptime and reliability you need to track? How do you think about that? **Nat Beuse 24:07** We track both. We track uptime — how long does it take to get the product out the terminal. Maybe I'll answer it this way: think about what their experience is today — we need to be matched at, or be better. **Nat Beuse 24:24** While the industry today might deal with the occasional driver calling in sick, or the road being shut down over here, those are the same metrics that we're going to track and keep a hold of. So those percentages have to be at that level or even higher, because if we're not adding value to the customer then it's not going to be useful to them. **Nat Beuse 24:43** It's all about making their experience — I would say — magical, in a way that it's just easy to use. They can dispatch the truck just like they would a normal truck today. The truck gets to its destination just like it does today, barring unforeseen circumstances. That's the level they expect. **Nat Beuse 25:13** I think this is also a difference — at least in my opinion, Nat's personal opinion — when you're in a business-to-business environment like we are, the bar is much higher both safety-wise and product-wise than if you call your taxi guy and he doesn't show up when you wanted him to, or it takes a little bit longer. As a consumer you have different choices you can make. When you've promised the business a certain product fidelity and a certain uptime, you better darn meet it, otherwise there are significant consequences on their side of the ledger.
**中文：** **主持人 24:01** 那有没有要追踪的可用率和可靠性数字？ **Nat Beuse 24:07** 两个都追踪。我们追踪**可用率（uptime）**、追踪产品从场站出来的时间等等。 我这样回答：想一想他们今天的体验是什么样——**我们要做到匹配，或者更好。** **Nat Beuse 24:24** 今天这个行业会遇到司机临时请病假、某条路封了之类的情况。这些就是我们同样要追踪、要守住的指标。所以那些百分比必须达到那个水平，甚至更高。 因为如果我们没有给客户**增加价值**，对他们就没用。关键在于让他们的体验——我会说——"有魔力"：用起来就是简单。他们像今天一样调度一台卡车，卡车像今天一样到达目的地，除非有不可预见的情况。这就是他们期待的水平。 **Nat Beuse 25:13** 还有一点差异（这是 Nat 的个人观点）：当你在一个 **B2B** 环境里，安全和产品两方面的门槛都比 2C 高得多。C 端你叫个出租车，它没按时到、或者晚一点，你还有别的选择。但当你向企业承诺了某种产品保真度和可用率，你就**必须**做到，否则对方账本上会有严重后果。

## 十、规模化：从 10 条路线到 50 条、100 条 / Scaling

**[25:45 – 28:02]**
**EN:** **Harry 25:51** It seems like Aurora is in a scaling and commercialization phase. You've got 10 routes out there and ambitious plans to grow that. Aurora is great at hitting milestones — if you've shared any targets or goals lately, would love to hear those as a north star. But what changes operationally or technically as the fleet grows from 10 routes to 50 to 100, and what should we expect from Aurora over the next year? **Nat Beuse 26:19** I would definitely say you should expect to see more trucks, more customers signing on to the product. What I would characterize as what changes is your operations get better and better and better — they have to handle more and more volume. If you're looking for a good analogy, think of a United or a Delta — the millions of passengers they move. We all go to the airport and expect the plane to take off on time, unless there's some weather event. And we all get dissatisfied when we're sitting on the tarmac for three hours for unknown reasons. Operations at that scale is what the business has to grow into. **Nat Beuse 27:14** What changes then is we'll go down the path of not constantly talking about "we added a new widget or a new feature," and more like what new customers signed on. It's really exciting from my standpoint, where we're moving from a handful of trucks highly concentrated in one area to a spot where they will be seen in the wild. **Nat Beuse 27:38** For me what's also going to be challenging is how we balance transparency and trust. Because we can't just put people in a tractor trailer and say "go for a ride" — we're going to have to keep working at how we explain what we're doing and what the product is doing, in a way that helps those communities the truck is driving through really appreciate what's happening and not be scared by the technology.
**中文：** **主持人 25:51** 看起来 Aurora 正处在规模化和商业化阶段。你有 10 条路线，也有雄心勃勃的扩张计划。Aurora 一向擅长兑现里程碑，如果最近有分享过什么目标，很想听听，可以作为北极星。但从 10 条到 50 条、100 条路线，运营上、技术上会发生什么变化？也可以顺便讲讲未来一年我们应该期待看到什么。 **Nat Beuse 26:19** 你肯定会看到更多卡车、更多客户签进来。 我会这样描述"什么变了"：你的**运营会越来越好、越来越好**，它们必须处理越来越大的量。打个好比方——想想美联航或者达美，它们每年运送数亿乘客。我们去机场，期待飞机准点起飞（除非天气事件）；如果我们在停机坪上不明原因坐了三个小时，所有人都会不满。所以**那种规模的运营**，正是这门生意必须长成的样子。 **Nat Beuse 27:14** 然后我觉得变化是：我们不会再去不停地说"我们又加了个新组件、新功能"，而更多是"哪些新客户签了"。 **Nat Beuse 27:38** 从我这边看这非常兴奋：我们从一个"只有少数几台车、高度集中在一个区域"的状态，走向"它们会在真实世界里被看到"。 对我来说，那种情况下也有挑战：**怎么平衡透明度和信任**。因为我们不能把人塞进半挂车里说"去兜一圈吧"，我们必须持续努力——如何解释我们在做什么、产品在做什么，让卡车经过的那些社区真正理解发生了什么，而不是被这项技术吓到。

## 十一、公众认知：误解、喷子与行业连坐 / Public perception

**[28:02]**
**EN:** **Harry 28:02** It sounds like your job up to this point has been more B2B and government relations. Do you think that public interface — what people are going to say or think or talk about the trucks — becomes more important to your role as you scale?
**中文：** **主持人 28:02** 听起来你此前的角色更像是 B2B 和政府关系。随着规模化，公众界面——人们会怎么说、怎么想、怎么议论这些卡车——在你角色里是不是变得更重了？

**[28:18]**
**EN:** **Nat Beuse 28:18** I think it's already there. There are lots of trolls that I already have, so to speak, who need to needle me every once in a while, sometimes in public, sometimes in private. For me it's just really being honest with them about what the product is doing.
**中文：** **Nat Beuse 28:18** 我觉得已经在那儿了。我已经有不少"喷子"了，时不时在公开或私下里戳我一下。

**[28:02 – 30:11]**
**EN:** Because there are a lot of misconceptions: is the truck actually working? Is there some secret spot in the back room where Chris Urmson is driving with a joystick? To be clear, he is not.
**中文：** 对我来说，就是**诚实地告诉他们产品在做什么**。因为有很多误解：卡车真的在工作吗？是不是有个秘密的后屋，Chris Urmson 拿着摇杆在开？——明确说，**他没有**。

**[28:53]**
**EN:** **Nat Beuse 28:53** But people have this weird perception, because there are all these different use cases in the industry, and we're all not the same in the way we approach safety, we're all not the same in the way we approach transparency. Unfortunately that breeds a little bit of confusion. So we just have to continue to rise above it, explain what we're doing and why we think it's safe.
**中文：** **Nat Beuse 28:53** 但人们确实有这种奇怪的认知，因为这个行业有太多不同的用例，我们做事的方式不一样，我们对待安全的方式也不一样，我们对待透明度的方式也不一样。不幸的是，这会滋生出一些混淆。所以我们只能继续往上走，继续解释我们在做什么、为什么我们认为是安全的。

**[29:25]**
**EN:** **Nat Beuse 29:25** We can't underestimate the impact that the ride-share incidents and issues will have — we've already seen that. There were some very public events with first responders, and my old agency responded with a letter telling everybody, hey, this is not cool, don't you go do something about this.
**中文：** **Nat Beuse 29:25** 而且我们不能低估**网约车那些事件**会带来的影响——我们已经看到了。有一些和急救人员相关的非常公开的事件，我原来的机构（NHTSA）发了信告诉所有人：这不酷，你们得做点什么。

**[29:45]**
**EN:** **Nat Beuse 29:45** We've never had any of those types of issues. The letter kind of was like, oh, this is interesting. But I think this will continue to be part of the job, and as you point out, going forward it will become the most important thing. I wouldn't say that — I think underlying safety still has to be the thing — but quality of the product will become a bigger part of how we talk about the future.
**中文：** **Nat Beuse 29:45** 我们从来没出现过那类问题。那封信对我们来说更像"哦，这挺有意思"。但我认为这类事情会继续成为这份工作的一部分，而且如你所说，往后会变成最重要的事。我不会说底层安全不再是核心——但**产品质量**会成为我们谈论未来时更大的一部分。

## 十二、竞争与协作：安全高于竞争 / Competition and collaboration

**[30:11 – 33:27]**
**EN:** **Harry 30:11** The autonomous trucking space is hot, a lot of competition, a lot of companies jumping in because of the opportunity. Aurora is quite established. But how carefully do you have to follow competitors, because other companies can impact the industry as a whole — whether on the regulatory side or how consumers or customers think about it? **Nat Beuse 30:55** Great question, Harry. For the most part — and I say most because I'm not one that generally speaks an absolute yes — the AV companies are actually collaborating in a way that is quite, quite impressive. Even from my old chair at NHTSA to now, safety seems to be one that most people can agree on: hey, let's figure out how not to be disruptive with each other, and figure out how to share best practices. **Nat Beuse 31:27** One of the groups we're involved in is the AVSC, the Automated Vehicle Safety Consortium. At its core it's just working on best practices that cut across the industry — something like how you interact with first responders, for example. Something we're very proud of is our safety management system, which is really about how the company, the employees and the executive team manage their safety risk posture. We actually co-wrote the best practice for that and published it with a bunch of other people. **Nat Beuse 32:15** One of the interesting things is that everyone in that consortium — the hook in it — is that if you are in the consortium at the time a best practice is being written, you actually commit to doing it. That's very different from any of the other industry standard groups out there. **Nat Beuse 32:28** So safety is one that rises above. On the competitive side, yes, we're going to be fierce competitors. But on the safety stuff, my view of the world is that we are much better at it — more akin to how the airline industry shares safety information with each other than where other industries have been. **Harry 32:42** I like that approach and I haven't heard anyone crystallize it like that. Safety trumps everything else. Obviously there may be aspects where you feel you have a stronger safety case than another company, but if there's another AV trucking company that's crashing all over the place, that's pretty bad for the industry as a whole, especially this early on. **Nat Beuse 33:26** For sure. For our part, we were quite willing to share even some things that folks would look at and say, oh, that's kind of proprietary, why are you sharing that. We put out our safety case framework long before we even closed it — giving anybody in the industry, but more importantly regulators and the public, a view into all the different boxes we were looking to close in order to say our safety case was complete. **Nat Beuse 34:05** We were also the only company putting out our rate of closure. We published and said, hey, we're not there yet folks, we're only at 95%, and we're not pulling this driver until this thing reaches a hundred. Others have since followed. **Nat Beuse 34:23** Now what's interesting is safety cases are all over the industry — they show up in interesting places. They showed up in a California rulemaking that finally unlocked trucking. That's a good one for me, because I was in the early days on the federal side trying to work with California, and now I'm on the private side finally reaping the benefits of a like 20-year process that finally opened up the state. I can't take all the credit for that, for sure, but certainly we had a big influence on how the industry is thinking about safety.
**中文：** **主持人 30:11** 无人卡车是个热门赛道，竞争激烈，很多新公司因为机会跳进来。Aurora 相对成熟，在安全、商业化上都在前面。但你会多密切地关注竞争对手？因为其他公司会影响整个行业——无论是监管层面还是消费者/客户的认知。 **Nat Beuse 30:55** 好问题，Harry。我认为**大部分情况下**——我说"大部分"是因为我不太喜欢讲绝对的"是"——AV 公司之间的协作程度相当惊人。 甚至从我当年在 NHTSA 的位子上到现在，**安全似乎是大多数人都能达成一致的事**：让我们想清楚怎么不互相干扰，怎么共享最佳实践。 **Nat Beuse 31:27** 我们参与的一个组织叫 **AVSC——自动驾驶车辆安全联盟（Automated Vehicle Safety Consortium）**。它的核心就是制定跨行业的最佳实践。比如如何和急救人员互动；还有我们很自豪的一件事——**安全管理体系**，也就是公司、员工和高管团队如何管理自己的安全风险姿态，这份最佳实践是我们共同撰写的。 **Nat Beuse 32:15** 有意思的是，这个联盟里所有人有一个"钩子"：如果你在某份最佳实践撰写时是成员，你就**承诺去执行它**。这跟其他行业标准组织很不一样。所以安全这件事是能超越竞争的。 当然，竞争的时候我们会是凶猛的对手；但在安全上，我的世界观是——我们更像**航空业互相共享安全信息**那样，而不是其他行业过去的样子。 **主持人 32:42** 我喜欢这个表述，我没听别人这么总结过。安全压倒一切。显然有些方面你可能觉得自己安全案例更强，但如果有另一家 AV 卡车公司到处撞车，对整个行业来说非常糟糕，尤其是在这么早期。而且这似乎是工程师们真的愿意在大会议上互相交流的领域。

## 十三、知识共享：先公布框架，再公布"关闭进度" / Knowledge sharing

**[33:26]**
**EN:** **Nat Beuse 33:26** For sure. For our part, we were quite willing to share even some things that folks would look at and say, oh, that's kind of proprietary, why are you sharing that.
**中文：** **Nat Beuse 33:26** 当然。就我们而言，我们很愿意分享一些别人可能觉得"这是专有技术，你为什么要公开"的东西。

**[33:26 – 34:54]**
**EN:** We put out our safety case framework long before we even closed it — giving anybody in the industry, but more importantly regulators and the public, a view into all the different boxes we were looking to close in order to say our safety case was complete.
**中文：** 比如我们在**还没关闭安全案例之前很久**，就发布了《安全案例框架》，让行业里任何人——更重要的是监管者和公众——看到我们要关闭的所有"格子"分别是什么。

**[34:05]**
**EN:** **Nat Beuse 34:05** We were also the only company putting out our rate of closure. We published and said, hey, we're not there yet folks, we're only at 95%, and we're not pulling this driver until this thing reaches a hundred. Others have since followed.
**中文：** **Nat Beuse 34:05** 我们还是**唯一一家公布"关闭进度（rate of closure）"的公司**。我们公开说："各位，我们还没到，我们只到 95%，这个数字不达到 100% 我们就不会撤掉司机。"后来别人也跟进了。

**[34:23]**
**EN:** **Nat Beuse 34:23** Now what's interesting is safety cases are all over the industry — they show up in interesting places. They showed up in a California rulemaking that finally unlocked trucking. That's a good one for me, because I was in the early days on the federal side trying to work with California, and now I'm on the private side finally reaping the benefits of a like 20-year process that finally opened up the state. I can't take all the credit for that, for sure, but certainly we had a big influence on how the industry is thinking about safety.
**中文：** **Nat Beuse 34:23** 现在有意思的是，**安全案例这个概念在整个行业都出现了**，而且出现在一些意想不到的地方——它出现在加州的一项立法/规则制定里，最终解锁了卡车运营。这对我来说挺好：我早年在联邦层面跟加州打交道，现在在私营部门终于收获了一个大概 20 年进程的成果。

## 十四、上市公司的好处：多了一群可以对话的人 / Being a public company

**[34:54 – 37:27]**
**EN:** **Harry 34:54** Having covered Uber and Lyft for a decade, I remember when they were private and then became public. Once you're a public company you have to share a lot more information with investors around financial disclosures. Aurora is one of the few public companies in the autonomous vehicle space. Does that present any unique opportunities or challenges to your job, or to the company as a whole? **Nat Beuse 35:34** Really good question. From my standpoint, it opens up another group of folks to talk with. When you asked me earlier about members of the public, I kind of group the public all into one group — whether it's our insurers, our investors, our customers — people who are not building tech. Being able to interact with those folks has been really awesome, because they're looking at a bunch of different companies, and it's really good to engage in a conversation with them to see where they see the differences, what they're concerned about. **Nat Beuse 36:09** Almost all the time I can point to something in the safety case and say, well, if you really want to know more about how we're thinking about that, go see here — or you can go look at our voluntary safety self-assessment. It's getting quite long now; it's one of my complaints with my team, it's getting too long. So we'll probably do some innovation to shrink that down to something more manageable. But there's a ton of information there. **Nat Beuse 36:42** As we grow — right now we're working on our Gen Two system, which is ruggedized and going into the international builds — we already also have our Gen Three system, which is going to be built by Movio[?] and line-side installed with Volvo. So this ecosystem we have is really expanding. **Nat Beuse 37:00** As a public company you get more questions about, well, what's going on with Volvo, what's going on with Movio[?]. The good news is all those things are on track, and we're definitely proud of the work we're doing with Roush[?]. Sometimes I'm involved in conversations with these folks because they have very serious safety questions about what we're doing, and being able to explain that in a way that's helpful to them is really beneficial.
**中文：** **主持人 34:54** 你提到了 Aurora 在透明上做的很多事。我报道 Uber 和 Lyft 十年，记得它们从私有变上市。上市后你必须向投资者披露更多信息。Aurora 是 AV 领域少数上市公司之一，这在卡车领域可能更少。这对你的工作带来什么独特的机会或挑战？ **Nat Beuse 35:34** 好问题。从我的角度，它**多打开了一群可以对话的人**。 你之前问我关于公众，我其实把公众归成一大类：保险方、投资者、客户——他们都不造技术。能和他们互动很棒，因为他们在同时看很多家公司，和他们聊能知道他们看到的差异在哪、担心什么。 **Nat Beuse 36:09** 而且几乎每次我都能指向安全案例里的某处说：如果你真想知道我们怎么想的，去看这里，或者去看我们的**自愿安全自我评估（VSSA）**。它现在变得相当长——这是我对团队的一个抱怨，太长了，我们大概会做些创新把它压缩到可管理的程度。但那里信息量很大。 **Nat Beuse 36:42** 随着我们成长——现在我们在做 **Gen Two** 系统，为了 ruggedize（加固/适应恶劣环境），会进入国际版车型；我们也已经有 **Gen Three**，将由 Movio[?] 制造，在沃尔沃产线旁安装（line-side installed with Volvo）。 **Nat Beuse 37:00** 所以这个生态在扩张。作为上市公司，你会被问更多问题：沃尔沃那边怎么样、Movio[?] 那边怎么样。好消息是这些都在轨道上，我们也很自豪和 Roush[?] 的合作。有时我会参与这些对话，因为他们对我们在做什么有非常严肃的安全疑问，能把这件事解释清楚对他们很有帮助。

## 十五、监管：一部法案、一套联邦框架、一个全球技术法规 / Regulatory landscape

**[37:27]**
**EN:** **Harry 37:27** Last topic: the regulatory landscape, which I was excited to talk to you about since you spent over a decade on the regulatory side. What's the topic du jour for AV trucking — what are people talking about behind the scenes? You're operating in a few states and just got California, which was big news. What keeps you up at night or what are you excited about?
**中文：** **主持人 37:27** 最后一个话题——监管。你 teasing 过了。你在监管方待了十多年，所以你是最合适的人。AV 卡车监管现在最热的话题是什么？幕后大家在谈什么？

**[38:04]**
**EN:** **Nat Beuse 38:04** A lot of good progress. From my perspective, knowing how long it takes to work on regulations, it's really great to see this administration put forward some actual proposals and an actual roadmap.
**中文：** **Nat Beuse 38:04** 进展很多。从我了解的情况看——知道做监管有多慢——这届政府拿出了一些真正的提案和路线图，这真的很棒。

**[38:11]**
**EN:** **Nat Beuse 38:11** I'll show you this way: I once worked on a rule that literally took a dozen years. That rule is the backup camera in your car. So if you think something simple like that takes 12 years, you can imagine the journey we're going to be on for a little while.
**中文：** **Nat Beuse 38:27** 我举个例子：我曾经参与过一条规则，**整整花了 12 年**。那条规则是——你车上那个倒车摄像头。所以如果这么简单的东西要 12 年，你可以想象我们还要走多久。

**[38:38]**
**EN:** **Nat Beuse 38:38** But it's exciting to finally see progress. There are many different things people are talking about right now. One is there's a bill floating around on the Hill that would provide a lot of good things not just for the industry but for the public at large, because there are a lot of safety pieces in there that would be the unifying federal framework that many of us have been asking for for quite some time.
**中文：** **Nat Beuse 38:38** 但终于看到进展很令人兴奋。现在这个领域大家在谈很多东西。一个是**国会山上有一部在流转的法案**，它不只对行业、对公众也有好处，因为里面有很多安全条款，会是很多人长期以来一直在要的那个**统一的联邦框架**。

**[39:15]**
**EN:** **Nat Beuse 39:15** Because states do have a role, but we can't have 50 different versions of what safety looks like depending on who you talk to — that would be backwards.
**中文：** **Nat Beuse 39:15** 因为州有州的角色，但**不能有 50 个不同版本的安全标准**，取决于你跟谁谈——那是倒退。

**[39:18]**
**EN:** **Nat Beuse 39:18** And we have to understand this is not just a US thing. There's a big conversation happening internationally. We are certainly the leaders in this space. One of the things I consistently hear from folks who come visit us, or folks I talk with from my previous life: they're quite jealous. They come over and say, wow, you guys actually have AVs running on the road with nobody in there — and I'm like, yeah we do. They're still in kind of these weird demo pilot things. But they're all working on regulations — whether it's Japan, Europe, Canada, even the US, everybody's working on rules.
**中文：** **Nat Beuse 39:18** 而且要理解这不只是美国的事。国际上有一场大对话。我们在这个领域确实是领先的——我经常从来访的人、或者我过去生涯里认识的人那里听到：他们很羡慕，说"哇，你们真的有 AV 在路上跑、车里没人"。而他们还在搞那些奇怪的 Demo 试点。但他们都在做监管——日本、欧洲、加拿大，包括美国，所有人都在写规则。

**[40:06]**
**EN:** **Nat Beuse 40:06** One of the interesting things that happened pretty recently is this thing called a global technical regulation. All these member countries signed up for this and said, generally this is the framework that we want, and then each country has to come back and fill in the details. That's exciting — literally many countries had to go through all of their various protocol apparatuses and actually agreed to something. That's pretty impressive.
**中文：** **Nat Beuse 40:06** 最近发生的一件有意思的事，是所谓**全球技术法规（Global Technical Regulation）**——所有成员国公司/国家签了这个，说"大致上这就是我们要的框架"，然后每个国家回去填补细节。这很令人兴奋，因为这意味着很多国家要走过他们各自那一整套程序，而且真的达成了一致。

**[40:28]**
**EN:** **Nat Beuse 40:28** To me the path is quite bright. In the US, for us, the US is mostly open now. There are a few more places to go, to adjust the regulations so it's actually appropriate for what we're trying to do, but it's not like we have blockers in a bunch of places. That's really exciting for us and for our customers.
**中文：** **Nat Beuse 40:28** 所以对我来说路径相当光明。美国现在大部分是开放的，还有一些地方需要调整法规，让它真正适配我们想做的事，但并不是说我们在一堆地方都有拦路石。这对我们和客户都是好消息。

**[40:58]**
**EN:** **Nat Beuse 40:58** Personally, seeing us as a country move from the first version of AV guidance — which was about two pages — to now actually talking about regulations and what would be in there, is awesome. I can see that progress continuing.
**中文：** **Nat Beuse 40:58** 对我个人来说，看到这个国家从第一版 AV 指南只有大概两页，走到现在真正在讨论法规、讨论里面该有什么，这很棒。我能看到这个进程继续下去。

## 十六、联邦框架的障碍：法案、两院、然后才是真正难的写规则 / Hurdles to a federal framework

**[41:07]**
**EN:** **Harry 41:07** It sounds like a federal framework would be the most useful if you had your genie in a bottle / magic wand wish list for Aurora.
**中文：** **主持人 41:07** 听起来联邦框架是最有用的。如果你的"瓶中精灵"愿望清单上只能许一个——**Aurora 最想要的是什么？**

**[41:16]**
**EN:** **Nat Beuse 41:16** Magic wand.
**中文：** **Nat Beuse 41:16** 魔法棒。

**[41:17]**
**EN:** **Harry 41:17** Magic wand. I think there's good support from the administration — the President and team. But beyond that, what are the steps? An actual bill would need to be passed between the Senate and the House? Is that typically the blocker with a federal framework, or what are you tracking going forward?
**中文：** **主持人 41:17** 对，魔法棒。我想行政层面是有支持的——总统和团队。但在这之外，需要走哪些步骤？需要在参众两院通过一部真正的法案？这通常才是联邦框架的卡点吗？你在追踪什么？

**[41:42]**
**EN:** **Nat Beuse 41:42** It's very old-school Schoolhouse Rock — "just a bill." Executive, legislative...
**中文：** **Nat Beuse 41:42** 这就是那个老派的《Schoolhouse Rock》（美国讲立法的动画）——"Just a bill"。行政、立法……

**[41:53]**
**EN:** **Nat Beuse 41:53** It's a process, having lived it a couple of times already. Once we get both chambers to do their thing, then typically the President would sign such a thing, but then it still comes back to the executive branch to do the work.
**中文：** **Nat Beuse 41:53** 这是个流程，我已经亲身经历过几次。等两院做完他们该做的事，通常总统会签署，**但之后还是回到行政部门去做这件事**。

**[42:09]**
**EN:** **Nat Beuse 42:09** And that's the part I spent most of my career in — which is, you've got to actually write the rule. It's actually difficult.
**中文：** **Nat Beuse 42:09** 而那正是我职业生涯大部分时间待的地方——**你实际得把规则写出来，这真的很难**。

**[42:13]**
**EN:** **Nat Beuse 42:13** There are some rules they have to live by: whatever they do has to be repeatable, has to be reproducible, you can't do it arbitrary and capriciously. There are all these things that have to go in, and then there's another thing called cost and burden that has to factor in. So all of that machinery has to get going.
**中文：** **Nat Beuse 42:13** 规则有一些必须遵守的约束：它必须是可重复的、可复现的；不能任意和反复无常（arbitrary and capricious）；还有一项叫"成本与负担（cost and burden）"必须计入。所以整套机器都得转起来。

**[42:38]**
**EN:** **Nat Beuse 42:38** Which is why, personally, I've been advocating for us to get on with the work and not try to solve all of the problems or all the issues or all the things that everybody wants to talk about in one fell swoop. Get it going and you can always add on to things.
**中文：** **Nat Beuse 42:38** 这也是我个人一直在主张的：**让我们先把工作推进起来**，不要试图一口气解决所有问题、所有人想谈的所有事。先动起来，之后随时可以往上加。

**[43:00]**
**EN:** **Nat Beuse 43:00** So the big blockers, if there are any, are just that this is a huge ecosystem and everybody has a different flavor of something they've been thinking about. But the fact that we actually have a bill that people generally agree upon signals to me, at least, that some of the people who may not be on board with it have actually shifted their focus a little bit.
**中文：** **Nat Beuse 43:00** 所以如果说有大的障碍，那就是这是个巨大的生态，每个人心里都有自己那一版"该怎么做"。但事实上我们现在有一部大家基本认同的法案——这至少说明，一些原本可能不赞成的人，关注点已经有所转移。

**[43:15]**
**EN:** **Harry 43:15** That's great. I definitely appreciate all of the time you've put in over the past couple of decades with the government, with Uber, with Aurora. We're all lucky to have you and the industry is lucky to have you moving things forward. I'm excited to see more of these Aurora trucks on the road. Nat, thank you for coming on.
**中文：** **主持人 43:15** 太好了。非常感谢你过去二十年在政府、Uber、Aurora 投入的时间。我们都很幸运有你、这个行业也很幸运有你推动事情往前走。期待在路上看到更多 Aurora 的卡车。Nat，谢谢你来。

**[43:41]**
**EN:** **Nat Beuse 43:41** Hey Harry, thanks so much for having me, and thank you very much for the kind words — that means a lot.
**中文：** **Nat Beuse 43:41** Harry，非常感谢你邀请我，也谢谢你的好话，这对我意义很大。

## 十七、尾声：听众评论与周边 / Outro

**[43:46]**
**EN:** **Harry 43:46** Before we go I want to read off the latest five-star review, which comes today from nerd futurist. He says this podcast is his weekly DDP — I guess that's Driverless Digest Podcast — the best podcast in the industry; he works in emergent mobility technology and finds it a helpful tool for staying sharp. Harry provides honest and thought-provoking assessments without pulling punches or playing favorites.
**中文：** **主持人 43:46** 走之前我想读一下最新一条五星评论，来自 nerd futurist。他说这个播客是他的"每周 DDP"——我猜是 Driverless Digest Podcast——是行业里最好的播客，对做新兴出行技术的人很有帮助，对圈外想了解交通科技的人也有用；Harry 提供诚实、发人深省的判断，不回避、不站队。

**[43:46 – 45:08]**
**EN:** Thank you. If you have a moment to leave a review on Apple Podcasts it's a big favor — and the first three people who email me a screenshot of their review get some of our latest TDD swag, including the new trucker hats. Until the next one.
**中文：** 谢谢。如果方便去 Apple Podcasts 留个评论，帮大忙；前三名把评论截图邮件发我的人，我会寄最新周边（新的卡车帽）。下期见。

**[43:46 – 45:08]**
**EN:** *Machine-transcribed from the episode audio, then manually cleaned: filler words trimmed, repeated false starts collapsed, proper nouns corrected against public sources. Movio[?] and Roush[?] could not be verified. At 13:29 the speaker says "Mexico"; given the surrounding list this is likely New Mexico.*
**中文：** > 本稿由播客音频全文听写后翻译整理。赞助商口播段落已略去内容、仅保留位置标记。原文为口语对话，为可读性做了断句与去口头语处理，语义未作改动。标注 [?] 的专有名词（Movio、Roush）音近但未能核实；"墨西哥/新墨西哥"处原文为 Mexico，按上下文可能指新墨西哥州或跨墨西哥路线，已标注。
