import matplotlib.pyplot as plt
import pandas as pd

district = '130631'#'141034'#'130522'#

# 读取第一个txt文件，包含线段定义
lines_df = pd.read_csv('../'+district+'/xyx_0/algorithm/'+district+'_pred_edges.txt', header=None, names=['line_id', 'start_id', 'end_id', 'type'])

# 读取第二个txt文件，包含坐标定义
coords_df = pd.read_csv('../'+district+'/xyx_0/algorithm/'+district+'_pred_vertices.txt', header=None, names=['point_id', 'longitude', 'latitude'])

# # 读取第一个txt文件，包含线段定义
# lines_df = pd.read_csv('../../../GraphSamplingToolkit-main_improve_GE_zl17/'+district+'/xyx_0/algorithm/'+district+'_pred_edges.txt', header=None, names=['line_id', 'start_id', 'end_id', 'type'])

# # 读取第二个txt文件，包含坐标定义
# coords_df = pd.read_csv('../../../GraphSamplingToolkit-main_improve_GE_zl17/'+district+'/xyx_0/algorithm/'+district+'_pred_vertices.txt', header=None, names=['point_id', 'longitude', 'latitude'])

# 创建一个字典，将每个点的ID映射到其坐标
coords_dict = coords_df.set_index('point_id')[['longitude', 'latitude']].to_dict('index')

# 开始绘图
# plt.figure(figsize=(10, 10))
for _, row in lines_df.iterrows():
    # 获取起点和终点的坐标
    start_coords = coords_dict.get(row['start_id'])
    end_coords = coords_dict.get(row['end_id'])

    # 确保起点和终点的坐标存在，然后绘制线段
    if start_coords and end_coords:
        x_values = [start_coords['longitude'], end_coords['longitude']]
        y_values = [start_coords['latitude'], end_coords['latitude']]
        
        plt.plot(x_values, y_values,  color='blue', linewidth=1) #marker='o',
        # print(x_values, y_values)


# # 读取第一个txt文件，包含线段定义
# lines_df = pd.read_csv('../'+district+'/xyx_0/groundtruth/'+district+'_groundtruth_txt_edges_osm.txt', header=None, names=['line_id', 'start_id', 'end_id', 'type'])

# # 读取第二个txt文件，包含坐标定义
# coords_df = pd.read_csv('../'+district+'/xyx_0/groundtruth/'+district+'_groundtruth_txt_vertices_osm.txt', header=None, names=['point_id', 'longitude', 'latitude'])

# # 创建一个字典，将每个点的ID映射到其坐标
# coords_dict = coords_df.set_index('point_id')[['longitude', 'latitude']].to_dict('index')

# # 开始绘图
# # plt.figure(figsize=(10, 10))
# for _, row in lines_df.iterrows():
#     # 获取起点和终点的坐标
#     start_coords = coords_dict.get(row['start_id'])
#     end_coords = coords_dict.get(row['end_id'])

#     # 确保起点和终点的坐标存在，然后绘制线段
#     if start_coords and end_coords:
#         x_values = [start_coords['longitude'], end_coords['longitude']]
#         y_values = [start_coords['latitude'], end_coords['latitude']]
        
#         plt.plot(x_values, y_values,  color='red', linewidth=1) #marker='o',
#         # print(x_values, y_values)


# 设置图例和标题
plt.title("Lines Plot Based on Coordinates")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# 显示图像
plt.grid(True)
plt.tight_layout
plt.show()
