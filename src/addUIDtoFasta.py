#!/usr/bin/env python
# conver
def main():

  if len(sys.argv) != 1:
    parser = argparse.ArgumentParser(description="generate aligned fasta file's accessions with unique ID's")
    parser.add_argument("-i", "--input-accession", help="input accession list (generated with getAccession.py)", required=True)
    parser.add_argument("-f", "--input-fasta", help="input aligned fasta file", required=True)
    parser.add_argument("-o", "--output-fasta", help="output fasta with UIDs in the file", required=True)
    args = parser.parse_args()

    inAccFn = args.input_accession
    inAlnFn = args.input_fasta
    outAlnFn = args.output_fasta
  else:
    inAccFn  = raw_input('Enter input accession file:')
    inAlnFn  = raw_input('Enter input aligned fasta file:')
    outAlnFn = raw_input('Enter output fasta file:')

  inACC = open(inAccFn,'r')
  inALN = open(inAlnFn,'r')
  outALN = open(outAlnFn,'w')

  UID = []
  ACC = []
  for line in inACC:
    line = line.strip()
    line = line.partition('\t')
    hack = line[2].partition('|')
    UID.append(str(line[0]))
    ACC.append(str(hack[0]))
  inACC.close()

  for line in inALN:
    if line.startswith('>'):
      outALN.write('\n')
      temp = line.partition('pdb|')
      if len(temp[1]) == 0:
        temp = line.partition('sp|')
      temp = temp[2].partition('|')
      temp = temp[0].partition('.')
      try:
        key = ACC.index(temp[0])
        plug = UID[key]
        outALN.write('>'+str(plug)+'\n')
      except ValueError:
        key = 'MISSING_IN_DATABASE'
        outALN.write('>'+str(key)+'\n')
    else:
      outALN.write(line)
  inALN.close()
  outALN.close()

if __name__ == "__main__":
  sys.exit(main())