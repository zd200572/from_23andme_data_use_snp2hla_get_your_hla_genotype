Updated 2019.8.30

Yet another HLA genotyper using hibag https://shiny.zd200572.com/HLA-HIBAG/,  code modified from https://github.com/nicokist/23andmeHLA, compared to the latter， my can predict the full result and Probability. The Correct rate is still low for some genotypes. It's a R Shiny app, deployed in Tencent cloud. Welcome  using!

![](https://github.com/zd200572/from_23andme_data_use_snp2hla_get_your_hla_genotype/blob/master/hla-hibag.jpg)
Updated 2018.8.20



I made a web page to enable this to genotype HLA by SNP chip data (in .txt format, commonly used to provide to customers by 23andme, etc). To use my web page, you can rename your txt data to your **email adress_name.txt**, such as zd@163.com.txt. Choose '选择文件' button, and choose your renamed data, uploaded by click '提交' button. The process may take 60 about seconds, depends on your data size. Thoeriticaly, any snp chip data can be used, the software used snp rs id to get HLA results. The datasets used to execute HLA genotype is **Pancific-Asian population**, and European population can be accessed on **snp2hla** website. 



My url is here: https://jiawen.zd200572.com/hla/HLA%E5%88%86%E5%9E%8B%E5%99%A81.html



My blog about this: https://jiawen.zd200572.com/431.html



可以用snp芯片数据实现HLA分型，任意的SNP芯片，只要位点数足够即可（几十万）。

由于本人几乎没有前端和后台水平，所以应用相当简陋，请谅解。请把数据命名为邮箱地址.txt,如zd@163.com.txt

请选择并上传你的芯片数据文件（及扩展数据，可选）即可完成HLA分型。使用的建站gcloud进行的，配置只有单核1.6G，HLA分型器会耗时30min左右，请耐心等待,结束后以结果以邮件形式发送到你的邮箱。

是采用大神开发的snp2hla进行分型的，具体过程可参考我的博客：https://jiawen.zd200572.com/431.html

snp2hla是大名鼎鼎的Broad研究所开发的，通过snp分型数据来获得HLA分型信息的软件。它的准确度主要依赖于一个尽可能大的，针对特定民族人群的参考数据集。这个网页采用的是2014年发表的东亚人群的参考数据集，部分准确度约为80%。由于不同芯片的数据中HLA区域位点的数目不同，可能获得的结果有n多候选，请悉知。

做这个纯属个人爱好，原始数据和结果将在得出结果后删除。也可以按软件说明自己搞，也挺简单的。

#### 联系邮箱

zd200572#163.com(#->@)

地址也放在这：

<https://jiawen.zd200572.com/hla/HLA%E5%88%86%E5%9E%8B%E5%99%A81.html>





以前的说明：

np2hla是大名鼎鼎的Broad研究所开发的，通过snp分型数据来获得HLA分型信息的软件。它的准确度主要依赖于一个尽可能大的，针对特定民族人群的参考数据集。
txt格式的数据，首先转换成vcf格式，然后转换成plink兼容格式，有点绕，但是是我找到的两个解决方案之一。另一个是C#程序，一步到位，但是我不会编译C#，只好做罢，估计是windows程序员开发的，github地址放在这：https://github.com/arrogantrobot/23andme2vcf
vcf2ped

使用vcftools搞定
ped等2bed等
SNP2HLA得到结果

如果你感兴趣却不能自己运行获得结果，可以把数据发邮件到zhaojiadong#zd200572.com，#换@，我可以在业余时间帮你得到hla分型数据，准确率总的在60%以上，仅供娱乐。我不会存储利用任何数据，得到结果后立即删除。

If you interested in this and can not do it by your self, you can sent your 23andme or other snp data to me ,zhaojiadong#zd200572.com ,@ replace #, I can help you get your own hla genotype, the correct portion is above 60%, just for fun. I will not save or use your data at any level, your data will deleted once the result sent to you.
