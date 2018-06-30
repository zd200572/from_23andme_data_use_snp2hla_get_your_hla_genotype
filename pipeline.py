import os
import shutil
from snp2hla import *

file_name = os.listdir('../test_data')
print(file_name)
people = file_name[0].split('.')[0]
os.mkdir(people)
os.chdir(people)
shutil.move('/home/zd200572/test_data/' + file_name[0], './') #

def get_ped_files():
    '''
    get ped files use vcftools from 23andme data in vcf format
    :param filename:
    :return:bed, map
    '''
    os.system('/home/zd200572/biosoft/vcftools_0.1.13/bin/vcftools --vcf ./people.vcf --out ./people --plink')


def get_vcf_file():
    '''
    get vcf file from a perl script
    :param file_name:.txt
    :return:.vcf
    '''
    os.chdir('/home/zd200572/biosoft/23andme2vcf')
    os.system('perl ./23andme2vcf.pl /home/zd200572/start/%s/%s /home/zd200572/start/%s/people.vcf ' % (people, file_name[0], people))
    os.chdir('/home/zd200572/start/%s' % people)


def get_bed_files():
    '''
    use plink to transfer ped files etc to bed etc
    :param file_bed:b
    :return:
    '''
    os.system('/home/zd200572/biosoft/plink-1.07-x86_64/plink  --noweb --file ./people --make-bed --out ./people')


def execute_snp2hla():
    '''
    use snp2hla to impute the hla genotype
    :param file_bed:ped, map
    :return:bed, fam
    '''
    os.system('/home/zd200572/biosoft/SNP2HLA_package_v1.0.3/SNP2HLA/SNP2HLA.csh ./people \
    /home/zd200572/biosoft/SNP2HLA_package_v1.0.3/Pan-Asian/Pan-Asian_REF ./people- \
    /home/zd200572/biosoft/SNP2HLA_package_v1.0.3/SNP2HLA/plink 1000 1000')


def get_hla_result():
    '''
    get result from the result file and print
    :param file_name:file_name
    :return:none
    '''
    get_vcf_file()
    get_ped_files()
    get_bed_files()
    execute_snp2hla()
    HLA_type, hla_id = get_sample_id('people-.bgl.phased')
    get_HLA_typing_result('people-.bgl.phased', HLA_type, hla_id)
    print('congratualtions, jobs are finished, get your result and just for fun')

get_hla_result()
os.chdir('..')