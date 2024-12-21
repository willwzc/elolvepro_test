from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MAKEDNIEMQGTVLETLPNTMFRVELENGHVVTAHISGKMRKNYIRILTGDKVTVELTPYDLSKGRIVFRSR', output_file='C:/Users/wzcwi/EvolvePro/output_result/kelsic_WT.fasta')
generate_single_aa_mutants('C:/Users/wzcwi/EvolvePro/output_result/kelsic_WT.fasta', output_file='C:/Users/wzcwi/EvolvePro/output_result/kelsic.fasta')
input("Press Enter to exit...")
exit()