# 中英对照逐字稿 / Bilingual Transcript

**Episode:** Einride's Autonomous Freight Strategy（Einride 的自动驾驶货运战略）
**节目：** The Driverless Digest Podcast
**嘉宾：** Henrik Green（Einride 首席技术官 CTO，曾任沃尔沃汽车 CTO）
**来源 / Source：** thedriverlessdigest.com · Spotify / Apple Podcasts

> 说明：英文为 Whisper 自动语音识别结果，中文为机器翻译并经过专有名词校对。时间戳为音频位置，章节标题依据对话内容主题划分。

## 开场 / Intro：交通的三大痛点与节目预告

**[00:00 – 01:17]**

**EN:** Transportation today is flawed or impaired in three major ways. I mean, one being the utilization of assets, which is inefficient. One being the utilization of energy, which is inefficient. And one being also the insecurity and the lack of resilience and stability and safety in human labor. Transporting people is highly emotional while transporting goods is very rational. I think it's an easier scaling for transport of goods. So I think once we get running, we have less of an uphill to run faster. So it's five years, I'd call it the dead-heat race. Before we get started today, I wanted to let you know that I'll be speaking at the SAE Automated Transportation Symposium taking place July 27th through July 30th in San Diego. It's one of the premier gatherings for the autonomous vehicle industry bringing together engineers, researchers, policy makers, regulators, and industry leaders for four days of technical discussions and networking.

**中文：** 当今的交通运输在三个主要方面存在缺陷或受损。我的意思是，其中之一是资产的利用，效率低下。一是能源利用效率低下。其中之一就是人类劳动力的不安全感以及缺乏弹性、稳定性和安全性。运送人是高度感性的，运送货物是非常理性的。我认为这对于货物运输来说更容易扩展。所以我认为一旦我们开始跑步，我们就可以少走上坡路，从而跑得更快。五年了，我称之为不分胜负的比赛。在今天开始之前，我想让您知道，我将在 7 月 27 日至 30 日在圣地亚哥举行的 SAE 自动化运输研讨会上发表演讲。这是自动驾驶汽车行业的重要聚会之一，工程师、研究人员、政策制定者、监管机构和行业领导者齐聚一堂，进行为期四天的技术讨论和交流。

**[01:17 – 01:48]**

**EN:** This year's keynote speakers include Uber's global head of autonomous mobility and delivery, Sarfraz Moradia, Zoox's co-founder and CTO, Jesse Levinson, and NHTSA administrator, Jonathan Morrison. I'm really excited to be attending and speaking, never been to the conference before. So hopefully I'll see you there. I'll be speaking on the journalist panel on Thursday, July 30th at 11 40 a.m. So if you're attending, would love to say hello. Now let's get into today's episode. Henrik Green is the chief technology officer at Einride

**中文：** 今年的主讲嘉宾包括 Uber 自动驾驶和配送全球主管 Sarfraz Moradia、Zoox 联合创始人兼首席技术官 Jesse Levinson 以及 NHTSA 局长 Jonathan Morrison。我很高兴能参加并发言，以前从未参加过该会议。希望我能在那里见到你。我将于 7 月 30 日星期四上午 11 点 40 分在记者小组上发表讲话。如果您出席，我很乐意向您问好。现在我们就进入今天的节目吧。 Henrik Green 是 Einride 的首席技术官

## 嘉宾介绍：Einride CTO Henrik Green 的背景

**[01:48 – 02:33]**

**EN:** where he leads the development and commercialization of autonomous freight systems, including electric and self-driving trucks and the software platforms that power them. Prior to Einride, Henrik spent nearly three decades at Volvo Cars serving as CTO and helping drive the company's electrification, software, and autonomous vehicle initiatives. He also played key roles in partnerships and ventures, including Polestar, Zenseact, Luminar Technologies, Google, and Qualcomm. Henrik, how are you doing today? I'm great and happy to be here. Good to meet you. Yeah, definitely. No, this is our first time chatting and Einride is a company that I've heard a lot about making a lot of news lately, but frankly, I don't know a ton about. So I'd say in a selfish way, I'm really excited to chat with you today just so I can further my own knowledge. So ready to get into it. Yeah, me too. I'm looking forward.

**中文：** 他领导自动货运系统的开发和商业化，包括电动和自动驾驶卡车以及为其提供动力的软件平台。在加入 Einride 之前，Henrik 在沃尔沃汽车公司工作了近三十年，担任首席技术官，帮助推动公司的电气化、软件和自动驾驶汽车计划。他还在 Polestar、Zenseact、Luminar Technologies、Google 和 Qualcomm 等合作伙伴和企业中发挥了关键作用。亨里克，你今天过得怎么样？我很高兴来到这里。很高兴认识你。是的，绝对是。不，这是我们第一次聊天，Einride是一家我最近听说了很多新闻的公司，但坦白说，我对此了解不多。所以我会以一种自私的方式说，我很高兴今天能和你聊天，这样我就可以进一步增长我自己的知识。所以准备好进入其中。是的，我也是。我很期待。

**[02:33 – 02:34]**

**EN:** Cool, awesome.

**中文：** 酷，棒极了。

## 从沃尔沃到 Einride：加入的动机与 legacy 车企 vs 初创

**[02:34 – 03:29]**

**EN:** Well, I'd love to start with your background because I mentioned in the bio, the Volvo angle and your sort of past history there. And when I went over to your LinkedIn earlier, I saw that you were at Volvo for 26 years. So I feel like we can't gloss over that fact because that's quite impressive, quite a long time. And I imagine formed a lot of the basis for your knowledge and what you're doing and what you're interested in industry. Tell me a little bit about that. Well, I mean, obviously I spent tons of years in automotive industry and with personal vehicles, which is in essence, a B2C business where you build your brand and you build your value with the end customer and you provide technology through that channel. And my focus all the time has been on the technology coming from Volvo. It has also always been around safety and those aspects.

**中文：** 好吧，我很想从您的背景开始，因为我在简历中提到了沃尔沃的角度以及您过去的历史。当我早些时候访问您的 LinkedIn 时，我看到您在沃尔沃工作了 26 年。所以我觉得我们不能掩盖这个事实，因为这是相当令人印象深刻的，相当长的时间。我想这为你的知识、你正在做的事情以及你对行业的兴趣奠定了很多基础。请告诉我一些相关情况。嗯，我的意思是，显然我在汽车行业和个人车辆领域工作了很多年，这本质上是一种 B2C 业务，您可以在其中建立自己的品牌，并与最终客户一起建立价值，并通过该渠道提供技术。我一直关注的是沃尔沃的技术。它也一直围绕着安全和这些方面。

**[03:29 – 04:34]**

**EN:** We were quite early into the autonomous among the incumbent, if you will, the incumbent OEMs on the car side. And that always sparked my interest in the way that it's both an amazing engineering challenge to solve the technology in itself. At the same time, it has this large impact on society and in how we move and transport in the Volvo context, people, but in an Einride context, how we transport goods differently tomorrow than we do today. What is one of the biggest differences from all of your work in the B2C, the customer space, and now in the autonomous industry, freight industry? Well, so I think it's two fundamental differences. And one is that Einride as an autonomous electric transport company was built and founded on the hypothesis of this technology change to happen and to make transport better. So we have a business model that goes hand in hand with a technology transformation

**中文：** 如果你愿意的话，我们在汽车方面的现有原始设备制造商中很早就进入了自动驾驶领域。这总是激发我的兴趣，因为解决技术本身就是一个惊人的工程挑战。与此同时，它对社会以及我们如何在沃尔沃环境中移动和运输人员产生巨大影响，但在 Einride 环境中，我们明天如何以与今天不同的方式运输货物。您在 B2C、客户领域以及现在的自动化行业、货运行业的所有工作中最大的区别之一是什么？嗯，所以我认为这是两个根本区别。其中之一是，Einride 作为一家自动驾驶电动运输公司，是建立在这种技术变革发生并让交通变得更好的假设之上的。所以我们有一个与技术转型齐头并进的商业模式

**[04:34 – 05:37]**

**EN:** in Einride. In a legacy car company, many times you come from a background and you have a strong heritage and you have a strong mature base and sometimes strong financials, but transformation is difficult. And changing both your technology and your business model at the same time can prove very, very difficult from time to time. So those are two typical differences. The other thing that I would say is transporting people is highly emotional while transporting goods is very rational. Yeah. What was the big reason, what drew you to Einride? So, I mean, there were a few things. I was spending nearly three decades at a large industrial automotive company. And at that time, being able to collaborate with smaller startups, tech companies from any size, really, got me really interested in trying to see how fast and how nimble you can move when you have a force

**中文：** 在艾因瑞德。在一家传统汽车公司，很多时候你有背景，有深厚的传统，有强大的成熟基础，有时还有雄厚的财务实力，但转型很困难。同时改变你的技术和商业模式有时会变得非常非常困难。这是两个典型的差异。我想说的另一件事是，运输人员是高度感性的，而运输货物是非常理性的。是的。是什么吸引您来到 Einride？所以，我的意思是，有一些事情。我在一家大型工业汽车公司工作了近三十年。当时，能够与规模较小的初创公司、任何规模的科技公司合作，真的让我很感兴趣，想看看当你有力量时，你能移动多快、多灵活。

**[05:37 – 06:28]**

**EN:** and a purpose that is really built to lead a transformation. And that got me curious. And Einride had this business model that matches this technology transformation in such an interesting way. And that also brought me over. Yeah. I know we have a lot of listeners who are either at large OEM or large established. And we also have a lot of people on the startup and the platform side. And then we have a lot of people that are going back and forth. Are there trends that you're seeing or is there advice? I'm guessing maybe people have reached out to you for advice that what they should consider, what type of a role is best for the right person, basically. Well, I think you basically said it there. I think that is some of us, like myself, I really enjoy working both at a large company with a strong heritage and a strong legacy.

**中文：** 以及真正为引领变革而建立的目标。这让我很好奇。 Einride 的商业模式以一种有趣的方式与这种技术转型相匹配。这也让我过来了。是的。我知道我们有很多听众，他们要么是大型 OEM，要么是大型企业。我们在初创公司和平台方面也有很多人。然后我们有很多人来来回回。您是否看到了趋势或有什么建议？我猜想也许人们已经向你寻求建议，告诉你他们应该考虑什么，什么类型的角色最适合合适的人。嗯，我想你基本上已经说了。我认为我们中的一些人，就像我自己一样，我真的很喜欢在一家拥有悠久传统和强大遗产的大公司工作。

**[06:28 – 06:47]**

**EN:** And I do really enjoy working at Einride which is quite newly founded even though we are 10 years now, a tech company. And I see the differences and I thrive and I learn and I develop from differences. Some people I may prefer one over the other. And I guess that comes to personality a lot. Yeah.

**中文：** 我真的很喜欢在 Einride 工作，这是一家刚刚成立的科技公司，尽管我们已经成立 10 年了。我看到了差异，我从差异中成长、学习和发展。有些人我可能更喜欢其中一个。我想这很大程度上取决于个性。是的。

## Einride 的三大支柱：资产、能源与人力利用的效率革命

**[06:47 – 07:35]**

**EN:** So you mentioned Einride has been around for 10 years. Can you share a little more background about the company and also what makes them stand out in the industry? So Einride was founded on the hypothesis that transportation today is flawed or impaired in three major ways. I mean, one being the utilization of assets which is inefficient, one being the utilization of energy which is inefficient and one being also the insecurity and the lack of resilience and stability and safety in human labor. And addressing these three can fundamentally change the transportation industry and Einride was built creating a model to address all of those three impactful transformations in the transport industry.

**中文：** 你提到 Einride 已经存在 10 年了。您能否分享更多关于该公司的背景以及是什么让他们在行业中脱颖而出？因此，Einride 的成立基于这样一个假设：当今的交通在三个主要方面存在缺陷或受损。我的意思是，一是资产的利用效率低下，一是能源的利用效率低下，一是人类劳动力的不安全感和缺乏弹性、稳定性和安全性。解决这三个问题可以从根本上改变运输行业，Einride 的建立创建了一个模型来解决运输行业中所有这三个有影响力的转型。

## 运营现状：电动卡车队 + 5 辆无人自动驾驶卡车（无安全员）

**[07:35 – 08:34]**

**EN:** Got it. And where are you operating? What's the product? What's the footprint look like? So today we're operating a fairly large fleet of human driven electric trucks that already addresses two of the pillars, the AI optimization to increase utilization of the asset itself, the trucks and also the energy consumption in the higher efficiency electric propulsion compared to the traditional diesel propulsion. In the case of autonomous, we have a fairly small fleet but we are commercial today. We're operating with five trucks globally both in Europe and US then combined as we speak with fully self-driving which is no safety driver on board trucks in day-to-day operations. And we see all these three pillars grow going forward. Yeah. So what are you, what is the company sort of most focused on, most excited about? Is it the human fleet of EV trucks, the autonomous side? I mean, it seems like we're at this interesting phase

**中文：** 知道了。你们在哪里经营？产品是什么？足迹是什么样子的？因此，今天我们正在运营一个相当大的人力驱动电动卡车车队，它已经解决了两个支柱：人工智能优化，以提高资产本身、卡车的利用率，以及与传统柴油推进相比，更高效的电力推进的能源消耗。就自动驾驶而言，我们拥有相当小的车队，但今天我们已经商业化。我们在全球欧洲和美国运营着五辆卡车，然后将其合并为完全自动驾驶，在日常运营中卡车上没有安全驾驶员。我们看到这三大支柱都在不断发展。是的。那么你是什么，公司最关注、最兴奋的是什么？是电动卡车的人力车队，还是自动驾驶方面？我的意思是，我们似乎正处于这个有趣的阶段

**[08:34 – 09:28]**

**EN:** right now where a lot of companies like yourself are making most of their money, most of their revenue, most of their business is from the human side but investors or media or public or even people like me care more about the autonomous side. So we'd love to know how you weigh those two considerations. Well, I mean, as a company we're fundamentally addressing both and we talk a lot about one end right internally which is how we make one plus one plus one equals more than three addressing these areas in combination gives us that extra value. Externally, I can say that if I oversimplify in Europe there is a very high interest for electrification slightly more hesitation towards automation or autonomous drive while in US there is more hesitation than I would say to electric trucks and a very, very strong interest and push on autonomous trucks.

**中文：** 现在，很多像你这样的公司的大部分钱、大部分收入、大部分业务都来自人类方面，但投资者、媒体、公众、甚至像我这样的人更关心自主方面。因此，我们很想知道您如何权衡这两个因素。嗯，我的意思是，作为一家公司，我们从根本上解决这两个问题，并且我们在内部谈论了很多关于一个目的的问题，这就是我们如何使一加一加一等于三以上，结合解决这些领域给我们带来了额外的价值。从外部来看，我可以说，如果我过于简单化的话，欧洲对电气化的兴趣非常高，对自动化或自动驾驶的犹豫程度稍高，而在美国，对电动卡车的犹豫程度比我所说的要多，对自动卡车的兴趣和推动力非常非常强烈。

**[09:28 – 09:30]**

**EN:** If I generalize.

**中文：** 如果我概括的话。

## 产品解析：cabless 自动驾驶卡车（Class 8、尺寸、GE Appliances 等客户）

**[09:30 – 10:21]**

**EN:** Yeah, no, I think I agree that makes sense. And I mean, I think you mentioned your autonomous fleet, five trucks. I appreciate that you said there's no safety driver because I feel like anytime there's an announcement about a new ride or a new operation if they don't mention explicitly that there's no safety driver there is a safety driver when you dig into the details but they don't always share that. So how is that going? Well, I mean, that's really exciting and we built our trucks currently with manufacturing partners but we build them cabless which means there isn't even a driver's seat in those trucks. It's built for autonomous operation only. And we do that with customer in selected areas in US and in Europe and we run their daily operation. It's rather short shuttles that do these typically repetitive boring flows that are to some extent

**中文：** 是的，不，我想我同意这是有道理的。我的意思是，我想你提到了你的自动驾驶车队，五辆卡车。我很欣赏你说没有安全司机，因为我觉得任何时候都会有关于新游乐设施或新运营的公告，如果他们没有明确提到没有安全司机，当你深入了解细节时，就会有安全司机，但他们并不总是分享这一点。那么进展如何呢？嗯，我的意思是，这真的很令人兴奋，我们目前与制造合作伙伴一起制造卡车，但我们制造的是无电缆的，这意味着这些卡车中甚至没有驾驶员座椅。它专为自主操作而设计。我们与美国和欧洲选定地区的客户合作，并负责他们的日常运营。执行这些典型的重复钻孔流程的穿梭机相当短，在某种程度上

**[10:21 – 11:17]**

**EN:** the easiest to automate because they are short and repetitive and predictable compared to more complex scenarios. And it's also scenarios where you, for instance, struggle to get drivers to appreciate the, well, the excitement, I guess, of driving back and forth between a warehouse and a factory all day long, so yes. Yeah, the vehicle is quite cool. We'll put a link and an image in the show notes but I believe, is it called the pod? You mentioned it as cabless, right? What's the product actually called? We call it, nowadays we call it the autonomous truck to make it, yeah. Okay, cool. And what are the sort of dimensions and size? So it's a class eight rigid flatbed which means we can do a fixed cargo hold with a full class eight weight class or we can do a 20 foot container on the flatbed. Okay, so quite a lot of space.

**中文：** 最容易自动化，因为与更复杂的场景相比，它们简短、重复且可预测。例如，在这种情况下，你很难让司机体会到，嗯，我想，整天在仓库和工厂之间来回开车的兴奋感，所以是的。是的，这辆车很酷。我们将在节目注释中放置一个链接和一张图像，但我相信，它被称为 Pod 吗？你提到它是电缆，对吧？该产品的实际名称是什么？我们称之为自动驾驶卡车，现在我们称之为自动驾驶卡车，是的。好吧，酷。尺寸和大小是怎样的？所以它是一个 8 级刚性平板，这意味着我们可以做一个完整的 8 级重量等级的固定货舱，或者我们可以在平板上做一个 20 英尺的集装箱。好吧，空间很大。

**[11:17 – 12:13]**

**EN:** And for example, what are the types of commercial runs that they're doing in the US or Europe, these autonomous trucks? So typically right now we are working with a majority of industrial customers that do produce goods for the industrial market. For instance, General Electric Appliances is one of our pinnacle and oldest customers to which we move their production goods from the production facility to the nearby warehouse on a daily basis with two autonomous truck that keep that flow completely up and running. And that's a typical setup. We have a similar setup in South Carolina and in Arizona and US and we also do that in Sweden, in Europe. Got it, so would these be on private roads and there's less kind of regulatory barriers or are they on public roads or how does that part work? Yeah, exactly, so there is a mix of that

**中文：** 例如，他们在美国或欧洲进行的商业运营类型是什么，这些自动驾驶卡车是什么？因此，现在我们通常与大多数为工业市场生产商品的工业客户合作。例如，通用电气公司是我们的顶级和最古老的客户之一，我们每天使用两辆自动卡车将他们的生产货物从生产设施转移到附近的仓库，以保持流程完全正常运行。这是一个典型的设置。我们在南卡罗来纳州、亚利桑那州和美国也有类似的设置，我们还在瑞典和欧洲也这样做。明白了，那么这些是在私人道路上且监管障碍较少，还是在公共道路上，或者这部分是如何工作的？是的，确实如此，所以有多种因素的混合

**[12:13 – 13:06]**

**EN:** and we have received public permit to operate in a few states in US and in total that including US, five countries over the world, which would mean then four European countries and US. So, and with that we can operate on public road in those particular cases and that's really our sweet spot because there are a number of companies out there who can operate solely on private grounds or fenced areas, which would require mainly technology that lives up to machine regulatory requirements, which is that's part of an industry or part of a factory if you will, but it's outdoors fenced where we build our products from ground up with the purpose to be public road applicable and to fulfill the NHTSA requirements, for example in US or what we call them the Transportstyrelsen and equivalent in Sweden

**中文：** 我们已获得在美国的几个州以及包括美国在内的总共五个国家/地区开展业务的公共许可，这意味着四个欧洲国家和美国。因此，在这些特殊情况下，我们可以在公共道路上运营，这确实是我们的最佳选择，因为有许多公司只能在私人场地或围栏区域运营，这主要需要符合机器监管要求的技术，这是行业或工厂的一部分，如果你愿意的话，但它是在室外围栏，我们从头开始制造我们的产品，目的是适用于公共道路并满足 NHTSA 要求，例如在美国或我们所说的国家/地区他们是 Transportstyrelsen 和瑞典的同等机构

## 部署与监管：公共道路许可、按站点审批、覆盖 5 国

**[13:06 – 14:04]**

**EN:** for public road operation. Got it, makes sense. Now, very interesting and cool to see that you're already live with operations. Sounds like you've got several customers, several countries and things are progressing well. What is the sort of main goal for yourself and the company going forward over the next year? So obviously executing on our plans and scaling this product now, we have a number of vehicles that is already in pipeline for deployment this year. So we will scale, I would call it intelligently scale, which means that we go for select customers and select route and we operate with quality and always with safety in mind. But that's how we plan to progress going forward. Yeah, where do you build the vehicles and how much do they cost or whatever you can share there? Are they expensive or what do you think on that side? No, yeah, so I mean,

**中文：** 用于公共道路运营。明白了，有道理。现在，看到您已经开始运营，非常有趣且很酷。听起来您有多个客户、多个国家/地区，而且事情进展顺利。您和公司明年的主要目标是什么？显然，我们现在正在执行我们的计划并扩展该产品，今年我们已经准备好部署许多车辆。因此，我们将扩大规模，我将其称为智能规模，这意味着我们选择特定的客户并选择路线，我们以质量和安全为中心进行运营。但这就是我们计划继续前进的方式。是的，你在哪里制造这些车辆，它们的成本是多少，或者你可以在那里分享什么？它们贵吗？或者您对此有何看法？不，是的，所以我的意思是，

**[14:04 – 15:11]**

**EN:** typically on all autonomous trucks today, you will find sensor sets and compute that are quite advanced. And today we still, we procure them as mainly most of our competitors do from the leading suppliers or tech companies that manufacture and design these components like lidars, radars, chipsets, et cetera. And of course, those are not part of a regular truck equipment and they go on top in this case. Removing the unit economics from having a labor onboard the vehicle well compensates for the added cost to the vehicle. Got it. Right now we are sourcing our chassis from a vehicle manufacturer in Holland. So they're made in Europe. Okay, cool, cool. And what is the sensor stack that you're using? You mentioned lidar, radar, obviously a chip stack. Yeah, so we do follow the mainstream here. I would say with the three modalities, lidar, radar and camera. We also use a ultrasonic for close range.

**中文：** 通常在当今的所有自动驾驶卡车上，您会发现非常先进的传感器组和计算。今天，我们仍然像大多数竞争对手一样从制造和设计激光雷达、雷达、芯片组等组件的领先供应商或科技公司采购它们。当然，这些不是常规卡车设备的一部分，在这种情况下它们位于顶部。消除车辆上的劳动力带来的单位经济性可以很好地补偿车辆增加的成本。知道了。目前，我们正在从荷兰的一家汽车制造商那里采购底盘。所以它们是欧洲制造的。好吧，酷，酷。您使用的传感器堆栈是什么？你提到了激光雷达、雷达，显然是芯片堆栈。是的，所以我们确实遵循这里的主流。我想说的是三种模式：激光雷达、雷达和摄像头。我们还使用超声波进行近距离测量。

**[15:11 – 16:14]**

**EN:** But the three modalities that I would say is almost industry standard, including long range and short range on those. And then Nvidia powered compute stack, which is also more or less standard among the leading companies in this space. Is there any hardware or software that is unique to your vehicle because you're in the freight industry and or because it's cabless? Well, I mean, so the fundamental, right? Yeah, yes. So there is no cab. So there is no steering wheel and there is no brake pedal. And that means you have electronic brake system. You have electronic steering system. All of those systems needs to be fault redundant and built and designed in a way so no single fault can ever cause an operational error. And that is part of the reason why we have built this chassis ground up with a manufacturing partner because basically there is no commercial available

**中文：** 但我想说的三种模式几乎是行业标准，包括远程和短程。然后是 Nvidia 支持的计算堆栈，这或多或少也是该领域领先公司的标准。是否有任何硬件或软件是您的车辆所独有的，因为您从事货运行业或因为它是无电缆的？嗯，我的意思是，这是最基本的，对吧？是的，是的。所以没有出租车。所以没有方向盘，也没有刹车踏板。这意味着你有电子制动系统。你有电子转向系统。所有这些系统都需要具有故障冗余性，并且以某种方式构建和设计，以便任何单一故障都不会导致操作错误。这就是我们与制造合作伙伴一起构建这款底盘的部分原因，因为基本上没有商业可用

**[16:14 – 16:32]**

**EN:** OEM built chassis that do comply to these redundancy standards. And these are necessary in order to operate autonomously in a safe way. They're also mandatory for most regulatory requirements to operate without the safety drive from public road, et cetera. Got it. I think that makes sense.

**中文：** OEM 制造的机箱确实符合这些冗余标准。为了以安全的方式自主运行，这些都是必要的。对于大多数监管要求来说，它们也是强制性的，以便在没有公共道路等安全驾驶的情况下运行。知道了。我认为这是有道理的。

## 货运 vs 客运：为何自动驾驶货运在监管与场景上更易落地

**[16:32 – 17:20]**

**EN:** So on the regulatory side, this might be a little bit in the weeds, so forgive me. But I know on when you're transporting passengers, you know, companies like Zoox, I think are waiting on special approvals, right? To be able to transport passengers because they don't have a steering wheel. It sounds like it might be different since you're not transporting passengers on the regulatory requirement side. So I would imagine it's easier to get permit to transport goods. I'm not the expert to exactly explain the differences but we have achieved permits, as I said before, in US and in Europe. So it is a per site permit, I'd like to emphasize. So we need to get a new permit for every new site we operate on. So are there any major differences or challenges or anything that stands out from a technical point of view since you are transporting goods

**中文：** 因此，在监管方面，这可能有点杂乱，所以请原谅我。但我知道，当你运送乘客时，像 Zoox 这样的公司，我认为正在等待特殊批准，对吗？能够运送乘客，因为他们没有方向盘。听起来情况可能有所不同，因为您不按照监管要求运送乘客。所以我想获得运输货物的许可证会更容易。我不是准确解释这些差异的专家，但正如我之前所说，我们已经在美国和欧洲获得了许可。我想强调的是，这是每个站点的许可证。因此，我们需要为我们运营的每个新地点获得新的许可证。那么，自从您运输货物以来，是否存在任何重大差异或挑战，或者从技术角度来看有什么突出的事情

**[17:20 – 18:14]**

**EN:** instead of passengers or, you know, people? Well, I would say the autonomous stack, if it transport people or goods to what I can think of right now is more or less the same. It is optimized, the vehicle itself is of course a truck. So it's optimized for transporting goods in that sense. And then I think the business model is also of course optimized around goods. There is a few, I mean, if you have a robot taxi you need to make sure you cater for the customer getting in and out of the vehicle which would be a problem they need to solve. We would need to solve a problem like how do we load and unload goods? How do you dock at the loading bay? Those would be the problems that we solve in our technology, for example. Yeah, so I'm trying to think, I guess really the heart of my question is, is it easier?

**中文：** 而不是乘客，或者，你知道，人？好吧，我会说自动堆栈，如果它能将人员或货物运送到我现在能想到的地方，或多或少是一样的。它是经过优化的，车辆本身当然是一辆卡车。因此，从这个意义上来说，它针对货物运输进行了优化。然后我认为商业模式当然也是围绕商品进行优化的。我的意思是，如果你有一辆机器人出租车，你需要确保满足顾客进出车辆的需求，这将是他们需要解决的问题。我们需要解决一个问题，比如如何装卸货物？如何停靠在装卸区？例如，这些就是我们在技术中解决的问题。是的，所以我试着思考，我想我的问题的核心实际上是，它更容易吗？

**[18:14 – 19:01]**

**EN:** And I don't know that it's necessarily easier because you have different challenges. And even from, you know, when the vehicles are operating on the roads it's not like you can have, you know, because there's no passenger, you know, you can have one less sensor or one less radar. You still have other cars on the road that you need to be aware of. So maybe there aren't any savings there. No, I would say the main difference on that aspect, I would say that goods tend to travel in desolated areas. We tend to build factories and warehouses in desolated areas. That helps us a lot. And it's, so we get the repetitive flows and we get the desolated areas where if you're a robot taxi company I imagine you want to be in the inner city where people want to move themselves in urban areas. And that's where you have the high volume

**中文：** 我不知道这一定会更容易，因为你面临着不同的挑战。即使从，你知道，当车辆在道路上行驶时，你也不能拥有，你知道，因为没有乘客，你知道，你可以少一个传感器或一个雷达。路上还有其他车辆需要注意。所以也许那里没有任何积蓄。不，我想说的是这方面的主要区别，我想说的是，货物往往在荒凉的地区流动。我们倾向于在荒凉地区建造工厂和仓库。这对我们有很大帮助。确实如此，所以我们得到了重复的流动，我们得到了荒凉的地区，如果你是一家机器人出租车公司，我想你希望位于市中心，人们希望在城市地区移动自己。这就是你拥有高音量的地方

**[19:01 – 19:09]**

**EN:** of people movement, which is much more complex and requires much more edge case verification.

**中文：** 人员流动的情况，这要复杂得多，需要更多的边缘情况验证。

## 产品形态演进：短途重复路线 → 半挂长途高速

**[19:10 – 20:03]**

**EN:** And so where do you see the Einride product, you know, over the next few years kind of having the best, you know, form factor, the best fit? You mentioned that it's doing, you know, if, you know, it sounds like maybe these are shorter routes right now for, you know, private companies. Do you see these, you know, on the highways? What do you think is like the best use case for the product going forward? Yeah, exactly. I mean, right now the form factor is optimal for these shorter routes and repetitive flows in desolated areas. And then moving forward, we see, we are next generation, we see ourselves progressing to a semi setup where there is a tractor trailer and a full trailer cargo capacity where we would go for longer shipments and longer routes and at higher speeds. And that's how we plan to scale and grow commercially.

**中文：** 那么，您在哪里看到 Einride 产品在未来几年内拥有最好的外形尺寸和最合适的尺寸？你提到它正在做，你知道，如果，你知道，听起来也许这些对于私营公司来说可能是更短的路线。你在高速公路上看到过这些吗？您认为该产品未来的最佳用例是什么？是的，完全正确。我的意思是，目前这种形状因素对于这些较短的路线和荒凉地区的重复流动来说是最佳的。然后向前迈进，我们看到，我们是下一代，我们看到自己正在发展到半设置，其中有牵引拖车和全拖车货运能力，我们将在其中以更高的速度进行更长的运输和更长的路线。这就是我们计划扩大规模和实现商业增长的方式。

**[20:03 – 21:02]**

**EN:** Got it. And so this would be sort of more the general kind of trucking landscape, you know, where big rigs are going all across the state, all across the country and places like the United States. It is. And there is a distinction here between us and many of our competitors since we run also human driven electric trucks and we have chosen the business model to provide freight capacity as a service to the end shipper. We do not typically do this hub to hub highway cases for multiple customers, but we do A to B shipments, point to point shipments for the end customer in which we own the operation. And that gives us more control over the use cases and over the customer, the end customer result. And that being distinctive, but in essence, yes, there is a full size heavy duty semi truck in the middle that does the transportation

**中文：** 知道了。因此，这将是一种更普遍的卡车运输格局，你知道，大型卡车正在全州、全国和美国等地行驶。这是。我们和许多竞争对手之间存在区别，因为我们还经营人力驱动的电动卡车，并且我们选择了向最终托运人提供货运能力作为服务的商业模式。我们通常不会为多个客户提供枢纽到枢纽的高速公路运输服务，但我们会为我们拥有业务的最终客户提供 A 到 B 的运输、点对点运输。这使我们能够更好地控制用例和客户以及最终客户的结果。这是独特的，但本质上，是的，中间有一辆全尺寸重型半挂卡车负责运输

**[21:02 – 21:08]**

**EN:** on a regular road. So that's still being the same. Got it. And you've sort of explained it here and there,

**中文：** 在常规道路上。所以这仍然是一样的。知道了。你已经在这里那里解释过了，

## 商业模式：把『货运能力』作为服务卖给托运人（端到端运营）

**[21:08 – 22:10]**

**EN:** but I guess if we take one step back for the audience and do kind of an overview of the landscape, you know, how do you look at the different sectors and like where you guys fit in best from, you know, getting a good basically from wherever it's manufactured to the customer, the end customer. Well, so basically I put ourselves, the way we are unique is that we are addressing all three dimensions of transportation than energy, human labor and asset utilization and doing that by selling to the end customer, which is the shipper, the person or the company that needs the goods to be shipped. And we run the operation for that customer, which means that we own a very large portion of that end to end logistic operation. That gives us the opportunity and the control to steer. Where is it optimum to use electric human driven vehicle?

**中文：** 但我想，如果我们为观众退后一步，对整个情况进行概述，你知道，你如何看待不同的行业，以及你们最适合的地方，你知道，基本上从制造到客户、最终客户的任何地方都能获得良好的结果。好吧，基本上我认为，我们的独特之处在于，我们正在解决运输的所有三个方面，而不是能源、人力和资产利用，并通过向最终客户（即托运人、需要运输货物的个人或公司）销售来实现这一目标。我们为该客户运营业务，这意味着我们拥有端到端物流业务的很大一部分。这为我们提供了引导的机会和控制力。在哪里最适合使用电动人力驾驶车辆？

**[22:10 – 22:53]**

**EN:** Where is it optimal to go in and do autonomous vehicles? How do we optimize that total fleet? Gives us that holistic view and we can give, we can sell to a rather immature customer in the sense that our customer gets the good transported. He or she does not need to know how to handle an autonomous truck or need to have an operational team to get trained or whatnot. That makes our product fairly easy to go to market and it gives us a lot of control in exactly what pieces we put together for that customer in his operation. And that's where I think we stand out most compared to our competitors.

**中文：** 哪里最适合进入自动驾驶汽车领域？我们如何优化整个机队？为我们提供了整体视图，我们可以向相当不成熟的客户销售产品，因为我们的客户得到了货物的运输。他或她不需要知道如何操作自动卡车，也不需要拥有一个操作团队来接受培训等等。这使得我们的产品相当容易进入市场，并且使我们能够在很大程度上控制我们在客户的运营中为客户组装哪些部件。我认为这就是我们与竞争对手相比最突出的地方。

## 技术挑战：无安全员安全证明与渐进式扩展

**[22:53 – 23:49]**

**EN:** Got it, got it. So what are some of the biggest technical challenges in building and deploying autonomous freight vehicles today? Well, I mean, the biggest challenge is of course to prove that you are safe enough to operate without the safety driver on public road in complex scenarios. And we are addressing that in a piecemeal manner where we start with the lower complexity areas and we grow incrementally from there. But in essence, that's the core problem we are all working on. Got it. And I mean, I think it's always a good reminder to remember for the approaches like Einride when there is no driver, no safety driver, no steering wheel, no brakes or no accelerator like you mentioned. I mean, is it just more of an iterative process? The vehicle goes out onto a one lane road in a very safe spot and then it starts making right turns around the block

**中文：** 明白了，明白了。那么，当今建造和部署自动货运车辆面临的最大技术挑战是什么？嗯，我的意思是，最大的挑战当然是证明你足够安全，可以在复杂的场景下在没有安全驾驶员的情况下在公共道路上进行操作。我们正在以零碎的方式解决这个问题，从复杂性较低的领域开始，然后从那里逐步发展。但本质上，这是我们正在努力解决的核心问题。知道了。我的意思是，我认为这总是一个很好的提醒，要记住像 Einride 这样的方法，当没有驾驶员、没有安全驾驶员、没有方向盘、没有刹车或没有加速器时，就像你提到的那样。我的意思是，这更像是一个迭代过程吗？车辆驶入非常安全地点的单车道道路，然后开始绕街区右转

**[23:49 – 24:39]**

**EN:** and then that gets bigger. Or can you share like actual, what are sort of the actual training of these vehicles look like in the real world? Is that kind of iterative nature or how does it work? Yeah, you're pretty much spot on. I would add to your description that even before we put the autonomous truck on site, we're there with a data collection vehicle. So we digitize the entire route from A to B. So we have a digital twin of that. We run tons of simulations and trainings on that particular site before we deploy. So even in the virtual space, we have done quite a lot of verification before we get the vehicle on site. Of course, when we get the vehicle on site, we start to operate and we grow incrementally on that site. And then we can also choose among our database with tens of thousands of routes

**中文：** 然后它会变得更大。或者您能否分享一下这些车辆在现实世界中的实际训练是什么样的？这是一种迭代性质吗？或者它是如何工作的？是的，你说得很对。我想在你的描述中补充一点，即使在我们将自动驾驶卡车放到现场之前，我们就已经有一辆数据收集车了。所以我们把从 A 到 B 的整个路线数字化。所以我们有一个数字孪生。在部署之前，我们会在该特定站点上进行大量模拟和培训。因此，即使在虚拟空间中，我们在现场拿到车辆之前也做了相当多的验证。当然，当我们把车辆送到现场时，我们就开始运营，并在该网站上逐步发展。然后我们还可以在我们拥有数万条路线的数据库中进行选择

**[24:39 – 25:02]**

**EN:** that we operate for, that our customers have in their flows and the customers that we are already operating for, we can also in a data-driven way, select how we grow that step incrementally. We go from a shorter route to a longer route. We go from a slightly low complexity to a medium complexity situation. What are some of the edge cases that you've seen

**中文：** 我们为之运营的客户、我们的客户在其流程中拥有的客户以及我们已经为其运营的客户，我们还可以以数据驱动的方式选择如何逐步发展这一步骤。我们从较短的路线走向较长的路线。我们从稍微低复杂度的情况变成中等复杂度的情况。您见过哪些极端情况

## 长尾案例与部署流程：雪堆轶事、远程协助、数字孪生路线

**[25:02 – 25:58]**

**EN:** or that you have to worry about or that keep you up at night? Now, yeah, so yeah, a bit of an anecdote, of course, a few years back, when I was out and we were operating for a customer in Gothenburg here in Sweden and suddenly there was a big snow pile next to us because it had been snowing the day before. And our system didn't recognize the snow pile, so it paused and the vehicle stopped and basically made a safe maneuver and our remote operator could go in and confirm to the vehicle that what it saw was the snow pile so it could safely pass next to it. And yes, no headache, but that's typically what can happen. Yeah, gotcha, makes sense. And so it sounds like based off what you've described with the repetitive shorter routes and you guys are mapping some of these routes ahead of time,

**中文：** 或者是你必须担心的事情或者让你彻夜难眠的事情？现在，是的，所以是的，有一点轶事，当然，几年前，当我外出时，我们正在为瑞典哥德堡的一位客户工作，突然我们旁边有一个大雪堆，因为前一天下了雪。我们的系统无法识别雪堆，因此它暂停了，车辆停下来，基本上进行了安全操作，我们的远程操作员可以进去并向车辆确认它看到的是雪堆，这样它就可以安全地通过雪堆旁边。是的，不头痛，但这通常会发生。是的，明白了，有道理。所以这听起来像是基于您所描述的重复的较短路线，并且你们正在提前绘制其中一些路线，

**[25:58 – 27:00]**

**EN:** it sounds like the kind of approach from a technical point of view would be more on the kind of pre-mapping side and leveraging that versus the other approach we have in AVs right now that's more of an end-to-end map-less approach. What are your thoughts on that sort of debate taking place? Yeah, so I mean, we see a hybrid of that and that's how we build our system. So we definitely see and are building these larger foundational models, which also with reasoning that will take more and more of the responsibility of the drive while we keep what we call then a guardrail at the deterministic system that we train particularly per site. Gotcha. So you can say that we constrain the world model with deterministic algorithms that we are site-proven to be safe in order for us to achieve the permit. But we also, the end goal is very similar

**中文：** 听起来，从技术角度来看，这种方法更多地是在预映射方面，并利用这种方法，而不是我们现在在自动驾驶汽车中采用的其他方法，后者更多是一种端到端的无地图方法。您对正在进行的此类辩论有何看法？是的，所以我的意思是，我们看到了这种混合体，这就是我们构建系统的方式。因此，我们肯定看到并正在构建这些更大的基础模型，这些模型也有推理，将承担越来越多的驱动器责任，同时我们在我们特别针对每个站点进行训练的确定性系统中保留我们所谓的护栏。明白了。因此，您可以说，我们使用确定性算法来约束世界模型，并且经过现场验证，这些算法是安全的，以便我们获得许可。但我们的最终目标也非常相似

## 技术路线：混合架构（基础模型+确定性护栏）、地图 vs 无图、双重定位

**[27:00 – 27:55]**

**EN:** to many of our competitors. When we scale, we're going to grow that capability and once we go from, and I think this is the interesting part because many people think about how you go from three handful of R&D vehicles to the world. And that's quite a big step. And I think what we are unlocking is how do we go from 10 to 20 to 100 to 200 to 600 vehicles. And that's the plan we have laid out before ourselves. And that's the sort of the vision and the roadmap we have. The end goal of that is of course, to unlock any driving situation anywhere. Yeah, to me, that hybrid approach always makes sense, especially when you think about transporting, whether it's people or goods from A to B. I mean, it's great to be able to take a map list and drive out in the middle of Sweden and the country roads.

**中文：** 我们的许多竞争对手。当我们扩大规模时，我们将增强这种能力，一旦我们离开，我认为这是有趣的部分，因为很多人都会思考如何从三把研发车辆走向世界。这是相当大的一步。我认为我们要解决的是如何将车辆数量从 10 辆增加到 20 辆、100 辆、200 辆到 600 辆。这就是我们摆在面前的计划。这就是我们的愿景和路线图。其最终目标当然是解锁任何地方的任何驾驶情况。是的，对我来说，这种混合方法总是有意义的，尤其是当你考虑运输时，无论是从 A 地到 B 地运送人还是货物。我的意思是，能够拿着地图列表在瑞典中部和乡村道路上行驶真是太棒了。

**[27:55 – 28:35]**

**EN:** But how many customers are actually gonna want that use case, like the density of where rides are taking place, of where goods are being moved are the same. So if they're going the same routes all the time, even if you have a map-less approach, you still obviously having a 3D map of where you're going is gonna add some help, right? I don't think. Yeah. And I mean, yeah. And I mean, we have dual localization systems in, I mean, we localize ourselves. This is a bit technical, but we localize ourselves with satellites and then we can compare that to a map. We can also localize ourselves completely with our sensor set and have that redundancy built in. Yeah.

**中文：** 但有多少客户实际上想要这个用例，比如乘车地点的密度、货物运输地点的密度是相同的。因此，如果他们一直走相同的路线，即使您采用无地图方法，显然您仍然拥有一张显示您要去的地方的 3D 地图，这会增加一些帮助，对吗？我不认为。是的。我的意思是，是的。我的意思是，我们有双重本地化系统，我们对自己进行本地化。这有点技术性，但我们用卫星定位自己，然后我们可以将其与地图进行比较。我们还可以使用我们的传感器组完全定位自己，并内置冗余。是的。

## 商业化与规模化：已验证产品市场契合，进入规模扩张期

**[28:35 – 29:30]**

**EN:** So I was curious to know, you mentioned scaling the company. I also, we talked a little bit about commercialization. How do you think about balancing, I guess you would call it commercialization and scaling. What phase do you think Einride is in in the company and what phase do you think the industry, the freight industry is in when it comes, AV freight industry is in? Yeah, I mean, frankly, I think that a lot of companies are struggling with how to commercialize and how to make sometimes a brilliant piece of technology into a sellable product. And I think that's really one of the key unique points with Einride is that we started from the question, how do we sell this product? Well, we sell it as freight capacity, which means that the customer don't need to worry about at all how autonomous technology works or who to operate or how to operate it.

**中文：** 所以我很想知道，你提到了扩大公司规模。我也，我们讨论了一些关于商业化的问题。你如何看待平衡，我想你会称之为商业化和规模化。您认为 Einride 公司正处于哪个阶段？您认为整个行业、货运行业正处于哪个阶段？当它到来时，AV 货运行业正处于哪个阶段？是的，坦白说，我认为很多公司都在努力解决如何商业化以及如何将一项出色的技术转化为可销售产品的问题。我认为这确实是 Einride 的关键独特点之一，那就是我们从这个问题开始：我们如何销售这个产品？好吧，我们将其作为货运能力出售，这意味着客户根本不需要担心自主技术如何工作或由谁操作或如何操作。

**[29:30 – 30:24]**

**EN:** We take care of all of that work. And we have these cabless vehicles that we can start to operate right now. We have a number of them in our possession and they are in pipeline and we can sell transport and we are selling transport. So some in that we unlocked the business equation and the customer proposition and we can grow. So from that, I think we have proven a product market fit and we are in a scaling question rather than how to sell it or how to commercialize it question, which I think and see many of our peers are still struggling with. Got it. So would you say that you have kind of a path to commercialization or you're trying to scale right now and make money on each vehicle? I guess that would be kind of that. Yeah, exactly. I would say that we are commercialized

**中文：** 我们负责所有这些工作。我们拥有这些无缆车辆，现在就可以开始运营。我们拥有许多这样的设备，并且正在准备中，我们可以出售运输，我们正在出售运输。因此，我们在某些方面解锁了业务方程式和客户主张，并且我们可以成长。因此，我认为我们已经证明了产品的市场契合度，我们面临着一个扩展问题，而不是如何销售它或如何将其商业化的问题，我认为并看到我们的许多同行仍在努力解决这个问题。知道了。那么你会说你有一条商业化的道路，还是你现在正试图扩大规模并在每辆车上赚钱？我想就是这样。是的，完全正确。我想说的是我们已经商业化了

**[30:24 – 30:35]**

**EN:** and we are in a scaling phase. So I guess that's kind of the best spot to be, right? It's a very interesting spot to be, especially now because I mean,

**中文：** 我们正处于扩展阶段。所以我想那是最好的地方，对吧？这是一个非常有趣的地方，尤其是现在，因为我的意思是，

## 未来展望：拯救生命、降本增效，货运自动化的多重收益

**[30:35 – 31:25]**

**EN:** as you also alluded to in the beginning, I've spent decades in this industry and around autonomous and we have many of us have waited for the moment when this was going to be commercialized. And actually, I think we are at the point right now where some of us are commercializing this and it will scale from here. Yeah, definitely. What are you most excited about over the next few years? You just mentioned, you know, your three decades looking and talking about autonomous vehicles and now they're here, they're scaling, they're commercializing what kind of keeps you up and keeps you motivated every day to go to work. Well, I mean, you said that already. I think it's an amazing technology. And I mean, everybody knows the speech on how autonomous will change the world of transportation and how we transport goods and people. And I think that is, if we do that right,

**中文：** 正如您一开始也提到的，我在这个行业和自动驾驶方面已经工作了几十年，我们中的许多人都在等待商业化的那一刻。事实上，我认为我们现在正处于我们中的一些人正在将其商业化的阶段，并且它将从此开始扩展。是的，绝对是。未来几年你最兴奋的是什么？你刚才提到，你知道，你三十年来一直在寻找和谈论自动驾驶汽车，现在它们已经出现了，它们正在扩展，它们正在将让你保持活力并每天激励你去工作的东西商业化。嗯，我的意思是，你已经说过了。我认为这是一项了不起的技术。我的意思是，每个人都知道关于自动化将如何改变交通运输世界以及我们如何运输货物和人员的演讲。我认为如果我们做得对的话

**[31:25 – 32:19]**

**EN:** that can be a very beautiful story. It can save lives. There is, I mean, there is a more than a million people dying in traffic every year. That's a very, very large number. Now, of course, before we have automated the total transport sector and traffic area, it's of course quite a long time, but it's a very interesting and inspiring purpose to work against. Got it. So you're excited about saving lives. I mean, what are some of the other benefits you think from automating freight that we'll see? Well, of course, saving already day one, we're saving costs and we're creating resilience and both energy and asset utilization. So those efficiencies are already here. Got it. And then, I mean, I guess it kind of also makes me think, this is an argument we hear a lot from the robotaxi companies too, that they're saving lives. And I don't know that they argue a ton

**中文：** 这可能是一个非常美丽的故事。它可以拯救生命。我的意思是，每年有超过一百万人死于交通事故。这是一个非常非常大的数字。当然，现在，在我们实现整个运输部门和交通区域的自动化之前，这当然还需要相当长的时间，但这是一个非常有趣和鼓舞人心的目标。知道了。所以你对拯救生命感到兴奋。我的意思是，您认为我们会看到自动化货运带来的其他好处是什么？嗯，当然，从第一天起就开始节省，我们正在节省成本，我们正在创造弹性以及能源和资产利用率。所以这些效率已经存在了。知道了。然后，我的意思是，我想这也让我想到，我们也从机器人出租车公司那里听到了很多这样的论点，他们正在拯救生命。我不知道他们争论了很多

**[32:19 – 32:28]**

**EN:** that they're bringing costs down, right? Because it's people just going around and maybe in the future, I guess that is the argument. What do you think about the adjacent industries

**中文：** 他们正在降低成本，对吗？因为人们只是四处走动，也许在未来，我想这就是争论。您对邻近行业有何看法

## 相邻行业：robotaxi 与无人配送的协同，Waymo 铺路

**[32:28 – 33:26]**

**EN:** to autonomous freight? It's a robotaxis, autonomous delivery. Are these areas that you're excited about that you keep your eye on or that aren't really pertinent to you? How do you think about these other adjacent autonomous vehicle industries? Well, I mean, personally, I'm very excited about them because I think they all have their purpose and position to play in society broader and in business. And I think that's amazing. I also think there is a practical, we're all using the same SOCs, we're using the same HPCs to train our deep learning networks, et cetera. So there is synergies across our industries and we can learn from each other. And I mean, right now, the Waymo and the robotaxi industry has paved the wave for many of us coming today. Yeah, well, I mean, I think that's one of the reasons why I started the driverless digest a couple of years ago.

**中文：** 自主货运？这是一辆机器人出租车，自主送货。这些领域是您感到兴奋并持续关注的领域，还是与您无关的领域？您如何看待其他邻近的自动驾驶汽车行业？嗯，我的意思是，就我个人而言，我对他们感到非常兴奋，因为我认为他们都有自己的目标和地位，可以在更广泛的社会和商业中发挥作用。我认为这太棒了。我还认为有一个实用的方法，我们都使用相同的 SOC，我们使用相同的 HPC 来训练我们的深度学习网络，等等。因此，我们的行业之间存在协同效应，我们可以互相学习。我的意思是，现在，Waymo 和机器人出租车行业已经为我们今天到来的许多人铺平了道路。是的，我的意思是，我认为这就是我几年前开始无人驾驶摘要的原因之一。

**[33:26 – 34:11]**

**EN:** I took my first Waymo and it is cool that from the robotaxi point of view, you get to experience it as a customer. Do you think that excitement that the robotaxi industry brings needs to be translated to freight? I mean, I, as a customer, I'm probably never gonna experience the product. I get to hear it and see it and talk about it. Do you think that matters or that's just the people don't care about how things get to them, but if they're faster and quicker and cheaper, they'll probably be happy. Mostly yes. And that's also what I meant in the introduction there when I said that personal transportation is highly emotional and it's people care about the brand that they are being transported in. They care about the comfort on that transport. They care about a lot of things with their vehicle and their personal transport,

**中文：** 我乘坐了我的第一辆 Waymo，从机器人出租车的角度来看，你可以作为客户体验它，这很酷。您认为机器人出租车行业带来的兴奋是否需要转化为货运？我的意思是，作为客户，我可能永远不会体验该产品。我能听到它、看到它并谈论它。你认为这很重要吗？或者只是人们不关心东西如何到达他们手中，但如果它们越来越快、越来越便宜，他们可能会很高兴。大多数情况下是的。这也是我在介绍中所说的意思，当时我说个人交通是高度情绪化的，人们关心他们乘坐的交通工具的品牌。他们关心交通工具的舒适度。他们关心车辆和个人交通的很多事情，

**[34:11 – 34:50]**

**EN:** which are to some extent, not always rational. And if you look at transporting of goods, it's probably the most rational business I ever been with. It's a very high cost, low margin business typically to many of the companies that we provide our service to. Logistics is the biggest part of their total cost structure and a percentage or two of saving goes directly to their profit margin and it becomes extremely rational. So what's the energy cost? What's the labor cost? What's the asset cost? And yeah, very rational decision.

**中文：** 在某种程度上，这并不总是理性的。如果你看看货物运输，你会发现这可能是我从事过的最理性的行业。对于我们提供服务的许多公司来说，这是一项成本非常高、利润率很低的业务。物流是他们总成本结构的最大组成部分，一两个比例的节省直接影响他们的利润率，这变得极其合理。那么能源成本是多少？人工成本是多少？资产成本是多少？是的，非常理性的决定。

## 感性 vs 理性：客运重品牌体验，货运重成本与利润

**[34:51 – 35:31]**

**EN:** Well, let's end on a fun one prediction time. Do you believe the autonomous freight industry or the robotaxi industry will be bigger in five years? Oh, that's a really good question because obviously robotaxi was earlier out and if you would measure today is more broadly used by customers, absolutely. I think it's an easier scaling for transport of goods. So I think once we get running, we have less of an uphill to run faster. So it's five years, I'd call it the dead-heat race. Okay, I like that.

**中文：** 好吧，让我们以一个有趣的预测时间结束吧。您认为五年内自动货运行业或机器人出租车行业会变得更大吗？哦，这是一个非常好的问题，因为显然机器人出租车很早就出现了，如果你今天衡量的话，绝对会被客户更广泛地使用。我认为这对于货物运输来说更容易扩展。所以我认为一旦我们开始跑步，我们就可以少走上坡路，从而跑得更快。五年了，我称之为不分胜负的比赛。好吧，我喜欢这样。

## 预测对决：robotaxi 与货运谁更大？『胶着赛跑』与配送的无限 TAM

**[35:31 – 36:20]**

**EN:** I think one thing that's interesting, sort of a dark horse when the goods and delivery space is because I think the TAM is actually, it's almost unlimited when you start getting the cost, the marginal cost of delivery down to zero, right? I only need so many rides per day for myself and I also have a car, right? I'm not gonna go take a bunch of rides because it's cheap or that many more. With delivery though and goods, it's like, anything, everything, food, groceries, items, whatever I mean, people, especially in the US love to buy things. So I think this will be interesting race to watch. Yeah, it's very interesting. If you would just have all the logistic costs for everything and you would take away the labor shortage bottlenecks so you could scale it more or less infinitely, how would that change the behavior of our consumers?

**中文：** 我认为有一件有趣的事情，当货物和交付空间时，它是一匹黑马，因为我认为 TAM 实际上，当你开始获得成本时，它几乎是无限的，交付的边际成本降至零，对吗？我自己每天只需要这么多的行程，而且我还有车，对吧？我不会因为便宜或更多而去乘坐很多游乐设施。不过，对于送货和货物来说，一切都一样，食物、杂货、物品，无论我的意思是什么，人们，尤其是在美国，喜欢买东西。所以我认为这将是一场有趣的比赛。是的，这很有趣。如果你只承担所有事情的物流成本，并且消除劳动力短缺瓶颈，这样你就可以或多或少地无限扩展它，这将如何改变我们消费者的行为？

**[36:20 – 36:24]**

**EN:** Yeah, I think we'll find out in a few years.

**中文：** 是的，我想几年后我们就会知道。

## 收尾与资源：如何关注 Einride

**[36:24 – 36:50]**

**EN:** So Henrik, really appreciate you coming on. If folks wanna learn more about Einride and what you're up to, we can leave a link in the show notes to the website, your LinkedIn profile, anywhere else they should go or keep their eyes on to stay tuned to Einride's next moves. Well, I think that's a good place and of course our www.enride.tech is also a good place to be. Perfect, all right, Henrik, thank you very much. Take care. Thank you, take care.

**中文：** Henrik，非常感谢你的到来。如果人们想了解有关 Einride 以及您的动态的更多信息，我们可以在展会备注中留下指向该网站、您的 LinkedIn 个人资料以及他们应该访问或关注的其他任何地方的链接，以随时关注 Einride 的下一步动向。嗯，我认为这是一个好地方，当然我们的 www.enride.tech 也是一个好地方。完美，好吧，亨利克，非常感谢你。小心。谢谢你，保重。
