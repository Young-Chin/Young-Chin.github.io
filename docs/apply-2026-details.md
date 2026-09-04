# Apply 2026 项目详情

此文件是 `apply/2026/details.js` 的唯一维护源。修改详情后运行：

```bash
python3 scripts/md2html.py docs/apply-2026-details.md apply/2026/details.js
```

## face
# 如何在多重控制下做到 ID 一致且保真
### 背景
- 生图的控制叠加使得人脸 ID 信息被削弱（LoRA / IPA / ControlNet）。
- 主流 ID-preserving 算法 InstantID / PuLID / LoRA 存在不足：侧脸和相似度难以两全。
### 技术演进路线
**FaceSwap** -> **Face-Inpainting** -> **End2End**
- **FaceSwap**：原图 + 人脸检测识别 + merge 新人脸图。优点：一致与保真，与多重控制解耦。缺点：融合边缘瑕疵，策略逻辑重，难以自适应。
- **Face-Inpainting**：原图 + ReID + 人脸 mask + 生成模型 inpainting。优点：更精准优雅的人脸定位，inpainting 显著减少融合瑕疵，一致与保真不变。缺点：复杂场景下 mask 成为瓶颈。
- **End2End**：UNO-Face 人脸场景融合，加入人脸 loss。优点：解决融合瑕疵，人脸更自然。缺点：增加一次模型推理。
### 成果
人物高一致性与高保真成为产品特色，人脸方案整合复用在其他产品。
![人脸一致性技术方案](images/face-consistency.png)

## region
# 如何做到精准的图像区域控制
### 背景
文生图中提示词描述到图像空间存在映射关系，但无法精准控制。
### 技术方案
构建区域拆分提示词，再对 attention map 进行对应的区域切分（或 mask），分别进行 attention 计算并叠加 IPAdapter 特征，再拼接回去进行生成。
### 成果
实现区域控制的提示词到图像映射，满足产品可控性和分镜特性。
![区域控制方案 1](images/region-control-1.png)
![区域控制方案 2](images/region-control-2.png)

## free-control
# 如何做到 Free Control
### 背景
基于控制信号的生成容易形成人物姿态瑕疵，没有控制信号无法实现分镜控制。
### 技术方案
基于区域控制实现底图生成，构建分镜 mask 与背景，再基于区域进行 inpainting，最后融入控制信号引导。
### 成果
满足分镜动作控制，同时避免人物动作瑕疵。
![Free Control 方案](images/free-control.png)
