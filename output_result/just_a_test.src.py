from evolvepro.src.process import generate_wt, generate_single_aa_mutants

generate_wt('MAKEDNIEMQGTVLETLPNTMFRVELENGHVVTAHISGKMRKNYIRILTGDKVTVELTPYDLSKGRIVFRSR', 
            output_file='/home/zjlab/luca-data/will/EvolvePro/output_result/kelsic_WT.fasta')

generate_single_aa_mutants('/home/zjlab/luca-data/will/EvolvePro/output_result/kelsic_WT.fasta', 
                           output_file='/home/zjlab/luca-data/will/EvolvePro/output_result/kelsic.fasta')
