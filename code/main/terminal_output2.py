
step  1  : loss =  4.20971
Dumped alphas
step  1  : bleu =  BLEU = 10.79, 50.2/21.6/8.9/2.3 (BP=0.887, ratio=0.893, hyp_len=35502, ref_len=39747)

Model saved in file:  ./tmp/seq2seq1.ckpt
 getLoss ...... ============================================================
step  2  : loss =  4.0017347
Dumped alphas
step  2  : bleu =  BLEU = 18.64, 60.1/30.0/15.1/6.9 (BP=0.893, ratio=0.899, hyp_len=35724, ref_len=39747)

step  3  : loss =  3.891541
Dumped alphas
step  3  : bleu =  BLEU = 21.89, 69.1/36.1/20.1/10.6 (BP=0.810, ratio=0.826, hyp_len=32816, ref_len=39747)

Model saved in file:  ./tmp/seq2seq3.ckpt
 getLoss ...... ============================================================
step  4  : loss =  3.7878766
Dumped alphas
step  4  : bleu =  BLEU = 27.41, 71.8/40.6/25.4/15.5 (BP=0.838, ratio=0.850, hyp_len=33771, ref_len=39747)

step  5  : loss =  3.7157223
Dumped alphas
step  5  : bleu =  BLEU = 31.08, 72.3/42.5/28.1/18.7 (BP=0.871, ratio=0.879, hyp_len=34938, ref_len=39747)

Model saved in file:  ./tmp/seq2seq5.ckpt
 getLoss ...... ============================================================
step  6  : loss =  3.6719112
Dumped alphas
step  6  : bleu =  BLEU = 33.18, 73.5/44.1/30.4/21.1 (BP=0.874, ratio=0.881, hyp_len=35032, ref_len=39747)

step  7  : loss =  3.6443899
Dumped alphas
step  7  : bleu =  BLEU = 33.89, 74.5/45.2/31.7/22.6 (BP=0.860, ratio=0.869, hyp_len=34549, ref_len=39747)

Model saved in file:  ./tmp/seq2seq7.ckpt
 getLoss ...... ============================================================
step  8  : loss =  3.6241686
Dumped alphas
step  8  : bleu =  BLEU = 33.89, 74.5/45.3/32.2/23.3 (BP=0.849, ratio=0.860, hyp_len=34170, ref_len=39747)

step  9  : loss =  3.6080937
Dumped alphas
step  9  : bleu =  BLEU = 34.31, 74.5/45.6/32.5/23.8 (BP=0.852, ratio=0.862, hyp_len=34270, ref_len=39747)

Model saved in file:  ./tmp/seq2seq9.ckpt
 getLoss ...... ============================================================
step  10  : loss =  3.5998087
Dumped alphas
step  10  : bleu =  BLEU = 35.00, 74.1/46.0/32.9/24.3 (BP=0.861, ratio=0.870, hyp_len=34567, ref_len=39747)

Model saved in file:  ./tmp/seq2seq10.ckpt
/////////////////
(mollsenv) mollys-mbp-3:main mollyhkim$ python mt_main.py inference tmp/seq2seq10.ckpt greedy
->
(mollsenv) mollys-mbp-3:main mollyhkim$ TEST:  BLEU = 34.87, 74.3/46.2/33.1/24.2 (BP=0.856, ratio=0.866, hyp_len=43061, ref_len=49735)

