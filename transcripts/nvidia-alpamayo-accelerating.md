## 开场与嘉宾介绍

**SECTION_NOTE**
- 主播 Harry Campbell；嘉宾 Matt Cragun，NVIDIA 自动驾驶产品总监
- 团队负责车载模型、训练工具与仿真测试工具
**END_SECTION_NOTE**

**[00:00 – 00:52]**
**EN:** Matt Cragun: The vehicles and the technology is coming along at this point is developing quite quickly. And I think that consumers' expectations are starting to change. We see a lot of automakers prepping their vehicles so that they're L4 capable. Deploying a vehicle on the road in a safe way is actually significantly more complicated than just Alpamayo itself. So Alpamayo, like I said, is good raw material. For building one of these AVs. Our hope is that a huge portion of all software development, including autonomous vehicle development, is built on top of open source. If they come to NVIDIA and they say, hey, I'm building a vehicle, can you help me? The answer to NVIDIA should be yes.
**中文：** Matt Cragun：此时的车辆和技术正在迅速发展。我认为消费者的期望正在开始改变。我们看到许多汽车制造商正在为他们的车辆做好准备，使其具备 L4 能力。以安全的方式在道路上部署车辆实际上比 Alpamayo 本身要复杂得多。因此，正如我所说，Alpamayo 是很好的原材料。用于构建其中一款 AV。我们希望所有软件开发的很大一部分，包括自动驾驶汽车开发，都是建立在开源之上的。如果他们来到 NVIDIA 并说，嘿，我正在制造一辆汽车，你能帮我吗？ NVIDIA的答案应该是肯定的。

**[00:52 – 01:03]**
**EN:** Harry Campbell: Matt Cragun is the Director of Product for Autonomous Vehicles at NVIDIA. He works day-to-day building Alpamayo, Nuro, Cosmos, and other simulation and model infrastructures. Matt, how are you doing today?
**中文：** Harry Campbell：Matt Cragun 是 NVIDIA 自动驾驶汽车产品总监。他每天致力于构建 Alpamayo、Nuro、Cosmos 以及其他模拟和模型基础设施。马特，你今天过得怎么样？

**[01:03 – 01:05]**
**EN:** Matt Cragun: I'm doing great.
**中文：** Matt Cragun：我做得很好。

**[01:05 – 01:26]**
**EN:** Harry Campbell: Excited to have you. NVIDIA is obviously a big name in the entire tech industry, I think one of the biggest companies. And it's one, though, that I think, I myself hear a lot of announcements. I don't necessarily know a ton about all that you guys have going on. So I guess you're probably one of the best people to have on to help me walk through in our audience, right?
**中文：** Harry Campbell：很高兴有你。 NVIDIA 显然是整个科技行业的大牌，我认为是最大的公司之一。不过，我认为我自己也听到过很多这样的公告。我不一定对你们所发生的事情了解很多。所以我想你可能是帮助我在观众中走动的最佳人选之一，对吧？

**[01:26 – 01:29]**
**EN:** Matt Cragun: Yeah, that's great. Where do you want to start?
**中文：** Matt Cragun：是的，那太好了。您想从哪里开始？

**[01:29 – 01:38]**
**EN:** Harry Campbell: Well, I'd love to start maybe at a high level, can you start maybe by introducing yourself and your role at NVIDIA? What is it that you focus on?
**中文：** Harry Campbell：好吧，我想从较高的层面开始，您能先介绍一下您自己以及您在 NVIDIA 的角色吗？你关注的焦点是什么？

**[01:38 – 02:02]**
**EN:** Matt Cragun: Sure. Yeah, happy to. So as you mentioned, I'm a director of product management here and I work specifically in our autonomous vehicles group. And my team, we focus specifically on the models that go inside the car, the tooling that you need to build those models, and then specifically simulation tools for testing the models as they get built. Gotcha.
**中文：** Matt Cragun：当然。是的，很高兴。正如您提到的，我是这里的产品管理总监，专门在我们的自动驾驶汽车团队工作。我的团队特别关注汽车内部的模型、构建这些模型所需的工具，以及用于在构建模型时对其进行测试的专门仿真工具。明白了。

**[02:02 – 02:09]**
**EN:** Harry Campbell: Cool. And so this would be the Alpamayo models. Can you help us with some of the terminology?
**中文：** Harry Campbell：凉爽的。这就是 Alpamayo 模型。您能帮助我们了解一些术语吗？

## 什么是 Alpamayo

**SECTION_NOTE**
- Alpamayo 取名自秘鲁山峰（最美也最难爬）
- 它是一整套 AV 开发产品家族，不止一个模型
**END_SECTION_NOTE**

**[02:09 – 02:50]**
**EN:** Matt Cragun: Yeah, sure. So we give our models different names. They're like, children for us. So we want to make sure that they're all appreciated. But Alpamayo, actually the name Alpamayo... is the name of a mountain in Peru. And it was given that name. It's actually supposedly one of the most beautiful mountains to climb, but also one of the most difficult. And so we gave that name to the model that we use for actually driving an autonomous vehicle. It's a challenge that we've been working on for some time. And we think it's going to be great when we get all the way there. And it certainly is challenging along the way, but it's very rewarding.
**中文：** Matt Cragun：是的，当然。所以我们给模型起了不同的名字。他们就像我们的孩子。所以我们想确保他们都受到赞赏。但阿尔帕马约，实际上阿尔帕马约这个名字……是秘鲁一座山的名字。它被赋予了这个名字。事实上，它被认为是最美丽的山脉之一，但也是最难攀登的山脉之一。因此，我们将这个名称命名为我们实际驾驶自动驾驶汽车所使用的模型。这是我们已经努力了一段时间的挑战。我们认为，当我们一路走到那一步时，一切都会很棒。一路上确实充满挑战，但也是非常有意义的。

**[02:50 – 03:10]**
**EN:** Harry Campbell: Interesting. Yeah, I actually had that down as a question that I just thought of and I wanted to ask you. So you're already reading my mind. Thank you for that. If you need more names, I remember I did a hike to Machu Picchu and there's a secondary mountain that you can climb up to the top called Juana Picchu. So I think if we need to brainstorm some other model ideas, I've got you covered.
**中文：** Harry Campbell：有趣的。是的，实际上我刚刚想到了这个问题，我想问你。所以你已经读懂了我的想法。谢谢你。如果你需要更多名字，我记得我徒步去了马丘比丘，那里有一座次级山，你可以爬到山顶，叫做胡安娜比丘。因此，我认为如果我们需要集思广益一些其他模型的想法，我可以满足您的要求。

**[03:10 – 03:45]**
**EN:** Matt Cragun: Sounds good. Well, let me tell you, I was just going to say, I can tell you a little bit more about Alpamayo just in general, though, because it's a little broader than just the model. We released, it's a product family, so it's basically all the tools that you would need to build an autonomous vehicle. So it includes the model. We have a couple of flavors of that, and we'll probably talk about that in a minute. But the models that you would use, and then there's a simulator called AlpaSim. And then there's a very large data set that we released also that is an open source data set of autonomous driving data. So it's a very large data set of 300,000 clips of driving.
**中文：** Matt Cragun：听起来不错。好吧，让我告诉你，我只是想说，我可以告诉你更多关于 Alpamayo 的一般情况，因为它比模型更广泛一些。我们发布了，它是一个产品系列，所以它基本上是构建自动驾驶汽车所需的所有工具。所以它包括模型。我们有几种风格，我们可能会在一分钟内讨论。但是您将使用的模型，还有一个名为 AlpaSim 的模拟器。然后我们还发布了一个非常大的数据集，这是自动驾驶数据的开源数据集。所以这是一个非常大的数据集，包含 300,000 个驾驶片段。

## NVIDIA 更偏硬件（芯片）还是软件（模型）

**SECTION_NOTE**
- NVIDIA 越来越以「模型」闻名
- 模型与权重发布于 Hugging Face，代码在 GitHub
**END_SECTION_NOTE**

**[03:45 – 04:11]**
**EN:** Harry Campbell: Yeah. So when people meet you at events or conferences, I almost feel like my... impression is that with Nvidia, they're sort of known for the chips and, a lot of AV operators and developers use, Nvidia chips for, their own models. But, do most people think of Nvidia in that category or this category where you're building your own models?
**中文：** Harry Campbell：是的。因此，当人们在活动或会议上见到你时，我几乎感觉我的印象是，Nvidia 因芯片而闻名，并且许多 AV 运营商和开发人员都使用 Nvidia 芯片来开发他们自己的模型。但是，大多数人是否认为 Nvidia 属于该类别或您正在构建自己的模型的类别？

**[04:11 – 04:42]**
**EN:** Matt Cragun: It's certainly becoming, we're becoming more and more known for the models. We've been building models for some time. But we're now, it's a major part of our strategy and our business. And we just are, over the last year, have We're very prolific and doing a lot of work in terms of the actual model building in addition to obviously the hardware and the other chips and the other sort of things that we work on.
**中文：** Matt Cragun：毫无疑问，我们的模型越来越出名。我们建立模型已经有一段时间了。但现在，它是我们战略和业务的重要组成部分。在过去的一年里，我们非常多产，除了硬件和其他芯片以及我们所做的其他事情之外，我们在实际模型构建方面做了很多工作。

**[04:42 – 04:48]**
**EN:** Harry Campbell: Got it. That might be the first time I've ever heard the term hugging face. What is that? Is that an open source directory or?
**中文：** Harry Campbell：知道了。这可能是我第一次听到“抱脸”这个词。那是什么？这是一个开源目录吗？

**[04:48 – 05:26]**
**EN:** Matt Cragun: Yeah, so Hugging Face is essentially just like GitHub is the place where you go where people can publish code. Hugging Face is effectively the equivalent of GitHub, but specifically for models. So models get distributed most of the time as weight. So when we actually published models, we published the model and the weights to Hugging Face. And if there's any code that you need to operate the model or to do some post training or some other functions with the model, we published that on GitHub. So GitHub was specifically built to handle code. Hugging Face is a repository that was specifically designed to handle models.
**中文：** Matt Cragun：是的，Hugging Face 本质上就像 GitHub 一样，是人们可以发布代码的地方。 Hugging Face 实际上相当于 GitHub，但专门针对模型。因此模型大部分时间都以权重的形式进行分配。因此，当我们实际发布模型时，我们将模型和权重发布到 Hugging Face。如果您需要任何代码来操作模型或使用模型进行一些后期训练或其他功能，我们会将其发布在 GitHub 上。所以 GitHub 是专门为处理代码而构建的。 Hugging Face 是专门为处理模型而设计的存储库。

## NVIDIA 的 AV 开发战略

**SECTION_NOTE**
- 核心原则：任何做 AV 的人来问『能帮我吗』，答案应是 yes
- 提供基础模型，让开发者在其上再训练 / 定制 / 部署
**END_SECTION_NOTE**

**[05:26 – 05:52]**
**EN:** Harry Campbell: That's pretty cool. So is the general belief behind Alpamayo and I guess this series of products that, a lot of AV companies are out there developing, maybe not the same technology, but they all kind of want the same end result, right? A safe AV out on the road that can handle all these different situations and why have 12 different companies kind of tackle the same thing when you guys can kind of be the point person for that?
**中文：** Harry Campbell：太酷了。 Alpamayo 背后的普遍信念是，我猜这一系列产品是很多 AV 公司正在开发的，也许不是相同的技术，但他们都想要相同的最终结果，对吗？一辆安全的自动驾驶汽车在路上可以处理所有这些不同的情况，为什么要让 12 家不同的公司来处理同样的事情，而你们可以成为这件事的关键人物呢？

**[05:52 – 06:53]**
**EN:** Matt Cragun: Yeah, I think that, generally speaking, NVIDIA's strategy with autonomous vehicle development is if somebody is in the business of building an autonomous vehicle, that if they come to NVIDIA and they say, hey, I'm building a vehicle, can you help me? The answer to NVIDIA should be yes. And so the needs of customers are different. So some customers that we work with are just using our GPUs in the data center and that's what they need. We have customers that use our hardware in the car. And now we have this opportunity to really help for developers who want to be able to accelerate their development of the actual software that goes in the car. And this is one of the main things that we can contribute is basically this foundation level model. And they can take that, they can do additional training on top of it, they can customize it, and then they can deploy it. But the goal is to basically give them kind of a running start to the development process with all the data and the training and compute that we've already kind of pumped into this model for them.
**中文：** Matt Cragun：是的，我认为，一般来说，NVIDIA 在自动驾驶汽车开发方面的策略是，如果有人从事自动驾驶汽车的制造业务，那么如果他们来到 NVIDIA 并说，嘿，我正在制造一辆汽车，你能帮我吗？ NVIDIA的答案应该是肯定的。所以客户的需求是不同的。因此，与我们合作的一些客户只是在数据中心使用我们的 GPU，而这正是他们所需要的。我们有客户在车上使用我们的硬件。现在，我们有机会真正为那些希望能够加速汽车实际软件开发的开发人员提供帮助。这是我们可以贡献的主要内容之一，基本上就是这个基础级模型。他们可以接受它，他们可以在其之上进行额外的培训，他们可以定制它，然后他们可以部署它。但我们的目标基本上是为他们的开发过程提供一个运行的开始，其中包括我们已经为他们注入到这个模型中的所有数据、训练和计算。

## 如何帮助新 AV 开发者加速

**SECTION_NOTE**
- 起步需数据中心 GPU、车载开发套件、传感器组
- AV 开发是『数据飞轮』：采集—处理—训练—测试循环
**END_SECTION_NOTE**

**[06:53 – 07:10]**
**EN:** Harry Campbell: Yeah. So I guess if let's say I was, starting my own one man AV company, I don't know if I'd recommend that, but you might need a few more people and a few more. Sounds ambitious, but yes, yes. If I was starting and I guess I came to NVIDIA, what would you tell me or where would I start?
**中文：** Harry Campbell：是的。所以我想，如果假设我正在创办自己的一个人 AV 公司，我不知道我是否会推荐这样做，但你可能需要更多的人和更多的人。听起来雄心勃勃，但是是的，是的。如果我刚开始工作并且我想我来到了 NVIDIA，您会告诉我什么或者我会从哪里开始？

**[07:10 – 08:04]**
**EN:** Matt Cragun: So actually, Alpamayo is a great place to start. Typically, developers will need a mix of things. So you need some hardware to get started. There's typically hardware that you need in the data center to work with the models. We have some hardware to go in a car, a development car, and we have, development kits to go in cars, and we have development sensor sets, and we have, obviously, GPUs that go in data centers. I think people know that. On top of that, we have a whole bunch of different software that we can help you with to get started. So typically you need two things. You need some software as infrastructure that you can use to, I mean, AV development is really about turning the flywheel, right? And these models are data driven. So you want to take data in, you want to process that data, train a new model, test the model, figure out where it needs improvement, and then do that cycle again, right?
**中文：** Matt Cragun：所以实际上，Alpamayo 是一个很好的起点。通常，开发人员需要混合多种东西。因此，您需要一些硬件才能开始。数据中心通常需要硬件来处理模型。我们有一些用于汽车的硬件，一辆开发汽车，我们有用于汽车的开发套件，我们有开发传感器组，显然，我们有用于数据中心的 GPU。我想人们都知道这一点。最重要的是，我们有一大堆不同的软件可以帮助您入门。所以通常你需要两件事。你需要一些软件作为基础设施，我的意思是，AV 开发实际上就是转动飞轮，对吧？这些模型是数据驱动的。所以你想要获取数据，你想要处理这些数据，训练一个新模型，测试模型，找出需要改进的地方，然后再次进行这个循环，对吗？

**[08:04 – 08:06]**
**EN:** Harry Campbell: And so there's an infrastructure
**中文：** Harry Campbell：所以有一个基础设施

**[08:06 – 08:37]**
**EN:** Matt Cragun: piece to that. Which you use to basically bring in your data and do simulation and select data, those sorts of things. And then you have the model, which is actually the thing that you're developing, and that gets deployed to the car. And so we have a wide range of tools. Alpamayo was certainly a great place to help get started. It's basically the raw material that you can use to build a policy that will go inside the car. But it's significantly more advanced than if you were just to start Completely from scratch. And so it gets you much further along that process.
**中文：** Matt Cragun：对此。您基本上可以用它来引入数据并进行模拟和选择数据之类的事情。然后你就有了模型，这实际上是你正在开发的东西，并将其部署到汽车上。因此我们拥有广泛的工具。 Alpamayo 无疑是一个帮助入门的好地方。它基本上是您可以用来制定车内保单的原材料。但它比您完全从头开始要先进得多。所以它会让你在这个过程中走得更远。

**[08:37 – 08:48]**
**EN:** Harry Campbell: Yeah, definitely makes sense. And I guess this might be a silly question, but do I need to use NVIDIA chips to be, kind of using these models and everything that you guys are offering with Alpamayo?
**中文：** Harry Campbell：是的，绝对有道理。我想这可能是一个愚蠢的问题，但是我是否需要使用 NVIDIA 芯片才能使用这些模型以及你们通过 Alpamayo 提供的所有内容？

## Alpamayo 有多开源？能否跑在非 NVIDIA 芯片

**SECTION_NOTE**
- 模型可部署到不同芯片，开源无锁定
- 但 NVIDIA 自身经验主要集中在自家芯片上
**END_SECTION_NOTE**

**[08:48 – 09:23]**
**EN:** Matt Cragun: That's a great question. The model itself that we build and we ship has obviously been built and developed on NVIDIA GPUs, and so it runs really well on NVIDIA GPUs. It can be deployed into a car on an NVIDIA chip that goes in the car, but you can certainly deploy it onto a different chip. If you wanted to, that could be done. We don't have a lot of experience doing that, as you might imagine. We certainly have a bias towards a certain brand of chips, but yeah, it could be done. It's open source, so there's no lock in here.
**中文：** Matt Cragun：这是一个很好的问题。我们构建和交付的模型本身显然是在 NVIDIA GPU 上构建和开发的，因此它在 NVIDIA GPU 上运行得非常好。它可以部署到汽车中的 NVIDIA 芯片上，但您当然可以将其部署到不同的芯片上。如果你愿意的话，那是可以做到的。正如您可能想象的那样，我们在这方面没有太多经验。我们当然对某个品牌的芯片有偏见，但是，是的，这是可以做到的。它是开源的，所以这里没有锁定。

**[09:23 – 09:36]**
**EN:** Harry Campbell: Gotcha. And I mean, I think that the obvious analogy that comes to my head, I think maybe you guys have even spoken to it in the past, that this is sort of the Android of AV. Is that a fair kind of analogy or description?
**中文：** Harry Campbell：明白了。我的意思是，我认为我脑海中浮现出一个明显的类比，我想你们过去甚至可能已经说过，这有点像 AV 的 Android。这是一个公平的类比或描述吗？

## Hyperion 与 AV 硬件平民化

**SECTION_NOTE**
- Hyperion 是含传感器的参考架构，驱动已写好即插即用
- 厂商可替换供应商；被比作『AV 的 Android』
**END_SECTION_NOTE**

**[09:36 – 10:34]**
**EN:** Matt Cragun: Yeah, I think that's a good description. We have effectively almost all of the components, if you want to build an AV yourself, that you could assemble and put together. And they're designed in such a way. We also have, as an example, an architecture for hardware, not just the chip in the car, but the sensors. It's called Hyperion. And Hyperion is a set of sensors where we have already built drivers that plug into our hardware. And you can order the Hyperion sensors, and it just works out. And it's still flexible. That way, if you're a manufacturer and you have a particular supplier that you really want to work with, you can swap some of those things out. But to the extent that you kind of align with the tooling and some of the products and some of the infrastructure and tools that we've already built, it kind of eases your development cycle because a lot of the hard parts and the acceleration and some of the other things that you'd want to do is already done for you.
**中文：** Matt Cragun：是的，我认为这是一个很好的描述。我们实际上拥有几乎所有组件，如果您想自己构建 AV，您可以组装并组装在一起。它们就是这样设计的。例如，我们还有一个硬件架构，不仅是汽车中的芯片，还有传感器。它的名字叫海伯利安。 Hyperion 是一组传感器，我们已经构建了可插入硬件的驱动程序。您可以订购 Hyperion 传感器，一切顺利。而且它仍然很灵活。这样，如果您是制造商并且您有一个真正想与之合作的特定供应商，您可以交换其中的一些东西。但是，如果您与我们已经构建的工具和一些产品以及一些基础设施和工具保持一致，它就会简化您的开发周期，因为许多困难的部分和加速以及您想要做的其他一些事情已经为您完成了。

**[10:34 – 10:54]**
**EN:** Harry Campbell: Gotcha. So it sounds like Harry's AV company, Company of One, I think the only thing I might need is a car, right? Obviously, a lot of companies are gravitating toward this Hyundai Ioniq 5, which is famous for being software-defined vehicles. Is that kind of all I would need? And are there other vehicles that you guys work with, or how does that work?
**中文：** Harry Campbell：明白了。听起来就像哈利的 AV 公司，Company of One，我想我唯一需要的就是一辆车，对吧？显然，许多公司都被现代 Ioniq 5 所吸引，它以软件定义汽车而闻名。这就是我所需要的一切吗？你们还使用其他车辆吗？或者它们是如何工作的？

## Hyperion 与车型无关、易集成

**SECTION_NOTE**
- 与多家 OEM 合作，车辆已预装 Hyperion 传感器组
- 开箱即用，作为开发平台
**END_SECTION_NOTE**

**[10:54 – 11:22]**
**EN:** Matt Cragun: Yeah, I mean, we have... We work with a lot of vehicles. We're basically vehicle agnostic. If you were actually to go out and purchase a vehicle, we have, there are OEMs that are building vehicles that are already on the, basically the Hyperion sensor set. So they already have that being built into their cars. And so that makes it really easy. the hardware is kind of already in place for you to be able to use that as a platform to do your development.
**中文：** Matt Cragun：是的，我的意思是，我们……我们与很多车辆合作。我们基本上对车辆不可知。如果你真的要出去购买一辆车，我们有，有一些原始设备制造商正在制造已经安装在 Hyperion 传感器组上的车辆。所以他们已经将其内置到他们的汽车中。这使得事情变得非常容易。硬件已经就位，您可以将其用作进行开发的平台。

## L4 如何从 Robotaxi 走向消费级车辆

**SECTION_NOTE**
- OEM 正把车做成『L4 capable』，靠 OTA 后续解锁 L4
- 最新 Hyperion（CES 发布）即 L4 就绪架构
**END_SECTION_NOTE**

**[11:22 – 11:42]**
**EN:** Harry Campbell: Yeah, I think that's a good point. I know you guys have announced some partnerships with OEMs. Is the model different, though, use case for OEMs versus robotaxis? Because OEMs are typically going more towards the L2 or the L2+, and robotaxis like Waymo and others are obviously shooting for more of a L3, L4, right?
**中文：** Harry Campbell：是的，我认为这是一个很好的观点。我知道你们已经宣布与原始设备制造商建立一些合作伙伴关系。但是，对于 OEM 与机器人出租车来说，该模型的用例是否有所不同？因为 OEM 通常更倾向于 L2 或 L2+，而 Waymo 等机器人出租车显然更倾向于 L3、L4，对吗？

**[11:42 – 13:24]**
**EN:** Matt Cragun: Yeah, so it's a really good question. I think that we're seeing a lot of things change in the industry generally. So the two things that I would say is that I think if you look at the past five years, that any level of autonomy in your car, L2, L2++, has basically, with the exception of maybe like AEB and Lane Keep and some of the other things that are at this point kind of industry standard, but most of the autonomous features have basically become Have in the past were kind of bonus features, right? It's a nice to have. I think as we look going forward that many of those basic features are going to become whether or not they're mandated by industry will be something that consumers look for specifically as a basic feature of their car, right? Yeah. Like this car doesn't have cruise control. That's crazy, right? Like the same thing I think is as we go forward that a lot of those autonomous features will fall into that same category. And then if you look at where we see when we talk with a lot of the automakers right now, We see a lot of automakers prepping their vehicles so that they're L4 capable. And what that means is that even though when they release it, their SOP date or their target started production date, they may not have a full L4 feature set. They want to make sure that the vehicles... With just a simple over-the-air update could become an L4 vehicle. And so we actually see most of the OEMs that we're working with. And actually, if you look at our newest Hyperion architecture, which we released at CES, is designed such that it could be an L4 capable system.
**中文：** Matt Cragun：是的，这是一个非常好的问题。我认为我们看到整个行业发生了很多变化。所以我要说的两件事是，我认为如果你看看过去的五年，你的汽车中的任何级别的自动驾驶，L2，L2++，基本上，除了 AEB 和车道保持以及其他一些目前已成为行业标准的东西，但大多数自动驾驶功能基本上已经成为过去的奖励功能，对吗？很高兴拥有它。我认为，随着我们展望未来，无论行业是否强制要求，许多基本功能都将成为消费者特别寻找的汽车基本功能，对吗？是的。就像这辆车没有定速巡航一样。这太疯狂了，对吧？就像我认为的那样，随着我们的前进，许多自主功能将属于同一类别。然后，如果你看看我们现在与许多汽车制造商交谈时看到的情况，我们会看到许多汽车制造商正在为他们的车辆做好准备，使其具备 L4 能力。这意味着，即使他们发布、SOP 日期或目标开始生产日期，他们也可能没有完整的 L4 功能集。他们希望确保这些车辆……只需进行简单的无线更新就可以成为 L4 车辆。因此，我们实际上看到了与我们合作的大多数原始设备制造商。事实上，如果你看看我们在 CES 上发布的最新 Hyperion 架构，就会发现它可以成为一个支持 L4 的系统。

**[13:24 – 14:11]**
**EN:** Harry Campbell: Yeah. Well, that would definitely be an exciting jump because I do feel like you're right. I think that, if you look at cars like Subaru or RAV4, a lot of these, kind of more, I'm not going to call them boring, but, normal cars, right? That people don't think of in the Tesla and the Waymo and, even Rivian category. They've had lane keep and, cruise control assist, right, that keeps you from hitting the car in front or behind you for, two, three, four, five years in some cases. And so it sort of seems like on the OEM side, there's kind of you guys are prepping for this big jump, right? Like a lot of cars out there have these L2 or L2++ features as standard or, slight add-on, but you're kind of prepping them for that jump versus RoboTaxi. everyone, obviously the goal with RoboTaxi is to remove the driver. So they kind of need to get towards that L4 quicker, right?
**中文：** Harry Campbell：是的。嗯，这肯定是一个令人兴奋的跳跃，因为我确实觉得你是对的。我认为，如果你看看像斯巴鲁或 RAV4 这样的汽车，很多这样的汽车，更多，我不会称它们无聊，但是，普通汽车，对吗？人们在 Tesla 和 Waymo 甚至 Rivian 类别中都没有想到这一点。他们有车道保持和巡航控制辅助功能，在某些情况下，可以让你在两年、三年、四年、五年内不会撞到前面或后面的汽车。因此，在 OEM 方面，你们似乎正在为这一巨大的飞跃做好准备，对吗？就像很多汽车一样，这些 L2 或 L2++ 功能作为标准功能或轻微的附加功能，但你是在为它们与 RoboTaxi 的跳跃做好准备。各位，显然 RoboTaxi 的目标是消除司机。所以他们需要更快地达到 L4，对吗？

**[14:11 – 15:06]**
**EN:** Matt Cragun: Yeah. And I think if you look at some of the announcements that have been made by various companies partnering together, we see as an example, Uber is working very hard to become essentially a The distributed platform for, obviously it's ride sharing, but essentially autonomous mobility is what they want to do in the future, right? So if you have a vehicle and you want to deploy it on the Uber network, then it needs to be capable of being able to do that. And so I think that we definitely are seeing that, the automotive industry is Depending on the design cycle, it's usually a three to five year design cycle. And so we're starting to see that they're starting to plan those hardware requirements now into their designs so that as the rest of the industry evolves, that they're not in a position where they're locked out of participating in some way because, they didn't have the proper hardware in their vehicle to begin with. Yeah, makes sense.
**中文：** Matt Cragun：是的。我认为，如果你看一下不同公司合作发布的一些公告，我们会看到一个例子，Uber 正在非常努力地成为一个分布式平台，显然它是乘车共享，但本质上自主移动是他们未来想做的，对吗？因此，如果您有一辆车并且想将其部署在 Uber 网络上，那么它需要能够做到这一点。因此，我认为我们肯定会看到，汽车行业取决于设计周期，通常是三到五年的设计周期。因此，我们开始看到他们现在开始将这些硬件要求规划到他们的设计中，以便随着行业其他公司的发展，他们不会因为他们的车辆中没有合适的硬件而无法以某种方式参与。是的，有道理。

## 深入 Alpamayo：工作原理与训练

**SECTION_NOTE**
- 模仿学习（imitation learning）打底
- 强化学习（RL）补低频 / 罕见场景；仿真环境用于持续评测
**END_SECTION_NOTE**

**[15:06 – 15:20]**
**EN:** Harry Campbell: Well, let's dig into the model a little bit. I guess this will be the technical part of our interview, but you mentioned, I guess there's kind of a couple of different parts. I guess first would sort of be more on the training and simulation. Is that kind of the first piece of it?
**中文：** Harry Campbell：好吧，让我们深入研究一下这个模型。我想这将是我们采访的技术部分，但你提到，我想有几个不同的部分。我想首先会更多地关注训练和模拟。这是第一部分吗？

**[15:20 – 15:32]**
**EN:** Matt Cragun: Yeah. So Alpha Mayo, we have a model itself, which we have tools to help you train it. And then we also have the simulator, which you can use to help you test the model.
**中文：** Matt Cragun：是的。所以 Alpha Mayo，我们本身就有一个模型，我们有工具来帮助你训练它。然后我们还有模拟器，您可以用它来帮助您测试模型。

**[15:32 – 15:40]**
**EN:** Harry Campbell: Got it. And how exactly would that work?
**中文：** Harry Campbell：知道了。那具体是如何运作的呢？

**[15:40 – 17:14]**
**EN:** Matt Cragun: Yeah, so the model is trained by Most often, a typical process we call is imitation learning. Imitation learning is where you take data examples of typically good behavior that you've observed, and then you feed those examples to the model, and it learns to imitate, like the name says, imitation learning, it learns to imitate the examples that you're feeding to it. After that, there's some advanced techniques that you can use. And we usually use this to help it overcome certain weaknesses or to train it to do specific behaviors, which is called reinforcement learning. And reinforcement learning is actually where the model can actually experiment. And as it experiments and as it begins to do something that we like, we reward it. And it starts to reward those behaviors that we like. And if it does something we don't like, we penalize it. And then it starts to stop doing those things that we don't like. And so usually you start with this process of imitation learning. You get the model to a point where it is working well. And that's usually based on just a massive amount of data that we've collected and observed over time. And then you start doing reinforcement learning typically for things where we have less data available. So especially if there's use cases or specific behaviors that we don't see very often, we can use reinforcement learning to help the model guide itself to what it should do in those unknown situations. And all of that, to do all of that process, especially the reinforcement learning side, we want to continually test and evaluate how we're doing. And so the simulation environment is how we do that.
**中文：** Matt Cragun：是的，所以模型是通过最常见的方式进行训练的，我们称之为模仿学习的典型过程。模仿学习是指你获取你观察到的典型良好行为的数据示例，然后将这些示例输入到模型中，它会学习模仿，就像它的名字所说的，模仿学习，它会学习模仿你输入的示例。之后，您可以使用一些高级技术。而我们通常用它来帮助它克服某些弱点或者训练它做出特定的行为，这就是所谓的强化学习。强化学习实际上是模型可以实际进行实验的地方。当它进行实验并开始做我们喜欢的事情时，我们就会奖励它。它开始奖励我们喜欢的那些行为。如果它做了我们不喜欢的事情，我们就会对其进行惩罚。然后它开始停止做那些我们不喜欢的事情。所以通常你会从模仿学习的过程开始。您可以使模型达到运行良好的程度。这通常基于我们随着时间的推移收集和观察的大量数据。然后你开始对我们可用数据较少的事情进行强化学习。因此，特别是如果存在我们不经常看到的用例或特定行为，我们可以使用强化学习来帮助模型引导自己在这些未知情况下应该做什么。所有这些，为了完成所有这些过程，特别是强化学习方面，我们希望不断测试和评估我们的表现。所以模拟环境就是我们做到这一点的方式。

## Alpamayo 的局限与按用例定制

**SECTION_NOTE**
- 模型 SOTA 但不完美
- 按地理 / 数据法规（如中国数据）做后训练；可偏向高速或城区架构
**END_SECTION_NOTE**

**[17:14 – 17:53]**
**EN:** Harry Campbell: Got it. Well, I guess I have to imagine that a lot of those learnings you would kind of want to apply to the entire model, right? So I'm curious to know what are the parts that, I as myself coming to NVIDIA and using the Elpa Maya model, I would kind of need to simulate and train. Yeah, that's a really good question. So as far as Alpamayo goes,
**中文：** Harry Campbell：知道了。好吧，我想我必须想象您想将其中的很多知识应用到整个模型，对吧？所以我很好奇，我自己来到 NVIDIA 并使用 Elpa Maya 模型时，我需要模拟和训练哪些部分。是的，这是一个非常好的问题。就阿尔帕马约而言，

**[17:53 – 19:18]**
**EN:** Matt Cragun: It's a great model. It's state of the art. It's also not perfect. Right. So we certainly don't claim that. And so there's certainly just helping the model to improve to the point where you'd feel comfortable deploying it on a car. But one of the things. And one of the things that we also observe is that there's a lot of ways that you can strengthen the model for specific use cases. So we see companies who are deploying vehicles in different geographies and different places. So that's certainly part of it. We work with a lot of partners who are overseas in some of Asian countries where, for various reasons, there's restrictions on data. So, as an example, Alpamayo hasn't been trained on any Chinese data to date, and there's... There's just data accessibility challenges that we have. And so zero shot, which means testing it out of the box on Chinese data, it performs well, but not as well as it could if it had more exposure to Chinese data. So we work with a lot of companies and they do some post-training themselves, again, for data access reasons. But then there are other things that, depending on the type of vehicle, you may have specific reasons why You want to focus more on a highway architecture or an urban architecture, and you can bias that data towards something that's important for you.
**中文：** Matt Cragun：这是一个很棒的模型。这是最先进的。它也并不完美。正确的。所以我们当然不会这么说。因此，这肯定会帮助模型改进到您可以放心将其部署在汽车上的程度。但其中一件事。我们还观察到的一件事是，有很多方法可以针对特定用例强化模型。因此，我们看到一些公司在不同的地理位置和不同的地方部署车辆。所以这肯定是其中的一部分。我们与许多海外合作伙伴合作，在一些亚洲国家/地区，由于各种原因，数据受到限制。因此，举个例子，迄今为止，Alpamayo 尚未接受过任何中国数据的培训，而且……我们面临的只是数据可访问性方面的挑战。因此，零射击，这意味着在中国数据上进行开箱即用的测试，它表现良好，但如果它更多地接触中国数据，它的表现就不会那么好。因此，我们与很多公司合作，出于数据访问的原因，他们自己也进行了一些后期培训。但还有其他一些事情，根据车辆的类型，您可能有特定的原因想要更多地关注高速公路建筑或城市建筑，并且您可以将该数据偏向于对您来说重要的东西。

## Alpamayo 的用例与思路

**SECTION_NOTE**
- 开源模型 ≠ 可直接量产；安全工程远超模型本身
- NVIDIA 也提供端到端全栈 + 经典栈双系统
**END_SECTION_NOTE**

**[19:18 – 19:34]**
**EN:** Harry Campbell: Cool. What kind of expectations do you set for your partners if they come to you? Do you tell them, oh, you should expect that, if you install everything and get it up and running, you'll be able to drive, the car will be able to drive itself around Los Angeles? Or how do they know kind of what to expect?
**中文：** Harry Campbell：凉爽的。如果你的合作伙伴来找你，你会对他们设定什么样的期望？你是否告诉他们，哦，你应该期望，如果你安装了所有东西并启动并运行，你将能够驾驶，汽车将能够在洛杉矶周围行驶？或者他们怎么知道会发生什么？

**[19:34 – 21:48]**
**EN:** Matt Cragun: I think it depends on what you mean by drive. So there's two things that are really important to deploying a vehicle. One is just, at least for Alpamayo itself, is just the raw capability of Alpamayo. How well does Alpamayo do? But then the other piece of it is actually to get something that you would want to use in production. There's a whole safety aspect that it goes well beyond Alpamayo in terms of how you'd engineer a vehicle. And so when we actually offer Alpamayo as an open source software We offer that as an open source model and people can use that and put it in their vehicle or work with that. But at the same time, we have some companies that we work with where we're involved in the full AV stack end to end. And we've announced some of those partnerships as well. We actually have, for the end-to-end stack, we have a whole parallel system that is inside the car. So we have Alpamayo, which is available, but then we also have what we call the classical stack, which is the type of stacks that have That's been built for a long time, which are a classical system, classical perception, DNN system that then generates the state of the world that then hands that off to a system that does the planning and control. In other words, a whole bunch of discrete blocks that are handling different functions of And then Alpamayo is this end-to-end thing, right? You pixels in and you get a trajectory out. And then what we do is we actually compare those two things and we have some guardrails in place and some constraints in place. And each one of those stacks is proposing a trajectory. and in the event that we don't like, or we're unsure, or there's a, a constraint that, we're not satisfied with, with Alpamayo, then we have this other trajectory, that we can, that we can choose. And so we have this arbitration layer and we can have a whole discussion if you want about safety and safety architectures, but, but suffice it to say that, Deploying a vehicle on the road in a safe way is actually significantly more complicated than just Alpamayo itself. So Alpamayo, like I said, is good raw material for building one of these AVs and can do some pretty amazing things even out of the box, but it's by no means sufficient.
**中文：** Matt Cragun：我认为这取决于你所说的驱动力是什么意思。因此，有两件事对于部署车辆来说非常重要。一是，至少对于 Alpamayo 本身来说，就是 Alpamayo 的原始能力。阿尔帕马约表现如何？但另一部分实际上是获得您想要在生产中使用的东西。就如何设计车辆而言，它在整个安全方面远远超出了 Alpamayo。因此，当我们实际上将 Alpamayo 作为开源软件提供时，我们将其作为开源模型提供，人们可以使用它并将其放入他们的车辆中或使用它。但与此同时，我们也与一些公司合作，参与端到端的完整 AV 堆栈。我们也宣布了其中一些合作伙伴关系。实际上，对于端到端堆栈，我们在汽车内部有一个完整的并行系统。所以我们有 Alpamayo，它是可用的，但我们也有所谓的经典堆栈，这是一种已经构建了很长时间的堆栈类型，它们是经典系统、经典感知、DNN 系统，然后生成世界状态，然后将其交给执行规划和控制的系统。换句话说，一大堆离散的块正在处理不同的功能，然后 Alpamayo 就是这个端到端的东西，对吗？你输入像素，然后得到一条轨迹。然后我们所做的就是实际比较这两件事，我们设置了一些护栏和一些限制。这些堆栈中的每一个都提出了一条轨迹。如果我们不喜欢，或者我们不确定，或者有一个我们不满意的约束，对于 Alpamayo，那么我们有另一个轨迹，我们可以，我们可以选择。因此，我们有这个仲裁层，如果您想了解安全性和安全架构，我们可以进行全面的讨论，但是，只要说一下，以安全的方式在道路上部署车辆实际上比 Alpamayo 本身要复杂得多。所以，正如我所说，Alpamayo 是构建这些自动驾驶汽车的良好原材料，甚至可以开箱即用地做一些非常令人惊奇的事情，但这绝不是足够的。

**[21:48 – 22:37]**
**EN:** Harry Campbell: Got it. So it sounds like it's sort of on the partner to, kind of walk through the various safety cases or, regulatory framework that, in California when they need a DMV permit, CPUC, and kind of prove all that out on the kind of actual driving side. But you guys, I guess, like, I like the way you put it. You provide that raw kind of capability of driving, right? Yep. And you mentioned too, I mean, the two, I guess that's pretty unique in, the kind of end-to-end stack working in parallel with a more classical approach. Is that how, can you talk a little bit more about that? Because I guess I was going to ask you what type of model Alpamayo is, since that seems to be all the rage these days, if it's end-to-end or, different approach, but I would love to dive into that with you.
**中文：** Harry Campbell：知道了。因此，听起来好像合作伙伴需要遍历各种安全案例或监管框架，在加利福尼亚州，当他们需要 DMV 许可证、CPUC 时，并在实际驾驶方面证明所有这些。但是你们，我想，我喜欢你们所说的方式。你提供了那种原始的驾驶能力，对吗？是的。你也提到了，我的意思是，这两者，我想这是非常独特的，那种端到端堆栈与更经典的方法并行工作。是这样吗，您能多谈谈吗？因为我想我会问你 Alpamayo 是什么类型的模型，因为这几天似乎很流行，它是端到端的还是不同的方法，但我很乐意与你一起深入探讨这个问题。

## 端到端 AI 与经典 AV 架构结合

**SECTION_NOTE**
- 安全靠多样性与冗余
- 端到端学自数据但难验证；经典栈确定性强；二者仲裁
**END_SECTION_NOTE**

**[22:37 – 24:15]**
**EN:** Matt Cragun: Yeah, I mean, the reason that we do that is twofold. One is just because it gives us a more robust system, but also for the safety and the validation targets that are important to us. Safety is all about two things. One is diversity, and the other is redundancy. So you want to be able to have multiple systems that can handle your task, and you don't want them to have the same single source of failure. So you want to have diversity and redundancy. When we think about our software architecture, we basically have one side of the software architecture that is this end-to-end stack. End-to-end stacks are great. This is Alpamayo, right? They learn from data. So we give it this imitation learning. And it's able to actually do some really incredible things in terms of its features and its behaviors that would just be way too hard to hand code as an engineer, right? Either with rules or heuristics or other things. It'd just be way too difficult. But by just observing a human doing some of these really complex things, it just learns how to do it, right? But at the same time, it's hard for those models to basically break apart and validate exactly why they're doing exactly what they're doing. And so that actually makes the validation case challenging. It also makes it hard that... If the model says to do something that we don't always have exactly the reasoning or the logic to know that maybe that's not the right thing to do. And sometimes these models do make judgments that we want to change.
**中文：** Matt Cragun：是的，我的意思是，我们这样做的原因是双重的。一是因为它为我们提供了一个更强大的系统，但也因为对我们来说很重要的安全性和验证目标。安全与两件事有关。一是多样性，二是冗余。因此，您希望能够拥有多个系统来处理您的任务，并且不希望它们具有相同的单一故障源。所以你想要有多样性和冗余性。当我们考虑我们的软件架构时，我们基本上有软件架构的一方面，即端到端堆栈。端到端堆栈很棒。这是阿尔帕马约，对吧？他们从数据中学习。所以我们给它这种模仿学习。就其功能和行为而言，它实际上能够做一些非常令人难以置信的事情，而这些对于工程师来说是很难编写的，对吧？要么用规则，要么用启发法，要么用其他东西。那就太难了。但只要观察人类做一些非常复杂的事情，它就会学会如何做，对吗？但与此同时，这些模型很难从根本上分解并验证它们为什么要做它们正在做的事情。因此，这实际上使验证案例变得具有挑战性。这也使得……如果模型要求做某事，但我们并不总是有确切的推理或逻辑来知道这可能不是正确的做法。有时这些模型确实做出了我们想要改变的判断。

**[24:15 – 24:16]**
**EN:** Harry Campbell: What would be
**中文：** Harry Campbell：会是什么

**[24:16 – 27:12]**
**EN:** Matt Cragun: a good example of that? Let me give you actually a good example of how these two stacks fit together that maybe makes the most sense. So a really good example, something that we encounter all the time when we drive in San Francisco is when we have to nudge into the oncoming lane. So you're driving down the street, there's a double parked vehicle, has their flashers on, and now you have to decide what to do, right? And normally, assuming that the oncoming lane of traffic is clear, as a human driver, you would just sneak into the oncoming lane, go around the vehicle and come back into your lane and continue on. That's actually a really difficult situation if you had to hand code all of the rules and the logic into when and why you move into the other lane. It's not actually very – it's something that we do all the time, but the logic there is actually – there's a lot. So what we do is we have – We want to make sure that we have two things. Number one, we want to make sure that we always have, most importantly, we always have a safe behavior. And the safe behavior is if there's a car in front of you in your lane, you just stop. You stop in lane. And that's not necessarily what I'll say is the preferred behavior as a user of the car, but it's definitely a safe behavior. So that's taken care of. Once that's taken care of, then you can talk about the preferred behavior. And so what we do is Alpha Maya is really good at executing a behavior like this lane nudge where it goes into the oncoming lane and comes back because it's observed humans do that a lot of times. And it can give you some explanations on how to do that, but it's not necessarily a rigid explanation or logical sequence of events that is... That you want to use for the validation or the safety case. On the other hand, we have our classical stack, which can propose the safe behavior. It recognizes there's an object in front of me and it knows how to stop in lane and it knows how to be safe. And so what we do is, that's why we have the arbitration. So we can make sure that basically the classical stack gives us a safe window of operation. It knows where it's safe for us to drive. And if it's not safe for us to drive, it has a default behavior that we know is safe. And because the classical stack is all these discrete components, it's easy for us to be able to check inputs and outputs and make sure that it's deterministic and it happens all the same way every single time and that is ability to recognize objects and And report issues meets our standards in terms of, the number of nines that we want in our percentage, of accuracy, right? So we feel good that it's doing its job and that it will always keep us safe. And then assuming that it gives us the all clear, it allows Alpamayo to take a more preferred trajectory if that's available.
**中文：** Matt Cragun：一个很好的例子？让我给你一个很好的例子来说明这两个堆栈如何组合在一起，这可能是最有意义的。这是一个很好的例子，当我们在旧金山开车时，我们经常遇到的事情就是我们必须慢慢驶入迎面而来的车道。当你沿着街道行驶时，有一辆并排停放的车辆，闪光灯也亮着，现在你必须决定要做什么，对吗？通常，假设迎面行驶的车道畅通无阻，作为人类驾驶员，您只需潜入迎面行驶的车道，绕过车辆，然后返回您的车道并继续行驶。如果您必须手动编写所有规则和逻辑以决定何时以及为何进入另一条车道，这实际上是一个非常困难的情况。这实际上并不是很多——这是我们一直在做的事情，但其中的逻辑实际上是——有很多。所以我们要做的就是我们拥有——我们想要确保我们拥有两件事。第一，我们要确保我们始终拥有，最重要的是，我们始终拥有安全的行为。安全的做法是，如果您前面的车道上有一辆车，您就停下来。你停在车道上。这不一定是我所说的作为汽车用户的首选行为，但这绝对是一种安全的行为。这样就解决了。一旦解决了这个问题，您就可以谈论首选行为。所以我们所做的是 Alpha Maya 非常擅长执行像车道推动这样的行为，它会进入迎面而来的车道并返回，因为据观察人类经常这样做。它可以为您提供一些关于如何做到这一点的解释，但它不一定是您想要用于验证或安全案例的严格解释或事件的逻辑顺序。另一方面，我们有经典的堆栈，它可以提出安全的行为。它识别出我前面有一个物体，它知道如何在车道上停车，它知道如何保证安全。所以我们所做的是，这就是我们进行仲裁的原因。所以我们可以确保基本上经典堆栈为我们提供了一个安全的操作窗口。它知道我们在哪里开车是安全的。如果我们驾驶不安全，它就会有一个我们知道是安全的默认行为。因为经典堆栈是所有这些离散组件，所以我们很容易能够检查输入和输出并确保它是确定性的，并且每次都以相同的方式发生，并且识别对象和报告问题的能力符合我们的标准，即我们想要的准确度百分比中的 9 个数，对吗？因此，我们感觉很好，因为它正在履行其职责，并且它将始终保证我们的安全。然后假设它让我们一切都清楚了，它允许 Alpamayo 采取更优选的轨迹（如果有的话）。

## 模型如何处理边缘场景

**SECTION_NOTE**
- 多数边缘 case 是数据问题，靠更多真实数据
- 用合成数据生成扩充罕见场景的曝光
**END_SECTION_NOTE**

**[27:12 – 27:59]**
**EN:** Harry Campbell: Hmm. Yeah, it's really amazing how much goes into just nudging around a car in San Francisco, whereas a human, kind of can. Yeah, we just do it. Yeah, just do it. Right. And you highlighted one case, but obviously there's, I don't know, infinite or, many more. Yeah, those are challenging behaviors that we have. Yeah. Got it. And how do you handle the edge cases, whether it's weather or, we've seen a lot of issues with, massive traffic or blackouts, or how do you kind of program that into the model and, handle that?
**中文：** Harry Campbell：唔。是的，在旧金山，在一辆汽车周围轻推一下就需要付出多少努力，而人类却可以做到这一点，真是令人惊讶。是的，我们只是这么做。是的，就这么做吧。正确的。你强调了一种情况，但显然，我不知道，有无限的或更多。是的，这些都是我们所拥有的具有挑战性的行为。是的。知道了。你如何处理边缘情况，无论是天气，还是我们已经看到的很多问题，大规模交通或停电，或者你如何将其编程到模型中并处理它？

**[27:59 – 28:50]**
**EN:** Matt Cragun: So the models respond really well to more data. Realistically, most of the edge case problems that we have are a data problem. And so as we expand and as we gather more data, we get more of those edge cases in. And then there are some edge cases that what we can do is when we see them, we don't see them a lot, but we see them every once in a while. Then we can expand essentially our exposure to those with synthetic data generation. So we have other tools. We haven't talked about a lot of them, which is fine. But we have other tools that help us with simulation and generative tools that can basically imagine these new scenarios that we might encounter and be able to give us effectively data that we can then train or model off of.
**中文：** Matt Cragun：因此，这些模型对更多数据的响应非常好。实际上，我们遇到的大多数边缘情况问题都是数据问题。因此，当我们扩展并收集更多数据时，我们会得到更多的边缘情况。然后有一些边缘情况，我们可以做的是，当我们看到它们时，我们不会经常看到它们，但我们偶尔会看到它们。然后我们可以从本质上扩大我们对合成数据生成的接触。所以我们还有其他工具。我们还没有谈论很多，这很好。但是我们还有其他工具可以帮助我们进行模拟和生成工具，这些工具基本上可以想象我们可能遇到的这些新场景，并能够为我们提供有效的数据，然后我们可以根据这些数据进行训练或建模。

**[28:50 – 29:20]**
**EN:** Harry Campbell: Got it. So I think definitely a compelling case for using Alpamayo, for AV developers and operators out there. Obviously, what are some of the downsides for an operator using this open source model instead of building their own? I mean, I think we've kind of done a pretty good job highlighting all the, I imagine there's massive time and cost savings, but do you lose some flexibility? It sounds like I can still kind of work with you and edit the model, but I'm curious, what are the trade-offs here?
**中文：** Harry Campbell：知道了。因此，我认为对于 AV 开发人员和运营商来说，使用 Alpamayo 绝对是一个令人信服的案例。显然，对于使用这种开源模型而不是构建自己的模型的运营商来说，有哪些缺点？我的意思是，我认为我们在强调所有方面做得相当不错，我想可以节省大量时间和成本，但是您是否会失去一些灵活性？听起来我仍然可以与您合作并编辑模型，但我很好奇，这里有什么权衡？

**[29:20 – 30:43]**
**EN:** Matt Cragun: Yeah, so the model, when you download the model, it comes with weights, and then it has some post-training scripts, which allow you to basically further train the model, either to adapt it to your sensors or adapt it to the place where you drive. And then it has some other scripts to basically help you use it. It comes with a... A lot of different components that everybody would need to build anyway. So our hope is that generally it's a net positive to the industry. There are some companies that feel really strongly about kind of... Data or code sovereignty, like they own everything top to bottom and that it's everything is in house. But they're just, they're companies that feel really strongly strategically that they don't want to have any dependencies. And so if that's the case, that's definitely, definitely a route that some companies choose to go. Our hope is, is that, a huge portion of all software development, including autonomous vehicle development, is built on top of open source, right? And so this is a place where we can contribute. We can contribute to the industry. We can help the whole industry, we hope, move faster and accelerate some of those companies. And to the extent that you're willing to have open source be a part of your strategy, then it works really well.
**中文：** Matt Cragun：是的，所以模型，当你下载模型时，它带有权重，然后它有一些训练后脚本，基本上可以让你进一步训练模型，要么让它适应你的传感器，要么让它适应你开车的地方。然后它还有一些其他脚本基本上可以帮助您使用它。它配备了...许多不同的组件，每个人都需要构建。因此，我们希望这总体上对行业产生积极的影响。有些公司对数据或代码主权有着强烈的感觉，就像他们自上而下拥有一切，而且一切都在内部。但他们只是，他们是那些在战略上非常强烈地认为他们不想有任何依赖的公司。如果是这样的话，这绝对是一些公司选择走的路线。我们的希望是，所有软件开发的很大一部分，包括自动驾驶汽车开发，都是建立在开源之上的，对吗？所以这是我们可以做出贡献的地方。我们可以为这个行业做出贡献。我们希望，我们可以帮助整个行业加快步伐，并加速其中一些公司的发展。如果您愿意让开源成为您战略的一部分，那么它就会非常有效。

## AV 开发现状

**SECTION_NOTE**
- L2++ 正变成『桌面赌注 / 标配』
- 厂商靠 L4 能力或个性化调校来差异化
**END_SECTION_NOTE**

**[30:43 – 31:30]**
**EN:** Harry Campbell: Yeah. I mean, I'm curious to get your take because it does seem like we're gravitating towards this place in the industry where, obviously there are AV operators deploying and doing paid driverless rides. And I don't know what percent of the AV driving, maybe you're the person to ask, but is, kind of like table six. I don't know whether it's 50 or 75% of the, puzzle of AV driving, a lot of people have figured out and are figuring out and you're kind of, presenting that in a box. And so it doesn't really seem like an opportunity for a company, to stand out. It seems like. Like they would want to use an Alpamayo for that. And then like you mentioned, go in with the weights and the measures and adapt for my style of driving or my vehicles or, kind of try to stand out in other areas. I'm curious to get your take on that and sort of where you see AV development at, more broadly.
**中文：** Harry Campbell：是的。我的意思是，我很想听听您的看法，因为我们似乎确实被行业中的这个地方所吸引，显然有自动驾驶运营商正在部署和进行付费无人驾驶乘车。我不知道自动驾驶汽车的比例是多少，也许你是要问的人，但有点像表六。我不知道这是否是 AV 驾驶难题的 50% 还是 75%，很多人已经弄清楚并且正在弄清楚，而你就像是把它放在一个盒子里。因此，对于一家公司来说，这似乎并不是一个脱颖而出的机会。看起来好像是。就像他们想要使用 Alpamayo 一样。然后就像你提到的那样，进行重量和测量，并适应我的驾驶风格或我的车辆，或者尝试在其他领域脱颖而出。我很想知道您对此的看法，以及您对 AV 开发的更广泛的看法。

**[31:30 – 32:49]**
**EN:** Matt Cragun: Yeah, I think it kind of goes back to the discussion that we had the beginning is I think that the vehicles and the technology is coming along at this point is developing quite quickly. And I think that consumers' expectations are starting to change, right? So a while ago, people expected to have AEB on their car and some of these more... The L2++ features were nice to haves. And I think we're moving into this situation in the next year to two to three years where a lot of these L2++ features are just going to become the table stakes. And then over time, I think... What we'll see is exactly what you described, which is that manufacturers will be looking to differentiate either by moving towards even more advanced features like these L4 features or making your car be L4 capable or L3 capable or L3 sometimes capable, whatever it is that they decide to do, or being able to do things to more sophisticated tuning of the driving model to your preferences as a consumer. So I did, but I definitely think we're starting to approach the point where basic L2 plus features are becoming just the expectation, not a bonus.
**中文：** Matt Cragun：是的，我认为这可以追溯到我们一开始的讨论，我认为目前的车辆和技术发展得相当快。我认为消费者的期望开始改变，对吧？不久前，人们期望在他们的汽车上配备 AEB 以及其他一些功能……L2++ 功能非常好。我认为我们将在未来一年到两到三年内进入这种情况，其中许多 L2++ 功能将成为赌注。然后，随着时间的推移，我认为...我们将看到的正是您所描述的，即制造商将寻求通过转向更先进的功能（例如这些 L4 功能）或使您的汽车具有 L4 功能或 L3 功能或有时具有 L3 功能（无论他们决定做什么）来实现差异化，或者能够根据您作为消费者的喜好对驾驶模型进行更复杂的调整。所以我这么做了，但我绝对认为我们已经开始接近这样一个阶段：基本的 L2+ 功能正变得只是期望，而不是额外的好处。

## 未来几年最让 Matt 兴奋的事

**SECTION_NOTE**
- 入行 8–9 年，L4 曾『永远还有五年』
- 如今『不到五年』且有清晰路径
**END_SECTION_NOTE**

**[32:49 – 33:07]**
**EN:** Harry Campbell: Definitely. So last question here, looking ahead, I'm curious what excites you most about the next few years of autonomous driving? You're obviously, spent a lot of time, you're working on it every day. And, what should we, what are you excited about personally? And, what should we expect from NVIDIA over the next few years?
**中文：** Harry Campbell：确实。那么最后一个问题，展望未来，我很好奇未来几年自动驾驶最让您兴奋的是什么？显然，你花了很多时间，每天都在努力。而且，我们应该做什么，你个人对什么感到兴奋？未来几年我们应该对 NVIDIA 抱有怎样的期望？

**[33:07 – 34:15]**
**EN:** Matt Cragun: I think for me, I've been working in the autonomous vehicle space now for eight or nine years, almost a decade, I guess. And every year, the promise of L4 has been perpetually five years away. And I think the thing that I'm most excited about right now is I actually do feel like we're at this point where It's within five years, right? It's no longer five years away. It's less than five years. And I feel like we're to the point where we have line of sight to that happening. And we look at the trajectory that we're on right now, and we look at the pace of development of the tools, and we look at just overall the pace of the industry as a whole. And we're going to, I have confidence that we're going to get there. And so that's, I think for me, that's the really exciting part is to be able to actually finally see that vision that we've had for a long time to kind of come into focus and to see that in hopefully the near future that will be there.
**中文：** Matt Cragun：我想对我来说，我已经在自动驾驶汽车领域工作了八九年了，我猜差不多有十年了。每一年，L4 的承诺都永远距离我们还有五年。我认为我现在最兴奋的事情是我确实觉得我们已经到了五年之内，对吧？已经不再是五年后的事了。时间还不到五年。我觉得我们已经可以看到这一切的发生了。我们着眼于我们现在所处的轨迹，我们着眼于工具的发展速度，我们着眼于整个行业的整体步伐。我们将会，我有信心我们会实现这一目标。所以，我认为对我来说，真正令人兴奋的部分是能够真正最终看到我们长期以来一直关注的愿景，并希望在不久的将来看到它。

## 收尾与结语

**SECTION_NOTE**
- 期待 Harry 首次乘坐 Alpamayo 驱动的车
**END_SECTION_NOTE**

**[34:15 – 34:36]**
**EN:** Harry Campbell: Yeah, no, it's definitely exciting to see the light at the end of the tunnel. And obviously it's a product that, consumers yourself, consumers can actually take it and ride and, experience it. So I'm definitely excited and looking forward to my first Alpamayo ride in the future. So hopefully that'll happen sooner rather than later. Appreciate it, Matt.
**中文：** Harry Campbell：是的，不，看到隧道尽头的曙光绝对令人兴奋。显然，这是一个消费者自己可以实际使用、乘坐和体验的产品。所以我非常兴奋并期待着未来我的第一次 Alpamayo 骑行。所以希望这会早点发生。欣赏它，马特。

**[34:36 – 34:36]**
**EN:** Matt Cragun: Yeah, so great. We'd love to get you in a car. So thanks for the time and we'll talk again soon.
**中文：** Matt Cragun：是啊，太棒了。我们很乐意送您开车。感谢您抽出宝贵的时间，我们很快就会再次交谈。
