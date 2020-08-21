package com.caddickbrown.algorithmic

import android.content.Context
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.add_product.*

class AddProductActivity: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.add_product)

        AddProductSubmitButton.setOnClickListener {
            val database = getSharedPreferences("Database", Context.MODE_PRIVATE)
            database.edit().apply {
                putString("SavedProductName",EditTextProductName.text.toString())
            }.apply()
        }


    }

}