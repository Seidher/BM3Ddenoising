from itertools import product
import numpy as np


class BM3D:
    def __init__(self, noisy_img, **kwargs):
        self.img = noisy_img
        self.N = noisy_img.shape[0]
        self.N1_th = kwargs.get("N1_th")
        self.N1_wie = kwargs.get("N1_wie")
        self.sigma = kwargs.get("sigma")
        self.lambda_3d = kwargs.get("lambda_3d")
        self.lambda_2d = kwargs.get("lambda_2d")
        self.tau_ht_match = kwargs.get("tau_ht_match")
        self.tau_wie_match = kwargs.get("tau_wie_match")

        self.w_th = np.zeros((self.N, self.N))
        self.w_wie = np.zeros((self.N, self.N))

        self.img_basic_estimate = np.zeros((self.N, self.N))
        self.img_final_estimate = np.zeros((self.N, self.N))

        self.S_xR_ht = np.empty((self.N, self.N))
        self.S_xR_wie = np.empty((self.N, self.N))
        self.th_itf_3d = np.zeros((self.N, self.N1_th, self.N1_th))
        self.wie_itf_3d = np.zeros((self.N, self.N1_wie, self.N1_wie))
        self.wiener_energies = np.zeros((self.N, self.N))

    def denoise(self):
        """
            Denoise self.img according to the algorithm described in the paper
        :return: 2d np array, same size as the input image
        """
        for i, j in product(range(self.N), 2):
            group_x_R_th = self.grouping_from_noisy(i, j)
            tf_3d = self.transformation_3d(group_x_R_th)

            thresholded = self.hard_threshold(tf_3d)
            self.w_th[i, j] = self.weight_th(thresholded)

            self.th_itf_3d[i, j, :, :] = self.itransformation_3d(thresholded)

        self.compute_y_basic()

        for i, j in product(range(self.N), 2):
            group_xR_noisy = self.grouping_from_noisy(i, j)
            group_xR_basic = self.grouping_from_basic_estimate(i, j)

            tf_3d_noisy = self.transformation_3d(group_xR_noisy)
            tf_3d_basic = self.transformation_3d(group_xR_basic)

            self.compute_wiener_energy(tf_3d_basic, i, j)
            self.w_wie[i, j] = self.weight_wie(i, j)

            wienered = self.wiener_filter(tf_3d_noisy, i, j)
            self.wie_itf_3d[i, j, :, :] = self.itransformation_3d(wienered)

        self.compute_y_final()

        return self.img_final_estimate

    def grouping_from_noisy(self, i, j):
        # TODO
        # use self.img
        # don't forget to put the groups (ii, jj) in self.S_xR_ht[i, j]
        pass

    def grouping_from_basic_estimate(self, i, j):
        # TODO
        # use self.img_basic_estimate
        # don't forget to put the groups (ii, jj) in self.S_xR_ht[i, j]
        pass

    def transformation_3d(self, group):
        # TODO
        pass

    def itransformation_3d(self, group):
        # TODO
        pass

    def hard_threshold(self, tf_3d):
        # TODO
        pass

    def wiener_filter(self, tf_3d, i, j):
        # TODO
        # wiener energy is in self.wiener_energies[i, j]
        pass

    def weight_th(self, thresholded):
        # Formula (10)
        # TODO
        pass

    def weight_wie(self):
        # Formula (11)
        # TODO
        pass

    def compute_y_basic(self):
        # Formula (12)
        # TODO
        # self.img_basic_estimate = ...
        pass

    def compute_y_final(self):
        # Formula (12)
        # TODO
        # self.img_final_estimate = ...
        pass

    def compute_wiener_energy(self, tf_3d_basic, i, j):
        # Formula (8)
        # TODO
        pass


params = {
    "N1_th": 4,
    "N1_wie": 4,
    "sigma": 2,
    "lambda_3d": 1,
    "lambda_2d": 1,
    "tau_ht_match": 1,
    "tau_wie_match": 1
}

denoiser = BM3D(np.zeros((16, 16)), **params)
img_denoised = denoiser.denoise()