# from flask import Flask, render_template, request, jsonify
# import networkx as nx
# import json
# from pgmpy.models import BayesianNetwork
# from pgmpy.factors.discrete import TabularCPD
# app = Flask(__name__)
#
#
# # 创建贝叶斯网络结构
# def create_bayesian_network():
#     G = nx.DiGraph()
#
#     # Add edges
#     edges = [
#         ('education_level', 'interview_performance'),
#         ('work_experience', 'interview_performance'),
#         ('major_relevance', 'interest_match'),
#         ('working_hours', 'interest_match'),
#         ('interest_match', 'offer_accepted'),
#         ('salary', 'benefits'),
#         ('benefits', 'offer_accepted'),
#         ('age', 'company_offer'),
#         ('interview_performance', 'company_offer'),
#         ('company_offer', 'admission'),
#         ('offer_accepted', 'admission')
#     ]
#
#     G.add_edges_from(edges)
#
#     # Add node information and random colors
#     node_info = {
#         # Probabilities for PhD, M, B
#         # 'education_level': {'label': 'Education Level','probability': [0.3, 0.5, 0.2]},
#         'education_level': {'label': 'Education Level','probability': 0.6},
#         'work_experience': {'label': 'Work Experience', 'probability': 0.8},
#         'interview_performance': {'label': 'Interview Performance', 'probability': 0.75},
#         'major_relevance': {'label': 'Major Relevance', 'probability': 0.5},
#         'working_hours': {'label': 'Working Hours', 'probability': 0.7},
#         'interest_match': {'label': 'Interest Match', 'probability': 0.85},
#         'offer_accepted': {'label': 'Offer Accepted', 'probability': 0.65},
#         'salary': {'label': 'Salary', 'probability': 0.5},
#         'benefits': {'label': 'Benefits', 'probability': 0.75},
#         'age': {'label': 'Age', 'probability': 0.6},
#         'company_offer': {'label': 'Company Offer', 'probability': 0.7},
#         'admission': {'label': 'Admission', 'probability': 0.8}
#     }
#
#     # 定义12种鲜艳的颜色
#     vibrant_colors = [
#         "rgb(255, 0, 0)",  # 红色
#         "rgb(0, 255, 0)",  # 绿色
#         "rgb(0, 0, 255)",  # 蓝色
#         "rgb(150, 180, 100)",  # 黄色
#         "rgb(0, 255, 255)",  # 青色
#         "rgb(255, 0, 255)",  # 品红色
#         "rgb(255, 165, 0)",  # 橙色
#         "rgb(75, 0, 130)",  # 靛蓝色
#         "rgb(255, 20, 147)",  # 深粉色
#         "rgb(128, 0, 0)",  # 深红色
#         "rgb(0, 128, 128)",  # 深青色
#         "rgb(255, 105, 180)"  # 热粉色
#     ]
#
#     # 确保每个节点都能获取一个颜色
#     colors = {node: vibrant_colors[i % len(vibrant_colors)] for i, node in enumerate(G.nodes())}
#
#     # 嵌套字典
#     for node in G.nodes():
#         G.nodes[node]['info'] = node_info.get(node, {})
#         G.nodes[node]['color'] = colors[node]
#
#     # 转换为适合D3.js的数据格式
#     nodes = [{"id": node, "info": G.nodes[node]['info'], "color": G.nodes[node]['color']} for node in G.nodes()]
#     links = [{"source": n1, "target": n2} for n1, n2 in G.edges()]
#
#     return {"nodes": nodes, "links": links}
#
#
# # Global variable to store data (for now)
# data = create_bayesian_network()
# json_data = data
# print(json_data)
#
# # # Step 1: 创建贝叶斯网络
# # admission_model = BayesianNetwork()
# #
# # # Step 2: 添加边
# # for link in json_data['links']:
# #     admission_model.add_edge(link['source'], link['target'])
# #
# # # Step 3: 添加条件概率分布（CPDs）
# # for node in json_data['nodes']:
# #     id = node['id']
# #     probability = node['info']['probability']
# #
# #     # 确定父节点
# #     parents = admission_model.get_parents(id)
# #
# #     variable_card = 2
# #     cpd_values = [[1 - probability], [probability]]
# #
# #     # if id == 'education_level':
# #     #     # 教育水平为多值变量
# #     #     # variable_card = 3  # 对应 PhD, M, B 三个值
# #     #
# #     #     variable_card = 2  # 对应 PhD, M, B 三个值
# #     #     cpd_values = [[1 - probability], [probability]]  # (2, 1)
# #     #
# #     #     # 将概率分布从一维数组变为二维数组，符合 CPD 的输入要求
# #     #     # cpd_values = [[p] for p in probability]  # (3, 1)
# #     # elif not parents:
# #     #     # 对于没有父节点的二元变量
# #     #     variable_card = 2
# #     #     cpd_values = [[1 - probability], [probability]]  # (2, 1)
# #     # else:
# #     #     # 对于有父节点的二元变量
# #     #     num_parent_values = 2 ** len(parents)  # 父节点状态组合数
# #     #     variable_card = 2
# #     #     cpd_values = [[1 - probability] * num_parent_values, [probability] * num_parent_values]  # (2, num_parent_values)
# #
# #     # 检查 cpd_values 形状是否正确
# #     try:
# #         cpd = TabularCPD(variable=id, variable_card=variable_card, values=cpd_values)
# #         admission_model.add_cpds(cpd)
# #     except ValueError as e:
# #         print(f"Error adding CPD for variable {id}: {e}")
# #         print(f"Expected shape: ({variable_card}, {len(cpd_values[0])}), Got shape: {len(cpd_values)}, {len(cpd_values[0])}")
# #         continue
# #
# # # 检查模型有效性
# # if admission_model.check_model():
# #     print("Model is valid.")
# # else:
# #     print("Model is invalid.")
# #
# # # 输出贝叶斯网络的结构
# # print("Edges in the Bayesian Network:", admission_model.edges())
#
#
#
# @app.route('/get_network_data')
# def get_network_data():
#     return jsonify(data)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# # 处理提交的节点概率数据
# @app.route('/update_probabilities', methods=['POST'])
# def update_probabilities():
#     global data
#     updated_probabilities = request.json  # 获取前端提交的JSON数据
#     for node in data['nodes']:
#         if node['id'] in updated_probabilities:
#             node['info']['probability'] = updated_probabilities[node['id']]
#     return jsonify(data)  # 返回更新后的网络数据
#
#
# # 获取贝叶斯网络数据的路由
# @app.route('/get_network_query', methods=['GET'])
# def get_network_query():
#     """
#     调取贝叶斯网络数据并返回给前端。
#     """
#     try:
#         # 假设 data 是你的贝叶斯网络数据存储变量
#         global data
#
#         # 检查数据是否存在
#         if not data:
#             return jsonify({"error": "贝叶斯网络数据不存在"}), 404
#
#         # 返回贝叶斯网络数据
#         return jsonify(data)
#
#     except Exception as e:
#         # 处理可能出现的异常
#         return jsonify({"error": f"发生错误: {str(e)}"}), 500
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# 导入必要的库
import dash  # 用于创建交互式的 Web 应用
from dash import dcc, html, Input, Output  # Dash 核心组件和回调功能
import dash_bootstrap_components as dbc  # 使用 Bootstrap 样式让界面更美观
import networkx as nx  # 用于创建贝叶斯网络的图结构
import plotly.graph_objects as go  # 用于绘制图形
from pgmpy.inference import VariableElimination  # 用于贝叶斯网络推断
from pgmpy.models import BayesianNetwork  # 贝叶斯网络的核心类
from pgmpy.factors.discrete import TabularCPD  # 用于定义条件概率表 (CPD)

# 1. 构建贝叶斯网络模型
# 创建贝叶斯网络的结构，定义节点和边
admission_model = BayesianNetwork([
    ('major', 'interest'), ('working_hours', 'interest'), ('salary', 'welfare'),
    ('interest', 'employee_offer'), ('welfare', 'employee_offer'),

    ('education_level', 'interview_performance'),
    ('work_experience', 'interview_performance'),
    ('age', 'company_offer'),
    ('interview_performance', 'company_offer'),

    ('company_offer', 'admission'), ('employee_offer', 'admission')
])

# 右边构建节点

# 变量名，变量取值个数，对应概率
# marjor 两个   文科（0）0.5 理科（1）0.5
cpd_major = TabularCPD(variable='major', variable_card=2, values=[[0.8], [0.2]])

# working_hours 三个  (0)0-5小时 0.2  (1)5-8小时 0.5    (2)每天超过8小时（1）0.3
cpd_working_hours = TabularCPD(variable='working_hours', variable_card=3, values=[[0.57], [0.29], [0.14]])

# salary  三个  (0)1k-5k  0.2  (1)5k-1w 0.6  (2)1w+ 0.2
cpd_salary = TabularCPD(variable='salary', variable_card=3, values=[[0.27], [0.36], [0.37]])

# interest, 两个， （0不感兴趣），(1感兴趣）
cpd_interest = TabularCPD(variable='interest', variable_card=2,
                          values=[[0.9, 0.8, 0.5, 0.7, 0.5, 0.1], [0.1, 0.2, 0.5, 0.3, 0.5, 0.9]],
                          evidence=['major', 'working_hours'],
                          evidence_card=[2, 3])

# welfare, 两个， （0好），（1不好）
cpd_welfare = TabularCPD(variable='welfare', variable_card=2,
                         values=[[0.4, 0.6, 0.8], [0.6, 0.4, 0.2]],
                         evidence=['salary'],
                         evidence_card=[3])

# 录取者同意, 两个， （0yes），（1no）
cpd_employee_offer = TabularCPD(variable='employee_offer', variable_card=2,
                                values=[[0.9, 0.7, 0.6, 0.2], [0.1, 0.3, 0.4, 0.8]],
                                evidence=['interest', 'welfare'],
                                evidence_card=[2, 2])

# 左边的
# education (0)研究生0.1 (1)本科0.4 (2)没有本科0.5
cpd_education_level = TabularCPD(variable='education_level', variable_card=3, values=[[0.1], [0.4], [0.5]])
# (0)没有工作经验 0.5 (1)有工作经验0.5
cpd_work_experience = TabularCPD(variable='work_experience', variable_card=2, values=[[0.67], [0.33]])
# (0)小于30岁 0.7   (1)大于30岁0.3
cpd_age = TabularCPD(variable='age', variable_card=2, values=[[0.6], [0.4]])

cpd_interview_performance = TabularCPD(variable='interview_performance', variable_card=3,
                                       values=[[0.7, 0.6, 0.5, 0.6, 0.5, 0.4], [0.2, 0.3, 0.3, 0.3, 0.3, 0.4],
                                               [0.1, 0.1, 0.2, 0.1, 0.2, 0.2]],
                                       evidence=['education_level', 'work_experience'],
                                       evidence_card=[3, 2])
cpd_company_offer = TabularCPD(variable='company_offer', variable_card=2,
                               values=[[0.9, 0.8, 0.3, 0.8, 0.7, 0.2], [0.1, 0.2, 0.7, 0.2, 0.3, 0.8]],
                               evidence=['age', 'interview_performance'],
                               evidence_card=[2, 3])

# 0 不录取 1 录取
cpd_admission = TabularCPD(variable='admission', variable_card=2,
                           values=[[0.99, 0.3, 0.01, 0.0], [0.01, 0.7, 0.99, 1.0]],
                           evidence=['company_offer', 'employee_offer'],
                           evidence_card=[2, 2])

# 添加概率表到贝叶斯网络
admission_model.add_cpds(cpd_education_level, cpd_work_experience, cpd_age, cpd_interview_performance,
                         cpd_company_offer,
                         cpd_admission, cpd_major, cpd_working_hours, cpd_salary, cpd_interest, cpd_welfare,
                         cpd_employee_offer)

# 验证模型是否有效
# 必须确保所有的 CPDs 已经正确添加，否则模型无效
admission_model.check_model()

# 创建推断对象，用于执行贝叶斯网络推断
inference = VariableElimination(admission_model)


# 2. 创建 NetworkX 图
def create_networkx_graph(model):
    """
    将贝叶斯网络模型转换为 NetworkX 图对象，用于可视化。
    """
    G = nx.DiGraph()  # 创建一个有向图
    G.add_edges_from(model.edges())  # 添加模型中的边

    return G


# 3. 将 NetworkX 图转换为 Plotly 图形
def create_plotly_figure(G):
    """
    将 NetworkX 图转换为 Plotly 图形对象，用于在 Dash 中显示。
    """
    pos = nx.spring_layout(G, seed=42)  # 计算图中节点的布局位置
    edge_x = []
    edge_y = []

    # 绘制图中的边
    for edge in G.edges():
        x0, y0 = pos[edge[0]]  # 起始节点的位置
        x1, y1 = pos[edge[1]]  # 终止节点的位置
        edge_x.extend([x0, x1, None])  # 添加边的坐标
        edge_y.extend([y0, y1, None])  # 添加边的坐标

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),  # 边的样式
        hoverinfo='none',  # 不显示悬停信息
        mode='lines'  # 边的显示模式为线条
    )

    node_x = []
    node_y = []
    node_text = []
    node_colors = []  # 保存节点的颜色

    # 给每个节点分配不同的颜色
    color_map = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22',
                 '#17becf']

    # 绘制图中的节点
    for i, node in enumerate(G.nodes()):
        x, y = pos[node]  # 获取节点位置
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)  # 节点文本为节点名称
        node_colors.append(color_map[i % len(color_map)])  # 使用循环分配颜色

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',  # 节点显示为标记点和文本
        text=node_text,  # 显示节点名称
        textposition="top center",  # 文本位置在节点上方
        hoverinfo='text',  # 悬停显示节点名称
        marker=dict(
            color=node_colors,  # 节点的颜色
            size=20,  # 节点大小
            line_width=2  # 节点边框宽度
        )
    )

    # 创建 Plotly 图形
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,  # 不显示图例
                        hovermode='closest',  # 启用悬停功能
                        margin=dict(b=0, l=0, r=0, t=0),  # 设置边距
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),  # 隐藏网格线、零线和坐标轴标签
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)  # 隐藏网格线、零线和坐标轴标签
                    ))
    return fig


# 4. 初始化 Dash 应用
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])  # 使用 Bootstrap 样式


G = create_networkx_graph(admission_model)  # 创建 NetworkX 图
fig = create_plotly_figure(G)  # 创建 Plotly 图形

# 5. 定义 Dash 页面布局
app.layout = dbc.Container([
    html.H3("Intern Admission Network", className="text-center"),
    html.Img(
        src='/assets/en_plot.jpg',
        alt='en_plot',
        style={'width': '100%', 'height': 'auto'}  # 自动调整宽度，保持比例
    ),
    dbc.Row([
        # 左侧：贝叶斯网络图形
        dbc.Col([
            html.H3("Bayesian Network", className="text-center"),
            dcc.Graph(id='bayesian-network', figure=fig)  # 图形显示组件
        ], width=8),  # 宽度占比为 8
        # 右侧：条件推断表单
        dbc.Col([
            html.H3("Query", className="text-center"),
            html.Div([
                html.Label("condition:"),
                dcc.Dropdown(  # 条件选择下拉框
                    id='evidence-dropdown',
                    options=[
                        {'label': 'major = related', 'value': 'major=0'},
                        {'label': 'major = not related', 'value': 'major=1'},

                        {'label': 'working_hours = 0-5h', 'value': 'working_hours=0'},
                        {'label': 'working_hours = 5-8h', 'value': 'working_hours=1'},
                        {'label': 'working_hours = over 8h', 'value': 'working_hours=2'},

                        # 添加教育水平的选项
                        {'label': 'education_level = B', 'value': 'education_level=2'},
                        {'label': 'education_level = M', 'value': 'education_level=1'},
                        {'label': 'education_level = PhD', 'value': 'education_level=0'},

                        # 添加工作经验的选项
                        {'label': 'work_experience = less than 2 years', 'value': 'work_experience=1'},
                        {'label': 'work_experience = 2 years and more', 'value': 'work_experience=0'},

                        # 添加年龄的选项
                        {'label': 'age = less than 30 years old', 'value': 'age=0'},
                        {'label': 'age = 30 years old and more', 'value': 'age=1'},

                        # 添加面试表现的选项
                        {'label': 'interview_performance = Bad', 'value': 'interview_performance=0'},
                        {'label': 'interview_performance = Good', 'value': 'interview_performance=1'},
                        {'label': 'interview_performance = Excellent', 'value': 'interview_performance=2'},

                        # 添加薪资的选项
                        {'label': 'salary = 55-57k', 'value': 'salary=0'},
                        {'label': 'salary = 58-61k', 'value': 'salary=1'},
                        {'label': 'salary = 62-65k', 'value': 'salary=2'},

                        # 添加兴趣的选项
                        {'label': 'interest = Yes', 'value': 'interest=1'},
                        {'label': 'interest = No', 'value': 'interest=0'},

                        # 添加福利的选项
                        {'label': 'welfare = Good', 'value': 'welfare=0'},
                        {'label': 'welfare = General', 'value': 'welfare=1'},

                        # 添加Offer接受的选项
                        {'label': 'company_offer = Yes', 'value': 'company_offer=1'},
                        {'label': 'company_offer = No', 'value': 'company_offer=0'},

                        # 添加Offer接受的选项
                        {'label': 'employee_offer = Yes', 'value': 'employee_offer=0'},
                        {'label': 'employee_offer = No', 'value': 'employee_offer=1'}
                    ],
                    multi=True  # 允许多选
                ),
                html.Br(),
                html.Label("query:"),
                dcc.Dropdown(  # 查询变量下拉框
                    id='query-dropdown',
                    options=[{'label': var, 'value': var} for var in admission_model.nodes()],
                    value='admission'  # 默认查询变量为 'admission'
                ),
                html.Br(),
                html.Button("inference", id='run-inference', className="btn btn-primary"),  # 按钮
                html.Br(), html.Br(),
                html.Div(id='inference-output', style={'whiteSpace': 'pre-line'})  # 推断结果显示区域
            ])
        ], width=4)  # 宽度占比为 4
    ])
])


# 6. 定义回调函数
@app.callback(
    Output('inference-output', 'children'),  # 更新推断结果
    Input('run-inference', 'n_clicks'),  # 监听按钮点击
    [Input('evidence-dropdown', 'value'),  # 监听条件选择
     Input('query-dropdown', 'value')]  # 监听查询变量选择
)
def update_inference(n_clicks, evidence, query):
    """
    根据用户输入的条件和查询变量执行推断，并返回结果。
    """
    if n_clicks is None:  # 如果按钮未被点击
        return "waiting inference..."
    if evidence is None:  # 如果没有输入条件
        evidence = {}
    else:
        # 将条件从字符串解析为字典
        evidence = {e.split('=')[0]: int(e.split('=')[1]) for e in evidence}

    # 执行推断
    result = inference.query(variables=[query], evidence=evidence)
    return str(result)  # 返回推断结果


# 7. 运行 Dash 应用
if __name__ == '__main__':
    app.run_server(debug=True)  # 启动服务器，调试模式开启
