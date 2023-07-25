import gzip


def read_gene_info(file_path):
    gene_mapping = {}
    with gzip.open(file_path, 'rt') as f:
        for line in f:
            if line.startswith('#'):
                continue
            gene_id, symbol, synonyms = line.strip().split('\t')[1:4]
            symbol = symbol.lower()
            gene_mapping[symbol] = gene_id
            for synonym in synonyms.split('|'):
                synonym = synonym.lower()
                gene_mapping[synonym] = gene_id
    return gene_mapping



def replace_symbols_with_entrez(gmt_file_path, gene_mapping):
    output_lines = []
    with open(gmt_file_path, 'r') as f:
        for line in f:
            fields = line.strip().split('\t')
            pathway_name, pathway_desc, *gene_names = fields
            entrez_ids = [gene_mapping.get(name.lower(), name) for name in gene_names]
            output_line = '\t'.join([pathway_name, pathway_desc] + entrez_ids)
            output_lines.append(output_line)
    return output_lines



def write_output_gmt(output_gmt_file_path, output_lines):
    with open(output_gmt_file_path, 'w') as f:
        f.write('\n'.join(output_lines))


#



if __name__ == "__main__":
    # **Replace these file paths with the actual paths of the gene_info, GMT files and also repale the  output_gmt_file_path.**
    gene_info_file_path = "C:/Users/pshri/Desktop/Shubham/Basu/Task/Homo_sapiens.gene_info.gz"
    gmt_file_path = "C:/Users/pshri/Desktop/Shubham/Basu/Task/h.all.v2023.1.Hs.symbols.gmt"
    output_gmt_file_path = "C:/Users/pshri/Desktop/Shubham/Basu/Task/h.all.v2023.1.Hs.entrez.gmt"

    gene_mapping = read_gene_info(gene_info_file_path)
    output_lines = replace_symbols_with_entrez(gmt_file_path, gene_mapping)
    write_output_gmt(output_gmt_file_path, output_lines)

print("An output file is created with name 'h.all.v2023.1.Hs.entrez.gmt' at given path ")