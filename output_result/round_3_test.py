from evolvepro.src.evolve import evolve_experimental

protein_name = 'kelsic'
embeddings_base_path = 'C:/Users/wzcwi/EvolvePro/output_result'
embeddings_file_name = 'kelsic_esm1b_t33_650M_UR50S.csv'
round_base_path = 'C:/Users/wzcwi/EvolvePro/output_result/rounds_data'
wt_fasta_path = 'C:/Users/wzcwi/EvolvePro/output_result/kelsic_WT.fasta'
number_of_variants = 12
output_dir = 'C:/Users/wzcwi/EvolvePro/output_result'
rename_WT = False

round_name = 'Round3'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)