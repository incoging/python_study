# coding = utf-8
# ���ж�ȡtxt�ļ����ݵķ���

# ����һ
f = open("foo.txt")             # ����һ���ļ�����
line = f.readline()              # �����ļ��� readline()����
while line:
    print(line,)                 # ����� ',' �����Ի��з�
    # print(line, end = '')������# �� Python 3��ʹ��
    line = f.readline()

f.close()

# ������
for line in open("foo.txt"):
    print(line,)                 # ����� ',' �����Ի��з�
    # print(line, end = '')������# �� Python 3��ʹ��


# ������
f = open("c:\\1.txt", "r")
lines = f.readlines()            # ��ȡȫ������
for line in lines:
    print(line)
f.close()

# ��귵��
# ����read�����������ģ���ô����λ�þͻ���������
# ʹ��f.tell()�������Է��ع�����ڵ�λ�á�tell()�����ǰ����ַ��������

# ������
'''
f.seek(0) ��������λ�ö�λ���ļ��Ŀ�ͷ��Ҳ����������������10��20��
'''

#python����numpy���ݣ�
# np.savetxt("result.txt", numpy_data)

#����list���ݣ�
# file=open('data.txt','w')
# file.write(str(list_data))
# file.close()

# file.writelines(lists) �ǲ����е�д�룬�������·�����д��ʱ���С�
# ����һ��
# for line in lists:
#     file.write(line+'\n')
#
# # ��������
# lists=[line+"\n" for line in lists]
# file.writelines(lists)
#
# # ��������
# file.write('\n'.join(lists))