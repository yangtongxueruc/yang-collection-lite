
## 开场：得州数据中心探访与核心疑问

**SECTION_NOTE**
- Dwarkesh 实地探访 Jane Street 位于得州的数据中心（本期为探访后的深度对谈）
- 嘉宾：技术团队共同负责人 Yaron Minsky、物理工程团队负责人 Dan Pontecorvo
- 核心疑问：既然要在纳秒级交易，怎么还能同时做 GPU 训练
**END_SECTION_NOTE**

**[00:00 – 00:20]**
**EN:** Jane Street are partners of my podcast and one of the fun ideas we had is why don't I come visit a data center uh for training that you guys run. So I just got a tour of this uh Texas data center from Yaron Minsky who co-heads the technology group and Dan Pontecorvo who heads the physical engineering team. So
**中文：** Jane Street 是我播客的合作伙伴，我们的有趣想法之一是我为什么不去参观一下你们运营的数据中心呢？我刚刚从技术团队联合负责人 Yaron Minsky 和物理工程团队负责人 Dan Pontecorvo 的带领下参观了这个德克萨斯州数据中心。所以

**[00:20 – 00:37]**
**EN:** thank you guys for showing me around it's worth I've never been here before so I also got I was also getting a tour which was great. Previously I was confused well how can you be doing GPU things if you need to be trading on nanoseconds and maybe you can talk through what is the actual time horizon of the
**中文：** 谢谢你们带我四处参观，我以前从未来过这里，所以我也得到了一次很棒的旅行。之前我很困惑，如果你需要以纳秒为单位进行交易，你怎么能做 GPU 的事情，也许你可以谈谈实际的时间范围是多少？

**[00:37 – 00:54]**
**EN:** trading you guys do can you afford to have be running big models to in in the middle of making trading decisions I think the thing to understand here is there isn't one time horizon there are many time horizons uh there are trading systems we build and trades that we do where in order to be competitive you
**中文：** 你们做的交易​​你们能负担得起在做出交易决策的过程中运行大型模型吗？我认为这里要理解的是，没有一个时间范围，而是有很多时间范围，呃，我们建立了一些交易系统，我们在哪里进行交易，以便与您竞争


## 交易的时间跨度谱系：从 100 纳秒到数小时

**SECTION_NOTE**
- 交易没有单一时间跨度，而是一条从 100 纳秒到半小时/当天的完整谱系
- 100 纳秒内无法用 CPU，只能靠 FPGA 直连网络；越慢的尺度可用越复杂的模型
- 最佳策略是集成（ensemble）：不同时间尺度配不同复杂度的决策
**END_SECTION_NOTE**

**[00:54 – 01:10]**
**EN:** actually have to turn around a packet in in under 100 nanoseconds and like that's a very different regime, right? You know, people sometimes talk about like, oh, can you guys write high performance stuff in OCaml? It's like we can, but like for this kind of speed, it's like it doesn't matter if you write in OCaml
**中文：** 实际上必须在 100 纳秒内周转一个数据包，这是一个非常不同的机制，对吧？你知道，人们有时会说，哦，你们能用 OCaml 编写高性能的东西吗？好像我们可以，但是像这种速度，就好像你用 OCaml 编写并不重要

**[01:10 – 01:24]**
**EN:** or Rust or C++. You can't use a CPU, right? you are going to be on an FPGA that's like direct wire attached to the network and you're going to be turning around the packet so fast that if you like attached an oscilloscope to the wire on the way in and the wire on the way out you would see the packet start
**中文：** 或 Rust 或 C++。你不能使用CPU，对吧？您将使用一个 FPGA，就像直接连接到网络的线路一样，您将如此快速地周转数据包，如果您喜欢将示波器连接到传入的线路和传出的线路，您将看到数据包开始

**[01:24 – 01:39]**
**EN:** to leave before it's done being consumed. So it's like a very different very specialized regime but like when you're in that time regime you really can't do very much computation. the decisions you're making are going to be very simple. And in fact, there's this kind of whole curve of trade-offs
**中文：** 在它被消耗完之前离开。所以这就像一个非常不同的非常专业的制度，但是就像当你处于那个时间制度时你真的不能做太多的计算。你所做的决定将非常简单。事实上，存在着这样一条完整的权衡曲线

**[01:39 – 01:57]**
**EN:** between how smart is the decision that you're making, be it a model or some other kind of maybe even like handwritten decision-m process, and how fast the turnaround is. And like the the right way to build uh an optimal trading strategy is really to have a kind of ensemble approach where for some kinds
**中文：** 您所做的决策（无论是模型还是其他类型的甚至可能是手写的决策过程）有多明智，以及周转速度有多快。就像建立呃最佳交易策略的正确方法一样，实际上是采用一种整体方法，对于某些类型

**[01:57 – 02:14]**
**EN:** of decisions you're making very s simple decisions very quickly. For some kind of decisions, you're operating at the scale of, you know, instead of thinking of a hundred nanos, maybe like a handful of mics or tens of microsconds or hundreds of microscs or milliseconds. And in some cases, there are processes where if you
**中文：** 您可以非常快速地做出非常简单的决定。对于某些类型的决策，您的操作规模可能是，您知道，而不是考虑一百纳秒，可能像一把麦克风或几十微秒或数百微秒或毫秒。在某些情况下，在某些流程中，如果您

**[02:14 – 02:33]**
**EN:** can get that decision turned around, you know, in an hour or that day, that's totally fine. And you're you're kind of competitive on a time basis at each of these horizons. Uh but you're making very different kinds of decisions at all of them. Maybe you can't say but what what is it exactly these models are
**中文：** 可以在一小时内或当天扭转决定，那完全没问题。在这些方面，你在时间上都具有竞争力。呃，但是你对所有这些都做出了非常不同的决定。也许你不能说，但这些模型到底是什么

**[02:33 – 02:45]**
**EN:** predicting like surely it's just not the next thing in the order book or maybe it is right so we're definitely like dancing towards stuff that's hard to talk about but I think the simplest and most important one that we've been thinking about like we think about it now but
**中文：** 预测这肯定不是订单中的下一件事情，或者也许是正确的，所以我们肯定喜欢朝着难以谈论的东西跳舞，但我认为我们一直在思考的最简单和最重要的事情就像我们现在思考的那样，但是


## 模型预测什么：公允价值（fair value）

**SECTION_NOTE**
- 最经典也最重要的预测目标是资产的公允价值（fair value）
- 可组合地融入多种交易流程；25 年前 Yaron 用线性回归时就在做这件事
- 并非唯一预测目标，但信息含量最高
**END_SECTION_NOTE**

**[02:45 – 03:00]**
**EN:** like also 25 years ago when I started at Jane Street when I was building like models out of linear regression you know and stuff like that like a very useful kind of thing is to predict a fair value for a thing like what do we think this thing is worth and that fits in in a very kind of composable a into lots of
**中文：** 就像 25 年前，当我在 Jane Street 开始工作时，我正在用线性回归构建类似的模型，你知道，类似的东西是一种非常有用的东西，就是预测一个东西的公允价值，比如我们认为这个东西值多少钱，并且它适合于一种非常可组合的东西

**[03:00 – 03:13]**
**EN:** different trading processes. That's not the only kind of thing that we use as a prediction target, but it's an important one. It seemed like a meme I was getting for a while about like what trading firms do is like you you got to get the colo and the where the NASDAQ exchanges and it's
**中文：** 不同的交易流程。这不是我们用作预测目标的唯一一类东西，但它是一个重要的东西。这似乎是我有一段时间听到的一个模因，关于贸易公司所做的事情就像你一样，你必须获得 colo 以及纳斯达克交易所的位置，它是


## 推理放在哪：托管（colo）、自建与工程约束

**SECTION_NOTE**
- 推理可放在 CPU / FPGA / GPU，取决于算力需求、模型大小与延迟要求
- 「必须把机器放在交易所旁边」是误解；越大越慢的负载可以放得更远
- 极端低延迟场景下，连光纤长度都要被测量优化
**END_SECTION_NOTE**

**[03:13 – 03:27]**
**EN:** very important that your machines are right there without thinking without thinking too much about the exact details of what we put where. like your inference processes might be on CPU, might be on FPGA, might be on GPU depending on the kind of constraints of
**中文：** 非常重要的是，您的机器就在那里，无需过多考虑我们放置的具体细节。就像你的推理过程可能在 CPU 上，可能在 FPGA 上，可能在 GPU 上，具体取决于约束的类型

**[03:27 – 03:40]**
**EN:** how much compute you need, how big the model is, what kind of latency turnaround do you need. And yeah, like bigger, slower things you can put farther away. It's annoying to have to put all the compute right by the exchange. And for the stuff that's like really really fast, like being in the
**中文：** 您需要多少计算量、模型有多大、您需要什么样的延迟周转。是的，比如更大、更慢的东西你可以放得更远。必须将所有计算都放在交换机上是很烦人的。对于那些非常非常快的事情，比如在

**[03:40 – 03:57]**
**EN:** colo isn't enough, you care about like how long is the spool of wire that gets you there. like you're literally like measuring out the length of the fiber runs when you're when again when you're like at this very very low nanosecond scale. Um but in general like the like bigger models give you a lot more
**中文：** colo 还不够，你关心的是让你到达那里的线轴有多长。就像你真的在测量光纤的长度一样，当你再次处于这个非常非常低的纳秒尺度时。嗯，但总的来说，更大的型号可以给你更多的东西

**[03:57 – 04:10]**
**EN:** flexibility in terms of where they physically go. If we're putting GPUs in some of these colloccated uh facilities that are next to the exchanges right now, you have to work with with their rules. You know, who is who is that provider? Who is who is giving you that space? Yeah. And your power, your
**中文：** 就他们实际去向而言的灵活性。如果我们现在将 GPU 放入交易所旁边的一些并置呃设施中，您就必须遵守他们的规则。你知道，那个提供者是谁？谁给你这个空间？是的。还有你的力量，你的

**[04:10 – 04:23]**
**EN:** cooling, all those constraints now are maybe slightly tighter than if you have a facility facility that you're designing and operating. Um so you're now having to kind of come up with ways to, hey, maybe I could only get one GPU in a rack because it consumes so much power. So now I have to spread it all
**中文：** 冷却，现在所有这些限制可能比您正在设计和运营的设施稍微严格一些。嗯，所以你现在必须想出一些方法，嘿，也许我只能在机架中放置一个 GPU，因为它消耗太多电量。所以现在我必须传播这一切

**[04:23 – 04:37]**
**EN:** out rather than being able to do liquid cooled in one rack. So these are all uh things we need to keep in mind as our comput you know comput. You guys recently signed a $6 billion comput deal with CoreWeave. Mhm. What are you going to use that for?
**中文：** 而不是能够在一个机架中进行液体冷却。所以这些都是我们在计算时需要牢记的事情。你们最近与 CoreWeave 签署了一项价值 60 亿美元的计算协议。嗯。你要用它做什么？


## 60 亿美元 CoreWeave 协议与 Jane Street 的「规模定律」

**SECTION_NOTE**
- Jane Street 与 CoreWeave 签下 60 亿美元算力协议（另含 10 亿美元股权投资）
- 「AI 世界有 scaling laws，我们也有 scaling laws」——但方向不同
- 不算「训一个通用大模型」，而是多样化架构 + 大量实验迭代
**END_SECTION_NOTE**

**[04:37 – 04:55]**
**EN:** The rest of the AI world has scaling laws. We have scaling laws too and there are lots of models that we want to train. I think the thing that's interesting and maybe different between us and the kind of more traditional AI labs is the amount of diversity in model architecture and the amount of
**中文：** 人工智能世界的其他部分也有缩放定律。我们也有缩放定律，并且我们想要训练很多模型。我认为我们与更传统的人工智能实验室之间有趣且可能不同的是模型架构的多样性和数量

**[04:55 – 05:10]**
**EN:** experimentation that we're doing. So a lot of the value you get from all of this is just people are like trying lots of very different new things in the model designs and giving researchers just like faster iteration time so they can discover more ideas and drive more innovation. It just turns out to be
**中文：** 我们正在做的实验。因此，您从所有这一切中获得的很多价值只是人们在模型设计中尝试许多不同的新事物，并为研究人员提供更快的迭代时间，以便他们可以发现更多想法并推动更多创新。事实证明是

**[05:10 – 05:25]**
**EN:** incredibly important. In the case of these foundation labs, there's some gain from have training just one model that does everything that is fully general rather than building a bunch of custom different models. Can you give me a sense of why there's a different trade-off at Jane Street? For
**中文：** 非常重要。就这些基础实验室而言，仅训练一个模型来完成完全通用的所有操作，而不是构建一堆自定义的不同模型，会带来一些好处。你能告诉我为什么简街有不同的权衡吗？为了

**[05:25 – 05:41]**
**EN:** us, some of the specialization is about being adapted to consume the right kind of data, right? And there are just like many possible data sources that we might be feeding in. There are like a bunch of just differences in the data rates that we need to achieve. Like just like another thing that like just makes us
**中文：** 对我们来说，一些专业化是为了适应使用正确类型的数据，对吧？我们可能会输入许多可能的数据源。我们需要实现的数据速率也存在很多差异。就像另一件事一样让我们

**[05:41 – 05:56]**
**EN:** need to kind of specialize some of what we're doing is just like the overall kind of both inference and trading dynamics are made different by just like the the bytes to flop ratio being different. We have like way more data that we are using to train the models, but the data is kind of bite for bite
**中文：** 需要对我们正在做的一些事情进行专门化，就像推理和交易动态的整体类型因字节与触发器比率的不同而变得不同一样。我们有更多的数据用于训练模型，但这些数据是逐利的

**[05:56 – 06:11]**
**EN:** less informative just because financial data is very noisy. Yeah. Um, and so the models tend to be smaller and the data tends to be noisier noisier and there tends to be a lot more of it. And it's also different between different models that we build for different applications, right? As we try
**中文：** 信息量较少只是因为财务数据非常嘈杂。是的。嗯，所以模型往往更小，数据往往更嘈杂，而且数据往往更多。我们为不同的应用程序构建的不同模型之间也有所不同，对吧？当我们尝试时

**[06:11 – 06:27]**
**EN:** and figure out like how can we leverage more of the information that we get. It's like oh now there's like all of the kind of decisions from like how do we store and load data efficiently to how do we shape the model to how do we make the inference process, you know, have both the throughput and latency that it
**中文：** 并弄清楚我们如何才能利用更多我们获得的信息。就像哦，现在有各种各样的决策，从我们如何有效地存储和加载数据，到我们如何塑造模型，再到我们如何进行推理过程，你知道，拥有它所需要的吞吐量和延迟。

**[06:27 – 06:44]**
**EN:** needs. those there's going to be a whole different set of trade-offs there. And so there's just like a lot of value in kind of working that out and picking the the best thing that you can do for for different applications. What is the um inference workload actually or how does it compare to what
**中文：** 需要。那里将会有一套完全不同的权衡。因此，解决这个问题并为不同的应用程序选择最好的事情是很有价值的。实际的推理工作负载是多少，或者它与实际的推理工作负载相比如何


## 推理工作负载：延迟、批处理与极高的数据速率

**SECTION_NOTE**
- 推理负载与 chatbot 公司差异明显：延迟更敏感、批处理更受约束
- 金融数据量大但单 byte 信息密度低（噪声高）
- 因此更强调 data loading 性能与按因果顺序消费数据
**END_SECTION_NOTE**

**[06:44 – 06:59]**
**EN:** your traditional big chatbot LLM company is doing in broadstrokes? Latency matters more as you might expect. Um, batching is still an issue. Like depending on the model you're doing, you might have models or a part of models that are kind of disagregated for different symbols that
**中文：** 你们传统的大型聊天机器人法学硕士公司正在做大事吗？正如您所料，延迟更重要。嗯，批处理仍然是一个问题。就像根据您正在做的模型一样，您可能拥有模型或模型的一部分，这些模型或模型的一部分针对不同的符号进行了分类

**[06:59 – 07:15]**
**EN:** you're looking at. And so the same kind of like pulling in data from multiple sources and batching them together makes a difference. I think another thing that's interesting is just like the data rates are really high. Like the amount the the aggregate data rate that you get in a large LLM LLM lab from like all of
**中文：** 你正在看。因此，从多个来源提取数据并将它们批处理在一起会产生不同的结果。我认为另一件有趣的事情是数据速率非常高。就像您在大型 LLM LLM 实验室中获得的总数据速率一样

**[07:15 – 07:31]**
**EN:** the different users is also very high. But the amount of sequential data that you're going to get from any one user is not that high. Whereas when you the the data that you're pulling is the bytes that are coming out of like the NASDAQ feed, it's like oh man the data rate that you want that kind of sequentially
**中文：** 不同用户的使用率也很高。但是，您从任何一个用户那里获得的顺序数据量并不是那么高。然而，当您提取的数据是来自纳斯达克提要的字节时，天哪，您想要的数据速率是连续的

**[07:31 – 07:49]**
**EN:** consumed in one domain kind of causally one after the other is really high. And so again like the dynamics change and like but I think a lot of the same kind of basic engineering questions are not so dissimilar but like all the constants are twiddled to different places and so you end up making different choices.
**中文：** 在一个领域中因果性地依次消耗的消耗量确实很高。再次像动态变化一样，但我认为很多相同类型的基本工程问题并没有那么不同，但就像所有常数都被扭曲到不同的地方，所以你最终会做出不同的选择。


## 存储、x86 与去中心化：被打破的两条捷径

**SECTION_NOTE**
- 过去「x86-64 + 现成存储」的捷径正在被打破
- 自建 object store、更大规模的数据存储系统
- 训练/推理 workload 与通用 LLM 实验室不同
**END_SECTION_NOTE**

**[07:49 – 08:04]**
**EN:** What what does that mean in terms of the how you how you had to design these systems where whether it's in terms of storage or whatever else. Yeah, there's I think more emphasis on the performance of the data loading than you might otherwise see. I think we're doing a lot of work to build out our own
**中文：** 这对于如何设计这些系统意味着什么，无论是在存储方面还是其他方面。是的，我认为数据加载的性能比您可能看到的更加重要。我认为我们正在做很多工作来建立我们自己的

**[08:04 – 08:21]**
**EN:** kind of largecale uh data storage system, our own kind of internal object store um where we've like used various kind of vendor products but um over time I think for some of these research focused use cases we kind of need to operate at a much larger scale and need also to deal with a diversity of data
**中文：** 一种大型呃数据存储系统，我们自己的内部对象存储，我们喜欢使用各种供应商产品，但是随着时间的推移，我认为对于其中一些以研究为重点的用例，我们需要以更大的规模进行操作，并且还需要处理各种数据

**[08:21 – 08:38]**
**EN:** centers right and this is like less a training time less a inference time and more of a training time question of like we just can't get all the compute we want all in the same place And I don't know, I feel like in general like a an important trick in like effectively running a technical organization is
**中文：** 中心正确，这就像更少的训练时间，更少的推理时间，更多的训练时间问题，就像我们无法在同一个地方获得我们想要的所有计算一样，我不知道，我觉得一般来说，有效运行技术组织的一个重要技巧是

**[08:38 – 08:51]**
**EN:** feeling is figuring out what shortcuts you can take. One shortcut that we were like privileged to be able to take for many years is we got to pretend like there was only one CPU architecture on the planet. Like everything was for like x86-64. We pretended like none of these other
**中文：** 感觉就是弄清楚你可以采取哪些捷径。多年来我们有幸能够采取的一条捷径是，我们必须假装地球上只有一种 CPU 架构。就像一切都是为了 x86-64 一样。我们假装不像其他人

**[08:51 – 09:08]**
**EN:** things existed. Uh and that simplified a bunch of things. Uh and we also had like one big research data center and one big storage cluster and that also simplified a ton of things. And actually both of those have now been unwound like you just can't get the amount of power like you cannot wire in enough thunderbolts
**中文：** 事物存在过。呃，这简化了很多事情。呃，我们还有一个大型研究数据中心和一个大型存储集群，这也简化了很多事情。实际上，这两个现在都已解除，就像您无法获得足够的电量，就像您无法连接足够的雷电一样

**[09:08 – 09:21]**
**EN:** into like the same data center to power all the things you need. You need to get the data centers built all over the place. So there's a big disagregation problem and that gives you a problem like oh now you have to think about like your compute scheduling and your storage scheduling being intertwined one with
**中文：** 就像同一个数据中心一样为您需要的所有东西提供动力。您需要在各处建立数据中心。因此，存在一个很大的分解问题，这给您带来了一个问题，哦，现在您必须考虑您的计算调度和存储调度与

**[09:21 – 09:39]**
**EN:** the other and there's a ton of data. So moving around is like non-trivial. Um, and also we had to give up on this x86 only thing because Nvidia has a bunch of cool new products that mean that you need to support ARM. Now zooming out, I want to ask a very naive question. There's maybe a naive view that uh, you
**中文：** 另一个有大量数据。因此，四处走动并不是一件小事。嗯，我们也不得不放弃这个 x86 唯一的东西，因为 Nvidia 有很多很酷的新产品，这意味着你需要支持 ARM。现在缩小范围，我想问一个非常天真的问题。也许有一种天真的观点认为，呃，你


## 交易是「AGI 完全」问题吗

**SECTION_NOTE**
- 类比「NP-complete」：交易被视为一种「AGI-complete」问题
- 如果真有了 AGI，它能否立刻取代 Jane Street 做的事
- 这也是 Jane Street 大量投入算力的底层动机
**END_SECTION_NOTE**

**[09:39 – 09:58]**
**EN:** know, if you have AGI, it can like immediately do what Jane Street does. Give me a sense of like why that naive view is naive. Yeah. And I don't want to totally discount it like you know there's a world that we should take seriously where like you know we're going to build
**中文：** 要知道，如果你有 AGI，它可以立即做 Jane Street 所做的事情。让我明白为什么这种幼稚的观点很幼稚。是的。我不想完全低估它，就像你知道有一个我们应该认真对待的世界，就像你知道我们要建立的那样

**[09:58 – 10:15]**
**EN:** large language models or some other AI systems that are like strictly smarter than all humans on the planet and more capable at all cognitive tasks and like yeah that's going to be weird and that's like a different that's a that's a different a different state of things. Um, and in that case, yeah, you know,
**中文：** 大型语言模型或其他一些人工智能系统，它们比地球上所有人类都更聪明，并且在所有认知任务上都更有能力，是的，这会很奇怪，就像一个不同的事物，这是一个不同的事物状态。嗯，在那种情况下，是的，你知道，

**[10:15 – 10:29]**
**EN:** maybe large amounts of things that Jane Street does will be automated away and, you know, maybe we'll all just like, you know, sit back and, you know, drink more margaritas or something. I don't know what that world looks like, but it doesn't feel like we're particularly close to that now. I think that like in
**中文：** 也许简街所做的大量事情都会被自动化消除，你知道，也许我们都会喜欢，你知道，坐下来，喝更多的玛格丽塔酒什么的。我不知道那个世界是什么样子，但感觉我们现在离那个世界并不是特别接近。我认为就像

**[10:29 – 10:47]**
**EN:** general I think it's like easy to underestimate the richness and complexity of the work both that like a company like Jane Street does but really that is done in kind of any really like ambitious high difficulty like company scale task. I think trading in particular feels to me as like kind of
**中文：** 总的来说，我认为很容易低估像 Jane Street 这样的公司所做的工作的丰富性和复杂性，但实际上这是以任何真正雄心勃勃的高难度（如公司规模的任务）完成的。我认为交易对我来说尤其感觉就像

**[10:47 – 11:06]**
**EN:** AGI-complete sort of like NP-complete. It's like meaning like that like all of the different problems of the world end up influencing what you're doing in a trading context because at the end of the day trading involves figuring out what things are worth which means making predictions about the future and lots of
**中文：** AGI 完全有点像 NP 完全。这就像世界上所有不同的问题最终都会影响你在交易环境中所做的事情一样，因为归根结底，交易涉及弄清楚事物的价值，这意味着对未来做出预测，并做出很多预测。

**[11:06 – 11:21]**
**EN:** different things flow into that and as various pieces of that get automated you know you have the usual thing of like the other hard parts that we don't yet know how to automate well that ends up being where the competitive edge lies I feel like humans and like human cognition are like more valuable than
**中文：** 不同的东西流入其中，随着其中的各个部分实现自动化，你知道你有通常的事情，就像其他困难的部分一样，我们还不知道如何很好地实现自动化，最终成为竞争优势所在，我觉得人类和人类认知比人类更有价值


## 人才悖论：越强的模型越抬高招聘门槛

**SECTION_NOTE**
- 「从未如此渴望招更多工程师」——模型越强，对人的要求反而越高
- 人类判断与稀缺性在算力扩张中并未被削弱
- 招聘标准只会更高，不会因算力替代而降低
**END_SECTION_NOTE**

**[11:21 – 11:38]**
**EN:** ever. Like I have never been more desperate to hire more engineers and more traders than I am today because everything people are doing is more valuable than it was. I mean some of this is just me being somewhat skeptical that we are quite as close to the models that are like smarter than humans at all
**中文：** 曾经。就像我从来没有像今天这样迫切地想要雇用更多的工程师和更多的交易员，因为人们所做的一切都比以前更有价值。我的意思是，其中一些只是我有点怀疑我们是否与比人类更聪明的模型非常接近

**[11:38 – 11:52]**
**EN:** the things as some people seem to think. Maybe it's like physical infrastructure like actually getting the colo. Maybe it's actually like the software infrastructure that you build. Like give me a sense of what it is that would Yeah, we build like a huge variety of complicated pieces of software, have
**中文：** 有些人似乎认为的事情。也许这就像物理基础设施一样，就像实际获得托管服务一样。也许它实际上就像您构建的软件基础设施。就像让我了解它是什么是的，我们构建了各种各样复杂的软件，有

**[11:52 – 12:06]**
**EN:** people thinking about lots of different trading problems, some of which are not very electronic at all. Like the business is just like way more diverse than I think people give it credit for. And there's an idea of like, oh yeah, it's like it must be that like simple thing where you just like you just have
**中文：** 人们思考许多不同的交易问题，其中一些根本不是很电子化。就像这个行业比我认为人们所认为的更加多样化一样。有一个想法，哦，是的，就像它一定是这样简单的事情，你只是喜欢你拥有

**[12:06 – 12:18]**
**EN:** smart people who like make smart decisions and write good software. And like if we could just automate the smartness part, that would be the whole thing. And I think it's just way more complicated than that. What what do you mean by the non electronic parts of trading?
**中文：** 聪明的人喜欢做出明智的决定并编写优秀的软件。就像如果我们能够将智能部分自动化，那就是全部了。我认为事情比这复杂得多。交易的非电子部分是什么意思？

**[12:18 – 12:32]**
**EN:** I mean, there's still trading that happens via chat between people talking to each other and making decisions and like someone like sizing up how much adverse selection they think the person on the other side of the phone represents. That's like still a real part of the
**中文：** 我的意思是，仍然存在通过人们之间的聊天进行交易并做出决定，就像有人喜欢评估他们认为电话另一端的人代表了多少逆向选择。那就像仍然是真实的一部分

**[12:32 – 12:52]**
**EN:** business. Um there's just like, you know, there's just different kinds of securities that have taken longer to get more automated. The bonds business for example is just like not nearly at the level of automation that you see in equities. Indeed, we I think we were kind of confused about this of like I
**中文：** 商业。嗯，就像，你知道，只是有不同种类的证券需要更长的时间才能变得更加自动化。例如，债券业务与股票业务的自动化水平相差甚远。事实上，我认为我们对此有点困惑，就像我一样

**[12:52 – 13:03]**
**EN:** think those of us who have been like in the business for a while. We kind of I mean I I started a little too late to really see the kind of transition of equities becoming electronic. But I think people who are you know paying attention a little earlier than me were like yeah and I guess everything else
**中文：** 想想我们这些已经在这个行业工作了一段时间的人。我的意思是，我开始有点太晚了，无法真正看到股票电子化的转变。但我认为比我早一点关注的人就像是的，我想其他一切

**[13:03 – 13:18]**
**EN:** comes next. And like you know what it's been like you know 25 30 years and like not everything has gone that way. the systems are still, you know, we don't have a lot of people like standing on the floor of exchanges anymore, but there's still lots of trading that is deeply intermediated by humans and human
**中文：** 接下来是。就像你知道 25 到 30 年来的情况一样，但并不是所有事情都朝着这个方向发展。你知道，系统仍然存在，我们不再有很多人站在交易所的地板上，但仍然有很多交易是由人类和人类深度中介的


## 人类在环、相变与非电子化交易

**SECTION_NOTE**
- 大量交易仍深度依赖人类中介与人的判断
- 系统要能穿越「相变（phase transition）」式的市场结构剧变
- 人类在环（human-in-the-loop）在异常场景中仍是关键
**END_SECTION_NOTE**

**[13:18 – 13:32]**
**EN:** judgment. King of which, how much are humans in the loop on between the model and the and the trading decision? Many of your most profitable days happen when like weird stuff happens and there are events and the world kind of goes crazy and like nobody knows what's going on and
**中文：** 判断。最重要的是，人类在模型和交易决策之间的循环有多少？许多最赚钱的日子发生在奇怪的事情发生时，发生了一些事件，世界变得疯狂，就像没有人知道发生了什么，

**[13:32 – 13:49]**
**EN:** like that's when it's like very hard to provide liquidity in those contexts and so you get paid more for doing it and there's often a lot of volume on days like that and doing that well often involves human judgment of like thinking about like how is today different from all of the other
**中文：** 就像那样，在这种情况下提供流动性非常困难，因此你会因此获得更多报酬，而且在这样的日子里通常会有很多交易量，而做好这件事往往需要人类的判断，比如思考今天与其他所有地方有何不同

**[13:49 – 14:06]**
**EN:** days and you know to the degree that we can we want to build the models that work well through phase transitions but also we think humans work better than models do through phase transitions and sometimes you need this kind of meta judgment to decide what to do and so there's a even for the systems that are
**中文：** 天，你知道我们可以建立在相变中运行良好的模型，但我们也认为人类在相变中比模型工作得更好，有时你需要这种元判断来决定做什么，所以对于系统来说，有一个甚至是

**[14:06 – 14:21]**
**EN:** largely automated there are decisions to be made by the people who are watching and we always have people who are watching right I think an important part of trading is paying attention to and thinking about what's happening during the trading day even if the individual transactions are going by far too fast
**中文：** 很大程度上是自动化的，决策是由观看的人做出的，而且我们总是有正确观看的人我认为交易的一个重要部分是关注并思考交易日内发生的事情，即使个别交易进展得太快

**[14:21 – 14:36]**
**EN:** for a human to kind of weigh in on a kind of transaction bytransaction basis. Dan, what what have been the more notable changes over the last 20 years that you've been doing in buildings like these? Yeah, people are actually care about data centers and want to talk about it.
**中文：** 让人们在逐笔交易的基础上进行权衡。 Dan，过去 20 年来，您在此类建筑中所做的最显着的改变是什么？是的，人们实际上很关心数据中心并且想要谈论它。


## 物理工程视角：20 年变迁与当前瓶颈

**SECTION_NOTE**
- Dan 从物理工程视角回顾数据中心 20 年的变化
- 从风冷到液冷、从少数机柜到高密度部署
- 当前瓶颈更多来自供应链与交付周期
**END_SECTION_NOTE**

**[14:36 – 14:50]**
**EN:** You know, been working on cooling for a while and now all a sudden people people talk about it and and and think it's interesting. So that's like that's fun and exciting. And for for folks on my team, I think they feel that way as well. There's people who have been in the data center industry for 20 years
**中文：** 你知道，我们在冷却方面的研究已经有一段时间了，现在突然人们开始谈论它并且认为它很有趣。所以这很有趣而且令人兴奋。对于我团队中的人来说，我认为他们也有这种感觉。有人从事数据中心行业20年

**[14:50 – 15:05]**
**EN:** that kind of still want to do it the way they used to. And I think that's kind of falling by the wayside now. Uh you're finding ways where people are um challenging previous thoughts. Hey, these my entire data center is backed up by generators. But generators are some of the longest lead time items you can
**中文：** 那种仍然想像以前那样做的人。我认为现在这种做法有点半途而废了。呃，你正在寻找人们挑战以前想法的方法。嘿，我的整个数据中心都是由发电机支持的。但发电机是您可以提供的交货时间最长的产品之一

**[15:05 – 15:22]**
**EN:** buy. So maybe we take those away and only put it for a core part of the system that needs that resiliency. Um that gets our GPUs on six months faster. Let's do it. So those are things that uh you know maybe Maybe it's not the best engineering decision, but it's truly the best business decision. And I think it's
**中文：** 买。因此，也许我们会把它们拿走，只把它放在需要这种弹性的系统的核心部分。嗯，这让我们的 GPU 运行速度加快了六个月。我们开始做吧。所以这些是你知道的事情，也许这不是最好的工程决策，但它确实是最好的商业决策。我认为这是

**[15:22 – 15:36]**
**EN:** stuff like that that has been coming up more and more often. It feels like every year people change the what what is bottlenecking scaling AI compute right now as you're doing more negotiations and trying to acquire more comput. What what is the current bottleneck and what do you expect it to
**中文：** 类似的事情越来越频繁地出现。感觉每年人们都会改变现在扩展人工智能计算的瓶颈，因为你正在进行更多的谈判并试图获得更多的计算。当前的瓶颈是什么以及您期望它是什么

**[15:36 – 15:49]**
**EN:** be for putting aside comput and memory and all that fun stuff. So generators, uh transformers, um some of the cooling equipment that's used now for the liquid cooling is is is in in a lot of demand. So um and it changes rapidly. What I tell you today is is going definitely
**中文：** 是为了把计算和内存以及所有有趣的东西放在一边。因此，发电机、呃变压器，嗯，现在用于液体冷却的一些冷却设备的需求量很大。所以嗯，它变化很快。我今天告诉你的是肯定会发生

**[15:49 – 16:05]**
**EN:** going to be different 2 weeks from now. Um we do this thing we work very closely with internal teams on the procurement side uh to to stock up on some of this stuff. Stuff that we know is fungeible across all our data centers. We will warehouse and have it ready to go. Um, there's components like generators where
**中文：** 两周后将会有所不同。嗯，我们做这件事时，我们与采购方面的内部团队密切合作，以储备一些这些东西。我们所知道的东西在我们所有的数据中心都是可替代的。我们将入库并准备好发货。嗯，有像发电机这样的组件

**[16:05 – 16:18]**
**EN:** you're not going to put a giant generator in a in a warehouse or or you know, for instance, if you're doing something behind the meter like a turbine, you're gonna you're going to have to think about those markets a little bit more. Um, where you're getting them, where you're staging them,
**中文：** 你不会把一个巨大的发电机放在仓库里，或者你知道，例如，如果你在仪表后面做一些事情，比如涡轮机，你将不得不更多地考虑这些市场。嗯，你在哪里得到它们，在哪里展示它们，

**[16:18 – 16:35]**
**EN:** you can't just leave them off to the side. Um, so I think the components definitely change. Those are some of the big ones. And uh you know as we get to more and more density you know I think one hope is that the buildings get a little bit smaller and maybe and and and we're able to like you know build the
**中文：** 你不能把它们放在一边。嗯，所以我认为组件肯定会改变。这些是一些大的。呃，你知道，随着我们的密度越来越大，我认为一个希望是建筑物变得更小一点，也许我们能够像你知道的那样建造

**[16:35 – 16:49]**
**EN:** buildings faster get all that compute kind of in a nice tight bundle and then all the infrastructure around it's got to got to be maybe pre-built and delivered to site right modular data centers or modular infrastructure is becoming more and more of a thing where these components especially the long
**中文：** 建筑物更快地将所有计算都集中在一个紧密的捆绑中，然后围绕它的所有基础设施都必须预先构建并交付到正确的位置模块化数据中心或模块化基础设施正变得越来越重要，其中这些组件尤其是长

**[16:49 – 17:07]**
**EN:** lead components are being um designed and built offsite and shipped to site. So almost as close to plug-and-play as you can get. Well, one of the points you made earlier is that as uh as the racks themselves get more uh dense uh you know more and more of the data center is like the
**中文：** 主要部件正在异地设计和制造并运送到现场。因此几乎尽可能接近即插即用。嗯，您之前提出的观点之一是，随着机架本身变得越来越密集，您知道越来越多的数据中心就像


## 机架密度、芯片封装类比与 NVL72 vs TPU

**SECTION_NOTE**
- 机架密度持续上升，建筑与基础设施要跟上
- 把数据中心类比为「封装」：芯片在板卡上，板卡在机柜里
- 讨论 NVL72 与 TPU 等不同技术路线的取舍
**END_SECTION_NOTE**

**[17:07 – 17:24]**
**EN:** infra around the actual racks which actually is kind of similar to um like a a a package on like a a chip right or like a chip on a package. It's like the the compute is a very small part of the total area of package. Yeah, it's it's interesting. thing. I
**中文：** 实际机架周围的基础设施实际上有点类似于嗯，就像一个封装，就像一个芯片，或者像封装上的芯片。这就像计算只是封装总面积的很小一部分。是的，这很有趣。事物。我

**[17:24 – 17:39]**
**EN:** mean I I don't you know um it it doesn't solve any problems per se. I mean maybe it creates it creates others. Sure. Like you know you get to a one megawatt rack, right? People are like what does that even mean? One megawatt in a rack and and you know you know the the cooling kind of the pipe is just going to get
**中文：** 我的意思是我不知道，它本身并不能解决任何问题。我的意思是，也许它创造了它也创造了其他人。当然。就像您知道的那样，您可以获得一兆瓦的机架，对吗？人们就像这到底意味着什么？机架中的一兆瓦，您知道管道的冷却类型将会变得

**[17:39 – 17:53]**
**EN:** larger that you're bringing there and uh the amount of power whether it's kind of the AC power that we're using now or 800 volt DC where it's where it's going in the future. You still have to bring all that those components to a spot. And the thing that's like interesting from our point of view is like you know we could
**中文：** 比你带到那里的功率要大，无论是我们现在使用的交流电还是未来使用的 800 伏直流电。您仍然需要将所有这些组件带到一个地方。从我们的角度来看，有趣的事情就像你知道我们可以

**[17:53 – 18:11]**
**EN:** design these these engineering things but at the end of the day whether it's Nvidia or an ASIC or who they have to sell a component that can work in a data center and they're they're thinking very hard about what they sell um because you need people to use it right if you're if you build a one megawatt data center um
**中文：** 设计这些工程东西，但归根结底，无论是 Nvidia 还是 ASIC，或者他们必须销售可以在数据中心工作的组件，他们都在认真思考他们销售的东西，因为如果你建造一个一兆瓦的数据中心，你需要人们正确使用它

**[18:11 – 18:25]**
**EN:** one megawatt rack but there's no way to power and cool it kind of useless. So, you know, we're working very closely with with kind of almost everyone in in that space to think about what are the components you need to be able to support these next generations because the lead times you're talking
**中文：** 一个兆瓦的机架，但没有办法为其供电和冷却，有点无用。所以，你知道，我们正在与该领域的几乎每个人密切合作，思考你需要哪些组件来支持这些下一代，因为你所说的交货时间

**[18:25 – 18:39]**
**EN:** about, you know, over a year sometimes and you're just you're deciding on the infrastructure before you're placing an order for the chips. So, you know, you're trying, for instance, the you know, TPUs, they use lower temperature water and they're they're half as dense as as you know, an
**中文：** 您知道，有时大约需要一年多的时间，您只是在订购芯片之前决定基础设施。所以，你知道，你正在尝试，例如，TPU，它们使用较低温度的水，它们的密度只有你知道的一半，


## 供应链：芯片、冷却、变压器与建设周期

**SECTION_NOTE**
- 发电机、变压器、液冷设备都在抢产能
- 关键部件异地制造后运抵现场组装
- 建设周期与交付能力成为新的约束
**END_SECTION_NOTE**

**[18:39 – 18:55]**
**EN:** NVL72 GB300, right? So that requires a different strategy and and you want to make sure you can handle those in the future. One of the things that allows hyperscalers to commit to large amounts of compute is that they have some reserve use for excess compute that
**中文：** NVL72 GB300，对吧？因此，这需要不同的策略，并且您希望确保将来能够处理这些问题。允许超大规模计算者进行大量计算的原因之一是它们对多余的计算有一些保留用途

**[18:55 – 19:13]**
**EN:** they're not using for training or inference of LLMs at a particular time. For example, like Meta, if they're not using some of the GPUs they bought, they can just say we'll just make our Instagram ad uh serving uh model slightly better for today. What is the equivalent sort of reserve use of compute for Jane
**中文：** 他们不用于在特定时间对法学硕士进行训练或推理。例如，像 Meta 一样，如果他们没有使用购买的某些 GPU，他们可以说我们只是让今天的 Instagram 广告呃服务呃模型稍微好一些。 Jane 的计算储备用途的等效类型是什么

**[19:13 – 19:28]**
**EN:** Street that's just a lower bound on how much that's worth for you? Part of what's going on is like in many ways we're just like very compute constrained. There's lots of innovation and experimentation and new ideas that people have that is bounded by the amount of compute that we have. And so
**中文：** 这条街只是对你来说价值多少的下限？正在发生的事情的一部分就像在很多方面我们就像非常计算受限一样。人们有很多创新、实验和新想法，但这些都受到我们拥有的计算量的限制。所以

**[19:28 – 19:46]**
**EN:** like in some ways like if we just think about like like we do a we try and and do a kind of moderately rigorous job of thinking about the value of the new different runs that we can do and the value of the runs that we're turning away is really quite high, right? So like we're doing what we think are the
**中文：** 就像在某些方面，如果我们只是像我们所做的那样思考，我们尝试并做一种适度严格的工作，思考我们可以做的新的不同跑步的价值，以及我们正在放弃的跑步的价值确实相当高，对吗？就像我们正在做我们认为的那样

**[19:46 – 20:00]**
**EN:** most valuable things but you know if you know if it turns out we have more compute than we need for those there's just like a ton of other research and experimentation that we can do in that space. So like we're we're we're nowhere near to like being like oh too much compute like we sort of have
**中文：** 最有价值的东西，但你知道我们是否拥有比我们需要的更多的计算能力，就像我们可以在该领域进行大量其他研究和实验一样。所以就像我们一样，我们远没有像我们那样拥有太多的计算能力

**[20:00 – 20:17]**
**EN:** have the opposite problem. I think there's also really lowhanging fruit in that direction. Just like it's valuable to retrain the models more often. There's some decay in the quality of models over time and being able to rerun them like that's that's kind of has immediate and clear value to the firm.
**中文：** 有相反的问题。我认为在这个方向上也有非常容易实现的成果。就像更频繁地重新训练模型很有价值一样。随着时间的推移，模​​型的质量会有所下降，而能够像这样重新运行它们，对公司来说具有直接而明显的价值。

**[20:17 – 20:36]**
**EN:** Uh there's also some amount of bulk inference tasks that that we can do that can like fill in the gaps in the systems where there's nothing else to schedule. Um so we don't quite have the thing that looks like the analog of like the Instagram ad serving thing, but there is just like a ton of other like kind of
**中文：** 呃，我们还可以执行一些批量推理任务，例如填补系统中没有其他可安排的空白。嗯，所以我们还没有类似 Instagram 广告服务的东西，但是有很多其他类似的东西

**[20:36 – 20:53]**
**EN:** dark space of like things that we're not doing, but we would if we had more compute. So we're like pretty unconcerned about getting value out of these. Here thing there is like there is a bunch of embedded bets like we are like investing a lot of money in in this stuff and you could imagine that like
**中文：** 我们没有做类似事情的黑暗空间，但如果我们有更多的计算能力，我们就会做。所以我们对从这些中获取价值并不关心。这里有很多嵌入的赌注，就像我们在这个东西上投入了很多钱，你可以想象像

**[20:53 – 21:07]**
**EN:** things won't get better at the rate that we are thinking they will in terms of like the value of the individual models and trades that we're doing and like it's a competitive environment. maybe other people will out compete us. We're like I think one part of remaining good is like always being nervous about other
**中文：** 事情不会以我们认为的速度变得更好，比如我们正在做的单个模型和交易的价值，以及这是一个竞争环境。也许其他人会比我们竞争。我们就像我认为保持良好的一部分就像总是对其他人感到紧张

**[21:07 – 21:24]**
**EN:** ways that competitors can like figure out doing similar things to what you're doing and reduce the value of of that. So like there are ways there are ways that it might not work out but uh certainly with anything like the current mix of compute jobs that we have we're just like very far from having this
**中文：** 竞争对手可能会想办法做与你正在做的事情类似的事情，并降低其价值。因此，就像有一些方法可能无法解决问题一样，但是呃，当然，对于我们目前拥有的计算工作组合之类的东西，我们距离实现这一目标还很远。

**[21:24 – 21:39]**
**EN:** problem. It's it's interesting to this doesn't exactly answer it but like you know you could disconnect the uh the powering the data center from the chips and say okay well you know I I I might need to use this compute later let me commit to the data center and the power now but like delay the decision on the
**中文：** 问题。有趣的是，这并没有完全回答这个问题，但就像你知道的那样，你可以断开数据中心与芯片的供电，然后说好吧，你知道我我我稍后可能需要使用此计算，让我现在就致力于数据中心和电源，但就像延迟做出决定一样


## 电力 vs 芯片：能否拆分与分流

**SECTION_NOTE**
- 可以把供电的「长周期」部分与芯片采购解耦，提前锁定
- 芯片昂贵且交期长，电力与空间可先行布局
- 电力容量而非空间，才是真正的上限
**END_SECTION_NOTE**

**[21:39 – 21:56]**
**EN:** chips which are very expensive right and and just be slightly long power and data center for that that that point of time where you might need that compute um and then we'll build in situations where hey maybe we can kind of offload some of that capacity to somebody else it's much easier for us I is to offload power and
**中文：** 芯片非常昂贵，而且只是稍微长一点的电源和数据中心，在那个时间点，你可能需要计算嗯，然后我们将在这样的情况下构建，嘿也许我们可以将一些容量卸载给其他人，这对我们来说要容易得多，我是卸载电源和

**[21:56 – 22:11]**
**EN:** data center capacity than is the chips themselves for obvious reasons. But uh you can you can really bifrocate those two. This also changes the considerations around hiring. I mean you already have like the highest bar for hiring but it just increases even more if you hire one
**中文：** 数据中心的容量比芯片本身更大，原因显而易见。但是呃，你可以，你真的可以把这两者分开。这也改变了招聘方面的考虑因素。我的意思是，你已经有了最高的招聘门槛，但如果你雇佣一个人，门槛就会更高


## GPU 规模：几万 → 几十万张，瓶颈是人才

**SECTION_NOTE**
- 当前在「几万张 GPU」量级，不久将进入「几十万张」量级
- 真正的瓶颈不是钱也不是电，而是人（研究员与导师辅导）
- 算力的机会成本高，团队之间会竞争同一批资源
**END_SECTION_NOTE**

**[22:11 – 22:29]**
**EN:** more person that is one person who will need compute to do their experiments and that compute is going to be traded off against somebody else who's excellent on your team who could be doing experiments themselves. I I hear what you're saying, but we don't think, oh, it would be weird to hire more researchers because
**中文：** 更多的人需要计算来完成他们的实验，并且计算将与团队中优秀的其他人进行权衡，而其他人可以自己做实验。我听到你在说什么，但我们不认为，哦，雇用更多研究人员会很奇怪，因为

**[22:29 – 22:44]**
**EN:** then we'd have to give them more comput. It's more like the research is incredibly valuable. The researchers are incredibly valuable. This is a good argument for buying more compute. Um, and so we're like very axed to grow the amount of compute. Like these days, we are in something like the range of like
**中文：** 那么我们就必须给他们更多的计算能力。更像是这项研究非常有价值。研究人员非常有价值。这是购买更多计算资源的一个很好的论据。嗯，所以我们非常渴望增加计算量。就像现在一样，我们处于类似的范围内

**[22:44 – 23:03]**
**EN:** tens of thousands of GPUs and we will in not too long be in the range of hundreds of thousands of of GPUs. And we think it's like well justified by the business like you know it's not it's it's not like it's it's not like you know we're worried about like oh you know can we justify it based on like the penals of
**中文：** 数以万计的 GPU，不久之后我们就会达到数十万 GPU 的范围。我们认为这在商业上是合理的，就像你知道的那样，不是这样的，不是你知道的，我们担心的是，哦，你知道，我们可以根据类似的惩罚来证明它是合理的吗？

**[23:03 – 23:19]**
**EN:** the trading strategy. It's like no no no it's like these are clearly good investments. Um so it doesn't feel like it's slowing us down on the hiring front. In some ways, the the biggest impediment to growth is that it takes time to like really train people and absorb them into the culture and kind of
**中文：** 交易策略。就像不不不，这些显然是很好的投资。嗯，所以感觉这并没有减慢我们在招聘方面的速度。在某些方面，增长的最大障碍是需要时间来真正培训人员并将他们吸收到文化和类型中。

**[23:19 – 23:34]**
**EN:** build build them up and build the place up. Like we want Jane Street to continue to be a great place to work. Like I I just don't think of the hardware thing as at all being the thing that slows us down. And and I think the real limiting factors are finding great people and having the mentorship capacity for them.
**中文：** 建造建造他们并建造这个地方。就像我们希望简街继续成为一个工作的好地方一样。就像我一样，我根本不认为硬件问题是拖慢我们速度的因素。我认为真正的限制因素是找到优秀的人才并为他们提供指导能力。

**[23:34 – 23:46]**
**EN:** I guess this might be a good opportunity for you guys to mention what kinds of roles you're currently hiring for. Oh man, why don't you start in the in the engineering space? Yeah, I I'll start. I mean, I think so, we're generally just looking for really smart people, people that that that are
**中文：** 我想这对你们来说可能是一个很好的机会来提及你们目前正在招聘的职位类型。天哪，你为什么不从工程领域开始呢？是的，我会开始。我的意思是，我认为是的，我们通常只是在寻找真正聪明的人，那些人


## 招聘哪些岗位

**SECTION_NOTE**
- 既招资深工程师，也招应届生，用多样化背景挑战既有假设
- 强调「聪明、好奇」的人与团队协作（whole team sport）
- 招聘门槛随算力扩张不降反升
**END_SECTION_NOTE**

**[23:46 – 24:03]**
**EN:** interested in in in doing this stuff and and that's, you know, mechanical engineers, electrical engineers, project managers, architects, people that help design and build some of these spaces. And, you know, our our our remit uh in my team is is really to to find the spaces, to design them, to construct
**中文：** 对做这些事情感兴趣，你知道，机械工程师、电气工程师、项目经理、建筑师、帮助设计和建造其中一些空间的人。而且，你知道，我们团队的职责实际上是寻找空间、设计空间、建造空间

**[24:03 – 24:18]**
**EN:** them, and then to operate them, right? So, it's full life cycle. So in each one of those you kind of need people you know lots of engineers, lots of what we call physical engineering which is a madeup term that that we came up with but uh you know mechanical engineers and structural engineers maybe electrical
**中文：** 然后去操作它们，对吗？所以，它是完整的生命周期。因此，在每一个领域，你都需要一些人，你认识很多工程师，很多我们所说的物理工程，这是我们想出的一个虚构术语，但是呃你知道机械工程师和结构工程师，也许是电气工程师

**[24:18 – 24:34]**
**EN:** engineers those types of folks and and machine learning and trading in general is really like a whole team sport and so we want to hire people from lots of different backgrounds and with lots of different capabilities. Uh we're certainly like very excited to hire people with kind of you know specific
**中文：** 工程师这些类型的人，机器学习和交易一般来说真的就像一个完整的团队运动，所以我们想雇用来自许多不同背景和具有许多不同能力的人。呃，我们当然非常高兴能够雇用具有您所了解的特定知识的人员

**[24:34 – 24:50]**
**EN:** like machine learning backgrounds of like you know designing architectures and building models in various cases. We both I mentioned that we have like a bunch of like custom architectures and stuff for like our own bespoke kind of kinds of data that we need like the data kind of characteristic of the markets.
**中文：** 就像你知道的机器学习背景一样，在各种情况下设计架构和构建模型。我们都提到过，我们有一堆类似的自定义架构和东西，用于我们需要的定制数据类型，例如市场特征的数据类型。

**[24:50 – 25:12]**
**EN:** Um we also build LLMs and people who experience in all sorts of part of the life cycle of LLM training. we're interested in hiring and have been growing that area. Um, you know, we we hire lots of like people with like generally good scientific and technical backgrounds from like math and CS and
**中文：** 嗯，我们还培养法学硕士和在法学硕士培训生命周期的各个方面都有经验的人员。我们对招聘很感兴趣，并且一直在扩大这个领域。嗯，你知道，我们雇佣了很多类似的人，他们具有良好的科学和技术背景，例如数学和计算机科学，

**[25:12 – 25:29]**
**EN:** physics and engineering and stuff to be traders and like there's a kind of mix of skills there. Uh, but that's like an area we continue to be very excited to hire in. On the software engineering side, there's like a general software engineering role which we're always eager to get great people for uh that,
**中文：** 物理和工程以及成为交易员的东西，就像那里有一种技能的组合。嗯，但这就像一个我们仍然非常高兴雇用的领域。在软件工程方面，有一个通用的软件工程角色，我们总是渴望为此找到优秀的人才，

**[25:29 – 25:43]**
**EN:** you know, I think just rewards a little bit, you know, it feels a little silly to say, but just like, you know, as Dan was saying, smart, curious people with really good CS backgrounds, uh, you know, fit into that generalist role and there's lots of different kinds of things they can end up doing. There's
**中文：** 你知道，我认为只是奖励一点点，你知道，这么说感觉有点傻，但就像，你知道，正如 Dan 所说，聪明、好奇、拥有良好 CS 背景的人，呃，你知道，适合那种通才角色，他们最终可以做很多不同类型的事情。有

**[25:43 – 25:59]**
**EN:** also a bunch of interesting specialized areas where we really are excited. Like here's a thing that's kind of new. With all of this scale, we are much more interested in fleet-wide optimization than we were in the past. Like we our old view about about performance optimization was that it was much more
**中文：** 还有一些我们非常兴奋的有趣的专业领域。就像这是一件新鲜事。有了如此规模，我们比过去对整个机队的优化更感兴趣。就像我们一样，我们对性能优化的旧看法是，它的作用要大得多

**[25:59 – 26:13]**
**EN:** about, you know, making the things that were most speedritical as fast as possible. And more generally, yeah, compute's kind of cheap and like people are expensive and we're not spending that much time optimizing our general compute. But like, man, we're doing a lot of general compute now. You know,
**中文：** 你知道，关于尽可能快地制作最快速的事情。更一般地说，是的，计算有点便宜，就像人很贵一样，我们不会花那么多时间来优化我们的通用计算。但是，伙计，我们现在正在做很多通用计算。你知道，

**[26:13 – 26:26]**
**EN:** you start investing billions of dollars in this stuff and it just becomes more valuable there. And there are people who have experience in doing this at some of the hyperscalers and we'd love to hire more people with that kind of background to think about the optimization problems that we're hitting which are like
**中文：** 你开始在这些东西上投资数十亿美元，它就会变得更有价值。有些人在一些超大规模企业有这方面的经验，我们很乐意雇用更多具有这种背景的人来思考我们遇到的优化问题，例如

**[26:26 – 26:44]**
**EN:** related in important ways different but like you know so it's like both a related challenge and a new one. Um we're like we do a lot of fun like hardware engineering stuff. We're like working on our own AS6 people with that kind of experience is super exciting. Um,
**中文：** 两者在重要方面有所不同，但正如你所知，所以这既是一项相关的挑战，又是一项新的挑战。嗯，我们好像做了很多有趣的事情，比如硬件工程。我们就像与拥有这种经验的 AS6 人员一起工作是非常令人兴奋的。嗯，

**[26:44 – 26:58]**
**EN:** one thing that we mentioned a little earlier at lunch was like we're starting to think about building out a formal methods team using basically mathematical proof to make software engineering more effective. That's like a new very speculative area and we're like very excited to find
**中文：** 我们在午餐时早些时候提到的一件事是，我们开始考虑使用基本的数学证明来建立一个正式的方法团队，以使软件工程更加有效。这就像一个新的非常投机的领域，我们很高兴发现

**[26:58 – 27:12]**
**EN:** people there. We feel like that's a kind of a set of a whole community of people who in the past I feel like I've always had to disappoint by like yeah we're not interested in formal methods but like I think the whole AI revolution makes formal methods suddenly a much more interesting field and so it's a place
**中文：** 那里的人。我们觉得这是一个由一群人组成的完整社区，在过去我觉得我总是不得不失望，是的，我们对形式方法不感兴趣，但我认为整个人工智能革命使形式方法突然成为一个更有趣的领域，所以这是一个地方

**[27:12 – 27:27]**
**EN:** we're excited to invest in. So I don't know and like I don't know project managers people who do front-end dev actually like for most of Jane Street's experience we pretended like this whole web thing had never happened and like almost all all of our tools were just like in the terminal but you know it
**中文：** 我们很高兴投资。所以我不知道，就像我不知道做前端开发的项目经理们实际上喜欢Jane Street的大部分经验一样，我们假装这整个网络事情从未发生过，就像我们所有的工具都像在终端一样，但你知道这一点

**[27:27 – 27:40]**
**EN:** turns out it's useful to be able to like draw a straight line and you know have a tool tip and things like that. So, we've actually invested a lot in building really good tools for doing front-end development and building tools for people and having great front-end engineers who are both really good
**中文：** 事实证明，能够画一条直线是很有用的，而且你知道有一个工具提示之类的东西。因此，我们实际上投入了大量资金来构建非常好的前端开发工具，并为人们构建工具，并拥有非常优秀的优秀前端工程师

**[27:40 – 27:56]**
**EN:** software engineers and have a good sense of what it means to make an application that's good for a person is really important. I say like as as a general meta point about all of this, I think that like in all of the like legitimate and real excitement around AI tooling, I think people sometimes like
**中文：** 对于软件工程师来说，充分了解制作对人有益的应用程序意味着什么，这一点非常重要。我说的是关于所有这一切的一般元点，我认为就像围绕人工智能工具的所有合法和真正的兴奋一样，我认为人们有时喜欢

**[27:56 – 28:12]**
**EN:** kind of miss out on the importance of the human element of all of this. I think that we really we really care a ton about building tools that are good for people and that comes that includes the AI tooling itself, right? I think trying to drive tooling in a way that increases human understanding and agency
**中文：** 有点忽视了人为因素在这一切中的重要性。我认为我们真的非常关心构建对人们有益的工具，其中包括人工智能工具本身，对吗？我认为尝试以增强人类理解和能动性的方式驱动工具

**[28:12 – 28:26]**
**EN:** and efficiency is like that's the core thing. We are limited more than anything else by the amazing people who work there and like being able to find more of the right people and grow the organization so that we can get more done. Uh and so we have a very kind of humanoriented way that we think about
**中文：** 效率就是核心。我们最受限制的是在那里工作的优秀人才，他们希望能够找到更多合适的人才并发展组织，以便我们能够完成更多工作。呃，所以我们有一种非常以人为本的思考方式

**[28:26 – 28:44]**
**EN:** the systems that we build. Um, it's been really cool to have you guys um, make these fun puzzles and challenges. I think in general you do that, but also you um, you've been uh, you guys have made a couple for the listeners of the podcast in particular. And I think people who are listening to
**中文：** 我们构建的系统。嗯，有你们来制作这些有趣的谜题和挑战真是太酷了。我认为一般来说你们都会这样做，但你们也特别为播客的听众制作了一些。我认为那些正在倾听的人


## 谜题文化与开放世界挑战

**SECTION_NOTE**
- Jane Street 以「谜题（puzzles）」作为工程文化的组成部分
- 开放世界式的挑战题，用于观察候选人如何思考
- 详情见 janestreet.com 的 puzzles 页面
**END_SECTION_NOTE**

**[28:44 – 29:02]**
**EN:** this might find it interesting to check those out. um uh including one by the way which not only was nobody who submitted to the competition able to solve but Jane Street itself cannot solve which um uh which involves finding back doors to various LLMs that have a trigger phrase baked into them. Anyways,
**中文：** 检查这些可能会很有趣。嗯嗯，顺便说一句，其中一个问题不仅是提交竞赛的人无法解决，而且简街本身也无法解决，这涉及到寻找各种法学硕士的后门，这些后门中嵌入了触发短语。无论如何，

**[29:02 – 29:15]**
**EN:** I mentioned this because um uh to the extent people are interested in learning more, I think these are the kinds of fun puzzles that might give some indication of what work is like and um uh why things like fun place. Yeah, puzzles are a deeply embedded part of the culture. So, it's kind of great
**中文：** 我提到这一点是因为嗯嗯，人们有兴趣了解更多，我认为这些都是有趣的谜题，可能会告诉你工作是什么样的，以及嗯嗯，为什么像有趣的地方这样的东西。是的，谜题是文化中根深蒂固的一部分。所以，这真是太好了

**[29:15 – 29:31]**
**EN:** to use them as a way to reach out to people as well. Yeah. Yeah. Um, I guess the plug here in this case is janestreet.com/doresh. Uh, so that people can learn more about the open worlds and about all these puzzles. Yep. Awesome. Cool. Thanks for doing this, guys. Thank you very much.
**中文：** 也用它们作为接触人们的一种方式。是的。是的。嗯，我猜这里的推广链接是 janestreet.com/doresh。呃，这样人们就可以更多地了解开放世界和所有这些谜题。是的。太棒了。太棒了。谢谢你们这样做，伙计们。非常感谢。

**[29:31 – 29:34]**
**EN:** Our pleasure.
**中文：** 我们的荣幸。

---

*说明：本逐字稿由 **YouTube 官方英文自动字幕（auto-generated captions）** 逐条导出，共 **453 条字幕块 / 约 6,378 词 / 全长 29:36**，每条均保留时间戳（`mm:ss`）；中文为机器翻译并做术语校对（`Ron Minsky→Yaron Minsky`、`Dan Ponttovo/Pavatova→Dan Pontecorvo`、`Okamel→OCaml`、`nanconds→nanoseconds`、`James Street→Jane Street`、`core reef→CoreWeave`、`NBL72 GP300→NVL72 GB300`、`Insta→Instagram`、`fleetwide→fleet-wide`）。*
