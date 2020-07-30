package com.example.umeed.login;

import android.util.Log;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.ViewModel;

import com.example.umeed.data.UmeedRepository;
import com.example.umeed.data.model.request.LoginRequestModel;
import com.example.umeed.data.model.request.RegisterRequestModel;
import com.example.umeed.data.model.response.LoginResponseModel;
import com.example.umeed.data.model.response.RegisterResponseModel;
import com.example.umeed.data.network.RetrofitService;

import java.util.regex.Pattern;

public class LoginViewModel extends ViewModel {
    private static final String TAG = "LoginViewModel";
    String mobileNumber;
    private UmeedRepository umeedRepository;

    public LoginViewModel() {
        umeedRepository = UmeedRepository.getInstance();
    }

    public LiveData<LoginResponseModel> login(String mobileNumber1, String password) {
        Log.d(TAG, "signIn: " + RetrofitService.getTOKEN());
        Log.d(TAG, "signIn: mobile: " + mobileNumber);
        LoginRequestModel requestModel = new LoginRequestModel();
        requestModel.setPhone(mobileNumber1);
        requestModel.setPassword(password);

        return umeedRepository.login(requestModel);
    }

    boolean isValidMobile(String phone) {
        this.mobileNumber = phone;
        return !Pattern.matches("\"(0/91)?[7-9][0-9]{9}\"", phone) && phone.length() == 10;
    }
}