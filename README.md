author: Nathaniel Perkins

A variant calling pipeline, requires bwa, samtools, freebayes, and snpEff.
Creates a subdirectory containing all intermediate files. WARNING: The
subdirectory is deleted after another call to script.py is made.

bwa index > bwa mem > samtools > freebayes > snpEff

Usage: python3 script.py ref.fa infile.fq snpEff_genome

	--bwa_path: path to bwa
	--samtools_path: path to samtools
	--freebayes_path: path to freebayes
	--snpEff_path: path to snpEff.jar
