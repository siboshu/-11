"""我的主页"""
import streamlit as st#导入streamlit库，并且用as取别名为st
from PIL import Image
# radio单击,参数1是侧边栏标题，参数2是具体表示哪几页，每点击到我的兴趣推荐页，则把对应的数据传递给左边的page变量
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智能词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    # 学生使用write()、image()、audio()等自行发挥
    a=Image.open('labubu.jpg')
    a=a.resize((400,300))
    st.image(a)
    st.write('打瓦')
    st.text('打瓦')
def page_2():
    '''我的图片处理工具'''
    st.write(":100:图片处理小程序:100:")
    st.write(':100:打瓦:100:')
    st.text('打瓦')
    uploader_file=st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploader_file:
        # 获取图片的文件名称，类型，大小
        file_name=uploader_file.name
        file_type=uploader_file.type
        file_size=uploader_file.size
        img=Image.open(uploader_file)
        st.image(img)#展示原图，
        st.image(img_change(img,1,2,0))#展示处理后的结果
def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表当中。split分割后的数据一定是存在列表的
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    # 将列表中的内容  再    进行分割，分成 “编号，  单词 ，   解释”
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')#是将列表里面的单个元素依次取出来之后，利用#分割，分割成功后，重新赋值给words_list[i]
    # 将列表中的内容导入字典，方便查询，格式为 单词： 编号、解释
    words_dict={}#创建空字典
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
def page_4():
    '''我的留言区'''
    st.write('兄弟的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        message_list=f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i]=message_list[i].split('#')
    # 利用for循环遍历列表里面的每一个元素，索引值为0是编号，1对应人名，2对应留言
    for i in message_list:
        if i[1]=='阿短':
            with st.chat_message('🐕'):
                st.write(i[1],':',i[2])
        elif i[1]=='编程猫':
            with st.chat_message('🐱'):
                st.write(i[1],':',i[2]) 
        elif i[1]=='吕布':
            with st.chat_message('👍'):
                st.write(i[1],':',i[2]) 
        elif i[1]=='邹思正':
            with st.chat_message('🐂'):
                st.write(i[1],':',i[2]) 
    name= st.selectbox('我是...',['阿短','编程猫','吕布','邹思正'])
    new_message=st.text_input('想要说的话...')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message=''
            for i in message_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]#去掉最后的换行符
            f.write(message)

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
            
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()