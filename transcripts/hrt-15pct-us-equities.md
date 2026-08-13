## 创立背景：2002 年的交易市场

**[00:01 – 00:31]**

**EN:** Hudson River Trading is a quantitative trading firm. To explain why HRT was founded — what the founders were ultimately trying to do — it's important to set the scene for what trading looked like at the time. Trading was automated to some extent in 2002, but there were humans involved. Although a lot of the trades happened on exchange, you can imagine pit traders yelling at each other, with a human in the loop clicking a button to make sure a trade gets executed. At the same time, there were more fully automated marketplaces — Island, ARCA, and other smaller electronic exchanges known as ECNs — that were growing in volume. So HRT was founded with the idea that, okay, there's really some automation that can happen here.

**中文：** Hudson River Trading（HRT）是一家量化交易公司。要解释 HRT 当初为何创立——创始人到底想做成什么——得先把当时的交易业态讲清楚。2002 年的时候，交易已经在一定程度上实现了自动化，但人依然在场。虽然大量成交发生在交易所里，但你大可以想象交易池里交易员互相喊价、靠人工点击按钮来确认一笔交易被执行。与此同时，也出现了更全自动化的市场——Island、ARCA，以及其它被称为 ECN（电子通信网络）的小型电子交易所——它们的成交量正在快速增长。所以 HRT 创立的出发点就是：好吧，这里确实有很大的自动化空间可以挖掘。

## 量化模型与市场影响

**[00:31 – 00:59]**

**EN:** As you might expect, predicting the price of anything tomorrow is really, really hard. And so these models are certainly much smarter than I am — or any single human — at predicting markets. But you shouldn't imagine them as being clairvoyant. They can't predict, say, the price of Tesla will be this tomorrow. What they can do is systematically make better-than-random predictions at massive scale on any instrument you can think of. That is sort of the core engine of our trading: being able to give a better estimate — or at least our best guess — of the price of any stock, future, or bond, in a minute, an hour, a day. And that is driven by an AI model of our own creation.

**中文：** 正如你所料，预测任何东西明天的价格都真的真的很难。所以这些模型在预测市场方面，肯定比我、也比任何一个单个人都聪明得多。但你不该把它们想象成能未卜先知的神谕。它们没法预言说"特斯拉明天的股价就会是这个数"。它们真正能做的，是在巨大规模上、对你所能想到的任何标的，系统性地做出优于随机的预测。这大概就是我们交易的核心引擎：能够在一分钟、一小时或一天的时间尺度上，对任何股票、期货或债券给出更优的估计——或者至少是我们最好的猜测。而这背后驱动着的，是我们自己研发的 AI 模型。

**[00:59 – 01:19]**

**EN:** The impact that HRT has had on these markets over the years has been pretty noticeable — not just HRT, but all of these quantitative trading firms. Retail investors are basically paying zero to trade into anything. And that's very different from how it was back in 2002. A lot of that can be attributed to automated trading and the role that quantitative trading firms such as HRT play in the world.

**中文：** 多年来，HRT 对这些市场产生的影响相当显著——而且不只是 HRT，所有这些量化交易公司都是如此。如今散户买卖任何东西，基本上都是零成本。这和 2002 年的情况截然不同。而这其中很大一部分，要归功于自动化交易，以及像 HRT 这样的量化交易公司在市场中扮演的角色。

## 为什么是 C++：性能的两难

**[01:19 – 01:26]**

**EN:** HRT uses C++ fairly extensively, at least in various performance-sensitive contexts. So that would be our live trading environment, and also various parts of our research environment.

**中文：** HRT 相当广泛地使用 C++，至少在各种对性能敏感的环节上是这样。也就是说，我们的实时交易环境，以及研究环境的多个部分，都大量用到 C++。

**[01:26 – 02:06]**

**EN:** So why does performance matter? There are two really important facets of performance. One is throughput, or scale; the other is latency. Talking about latency first: latency is how long it takes to get a particular message through the system. Latency is really important in trading, because when you have trading strategies, packets can only move at the speed of light. They're always looking into the past — they're reacting to some market event that already happened. Microseconds matter in this space, and C++ is a language that lets you achieve that latency without needing to micro-optimize every line of code. These days, market data scale is about 20 terabytes of streaming market data every day that HRT consumes — that's very high throughput. It's also latency-sensitive. And so these market data parsers sit between the exchange and HRT, translating market data from an external format into something more standardized that HRT can then consume.

**中文：** 那么为什么性能如此重要？性能有两个真正关键的维度。一个是吞吐量，也就是规模；另一个是延迟。先说延迟：延迟就是一条特定消息穿过整个系统所需的时间。在交易中，延迟极其重要，因为只要你运行交易策略，数据包就只能以光速传播。策略永远在"看后视镜"——它们是在对某个已经发生过的市场事件做出反应。在这个领域，微秒都至关重要；而 C++ 正是一门能让你达成这种低延迟、又无需逐行微优化的语言。如今，HRT 每天要处理的市场数据流式规模约为 20 TB——这是极高的吞吐量。同时它又对延迟极其敏感。所以这些市场数据解析器就位于交易所和 HRT 之间，把外部格式的市场数据翻译成 HRT 能够消费的、更标准化的格式。

**[02:06 – 02:21]**

**EN:** Some people are concerned by the lack of memory safety that C++ provides. HRT isn't very concerned by that. I think that comes with the territory, is how I would frame it. When you want to use a language as highly performant as C++, there's some amount of safety that you sign yourselves up for, in order to achieve that level of performance. How do we get over that hump? Well, we hire strong developers who ultimately know how computers work, and can map the language — C++ — to what is happening under the hood, and write safe and performant code at the same time.

**中文：** 有些人会担心 C++ 缺乏内存安全机制。HRT 倒不是特别担心这一点。我的看法是，这本来就是这门语言"自带"的代价。当你想用像 C++ 这样高性能的语言时，为了达成那种性能水平，你就要在安全性上做出一定程度的妥协。那我们怎么跨过这道坎？很简单——我们招募真正强的工程师，他们不仅懂计算机底层的运作原理，能把 C++ 这门语言映射到机器底层实际发生的事，还能同时写出既安全又高性能的代码。

## 与 C++ 共成长，占据 15% 市场

**[02:21 – 02:26]**

**EN:** HRT has really grown and grown up with C++ over the years. If you look at our impact on the market right now — US equities in particular — HRT is roughly 15% of the market.

**中文：** 这些年来，HRT 真的是和 C++ 一起成长、一起成熟的。看看我们如今对市场的影响——尤其是美国股市——HRT 大约占了整个市场的 15%。

**[02:26 – 02:32]**

**EN:** And I truly don't think HRT could have done it without C++.

**中文：** 而我真心认为，如果没有 C++，HRT 不可能走到今天这一步。

---

*说明：本视频的 YouTube 自动生成字幕（VTT）在 02:32 之后存在一段与前述「性能 / C++」内容完全重复的尾巴（至 03:53），属字幕生成器的重复切片 artifact。本逐字稿已对重复部分去重，仅保留唯一的第一遍讲述（00:01–02:32）。英文为自动字幕原文（已顺手修掉少量口误重复，如 "the the"、"better better"），中文为人工翻译。*
