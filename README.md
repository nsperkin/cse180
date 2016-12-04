author: Nathaniel Perkins

A variant calling pipeline, requires bwa, samtools, freebayes, and snpEff

bwa index > bwa mem > samtools > freebayes > snpEff

Usage: python3 script.py <ref.fa> <infile.fq> <snpEff genome>

	--bwa_path: path to bwa
	--samtools_path: path to samtools
	--freebayes_path: path to freebayes
	--snpEff_path: path to snpEff.jar
