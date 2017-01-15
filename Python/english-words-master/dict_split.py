#!/usr/lib/bin/python3

import os
import sys

dir = "/Users/yili/Documents/Richard USB info/Learning-Code/Python/english-words-master/"
f_name="word_dict_sorted.txt"

ori_f = open(os.path.join(dir, f_name), 'r')

txt = ori_f.read().split('\n')

ori_f.close()
filtered_txt = [x for x in txt if len(x) > 2]

a_txt = [x for x in filtered_txt if x[0] == 'a']
f_a = open(os.path.join (dir, 'dict_a.txt'), 'w+')
f_a.write('\n'.join(a_txt))
f_a.close()

b_txt = [x for x in filtered_txt if x[0] == 'b']
f_b = open(os.path.join (dir, 'dict_b.txt'), 'w+')
f_b.write('\n'.join(b_txt))
f_b.close()

c_txt = [x for x in filtered_txt if x[0] == 'c']
f_c = open(os.path.join (dir, 'dict_c.txt'), 'w+')
f_c.write('\n'.join(c_txt))
f_c.close()

d_txt = [x for x in filtered_txt if x[0] == 'd']
f_d = open(os.path.join (dir, 'dict_d.txt'), 'w+')
f_d.write('\n'.join(d_txt))
f_d.close()

e_txt = [x for x in filtered_txt if x[0] == 'e']
f_e = open(os.path.join (dir, 'dict_e.txt'), 'w+')
f_e.write('\n'.join(e_txt))
f_e.close()

f_txt = [x for x in filtered_txt if x[0] == 'f']
f_f = open(os.path.join (dir, 'dict_f.txt'), 'w+')
f_f.write('\n'.join(f_txt))
f_f.close()

g_txt = [x for x in filtered_txt if x[0] == 'g']
f_g = open(os.path.join (dir, 'dict_g.txt'), 'w+')
f_g.write('\n'.join(g_txt))
f_g.close()

h_txt = [x for x in filtered_txt if x[0] == 'h']
f_h = open(os.path.join (dir, 'dict_h.txt'), 'w+')
f_h.write('\n'.join(h_txt))
f_h.close()

i_txt = [x for x in filtered_txt if x[0] == 'i']
f_i = open(os.path.join (dir, 'dict_i.txt'), 'w+')
f_i.write('\n'.join(i_txt))
f_i.close()

j_txt = [x for x in filtered_txt if x[0] == 'j']
f_j = open(os.path.join (dir, 'dict_j.txt'), 'w+')
f_j.write('\n'.join(j_txt))
f_j.close()

k_txt = [x for x in filtered_txt if x[0] == 'k']
f_k = open(os.path.join (dir, 'dict_k.txt'), 'w+')
f_k.write('\n'.join(k_txt))
f_k.close()

l_txt = [x for x in filtered_txt if x[0] == 'l']
f_l = open(os.path.join (dir, 'dict_l.txt'), 'w+')
f_l.write('\n'.join(l_txt))
f_l.close()

m_txt = [x for x in filtered_txt if x[0] == 'm']
f_m = open(os.path.join (dir, 'dict_m.txt'), 'w+')
f_m.write('\n'.join(m_txt))
f_m.close()

n_txt = [x for x in filtered_txt if x[0] == 'n']
f_n = open(os.path.join (dir, 'dict_n.txt'), 'w+')
f_n.write('\n'.join(n_txt))
f_n.close()

o_txt = [x for x in filtered_txt if x[0] == 'o']
f_o = open(os.path.join (dir, 'dict_o.txt'), 'w+')
f_o.write('\n'.join(o_txt))
f_o.close()

p_txt = [x for x in filtered_txt if x[0] == 'p']
f_p = open(os.path.join (dir, 'dict_p.txt'), 'w+')
f_p.write('\n'.join(p_txt))
f_p.close()

q_txt = [x for x in filtered_txt if x[0] == 'q']
f_q = open(os.path.join (dir, 'dict_q.txt'), 'w+')
f_q.write('\n'.join(q_txt))
f_q.close()

r_txt = [x for x in filtered_txt if x[0] == 'r']
f_r = open(os.path.join (dir, 'dict_r.txt'), 'w+')
f_r.write('\n'.join(r_txt))
f_r.close()

s_txt = [x for x in filtered_txt if x[0] == 's']
f_s = open(os.path.join (dir, 'dict_s.txt'), 'w+')
f_s.write('\n'.join(s_txt))
f_s.close()

t_txt = [x for x in filtered_txt if x[0] == 't']
f_t = open(os.path.join (dir, 'dict_t.txt'), 'w+')
f_t.write('\n'.join(t_txt))
f_t.close()

u_txt = [x for x in filtered_txt if x[0] == 'u']
f_u = open(os.path.join (dir, 'dict_u.txt'), 'w+')
f_u.write('\n'.join(u_txt))
f_u.close()

v_txt = [x for x in filtered_txt if x[0] == 'v']
f_v = open(os.path.join (dir, 'dict_v.txt'), 'w+')
f_v.write('\n'.join(v_txt))
f_v.close()

w_txt = [x for x in filtered_txt if x[0] == 'w']
f_w = open(os.path.join (dir, 'dict_w.txt'), 'w+')
f_w.write('\n'.join(w_txt))
f_w.close()

x_txt = [x for x in filtered_txt if x[0] == 'x']
f_x = open(os.path.join (dir, 'dict_x.txt'), 'w+')
f_x.write('\n'.join(x_txt))
f_x.close()

y_txt = [x for x in filtered_txt if x[0] == 'y']
f_y = open(os.path.join (dir, 'dict_y.txt'), 'w+')
f_y.write('\n'.join(y_txt))
f_y.close()

z_txt = [x for x in filtered_txt if x[0] == 'z']
f_z = open(os.path.join (dir, 'dict_z.txt'), 'w+')
f_z.write('\n'.join(z_txt))
f_z.close()

