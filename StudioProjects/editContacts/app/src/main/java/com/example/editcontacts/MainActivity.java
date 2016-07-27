package com.example.editcontacts;

import java.io.ByteArrayOutputStream;

import android.app.Activity;
import android.content.ComponentName;
import android.content.ContentUris;
import android.content.ContentValues;
import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.provider.ContactsContract.CommonDataKinds.Email;
import android.provider.ContactsContract.CommonDataKinds.Phone;
import android.provider.ContactsContract.CommonDataKinds.Photo;
import android.provider.ContactsContract.CommonDataKinds.StructuredName;
import android.provider.ContactsContract.RawContacts;
import android.provider.ContactsContract.RawContacts.Data;
import android.text.TextUtils;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends Activity {
	EditText editNumber;
	Button addContacts;
	Button addMessages;
	Button openContacts;
	Button openMessages;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		editNumber = (EditText) findViewById(R.id.edit_number);
		addContacts = (Button) findViewById(R.id.add_contacts);
		addContacts.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				String number = editNumber.getText().toString();
				if (!TextUtils.isEmpty(number)) {
					writeContacts(number);
				} else {
					// number = "100";
					// writeContacts(number);
					;
				}
			}
		});
		// addMessages = (Button) findViewById(R.id.add_messages);
		// addMessages.setOnClickListener(new OnClickListener() {
		// public void onClick(View v) {
		// String number = editNumber.getText().toString();
		// if(!TextUtils.isEmpty(number)){
		// ;
		// }
		// }
		// });
		openContacts = (Button) findViewById(R.id.open_contacts);
		openContacts.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				startApp("com.android.contacts");
			}
		});
		openMessages = (Button) findViewById(R.id.open_messages);
		openMessages.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				startApp("com.android.mms");
				startApp("com.android.messaging");
			}
		});
	}

	public void startApp(String packageName) {
		Intent intent = this.getPackageManager().getLaunchIntentForPackage(
				packageName);
		if (intent != null) {
			startActivity(intent);
		} else {
			return;
		}
	}

	private void writeContacts(String number) {
		String name = "liuming";
		String work_email="772985548@qq.com";
		// TODO Auto-generated method stub
		ContentValues values = new ContentValues();
		Uri rawContactUri = getContentResolver().insert(
				RawContacts.CONTENT_URI, values);// 向RawContacts.CONTENT_URI执行一个空值插入
		long rawContactId = ContentUris.parseId(rawContactUri); // 获取系统返回的rawContactId
		// 往data表插入姓名数据
		if (name != "") {
			values.clear();
			values.put(Data.RAW_CONTACT_ID, rawContactId);
			values.put(Data.MIMETYPE, StructuredName.CONTENT_ITEM_TYPE);// 内容类型
			values.put(StructuredName.GIVEN_NAME, name);
			getContentResolver().insert(ContactsContract.Data.CONTENT_URI,
					values);
		}
		// 往data表插入电话数据
		if (number != "") {
			values.clear();
			values.put(Data.RAW_CONTACT_ID, rawContactId);
			values.put(Data.MIMETYPE, Phone.CONTENT_ITEM_TYPE);
			values.put(Phone.NUMBER, number);
			values.put(Phone.TYPE, Phone.TYPE_MOBILE);
			getContentResolver().insert(ContactsContract.Data.CONTENT_URI,
					values);
		}
		if (work_email != "") {
			values.clear();
			values.put(Data.RAW_CONTACT_ID, rawContactId);
			values.put(Data.MIMETYPE, Email.CONTENT_ITEM_TYPE);
			values.put(Email.DATA, work_email);
			values.put(Email.TYPE, Email.TYPE_WORK);
			getContentResolver().insert(ContactsContract.Data.CONTENT_URI,
					values);
		}
//		Bitmap sourceBitmap = BitmapFactory.decodeResource(getResources(),
//				R.drawable.ic_launcher);
//		final ByteArrayOutputStream os = new ByteArrayOutputStream();
//		// 将Bitmap压缩成PNG编码，质量为100%存储
//		sourceBitmap.compress(Bitmap.CompressFormat.PNG, 100, os);
//		byte[] avatar = os.toByteArray();
//		values.put(Data.RAW_CONTACT_ID, rawContactId);
//		values.put(Data.MIMETYPE, Photo.CONTENT_ITEM_TYPE);
//		values.put(Photo.PHOTO, avatar);
//		getContentResolver().insert(ContactsContract.Data.CONTENT_URI, values);
	}

}
