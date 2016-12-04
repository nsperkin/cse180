import os
import sys
import argparse

def pipeline():
    # check args

    if len(sys.argv) < 4:
        print("USAGE: python script.py <ref> <infile>")
        return

    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs=3)
    parser.add_argument('--bwa_path', default='bwa', help='Destination of bwa')
    parser.add_argument('--samtools_path', default='samtools', help='Destination of samtools')
    parser.add_argument('--freebayes_path', default='freebayes', help='Destination of freebayes')
    parser.add_argument('--snpEff_path', default='snpEff.jar', help='Destination of snpEff')

    args = parser.parse_args()

    os.system(args.bwa_path + " index " + args.file[0])
    os.system(args.bwa_path + " mem -M -t 16 " + args.file[0] + " " + args.file[1] + " > output.sam")
    os.system(args.samtools_path + ' view -Sb output.sam | ' + args.samtools_path + ' sort -o output.bam')
    os.system(args.freebayes_path + " -f " + args.file[0] + " output.bam > output.vcf")
    os.system("java -jar " + args.snpEff_path + " " + args.file[2] + " output.vcf > output.ann.vcf")

    if(os.path.exists("./intermediate_files")):
        os.system("rm -rf intermediate_files")
    os.system("mkdir intermediate_files && mv *.amb *.ann *.bwt *.fai *.pac *.sa *.bam *.sam *.vcf intermediate_files")

pipeline()
