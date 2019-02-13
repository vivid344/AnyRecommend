const gulp = require("gulp");
const sass = require("gulp-sass");
const sassGlob = require("gulp-sass-glob");

// Sassコンパイルタスクの定義
gulp.task("default", function () {
    return gulp.watch('./style/**/*.scss', function () { // 指定ファイルの変更をみて，変更されたら以下が動く
        return gulp.src("./style/style.scss") // ファイルの選択
            .pipe(sassGlob()) // 選択したファイルに記述されてあるファイルを一つのファイルに纏める
            .pipe(sass({ outputStyle: 'compressed' })) // cssにコンパイルする outputStyle: compressedで最小限の内容でコンパイル
            .pipe(gulp.dest("./public/css")); // 出力する
    });
});
