## 开场：探访得州数据中心

**SECTION_NOTE**
- Dwarkesh 实地探访 Jane Street 位于得州的数据中心
- 嘉宾：技术团队共同负责人 Yaron Minsky、物理工程团队负责人 Dan Pontecorvo
- 核心疑问：纳秒级交易如何与 GPU 训练共存
**END_SECTION_NOTE**

**[—]**
**EN:** Dwarkesh: Jane Street is a partner on my podcast, and we had this fun idea: why don't I come visit the data center you run for training AI models? So I just toured your data center in Texas, led by Yaron Minsky—co-head of the tech group (the transcript mislabeled him as Ron Minsky)—and Dan Pontecorvo, who runs the physical engineering team. Thank you both for the tour. I'd never been to a place like this before, so this was my first visit, and it was fantastic. I've always been confused: since you trade at the nanosecond level, how can you also do GPU stuff? Maybe you can walk me through what your actual trading time horizons look like. When you make a trading decision, can you afford the cost—or the latency—of running a large model?
**中文：** Dwarkesh：Jane Street 是我播客的合作伙伴，我们想到的一个有趣点子是：为什么我不过来亲自参观一下你们运行的用于训练（AI模型）的数据中心呢？所以我刚刚在技术团队共同负责人 Yaron Minsky（译注：视频中口误及速记为 Ron Minsky）和物理工程团队负责人 Dan Pavatova（译注：速记为 Dan Ponttovo）的带领下，参观了这个位于德克萨斯州的数据中心。非常感谢两位带我参观。值得一提的是，我以前从未去过这种地方，所以我也是第一次参观，这太棒了。 以前我一直很困惑：既然你们需要在纳秒（nanosecond）级别进行交易，那你们怎么能做 GPU 相关的事情呢？也许你们可以详细讲讲，你们交易的实际时间跨度（时限）是怎样的？在做出交易决策的过程中，你们能负担得起运行大型模型的成本（或时间延迟）吗？


## 时间跨度的谱系：从 100 纳秒到数小时

**SECTION_NOTE**
- 交易并非单一时间跨度，而是从 100 纳秒到半小时/当天的完整谱系
- 极速段（100 纳秒内）只能靠 FPGA 直连网络，决策极简；越慢的段可做越大模型
- 最佳策略是集成（ensemble）：不同时间尺度用不同复杂度的决策
**END_SECTION_NOTE**

**[—]**
**EN:** Yaron: I think the key thing to understand here is that there isn't a single time horizon—there's a whole spectrum of them. Some of the trading systems we build, and some trades we do, to stay competitive you actually have to process and return a packet within 100 nanoseconds. That's a completely different technical regime, right? People sometimes ask, 'Oh, can you write high-performance stuff in OCaml?' Our answer is: 'We can. But at that speed it doesn't matter whether you write it in OCaml, Rust, or C++, because you can't use a CPU at all. You have to use an FPGA wired directly into the network. You return the packet so fast that if you put an oscilloscope on the input and output wires, you'd see the packet start leaving the output before it's even finished arriving on the input.' So that's a very different, very special domain. But when you're in that time regime, you can't actually do much computation—the decisions you make are very simple. In fact, there's a whole trade-off curve between how 'smart' a decision is—whether it's a model or even a hand-written decision process—and how fast you return it. And the right way to build the best trading strategy is really an ensemble approach. For some kinds of decisions you make very simple ones extremely fast; for others your operating scale might be—not 100 nanoseconds anymore, but maybe microseconds, tens of microseconds, hundreds of microseconds, or milliseconds; and in some cases a process that returns a decision within half an hour or by the end of the day is totally fine, and you're equally competitive on that time basis. But the type of decision you make is completely different across all those horizons.
**中文：** Yaron：我认为这里需要理解的核心一点是，并没有单一的时间跨度，而是存在着许多不同的时间跨度。我们构建的一些交易系统和进行的某些交易，为了保持竞争力，你实际上必须在 100 纳秒以内处理并返回一个数据包。这是一个完全不同的技术范畴，对吧？ 人们有时会讨论，比如：“哦，你们能用 OCaml 编写高性能的东西吗？”我们的回答是：“我们可以。但对于这种级别的速度，不管你是用 OCaml、Rust 还是 C++ 编写都不重要，因为你根本无法使用 CPU。你必须使用 FPGA，它直接通过导线连接到网络上。你返回数据包的速度非常快，如果你在输入和输出的导线上连接一个示波器，你会看到数据包在被完全接收完之前，就已经开始从输出端发出去了。” 所以这是一个非常不同、非常特殊的领域。但是，当你处于这个时间领域时，你实际上无法进行太多的计算，你所做的决策将会非常简单。事实上，在决策的“聪明程度”（无论是模型还是其他某种甚至是手写的决策过程）与“返回速度”之间，存在着一条完整的权衡曲线。 而构建最佳交易策略的正确方法，实际上是采用一种集成（ensemble）方法。对于某些类型的决策，你会非常迅速地做出非常简单的决策；对于某些类型的决策，你的运作规模可能是——不再是考虑 100 纳秒，也许是几微秒、几十微秒、几百微秒或毫秒；而在某些情况下，有些流程如果能在半小时或当天内完成决策返回，那也完全没问题，在这些时间跨度上，你在时间基础上同样具有竞争力。但在所有这些不同的时间跨度上，你所做的决策类型是完全不同的。

**[—]**
**EN:** Dwarkesh: Maybe you can't disclose this, but what are these models actually predicting? Surely not just the next tick in the order book—or maybe they are?
**中文：** Dwarkesh：也许你不便透露，但这些模型究竟在预测什么？肯定不只是订单簿（order book）中的下一个变动吧，或者也许就是？


## 模型在预测什么：公允价值

**SECTION_NOTE**
- 最经典也最重要的预测目标是某资产的公允价值（fair value）
- 可组合地融入多种交易流程；不止预测订单簿下一跳
**END_SECTION_NOTE**

**[—]**
**EN:** Yaron: We're clearly touching on topics that are hard to talk about publicly. But I think the simplest and most important one—and the one we've been thinking about, not just now but since 25 years ago when I joined Jane Street and was building models with linear regression—is predicting something's fair value. Like, what do we think this thing is actually worth? That can compose into many different trading flows in a very composable way. It's not the only class of thing we predict, but it's a very important one.
**中文：** Yaron：我们现在显然是在触及一些很难公开谈论的话题。但我认为最简单也最重要的一个，也是我们一直在思考的——不仅是现在在想，25 年前我刚加入 Jane Street、用线性回归等工具构建模型时就在想——一个非常有用、非常经典的事情就是预测某样东西的公允价值（fair value）。比如，我们认为这个东西真正值多少钱？这能够以一种非常可组合的方式融入到许多不同的交易流程中。这并不是我们作为预测目标的唯一一类事物，但它是一个很重要的目标。


## 推理放在哪：托管（colo）、FPGA 与 GPU 的权衡

**SECTION_NOTE**
- 推理可在 CPU / FPGA / GPU 上，取决于算力、模型大小与延迟
- 越大的模型在物理位置上越灵活；极速段甚至要量光纤长度
- 把 GPU 塞进交易所旁托管机房会受供电/冷却/服务商规则约束
**END_SECTION_NOTE**

**[—]**
**EN:** Dwarkesh: For a while there was this meme about what trading firms do: you've got to nail colocation—move next to the NASDAQ exchange, your machines have to be right there, that's super important.
**中文：** Dwarkesh：有一阵子，我感觉有一种关于交易公司在做什么的梗（meme），那就是：你必须搞定服务器托管（colo），搬到纳斯达克交易所所在的地方，你的机器必须紧挨着那儿，这非常重要。

**[—]**
**EN:** Yaron: Without going into where we put what specifically, your inference process might run on CPU, on FPGA, or on GPU, depending on how much compute you need, how big the model is, what latency you need to return. Yes, the bigger, slower things you can put farther away. Cramming all your compute right next to the exchange is a headache. And for the truly extremely fast stuff, just being in the colo isn't enough—you even care about how long the cable coil is, because at those nanosecond levels you really have to measure the fiber length. But in general, bigger models give you far more flexibility in where they're physically placed.
**中文：** Yaron：在不深入讨论我们把什么东西放在哪里的具体细节的前提下，你的推理（inference）过程可能在 CPU 上，可能在 FPGA 上，也可能在 GPU 上，这取决于你需要多少计算量、模型有多大、需要怎样的延迟返回等约束条件。 是的，更大、更慢的东西，你可以把它放得更远一些。把所有的计算设备都紧挨着交易所放置是很令人头疼的。而对于那些真正极其快速的事物，仅仅待在托管机房里是不够的，你甚至会关心通往那里的线缆线圈有多长——在那种极低的纳秒级别下，你真的需要去测量光纤布线的长度。但总的来说，更大的模型在它们物理放置的位置上给你带来了大得多的灵活性。

**[—]**
**EN:** Dan: If we put GPUs in those colo facilities next to the exchange, now you have to follow their rules—whoever is the provider giving you that space. Also, your power, cooling, all those constraints are now a bit tighter than in a facility you design and operate yourself. So you have to come up with things like: 'Hey, maybe I can only fit one GPU per rack because it draws so much power, so I have to spread them out instead of being able to do efficient liquid cooling in a single rack.' So as our compute needs keep growing, these are the things we have to think about.
**中文：** Dan：如果我们把 GPU 放在交易所旁边的这些托管设施中，现在你必须遵守他们的规则，你懂吧，是谁作为服务商为你提供那个空间。此外，你的电力、冷却，所有这些约束条件现在可能都比你自己设计和运营的设施要稍微更紧俏一些。所以，你现在必须想出一些办法，比如：“嘿，可能一个机架里我只能放一个 GPU，因为它消耗太多电了，所以我必须把它分散开来，而不是能够在一个机架里实现高效的液冷。”所以随着我们的计算需求不断增长，这些都是我们需要考虑的事情。


## 60 亿美元 CoreWeave 协议与 Jane Street 的「规模定律」

**SECTION_NOTE**
- 与 CoreWeave 签下 60 亿美元算力协议
- 与基础模型实验室不同：价值来自模型架构的多样性与海量实验
- 专用化源于数据源差异与「字节/浮点比」——金融数据噪声大、量更大
**END_SECTION_NOTE**

**[—]**
**EN:** Dwarkesh: You recently signed a $6 billion compute deal with CoreWeave (transcript misheard as 'core reef'). So what are you going to use it for?
**中文：** Dwarkesh：你们最近与 CoreWeave（译注：速记错录为 core reef）签署了一项价值 60 亿美元的计算协议。嗯，你们打算用它来做什么？

**[—]**
**EN:** Yaron: Other parts of the AI world have scaling laws, and we have our scaling laws too—there are a lot of models we want to train. I think the interesting and possibly different point versus more traditional AI labs is the diversity of our model architectures and the number of experiments we're running. So a lot of the value comes from people trying a lot of very different new things in model design, giving researchers faster iteration times so they can discover more ideas and drive more innovation—and that turns out to be extremely important.
**中文：** Yaron：AI 世界的其他领域有规模定律（scaling laws），我们也有我们的规模定律，有很多模型我们都想训练。我认为我们与那些更传统的 AI 实验室之间有趣且可能不同的一点在于，我们模型架构的多样性以及我们正在进行的实验数量。因此，你从中获得的大部分价值就在于，大家在模型设计中尝试了大量非常不同的新事物，给研究人员提供了更快的迭代时间，让他们能够发现更多的想法并推动更多的创新，这被证明是极其重要的。

**[—]**
**EN:** Dwarkesh: In the case of those foundation-model labs, there's a benefit to training one fully general model that does everything, rather than building a bunch of custom different models. Can you help me understand why at Jane Street the trade-offs are different?
**中文：** Dwarkesh：在那些基础模型实验室的情况下，训练一个能够做所有事情的、完全通用的单一模型是有好处的，而不是构建一堆定制的不同模型。你能让我了解一下，为什么在 Jane Street 会有不同的权衡取舍吗？

**[—]**
**EN:** Yaron: For us, some of the specialization is to be able to fit and consume the right data types, right? There are a huge number of potential data sources we can feed in. For example, we have many differences in the data rates we need to hit. Another factor that forces some specialization in what we do is that the overall inference and trading dynamics differ completely because of the 'bytes-to-flop ratio.' The data we train on is much larger, but per byte it carries less information, because financial data is very noisy. So the models tend to be smaller, while the data is noisier, has more noise, and is much larger in volume. Also, the different models we build for different applications differ from each other, right? When we figure out 'how do we exploit the additional information we get,' it involves all kinds of decisions—from 'how do we efficiently store and load data,' to 'how do we shape the model,' to 'how do we give the inference process the throughput and latency it needs.' There's a completely different set of trade-offs, so sorting that out and picking the best option for each application is very valuable.
**中文：** Yaron：对我们来说，某些专门化是为了能够适应和消耗正确的数据类型，对吧？我们可以喂进去的潜在数据源非常多。比如我们在需要达到的数据速率上存在许多差异。 另一个让我们需要对所做的工作进行某些专门化的因素是，整体的推理和交易动态都因“字节与浮点运算比率”（bytes to flop ratio）的不同而变得截然不同。我们用来训练模型的数据量要大得多，但就单字节而言，这些信息量却比较少，因为金融数据噪声（noise）非常大。是的。因此，模型往往更小，而数据往往噪声更大、噪声更多，且数据量要大得多。 另外，我们针对不同应用构建的不同模型之间也是不一样的，对吧？当我们试图找出“我们该如何利用我们获得的更多信息”时，就会涉及到各种决策，从“我们如何高效地存储和加载数据”，到“我们如何塑造模型”，再到“我们如何让推理过程具备它所需的吞吐量和延迟”。这其中会有一整套截然不同的权衡。因此，去理清这些并为不同的应用挑选出最佳方案，是非常有价值的。

**[—]**
**EN:** Dwarkesh: So what does your inference workload actually look like, or how does it compare to the big companies running LLM chatbots?
**中文：** Dwarkesh：那你们的推理（inference）工作负载实际上是怎样的，或者说，它与传统的那些做大语言模型聊天机器人的大公司相比如何？


## 推理工作负载：延迟、批处理与极高的数据速率

**SECTION_NOTE**
- 延迟比 LLM 聊天机器人更关键；批处理仍是问题
- 单一市场（如纳斯达克行情）内因果序列化数据速率极高
- 更关注数据加载；自研大规模对象存储
**END_SECTION_NOTE**

**[—]**
**EN:** Yaron: Broadly, as you'd expect, latency matters more. Batching is still an issue; depending on the model you may have disaggregated models or parts of a model for the different symbols you're watching. So pulling data from multiple sources and batching it together matters too. I think another interesting point is that the data rate is really high. At big LLM labs the aggregate data rate from all users is high, but the sequential data from any single user is small; whereas when you're pulling bytes from the NASDAQ feed, the serial data rate you have to consume causally, within a single domain, is enormous. So again, the dynamics change. But I think a lot of the underlying engineering problems are similar—it's just that all the constants are tuned to different places, so you end up making different choices.
**中文：** Yaron：大体上说，正如你所预料的，延迟更为关键。批处理（batching）仍然是一个问题，取决于你所做的模型，你可能会有针对你所观察的不同交易代码（symbols）进行解耦/分散（disaggregated）的模型或模型的一部分。因此，从多个数据源拉取数据并将其打包批处理在一起同样会产生影响。 我认为另一个有趣的点是，数据速率真的非常高。在大型大语言模型实验室里，你从所有不同用户那里获得的总体（聚合）数据速率也很高，但你从任何单一用户那里获得的序列数据量（sequential data）并不大；而当你拉取的数据是来自纳斯达克行情馈送（NASDAQ feed）的字节时，天哪，在单一领域内需要以因果前后相继的方式进行序列化消耗的数据速率极高。所以再次强调，这里的动态发生了改变。不过我认为，很多类似的基础工程问题其实大同小异，只是所有的常量都被微调到了不同的位置，因此你最终做出了不同的选择。

**[—]**
**EN:** Dwarkesh: So what does that mean concretely for how you have to design these systems, from storage and otherwise?
**中文：** Dwarkesh：这意味着在你们必须如何设计这些系统方面，无论是从存储还是其他方面来看，有什么具体体现？


## 存储、x86 与去中心化：被打破的两条捷径

**SECTION_NOTE**
- 曾靠「全 x86」与「单一大型数据中心」两条捷径简化工程
- 如今电力受限、需全球分布式数据中心，计算与存储调度深度耦合
- 被迫支持 ARM，放弃纯 x86
**END_SECTION_NOTE**

**[—]**
**EN:** Yaron: Yes, I think we care more about data-loading performance than you typically see. We're doing a lot of work building our own large-scale data storage system, our own internal object store. We've used various vendors' products over time, but I think for some of these research-oriented use cases we need to run at a larger scale and deal with data-center diversity. Right? It's less an inference-time problem and more a training-time problem—we just can't get all the compute we want in one place. I don't know, I think a general trick to running a tech org effectively is figuring out which shortcuts you can take. One shortcut we were lucky to take for years was pretending the planet has only one CPU architecture—everything targeting x86_64, pretending nothing else exists—which simplified a lot. We also had one big research data center and one big storage cluster, which simplified a lot. And both of those are now broken. You just can't get that much power—you can't bring enough power into a single data center (Yaron jokingly called it 'thunderbolts') to power everything you need, so you have to build data centers around the world. So there's a huge disaggregation problem, which gives you a puzzle like: oh, now you have to interleave your compute scheduling and storage scheduling tightly. And there's a massive amount of data, so moving it between them is non-trivial. Also, we've had to give up 'x86-only' because Nvidia shipped a bunch of cool new products, which means you now have to support ARM too.
**中文：** Yaron：是的，我认为与你通常看到的相比，我们对数据加载性能的关注度更高。我想我们正在做大量工作来构建我们自己的大规模数据存储系统，我们自己的内部对象存储（object store）。我们之前使用过各种供应商的产品，但随着时间的推移，我认为对于其中一些以研究为导向的用例，我们需要在更大的规模下运行，还需要应对数据中心的多样性。 对吧？这不太是一个推理时的问题，而更多是一个训练时的问题——也就是说，我们就是无法在同一个地方获得我们想要的所有计算资源。我不知道，我觉得总的来说，有效运营一个技术组织的一个重要诀窍就是去弄清楚你可以走哪些捷径。 我们多年来很幸运能够走的一个捷径是，我们可以假装这个星球上只有一种 CPU 架构，比如所有东西都是针对 x86_64 的，我们假装其他任何东西都不存在，这简化了许多事情。我们还曾拥有一个大型的研究数据中心和一个大型的存储集群，这也极大地简化了许多事情。 而实际上，这两点现在都已被打破了。比如，你就是无法获得那么大的电力，你无法在同一个数据中心里接入足够多的电力引入（译注：此处 Yaron 幽默地用了“thunderbolts/雷电”一词指代极高电力）来为你所需的所有事物供电，你需要把数据中心建在世界各地。所以这里存在一个巨大的去中心化/分散（disaggregation）问题，这也给你带来了一个难题，比如：哦，现在你必须考虑让你的计算调度和存储调度紧密交织在一起。而且有海量的数据，因此在它们之间移动这些数据绝非易事。 另外，我们也不得不放弃“仅限 x86”的做法，因为英伟达推出了一系列酷炫的新产品，这意味着你现在必须支持 ARM 架构了。

**[—]**
**EN:** Dwarkesh: Zooming out, I want to ask a very naive question. There's a naive view that if you had AGI it could immediately do what Jane Street does. Help me understand why that naive view is naive.
**中文：** Dwarkesh：放大视角，我想问一个非常天真的问题。可能会有一种天真的看法，认为如果你拥有了通用人工智能（AGI），它就能立刻做 Jane Street 所做的事情。请让我了解一下，为什么这种天真的看法是天真的？


## 交易是「AGI 完全」问题

**SECTION_NOTE**
- 激进问题：AGI 会立刻让 Jane Street 失业吗？——距离尚远
- 交易类似「AGI 完全」/「NP 完全」：万事最终汇入交易
- 人类认知比以往更有价值；招聘需求更强
**END_SECTION_NOTE**

**[—]**
**EN:** Yaron: Yes, I don't want to totally dismiss it. There is a picture of the world we have to take seriously: that we build LLMs or other AI systems that are strictly smarter than all humans on Earth, more capable on every cognitive task. Yes, that would be incredible; that's a completely different state. In that case, a large part of what Jane Street does could be automated, maybe we'd all sit back and drink more margaritas or something—I don't know what that world looks like. But it feels like we're not especially close to that stage. I think overall people easily underestimate how rich and complex this work is—not just at a company like Jane Street, but in any truly ambitious, hard, corporate-scale task. I especially feel that trading is kind of like an 'AGI-complete' problem, similar to how 'NP-complete' is. That means all the different problems in the world eventually bear on what you're doing in trading, because at the end of the day trading is about figuring out what things are worth, which means predicting the future, and a huge number of different things feed into that. As the parts get automated one by one, you run into the usual situation: the other hard parts we don't yet know how to automate well become the source of competitive advantage. I feel human cognition is more valuable than ever. I've never wanted to hire more engineers and traders than I do today, because everything people do is more valuable than before. Part of that is my skepticism that we're as close to models smarter than humans at everything as some think.
**中文：** Yaron：是的，我不想完全否定它。确实有这样一种世界景象是我们需要认真对待的：也就是我们将构建出大语言模型或其他人工智能系统，它们在严格意义上比地球上的所有人类都更聪明，在所有认知任务上都更有能力。是的，那将会很不可思议，那将是一种完全不同的状态。在那种情况下，确实，Jane Street 所做的很大一部分事情可能会被自动化取代，也许我们大家都会坐享其成，多喝点玛格丽特鸡尾酒之类的，我不知道那个世界会是什么样子。但感觉我们现在距离那个阶段还不是特别近。 我认为总的来说，人们很容易低估这项工作的丰富性和复杂性，不仅是像 Jane Street 这样的公司所做的工作，实际上在任何真正有野心、高难度的公司级任务中都是如此。我尤其觉得，交易对我来说有点像“AGI 完全”（AGI-complete）问题，类似于“NP 完全”（NP-complete）问题。 这意味着世界上所有不同的问题最终都会在交易背景下影响你正在做的事情，因为归根结底，交易涉及弄清楚事物的价值，这意味着对未来做出预测，而许多不同的事情都会汇入其中。随着其中的各个部分被逐渐自动化，你就会遇到常见的情况：那些我们还不知道如何很好地自动化的其他困难部分，最终成为了竞争优势之所在。 我觉得人类和人类的认知比以往任何时候都更有价值。我从来没有像今天这样迫切地想要招聘更多的工程师和交易员，因为人们所做的每一件事都比过去更有价值。我的意思是，这在一定程度上是因为我持有一些怀疑态度，不认为我们距离在所有事情上都比人类聪明的模型像某些人想象的那么近。

**[—]**
**EN:** Dwarkesh: Maybe this touches on physical infrastructure—actually nailing the colo—or maybe it's the software infrastructure you build. Can you help me understand what actually...
**中文：** Dwarkesh：也许这涉及到物理基础设施，比如实际搞定托管机房；也许实际上是你们构建的软件基础设施。能让我了解一下到底是什么东西会……

**[—]**
**EN:** Yaron: Yes, we build all kinds of extremely complex software for people to think about many different trading problems, some of which aren't very electronic at all. The diversity of this business is far richer than people imagine. There's a view like: 'Oh right, that must be a simple thing—you just need a bunch of smart people making smart decisions and writing good software, and if we automate the smart part we're done.' But I think it's more complex than that.
**中文：** Yaron：是的，我们构建了各种各样极其复杂的软件，让人们去思考许多不同的交易问题，其中一些问题根本不怎么电子化。这个业务的多样性远比人们以为的要丰富得多。有一种想法是：“哦，对，那肯定是一件很简单的事，你只要有一群聪明的人，他们做出聪明的决策，写出优质的软件就行了。如果我们能把聪明这部分自动化，那就万事大吉了。”但我认为事情要比这复杂得多。

**[—]**
**EN:** Dwarkesh: What do you mean by the 'non-electronic' part of trading?
**中文：** Dwarkesh：你所说的交易中“非电子化”的部分是指什么？

**[—]**
**EN:** Yaron: I mean there's still trading done through chat between people, communicating and making decisions together. For example, someone will assess how much adverse selection the person on the other end of the phone represents—that's still a very real part of the business. There are different kinds of securities that take much longer to automate to a higher degree. For instance, the bond business is far less automated than what you see in equities. We're actually a bit puzzled by this ourselves. Those of us who've been in the industry a while—I started a bit late, so I didn't witness the equitization transition firsthand—but those who paid attention earlier felt: 'Alright, I guess everything else will go that way too.' Yet, you know, 25 to 30 years have passed and not everything went that direction. We don't see many people standing on exchange floors anymore, but there's still a lot of trading that deeply relies on humans and human judgment as an intermediary.
**中文：** Yaron：我的意思是，现在仍然有通过聊天工具在人与人之间进行沟通、共同决策并完成的交易。比如有人会去评估电话那头的人代表了多大程度的逆向选择（adverse selection），这依然是业务中非常真实的一部分。 你知道，就是有不同种类的证券需要更长的时间才能实现更高程度的自动化。例如，债券业务的自动化程度就远不及你在股票业务中看到的水平。实际上，我们对此也有点困惑。我认为我们这些在行业里待了一段时间的人，虽然我开始得有点晚，没能真正见证股票走向电子化的转型过程，但那些比我关注得早一点的人会觉得：“行吧，我猜其他所有领域接下来也会这样。” 然而，你懂的，已经过去了 25 到 30 年，并不是所有事情都走向了那个方向。虽然我们现在已经不怎么看到有很多人站在交易所大厅里了，但依然有大量的交易深度依赖于人类以及人类的判断作为中介。


## 人类在环、相变与非电子化交易

**SECTION_NOTE**
- 高度赚钱日往往发生在极端事件、世界疯狂时，需人类判断
- 模型难应对相变（phase transitions），人类元判断更优
- 债券等品类自动化远低于股票；仍大量依赖人际沟通与判断
**END_SECTION_NOTE**

**[—]**
**EN:** Dwarkesh: Speaking of that, how much human-in-the-loop is there between the model and the trading decision?
**中文：** Dwarkesh：说到这个，在模型和交易决策之间，人类参与（humans-in-the-loop）的程度有多高？

**[—]**
**EN:** Yaron: Many of your most profitable days happen when something weird occurs, a big event, the world goes crazy, nobody knows what's happening. Providing liquidity in those situations is extremely hard, so you get paid more for it, and those days usually have enormous volume. Doing that well often requires human judgment—thinking 'what's different about today versus every other day?' To the extent possible we want to build models that handle phase transitions well, but we also think humans handle phase transitions better than models, and sometimes you need that meta-judgment about what to do. So even for highly automated systems there are people monitoring and making decisions, and we always have people watching—right? I think an important part of trading is paying attention during the day to what's happening and thinking about it, even though individual trades happen far too fast for a human to intervene on a single-trade basis.
**中文：** Yaron：你们许多最赚钱的日子往往发生在一些奇怪的事情发生、出现重大事件、世界变得疯狂、没人知道发生了什么的时候。在那些情况下提供流动性往往极其困难，所以你为此获得的报酬也更高，而且在那些日子里通常会有巨大的交易量。要把这些做好，往往需要人类的判断力，去思考“今天与以往所有日子有什么不同？” 虽然在可能的范围内，我们希望构建能够很好应对相变（phase transitions）的模型，但我们也认为，人类在应对相变时比模型表现得更好，有时你需要这种元判断（meta judgment）来决定该怎么做。因此，即使对于高度自动化的系统，也需要负责监控的人员做出决策，而我们始终都有人在进行监控，对吧？我认为交易中一个重要的部分是在交易日内去关注和思考正在发生的事情，即使个别交易的发生速度远远快到人类无法在单笔交易的基础上进行干预。

**[—]**
**EN:** Dwarkesh: Dan, in the 20 years you've done this kind of construction (data centers), what's been the most significant change?
**中文：** Dwarkesh：Dan，在你从事这类建筑（数据中心）工作的过去 20 年里，最显著的变化是什么？


## 物理工程视角：20 年变迁与当前瓶颈

**SECTION_NOTE**
- Dan：行业老方法被淘汰，开始为「能否早 6 个月上线 GPU」牺牲工程洁癖
- 当前瓶颈：发电机、变压器、液冷设备交期长且变化快
- 模块化/预制基础设施成为趋势
**END_SECTION_NOTE**

**[—]**
**EN:** Dan: Yeah, people actually care about data centers now and want to talk about them. I've been doing cooling for a while, and suddenly everyone's discussing it and finds it interesting. So it's fun, exciting—I think my team feels the same. Some people in the data-center industry for 20 years still want to do things the old way, but I think that old method is being eliminated now. You see people challenging old assumptions, like: 'Hey, my whole data center has generators as backup power, but generators are one of the longest-lead-time items you can buy. So maybe we pull them out and only use generators for the core systems that need that resilience. That lets our GPUs come online six months earlier—let's do it!' So some things might not be the best engineering decision, but they're absolutely the best business decision. I think we're seeing more of that.
**中文：** Dan：是啊，人们现在居然真的开始关心数据中心了，并且想要聊聊它。你知道，我做冷却系统已经有一段时间了，现在突然之间大家都开始讨论它，觉得它很有趣。所以这挺好玩的，很让人兴奋，我想我团队里的人也有同感。 有些在数据中心行业干了 20 年的人，仍然想用过去的方式去做事，但我认为这种老方法现在正在被淘汰。你会发现大家正在挑战以前的观念，比如：“嘿，我的整个数据中心都有发电机作为后备电源，但发电机是你能买到的交货周期（lead time）最长的设备之一。所以也许我们把它们拿掉，只把发电机用于需要这种弹性的系统核心部分。这能让我们的 GPU 提早六个月上线，那就干吧！”所以，你知道，有些事情也许从纯工程角度看不是最好的决定，但它绝对是最好的业务决定。我觉得类似这样的事情正在越来越多地出现。

**[—]**
**EN:** Dwarkesh: It feels like every year the bottleneck to scaling AI compute changes. As you do more negotiating and try to get more compute, setting aside compute, memory, and all the fun stuff, what's the bottleneck now, and what do you expect it to be?
**中文：** Dwarkesh：感觉每年人们在扩大 AI 计算规模时遇到的瓶颈都在发生变化。在你们进行更多谈判并试图获取更多计算资源的过程中，抛开计算、内存和所有那些好玩的东西不谈，目前的瓶颈是什么？你预计未来的瓶颈会是什么？

**[—]**
**EN:** Dan: Generators, transformers, and some of the liquid-cooling equipment currently in use are in very high demand. And it changes fast—what I tell you today will be different in two weeks. One thing we do is work very closely with the internal procurement team to stockpile some of these. For the things we know are reusable across all data centers, we warehouse them and keep them ready. But parts like generators—you can't just put a huge generator in a normal warehouse; or if you're doing 'behind-the-meter' projects like turbines, you have to think more about those markets—where you get them, where you place them; you can't just set them aside. So the scarce parts definitely shift; those are some of the big ones. And as our density rises, one hope is that buildings can get a bit smaller, maybe we can build them faster, bundle all the compute tightly, and all the surrounding infrastructure is prefabricated and shipped to site. Right—modular data centers or modular infrastructure are becoming more common; these components, especially the long-lead-time ones, are designed and built off-site, then shipped to site, as close to plug-and-play as possible.
**中文：** Dan：发电机、变压器，还有一些目前用于液冷的冷却设备，需求量都非常大。而且它变化得很快，我今天告诉你的情况，两周后肯定就不一样了。 我们做的一件事是，与内部的采购团队非常紧密地合作，去囤积其中的一些物资。对于那些我们知道在所有数据中心之间都可以通用的物资，我们会进行仓储并随时准备使用。但像发电机这样的部件，你不可能把一个巨大的发电机放进普通的仓库里；或者，例如如果你在做像涡轮机（turbine）这样“表后”（behind-the-meter）的项目，你就必须对这些市场多做一些思考——你从哪里获取它们，在何处进行安置，你不能随随便便把它们搁在一边。 所以，我认为紧缺的部件肯定是会变化的，刚才提到的就是其中一些大件。而且，随着我们的密度越来越高，一个希望是建筑可以变得稍微小一点，也许我们能够更快地把建筑盖好，把所有的计算资源紧凑地捆绑在一起，然后周围的所有基础设施可能都是预制好并运送到现场的。没错，模块化数据中心或模块化基础设施正在变得越来越普遍，这些组件（尤其是那些长交货周期的组件）在场外进行设计和建造，然后运到现场，尽可能地接近“即插即用”（plug-and-play）。

**[—]**
**EN:** Dwarkesh: One point you made earlier is that as rack density rises, more and more of the data center is actually the infrastructure around the rack itself. That's a bit like the package on a chip, right? Or the chip on the package. The compute core is only a tiny fraction of the total package area.
**中文：** Dwarkesh：你之前提到的一个观点是，随着机架本身的密度越来越高，数据中心里越来越多的部分其实是围绕实际机架周围的基础设施。这实际上有点类似于芯片上的封装（package），对吧？或者说封装上的芯片。计算核心只占整个封装总面积的极小一部分。


## 机架密度、封装类比与 NVL72 vs TPU

**SECTION_NOTE**
- 单机架迈向 1 兆瓦，冷却管路与供电是核心约束
- 数据中心越来越像芯片封装：计算核心只占极小面积
- NVL72/GB200 与 Google TPU 密度/水温策略不同，需前瞻兼容
**END_SECTION_NOTE**

**[—]**
**EN:** Dan: Yes, it's interesting. I mean, it doesn't solve anything by itself, and might cause other problems, of course. For example, when you hit 1 megawatt per rack, people ask: 'What does 1 MW per rack even mean?' The cooling pipes you hook into just get thicker and thicker. And whether we're using AC now or the trend toward 800V DC in the future, you still have to bring all those components to the same place. From our perspective, the interesting part is: we can design these engineering things, but at the end of the day, whether it's Nvidia, an ASIC company, or anyone else, they have to sell components that run in a data center, and they're thinking hard about what to sell, because you need people to be able to use it, right? If you build a 1 MW data center or a 1 MW rack but have no way to power and cool it, it's useless. So we're working very closely with almost everyone in this space to think about what components you need to support these next-gen products. Because lead times can exceed a year, and you often have to decide on infrastructure before you've even ordered the chips. So, for example, you try to... you know Google's TPUs use cooler water and are only about half the density of Nvidia's NVL72 (transcript misheard as 'NBL72 GP300'; this is Nvidia's NVL72 with GB200 chips). Right? So that needs a different strategy, and you have to make sure you're forward-compatible with handling these.
**中文：** Dan：是的，这很有意思。我的意思是，这本身并不能解决任何问题，反而可能会带来其他问题，当然。比如，当你达到单机架 1 兆瓦（megawatt）的水平时，大家会问：“单机架 1 兆瓦到底是什么概念？”你接入那里的冷却管道只会变得越来越粗。而且，无论我们现在使用的是交流电（AC），还是未来的趋势——800 伏直流电（DC），你仍然必须把所有这些组件带到同一个地方。 从我们的角度来看，有趣的一点是，虽然我们可以设计这些工程上的东西，但归根结底，无论是英伟达、定制芯片（ASIC）公司还是其他任何人，他们都必须销售能够在数据中心运行的组件，而且他们也在非常认真地思考他们要卖什么，因为你需要人们能够用得上它，对吧？如果你建造了一个 1 兆瓦的数据中心或 1 兆瓦的机架，但却没有办法为其供电和冷却，那就毫无用处。所以我们正在与该领域的几乎所有人开展非常紧密的合作，去思考你需要哪些组件才能支持这些下一代产品。因为你所说的交货周期有时会超过一年，而你往往是在为芯片下订单之前就得对基础设施做出决定。 所以，比如你得尝试……你知道谷歌的 TPU，它们使用温度更低的水，而且它们的密度只有英伟达 NVL72（译注：此处速记错录为 NBL72 GP300，实际结合上下文应为英伟达的 NVL72 架构配 GB200 芯片）的一半。对吧？所以这需要不同的策略，而你必须确保未来能够兼容处理这些设备。


## 算力的「备用用途」与「盲区」

**SECTION_NOTE**
- 与大厂不同，JS 几乎不存在闲置算力的「备用用途」
- 存在大片「盲区」：若有更多算力就会去做的研究与实验
- 隐性下注：竞争可能削弱业务价值，需时刻保持紧张
**END_SECTION_NOTE**

**[—]**
**EN:** Dwarkesh: One reason hyperscalers can promise massive compute is they have some 'reserve use' for idle compute—something they can use at times they're not training or serving LLMs. For example, a company like Meta, if some GPUs aren't in use, can just say: 'Today we'll make the Instagram ad model slightly better.' For Jane Street, is there an equivalent reserve use for compute? That's arguably the floor of how much this compute is worth to you.
**中文：** Dwarkesh：超大规模云服务商（hyperscalers）之所以能够承诺投入海量的计算资源，原因之一是他们对闲置计算资源有一些“备用用途”（reserve use），可以在特定时间不用于大语言模型训练或推理时派上用场。例如，像 Meta 这样的公司，如果他们买的某些 GPU 没在用，他们可以直接说：“我们今天就把 Instagram 的广告投放模型做得稍微好一点。”那么对于 Jane Street 来说，有什么对等的计算资源备用用途吗？这可以说是这些计算资源对你们价值的底线。

**[—]**
**EN:** Yaron: Part of it is that in many ways we're actually quite compute-constrained. A lot of the innovation, experimentation, and new ideas people have are limited by the compute we have. So in a sense, if we strictly evaluated the value of the different new tasks we could run, the value of the tasks we've had to turn down is actually very high. Right? So we're doing what we think is most valuable, but if it turned out we had more compute than those tasks need, there's a huge amount of other research and experimentation we could do in that space. So we're far from 'oh, we have too much compute'—we have the opposite problem. I think there are a lot of 'low-hanging fruits' in this direction, like retraining models more frequently, which is valuable. Over time model quality decays, and being able to re-run them has direct, clear value to the company. Also we can do a certain amount of bulk inference to fill gaps when nothing else is schedulable. So we don't have exactly an Instagram-ads equivalent, but there's a large 'dark space' of things we're not doing that we would do with more compute. So we're not at all worried about extracting value from these devices.
**中文：** Yaron：部分原因在于，我们在很多方面其实面临着非常严重的计算资源受限。人们拥有的大量创新、实验和新想法都受限于我们所拥有的计算量。所以从某种意义上说，如果我们稍微严格地去评估一下我们能够运行的那些不同新任务的价值，会发现那些我们不得不拒绝的任务的价值实际上是非常高的。对吧？所以我们正在做我们认为最有价值的事情，但如果事实证明我们拥有的计算资源超出了这些任务所需，那么在那个领域还有海量的其他研究和实验可以做。所以我们还远远没有到说“噢，计算资源太多了”的地步，我们反而是遇到了相反的问题。 我认为在这个方向上也有很多“低垂的果实”（low-hanging fruit，容易实现的成果），比如更频繁地重新训练模型就是很有价值的。随着时间的推移，模型的质量会有所衰退，而能够重新运行它们——这对公司具有直接且明确的价值。此外，我们还可以执行一定数量的大量（bulk）推理任务，当系统中没有其他可调度的任务时，可以用它们来填补空白。因此，我们并没有完全类似于 Instagram 广告投放那样的应用，但确实存在一大片“盲区/未知空间（dark space）”，即那些我们没在做、但如果有了更多计算资源就会去做的事情。所以我们非常不担心无法从这些设备中榨取价值。 这里面确实有一系列的隐性下注（embedded bets），比如我们正在这些东西上投入巨资，你可以想象，有些事情的发展速度可能不会像我们预期的那么快，比如我们正在运行的各个模型和交易所产生的价值；而且这是一个竞争激烈的环境，也许其他人会击败我们。我认为保持优秀的要素之一，就是始终对竞争对手可能摸索出与你类似的做法并降低你的业务价值而感到紧张。所以，确实有可能出现一些并不顺利的情况。但显然，以我们目前现有的计算任务组合来看，我们距离遇到“算力过剩”这个问题还非常遥远。


## 电力 vs 芯片：拆分与分流

**SECTION_NOTE**
- 可将「供电/数据中心」与「买芯片」拆分，先锁定电力做多
- 把部分容量分流（offload）给他人比分流芯片容易
**END_SECTION_NOTE**

**[—]**
**EN:** Dan: This is interesting—it doesn't fully answer the question, but you can separate 'powering the data center' from 'buying the chips,' and say: 'Okay, I might need this compute later, let me lock in the data center and power now, but defer the very expensive chip purchase decision.' Right? At the time you might need the compute, position yourself as a bit 'long' on power and data-center capacity. Then we can design mechanisms like: hey, maybe we offload some of that capacity to others. For obvious reasons, for us it's much easier to offload power and data-center capacity than the chips themselves, but you can clearly split the two.
**中文：** Dan：这很有意思，虽然这没有完全回答问题，但你可以把“为数据中心供电”与“购买芯片”剥离开来，然后说：“好吧，我以后可能会需要使用这些计算资源，让我现在先锁定数据中心和电力资源，但推迟对非常昂贵的芯片做出采购决策。”对吧？在那个你可能需要计算资源的时间节点上，先让自己处于电力和数据中心容量稍微“做多”（long，充裕）的状态。然后我们可以设计一些机制，比如：嘿，也许我们可以把其中一部分容量分流（offload）给其他人。出于显而易见的原因，对我们来说，分流电力和数据中心容量要比分流芯片本身容易得多，但你确实可以将这两者清晰地一分为二。

**[—]**
**EN:** Dwarkesh: This also changes the hiring calculus. I mean, your hiring bar is already extremely high, but this raises it further. If you hire one more person, that person needs compute to run experiments, and that compute has to be traded off against other equally great people on your team who could do their own experiments.
**中文：** Dwarkesh：这也改变了关于招聘的考量。我是说，你们招聘的门槛已经高到极致了，但这会让它进一步提高。如果你多招一个人，那这个人就需要计算资源来做实验，而这部分计算资源将不得不与你团队中其他同样优秀、本可以自己做实验的人进行权衡和取舍。


## GPU 规模：几万 → 几十万张；真正的瓶颈是人才

**SECTION_NOTE**
- 当前 GPU 约几万张，不久将达几十万张，由业务效益证明合理
- 增长最大阻碍是培训新人、文化与导师辅导能力
- 限制因素不是硬件，是找到优秀人才
**END_SECTION_NOTE**

**[—]**
**EN:** Yaron: I see what you mean, but we wouldn't think: 'Oh, hiring more researchers is weird because then we'd have to give them more compute.' Instead, our logic is: research itself is extremely valuable, researchers are extremely valuable, and that's a great reason to buy more compute. So we're very motivated to scale up compute. For example, right now we have on the order of tens of thousands of GPUs, and in the not-too-distant future we'll be at hundreds of thousands of GPUs. We think that's fully justified by the business case. It's not like we're worried there: 'Oh, can we justify it by the trading P&L?' No, no, no—this is clearly a great investment. So on the hiring side this doesn't slow us down. In some ways the biggest constraint on growth is the time needed to actually train new people, integrate them into our culture, grow with them, and build this place together. We want Jane Street to remain a great place to work. I absolutely don't think hardware is the constraint on our development; I think the real constraint is finding great people, and our mentorship capacity.
**中文：** Yaron：我明白你的意思，但我们不会去想：“噢，再招更多研究人员会很奇怪，因为那样我们就必须给他们更多的计算资源。”相反，我们的逻辑是：研究本身极其有价值，研究人员也极其有价值，这反而是购买更多计算资源的一个绝佳理由。 因此，我们非常有动力去扩大计算规模。比如目前，我们的 GPU 数量大约在几万张的范围内，而在不久的将来，我们将达到几十万张 GPU 的规模。我们认为这完全可以由业务效益来证明其合理性。你知道，这并不是说我们会在那里担心：“哦，我们能不能根据交易策略的损益（P&L）来证明它的合理性呢？”不，不，不，这显然是很好的投资。所以在招聘方面，这并不会让我们放慢脚步。 在某些方面，增长的最大阻碍在于需要时间去真正培训新人、让他们融入我们的文化、伴随他们成长并共同建设这个地方。我们希望 Jane Street 继续成为一个伟大的工作场所。我完全不认为硬件问题是阻碍我们发展的因素，我认为真正的限制因素是寻找优秀的人才，以及我们对他们的导师辅导能力（mentorship capacity）。


## 招聘哪些岗位

**SECTION_NOTE**
- 物理工程：机械/电气/结构工程师、项目经理、建筑师（全生命周期）
- ML/交易：架构设计、各类定制模型、LLM 训练全周期经验
- 软件/硬件：通用 SWE、fleet-wide 优化、ASIC 设计
- 新兴：形式化方法（用证明提效）、前端工程
- 以人为本：工具应提升人的理解力、能动性与效率
**END_SECTION_NOTE**

**[—]**
**EN:** Dwarkesh: I guess this might be a good chance for you to mention what kinds of roles you're hiring for right now?
**中文：** Dwarkesh：我猜这可能是一个很好的机会，让你们提一下你们目前正在招聘哪些类型的职位？

**[—]**
**EN:** Yaron: Gosh, Dan, do you want to start with engineering?
**中文：** Yaron：天哪，那 Dan，你要不要先从工程领域开始聊聊？

**[—]**
**EN:** Dan: Sure, I'll start. Broadly, we're looking for very smart people interested in doing this kind of work. That includes mechanical engineers, electrical engineers, project managers, architects—the people who help design and build some of these spaces. My team's job is really to find the spaces, design them, build them, and then operate them—a full life cycle. So you need talent at every stage. You need a lot of engineers, a lot of what we call 'physical engineering'—a term we invented. Specifically mechanical, structural, maybe electrical engineers.
**中文：** Dan：好的，我先来。我的意思是，总的来说，我们就是在寻找非常聪明、对做这些事情感兴趣的人。这包括机械工程师、电气工程师、项目经理、建筑师——也就是帮助设计和建造其中一些空间的人。你知道，我团队的职责实际上是寻找这些空间、进行设计、建造，然后去运营它们，这是一个全生命周期（full life cycle）。所以在每个阶段你都需要人才。你需要很多工程师，很多我们称之为“物理工程”（physical engineering）领域的人，这是我们自己发明的一个词。但具体来说就是机械工程师、结构工程师，可能还有电气工程师这类人才。

**[—]**
**EN:** Yaron: And ML and the whole trading industry are really like a team sport, so we want to hire people from many different backgrounds with many different abilities. We're certainly excited to hire people with specific ML backgrounds—people doing architecture design and building models in various settings. As I mentioned, we have a bunch of custom architectures for our own specific, market-characteristic data. Also we build LLMs, and we're very interested in and scaling up people with experience across the LLM training life cycle. We hire a lot of people with good science and tech backgrounds—math, CS, physics, engineering—as traders. That requires a combined skill set, but it's an area we're continuously excited to hire in. On the software-engineering side, there's a general software-engineer role where we always want great people; it pays off well. As Dan said, smart, curious people with great CS backgrounds fit this general role and end up doing many different things. There are also many interesting specializations that excite us—for example, something fairly new: with today's compute scale, we're much more interested in fleet-wide optimization than before. Our old view of performance optimization was more about making the speed-critical parts as fast as possible, and generally compute was cheap while people were expensive, so we didn't spend much time optimizing general compute. But boy, now we're doing massive general compute, and when you start investing billions of dollars in this space, optimization becomes more valuable. People with experience at some hyperscalers—we very much want to hire more with that background to think about the optimization problems we're hitting. They're related but differ in important ways, so it's both a familiar and a new challenge. Also we do a lot of interesting hardware engineering, like designing our own custom chips (ASICs)—people with that experience excite us hugely. One more thing we mentioned at lunch: we're starting to think about a formal-methods team, basically using mathematical proofs to make software engineering more efficient. That's a very new, speculative area we're excited to invest in. I think that's a whole group of people I used to have to disappoint, telling them 'yes, we're not interested in formal methods.' But because of the whole AI revolution, formal methods suddenly became a much more interesting area, so that's somewhere we're excited to invest. Also, project managers, front-end devs. Actually, for most of Jane Street's history we pretended the whole web tech never happened—almost all our tools just ran in the terminal. But it turns out being able to draw a straight line, or have a tooltip, is really useful. So we've actually invested a lot in building great front-end tools and building tools for people. Having excellent front-end engineers—who are both great software engineers and understand how to make a user-friendly app—is very important. On all this, a meta point: I think amid all the reasonable and real excitement about AI tools, people sometimes overlook the importance of the human element. We really value building tools that benefit humans—including the AI tools themselves, right? I think advancing tools in a way that increases human understanding, agency, and efficiency is the core thing. The biggest constraint on our development is the outstanding people here, and whether we can find more of the right people and scale the organization so we can do more. So we take a very human-oriented approach to the systems we build.
**中文：** Yaron：而且机器学习和整个交易行业其实非常像一项团队运动，所以我们希望招聘来自许多不同背景、拥有许多不同能力的人才。我们当然非常兴奋能招到一些拥有特定机器学习背景的人，比如从事架构设计和在各种情况下构建模型的人。就像我提到的，我们针对自己特有的、市场特征所需的数据，拥有一大堆定制的架构等。此外，我们也构建大语言模型（LLM），我们对在 LLM 训练生命周期的各个阶段有经验的人都非常感兴趣，并且一直在扩大这个领域的规模。 你知道，我们招募了大量拥有良好科学和技术背景的人——比如数学、计算机科学（CS）、物理、工程等专业——来做交易员。这需要一种综合性的技能。但这是我们持续非常兴奋去招人的一个领域。 在软件工程方面，有一个通用的软件工程师职位，我们总是渴望招到优秀的人才。我觉得这能带来很好的回报。虽然说起来有点傻，但正如 Dan 所说，聪明、充满好奇心且拥有极佳计算机科学背景的人，非常适合这个通用职位的角色，他们最终可以做很多不同类型的事情。 还有许多有趣的专业领域也让我们非常兴奋，例如有件相当新的事情：随着如今算力规模的发展，我们对全集群/全舰队范围的优化（fleet-wide optimization）比过去感兴趣得多。我们以前对性能优化的看法是，它更多是关于让那些对速度最关键（speed-critical）的部分尽可能地快，而更普遍的情况是，算力挺便宜的，而人力很贵，所以我们并不会花太多时间去优化我们的通用计算。但是，天哪，我们现在正在进行海量的通用计算，当你开始在这个领域投资数十亿美元时，优化就变得更有价值了。有些人曾在某些超大规模云服务商（hyperscalers）那里有过这方面的经验，我们非常希望招到更多具有这种背景的人，来思考我们正在遇到的优化问题。这些问题有相通之处，但在重要方面又有所不同，所以这既是一个相关的挑战，也是一个新的挑战。 另外，我们还做许多有趣的硬件工程工作，比如设计我们自己的定制芯片（ASICs），拥有这种经验的人同样让我们感到超级兴奋。 还有一件事，我们刚才吃午饭时提到过，我们开始考虑建立一个形式化方法（formal methods）团队，基本上是利用数学证明来让软件工程变得更有效率。这是一个非常新、极具探索性（speculative）的领域，我们非常兴奋能在那里找到人才。我觉得这是一整个群体的人，在过去我总不得不让他们失望，对他们说：“是的，我们对形式化方法不感兴趣。”但由于整个人工智能革命，形式化方法突然变成了一个有趣得多的领域，所以这是我们很兴奋去投资的地方。 另外，我也不知道，比如项目经理、做前端开发（front-end dev）的人。事实上，在 Jane Street 的大部分发展历程中，我们都假装这整套 Web 网页技术从未发生过，我们几乎所有的工具都只是在终端（terminal）里运行。但事实证明，如果能画一条直线，或者有一个工具提示（tool tip）之类的内容，是非常有用的。所以我们实际上投入了大量资源来构建非常出色的前端开发工具，并为人们打造工具。拥有杰出的前端工程师——他们既是优秀的软件工程师，又对“如何制作一款对用户友好的应用”有很好的理解——这是非常重要的。 关于所有这些，我想说一个总体的、更高维度的观点（meta point）：我认为，在当前围绕 AI 工具的所有合理且真实的兴奋中，人们有时会忽视这一切当中“人的因素”（human element）的重要性。我们真的非常看重构建对人类有益的工具，这也包括 AI 工具本身，对吧？我认为，以一种能够提高人类理解力、能动性（agency）和效率的方式去推动工具的发展，才是最核心的事情。限制我们发展的最主要因素，莫过于在这里工作的杰出人才，以及能否找到更多合适的人并扩大组织规模，从而让我们能做更多的事情。因此，在思考我们所构建的系统时，我们采用了一种非常以人为本（human-oriented）的方式。


## 谜题文化与后门挑战

**SECTION_NOTE**
- 谜题是 Jane Street 文化核心，曾出题寻找 LLM 后门触发词
- 后门挑战无人能解全三题
- 以谜题传递「在这里工作是什么样」
**END_SECTION_NOTE**

**[—]**
**EN:** Dwarkesh: It's cool seeing you make these fun puzzles and challenges. I think you do this normally, and you made a few specifically for our podcast listeners. I think listeners going through this might find the puzzles interesting. By the way, one of the puzzles—not only did none of the contestants solve it, Jane Street itself couldn't solve it. That puzzle involved finding trigger phrases planted in various LLMs with backdoors. Anyway, I mention it because if people are interested in going deeper, I think these fun puzzles show a bit of what it's like to work here, and why it's an interesting place.
**中文：** Dwarkesh：看你们制作这些有趣的谜题和挑战真的很酷。我认为你们平时就在这么做，而且你们还专门为我们播客的听众制作了几个。我觉得在听这期内容的听众可能会对去看看这些谜题很感兴趣。顺便说一句，其中有一个谜题，不仅提交参加竞赛的人里没有一个能解出来，连 Jane Street 自己也解不出来。那个谜题涉及寻找各种内置了触发词（trigger phrase）的大语言模型的后门。不管怎么说，我提到这一点是因为，如果大家有兴趣深入了解，我认为这些有趣的谜题可能会在一定程度上展现出在这里工作是什么样子的，以及为什么这里是一个有趣的地方。

**[—]**
**EN:** Yaron: Yes, puzzles are deeply rooted in our culture, so using them as a way to connect with people is really great.
**中文：** Yaron：是的，谜题是我们文化中根深蒂固的一部分，所以用它们作为一种与大家建立联系的方式真的很棒。

**[—]**
**EN:** Dwarkesh: Great, thank you both for the conversation.
**中文：** Dwarkesh：太好了，感谢两位参与这次对话。

**[—]**
**EN:** Yaron & Dan: Thank you so much, our pleasure.
**中文：** Yaron & Dan：非常感谢，我们的荣幸。
