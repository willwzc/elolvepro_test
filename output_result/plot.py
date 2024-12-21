from evolvepro.src.plot import read_exp_data, plot_variants_by_iteration

round_base_path = "/home/zjlab/luca-data/will/EvolvePro/output_result/rounds_data"
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx', 'kelsic_Round4.xlsx', 'kelsic_Round5.xlsx']
wt_fasta_path = "/home/zjlab/luca-data/will/EvolvePro/output_result/kelsic_WT.fasta"

df = read_exp_data(round_base_path, round_file_names, wt_fasta_path)
plot_variants_by_iteration(df, activity_column='activity', output_dir="/home/zjlab/luca-data/will/EvolvePro/output_result/plots", output_file="kelsic")
