{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"name":"python","version":"3.7.12","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"# This Python 3 environment comes with many helpful analytics libraries installed\n# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n# For example, here's several helpful packages to load\n\nimport numpy as np # linear algebra\nimport pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n\n# Input data files are available in the read-only \"../input/\" directory\n# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n\nimport os\nfor dirname, _, filenames in os.walk('/kaggle/input'):\n    for filename in filenames:\n        print(os.path.join(dirname, filename))\n\n# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session","metadata":{"_uuid":"8f2839f25d086af736a60e9eeb907d3b93b6e0e5","_cell_guid":"b1076dfc-b9ad-4769-8c92-a6c4dae69d19","execution":{"iopub.status.busy":"2023-04-01T07:47:10.079530Z","iopub.execute_input":"2023-04-01T07:47:10.080050Z","iopub.status.idle":"2023-04-01T07:47:10.098344Z","shell.execute_reply.started":"2023-04-01T07:47:10.080004Z","shell.execute_reply":"2023-04-01T07:47:10.097135Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"d = pd.read_csv(\"/kaggle/input/iowa-house-prices/train.csv\")\nd_frame=pd.DataFrame(d)\n","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.100523Z","iopub.execute_input":"2023-04-01T07:47:10.101702Z","iopub.status.idle":"2023-04-01T07:47:10.130229Z","shell.execute_reply.started":"2023-04-01T07:47:10.101654Z","shell.execute_reply":"2023-04-01T07:47:10.128943Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"d_frame.columns  \n#d_frame.head","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.132573Z","iopub.execute_input":"2023-04-01T07:47:10.133086Z","iopub.status.idle":"2023-04-01T07:47:10.142377Z","shell.execute_reply.started":"2023-04-01T07:47:10.133034Z","shell.execute_reply":"2023-04-01T07:47:10.140973Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"from sklearn.tree import DecisionTreeRegressor as reg\nimport joblib\nli=['LotArea','OverallCond','YrSold']\nx=d_frame[li]\nprint(x)\nY=d_frame.SalePrice","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.144039Z","iopub.execute_input":"2023-04-01T07:47:10.144515Z","iopub.status.idle":"2023-04-01T07:47:10.159137Z","shell.execute_reply.started":"2023-04-01T07:47:10.144446Z","shell.execute_reply":"2023-04-01T07:47:10.157650Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"p_model=reg()\np_model.fit(x,Y)\nrdi=p_model.predict(x)\nrdi_d=pd.DataFrame(rdi)\nrdi_d.to_csv('mypred_train.csv')\nprint(rdi_d)\n\n","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.161793Z","iopub.execute_input":"2023-04-01T07:47:10.162514Z","iopub.status.idle":"2023-04-01T07:47:10.182219Z","shell.execute_reply.started":"2023-04-01T07:47:10.162412Z","shell.execute_reply":"2023-04-01T07:47:10.181428Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"import matplotlib.pyplot as plt \n\nplt.scatter(rdi,Y)","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.183395Z","iopub.execute_input":"2023-04-01T07:47:10.184197Z","iopub.status.idle":"2023-04-01T07:47:10.445145Z","shell.execute_reply.started":"2023-04-01T07:47:10.184163Z","shell.execute_reply":"2023-04-01T07:47:10.443904Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"d_test = pd.read_csv(\"/kaggle/input/iowa-house-prices/test.csv\")\nd_frame_test=pd.DataFrame(d_test)\n#d.head\n#d.describe\nd_test.columns\n#d_frame.SalePrice false\n","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.446395Z","iopub.execute_input":"2023-04-01T07:47:10.446719Z","iopub.status.idle":"2023-04-01T07:47:10.475634Z","shell.execute_reply.started":"2023-04-01T07:47:10.446689Z","shell.execute_reply":"2023-04-01T07:47:10.474774Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"li_test=['LotArea','OverallCond','YrSold']\nx_test=d_frame_test[li_test]\n\n","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.476678Z","iopub.execute_input":"2023-04-01T07:47:10.477533Z","iopub.status.idle":"2023-04-01T07:47:10.483557Z","shell.execute_reply.started":"2023-04-01T07:47:10.477500Z","shell.execute_reply":"2023-04-01T07:47:10.482315Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"t_res=p_model.predict(x_test)\nprint(t_res)\nt_frame=pd.DataFrame(t_res)\nt_frame.to_csv('test_pred.csv')\n","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.485103Z","iopub.execute_input":"2023-04-01T07:47:10.485473Z","iopub.status.idle":"2023-04-01T07:47:10.504565Z","shell.execute_reply.started":"2023-04-01T07:47:10.485406Z","shell.execute_reply":"2023-04-01T07:47:10.503253Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"def inputter(lot,overalc,yrsol) :\n    i=np.array([[lot,overalc,yrsol]])\n    fin=p_model.predict(i)\n    print(\"your house price $ \",fin)\n    ","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.506138Z","iopub.execute_input":"2023-04-01T07:47:10.506490Z","iopub.status.idle":"2023-04-01T07:47:10.512840Z","shell.execute_reply.started":"2023-04-01T07:47:10.506422Z","shell.execute_reply":"2023-04-01T07:47:10.511662Z"},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"a=int(input(\"enter lot area : \"))\nb=int(input(\"enter the overall condition of the plot : \" ))\nc=int(input(\"enter the year sold or finished :  \" ))\ninputter(a,b,c)","metadata":{"execution":{"iopub.status.busy":"2023-04-01T07:47:10.515789Z","iopub.execute_input":"2023-04-01T07:47:10.516487Z","iopub.status.idle":"2023-04-01T07:47:29.085631Z","shell.execute_reply.started":"2023-04-01T07:47:10.516425Z","shell.execute_reply":"2023-04-01T07:47:29.084154Z"},"trusted":true},"execution_count":null,"outputs":[]}]}