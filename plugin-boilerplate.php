<?php
/*
Plugin Name: ⟪プラグインの名前⟫⟪⟫
Plugin URI: ⟪プラグインのメインページのURL⟫
Description: ⟪プラグインの概要⟫
Version: ⟪バージョン番号⟫
Author: ⟪作者名⟫
Author ⟪作者URL⟫
License: ⟪ライセンス⟫
*/

class ClassName { // ルールが決まっているわけではないが、プラグイン名をクラス名にする

    /**
     * constructor
     */
    function __construct() {
        /**
         * add admin menu
         */
        add_action('admin_menu', function(){
            add_menu_page(
                'TitleName', // メニューが選択されたとき、ページの<title>タグに表示されるテキスト（必須）
                'Menu Name', // 管理画面のメニューに表示されるテキスト（必須）
                'moderate_comments', // 管理画面のメニューを表示するために必要なユーザー権限（必須）
                's947ci', // メニューのスラッグ名（必須）
                array($this,'show_page'), // 管理画面ページのHTMLを出力する関数等
                '', // メニューに表示されるアイコン
                99 // メニューの表示位置
            );
        });
    }

    /**
     * add admin page
     */
    function show_page() {
        echo '<p>Hey</p>';
    }
}
$className = new ClassName();
