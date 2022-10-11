import numpy as np

class KalmanFilter(object):

    def __init__(self, dt, u_x,u_y, std_acc, x_std_meas, y_std_meas):

        # sampling time
        self.dt = dt
        # control input variables
        self.u = np.matrix([[u_x],[u_y]])
        # initial State
        self.x = np.matrix([[0], [0], [0], [0]])
        # state transition matrix A
        self.A = np.matrix([[1, 0, self.dt, 0],
                            [0, 1, 0, self.dt],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]])
        # control input matrix B
        self.B = np.matrix([[(self.dt**2)/2, 0],
                            [0,(self.dt**2)/2],
                            [self.dt,0],
                            [0,self.dt]])
        # measurement mapping matrix
        self.H = np.matrix([[1, 0, 0, 0],
                            [0, 1, 0, 0]])
        # initial process noise covariance
        self.Q = np.matrix([[(self.dt**4)/4, 0, (self.dt**3)/2, 0],
                            [0, (self.dt**4)/4, 0, (self.dt**3)/2],
                            [(self.dt**3)/2, 0, self.dt**2, 0],
                            [0, (self.dt**3)/2, 0, self.dt**2]]) * std_acc**2
        # initial measurement noise covariance
        self.R = np.matrix([[x_std_meas**2,0],
                           [0, y_std_meas**2]])
        # initial covariance matrix
        self.P = np.eye(self.A.shape[1])

    def predict(self):

        # update time state 
        self.x = np.dot(self.A, self.x) + np.dot(self.B, self.u)
        # calculate error covariance    
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        return self.x[0:2]

    def update(self, z):

        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        # calculate the kalman gain
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))  
        self.x = np.round(self.x + np.dot(K, (z - np.dot(self.H, self.x))))   
        I = np.eye(self.H.shape[1])
        # update error covariance matrix
        self.P = (I - (K * self.H)) * self.P   
        return self.x[0:2]
