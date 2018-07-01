np2hla是大名鼎鼎的Broad研究所开发的，通过snp分型数据来获得HLA分型信息的软件。它的准确度主要依赖于一个尽可能大的，针对特定民族人群的参考数据集。
txt格式的数据，首先转换成vcf格式，然后转换成plink兼容格式，有点绕，但是是我找到的两个解决方案之一。另一个是C#程序，一步到位，但是我不会编译C#，只好做罢，估计是windows程序员开发的，github地址放在这：https://github.com/arrogantrobot/23andme2vcf
vcf2ped

使用vcftools搞定
ped等2bed等
SNP2HLA得到结果

如果你感兴趣，可以把数据发邮件到zhaojiadong#zd200572.com，#换@，我可以帮你得到hla分型数据，准确率总的在60%以上，仅供娱乐。我不会存储利用任何数据，得到结果后立即删除。
